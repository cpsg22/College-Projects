import os
import platform
import subprocess




#RUN THIS PROGRAM USING CONTROL + t FOR BETTER USER EXPERIENCE


# Function to clear the screen
def clear_screen():
    subprocess.call("cls", shell=True)

# Function to display current directory
def display_current_directory(directory):
    print("\t _____________________________________________________________________________")
    print("\t|_______________________________________________________________________|_|-|x|")
    print("\t|                                                                             |")
    print("\t|                      | GROUP 8 - TERMINAL FILE MANAGER |                    |")
    print("\t|_____________________________________________________________________________|")
    print(f"\t||◄|►|▲|| Current Path: {directory} ")
    print("\t|_____________________________________________________________________________|")
    print("\t|                                                                             |")

# Function to list directories and files
def list_directories_and_files(directory):
    print("\t| Files:")
    items = [item for item in os.listdir(directory) if os.path.isfile(os.path.join(directory, item))]
    items.sort()  # Sort items alphabetically
    for i, item in enumerate(items, 1):
        print(f"\t| [{i}] {item}")
    return items

# Function to create a new folder
def create_folder(directory):
    folder_name = input("\t| Enter folder name: ")
    folder_path = os.path.join(directory, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        clear_screen()
        print("\t _____________________________________________________________________________ ")
        print("\t|____________________________NOTIFICATION MESSAGE:______________________|_|-|X|")
        print("\t|                                                                             |")
        print("\t|                        Folder created successfully!                         |")
        print("\t|_____________________________________________________________________________|\n\n")
    else:
        clear_screen()
        print("\t _____________________________________________________________________________ ")
        print("\t|____________________________NOTIFICATION MESSAGE:______________________|_|-|X|")
        print("\t| Folder with the same name already exists or you choose invalid option. .    |")
        print("\t|                       Please choose a different name                        |")
        print("\t|_____________________________________________________________________________|\n\n")

# Function to delete a folder
def delete_folder(directory):
    folder_names = [item for item in os.listdir(directory) if os.path.isdir(os.path.join(directory, item))]
    if not folder_names:
        print("\t _____________________________________________________________________________ ")
        print("\t|____________________________NOTIFICATION MESSAGE:______________________|_|-|X|")
        print("\t| No folders found in this directory.                                         |")
        print("\t|_____________________________________________________________________________|\n")      
        return
    
    print("\t|_Delete Folder\s:____________________________________________________________|\n\t| ")
    
    for i, folder_name in enumerate(folder_names, 1):
        print(f"\t| [{i}] {folder_name}")
        
    while True:
        
        print("\t _____________________________________________________________________________ ")
        print("\t|____________________________NOTIFICATION MESSAGE:______________________|_|-|X|")
        print("\t| REMINDER! :                                                                 |")
        print("\t| You are about to delete a folder that is currently saved on this computer.  |")
        print("\t| Please make sure that you will ONLY delete folder/s that are created within |")
        print("\t|       this demonstration and/or folder/s that are no longer in use.         |")
        print("\t|                                 Thank you!                                  |")
        print("\t|_____________________________________________________________________________|\n") 

        choice = input("\n\t| Enter the number of the folder you want to delete (choose : 0 or Enter to cancel): ")
        
        if choice.isdigit():  # Check if input is a digit
            choice = int(choice)
            if choice == 0:
                return
            elif 1 <= choice <= len(folder_names):
                folder_name = folder_names[choice - 1]
                folder_path = os.path.join(directory, folder_name)
                if os.path.exists(folder_path):
                    try:
                        if os.listdir(folder_path):
                            response = input("\t| All the files inside this folder will be deleted. Are you sure you want to delete? (y/n): ")

                            if response.lower() == 'y':
                                
                                clear_folder(folder_path)
                                os.rmdir(folder_path)
                                clear_screen()
                                print("\t _____________________________________________________________________________ ")
                                print("\t|____________________________NOTIFICATION MESSAGE:______________________|_|-|X|")
                                print("\t|                        Folder deleted successfully!                         |")
                                print("\t|_____________________________________________________________________________|\n")
                                return
                            else:
                                clear_screen()
                                print("\t _____________________________________________________________________________ ")
                                print("\t|____________________________NOTIFICATION MESSAGE:______________________|_|-|X|")
                                print("\t|                              Deletion canceled.                             |")
                                print("\t|_____________________________________________________________________________|\n")
                                return
                        else:
                            response = input("\t Are you sure you want to delete this empty folder? (y/n): ")
                            if response.lower() == 'y':
                                os.rmdir(folder_path)
                                clear_screen()
                                print("\t _____________________________________________________________________________ ")
                                print("\t|____________________________NOTIFICATION MESSAGE:______________________|_|-|X|")
                                print("\t|                        Folder deleted successfully!                         |")
                                print("\t|_____________________________________________________________________________|\n")
                                return
                            else:
                                clear_screen()
                                print("\t _____________________________________________________________________________ ")
                                print("\t|____________________________NOTIFICATION MESSAGE:______________________|_|-|X|")
                                print("\t|                              Deletion canceled.                             |")
                                print("\t|_____________________________________________________________________________|\n")
                                return
                                
                    except OSError as e:
                        print("\t| Error:", e)
                        print("\t|_____________________________________________________________________________|\n")
                else:
                    clear_screen()
                    print("\t _____________________________________________________________________________|")
                    print("\t|____________________________NOTIFICATION MESSAGE:______________________|_|-|X|")
                    print("\t|                            Folder does not exist.                           |")
                    print("\t|_____________________________________________________________________________|\n")
                    return
            else:
                clear_screen()
                print("\t _____________________________________________________________________________")
                print("\t|____________________________NOTIFICATION MESSAGE:______________________|_|-|X|")
                print("\t|                Invalid choice. Please choose a valid number.                |")
                print("\t|_____________________________________________________________________________|\n")
                return
        else:
            clear_screen()
            print("\t _____________________________________________________________________________")
            print("\t|____________________________NOTIFICATION MESSAGE:______________________|_|-|X|")
            print("\t|                    Invalid input. Please enter a number.                    |")
            print("\t|_____________________________________________________________________________|\n")
            return
                
# Function to clear a folder
def clear_folder(folder_path):
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isfile(item_path):
            os.remove(item_path)
        elif os.path.isdir(item_path):
            clear_folder(item_path)

# Function to create a file
def create_file(directory):
    file_name = input("\t| Enter file name with extension: ")
    file_path = os.path.join(directory, file_name)
    if not os.path.exists(file_path):
        open(file_path, 'a').close()
        clear_screen()
        print("\t _____________________________________________________________________________")
        print("\t|____________________________NOTIFICATION MESSAGE:______________________|_|-|X|")
        print("\t|                         File created successfully!                          |")
        print("\t|_____________________________________________________________________________|\n")
        return
    else:
        clear_screen()
        print("\t _____________________________________________________________________________")
        print("\t|____________________________NOTIFICATION MESSAGE:______________________|_|-|X|")
        print("\t|   File with the same name already exists. Please choose a different name.   |")
        print("\t|_____________________________________________________________________________|")
        return

# Function to delete a file
def delete_file(directory):
    items = list_directories_and_files(directory)
    if not items:
        clear_screen()
        print("\t _____________________________________________________________________________")
        print("\t|____________________________NOTIFICATION MESSAGE:______________________|_|-|X|")
        print("\t|                           The directory is empty.                           |")
        print("\t|_____________________________________________________________________________|\n")
        return
    
    while True:        
        
        print("\t _____________________________________________________________________________ ")
        print("\t|____________________________NOTIFICATION MESSAGE:______________________|_|-|X|")
        print("\t| REMINDER! :                                                                 |")
        print("\t| You are about to delete file/s that is currently saved on this computer.    |")
        print("\t| Please make sure that you will ONLY delete files that are created within    |")
        print("\t|    this demonstration and/or files/folder that are no longer in use.        |")
        print("\t|                                 Thank you!                                  |")
        print("\t|_____________________________________________________________________________|\n")
        
        choice = input("\n\t| Enter the number of the file you want to delete (0 to cancel): ")
        if choice.isdigit():  # Check if input is a digit
            choice = int(choice)
            if choice == 0:
                return 
            elif 1 <= choice <= len(items):
                file_name = items[choice - 1]
                file_path = os.path.join(directory, file_name)
                if os.path.isfile(file_path):
                    try:
                        # Ask for confirmation before deleting the file
                        confirm_delete = input("\t| Are you sure you want to delete the file? [y/n]: ")
                        if confirm_delete.lower() == 'y':
                            os.remove(file_path)                        
                            print("\t _____________________________________________________________________________")
                            print("\t|____________________________NOTIFICATION MESSAGE:______________________|_|-|X|")
                            print(f"\t|                File '{file_name}' deleted successfully!                    ")
                            print("\t|_____________________________________________________________________________|\n")
                            return
                            

                        else:                          
                            print("\t _____________________________________________________________________________")
                            print("\t|____________________________NOTIFICATION MESSAGE:______________________|_|-|X|")
                            print("\t|                              Deletion canceled.                             |")
                            print("\t|_____________________________________________________________________________|\n")
                            return
                            
                    except Exception as e:                      
                        print("\t _____________________________________________________________________________")
                        print("\t|____________________________NOTIFICATION MESSAGE:______________________|_|-|X|")
                        print(f"\t|               Error occurred while deleting the file: {e}                  |")
                        print("\t|_____________________________________________________________________________|\n")
                        return
                else:                   
                    print("\t _____________________________________________________________________________")
                    print("\t|____________________________NOTIFICATION MESSAGE:______________________|_|-|X|")
                    print("\t|                    Invalid choice. Please choose a file.                    |")
                    print("\t|_____________________________________________________________________________|\n")
                    return
            else:               
                print("\t _____________________________________________________________________________")
                print("\t|____________________________NOTIFICATION MESSAGE:______________________|_|-|X|")
                print("\t|                 Invalid choice. Please choose a valid number.               |")
                print("\t|_____________________________________________________________________________|\n")
                return
        else:            
            print("\t _____________________________________________________________________________")
            print("\t|____________________________NOTIFICATION MESSAGE:______________________|_|-|X|")
            print("\t|                    Invalid input. Please enter a number.                    |")
            print("\t|_____________________________________________________________________________|\n")
            return
            
# Function to edit a file
def edit_file(directory):
    # List of editable text-based file extensions supported by Thonny
    text_based_extensions = ['.txt', '.md', '.py', '.sh', '.pl', '.java', '.c', '.cpp', '.cs', '.js', '.rb', '.ps1', '.swift', '.kt', '.ts', '.sql', '.asm', '.m', '.vbs', '.cfg', '.docx']

    # Filter files with compatible extensions
    items = [item for item in os.listdir(directory) if os.path.isfile(os.path.join(directory, item)) and
             os.path.splitext(item)[1].lower() in text_based_extensions]

    if not items:
        clear_screen()
        print("\t _____________________________________________________________________________")
        print("\t|____________________________NOTIFICATION MESSAGE:____________________________|")
        print("\t|          No editable text-based files found in this directory.              |")
        print("\t|_____________________________________________________________________________|\n")
        return

    while True:
        print("\t|_Editable Text-based Files: _________________________________________________|")
        print("\t|_____________________________________________________________________________|")
        for i, item in enumerate(items, 1):
            print(f"\t| [{i}] {item}")

        choice = input("\t|_____________________________________________________________________________|\n\t| Enter the number of the file you want to edit (0 to cancel): ")
        if choice.isdigit():  # Check if input is a digit
            choice = int(choice)
            if choice == 0:
                return
            elif 1 <= choice <= len(items):
                file_name = items[choice - 1]
                file_path = os.path.join(directory, file_name)
                if os.path.isfile(file_path):
                    try:
                        with open(file_path, 'r', encoding='utf-8') as file:
                            original_content = file.read()
                            print(f"\n\t| Content of '{file_name}':\n")
                            print("\t", original_content)
                            print("\n\t _____________________________________________________________________________")                                     
                            print("\t| Start re-writing below:                                                     |")
                            updated_content = input(f"\t|_(Type (.) on a new line then press enter to stop)___________________________|\n\n")
                            new_content = ""
                            while updated_content != '.':
                                new_content += updated_content + '\n\t '
                                updated_content = input()

                        response = input("\t| Do you want to save the changes? [y/n]: ")
                        if response.lower() == 'y':
                            with open(file_path, 'w', encoding='utf-8') as file:
                                file.write(new_content)
                            clear_screen()
                            print("\t _____________________________________________________________________________")
                            print("\t|____________________________NOTIFICATION MESSAGE:______________________|_|-|X|")
                            print("\t|                        Changes saved successfully!                          |")
                            print("\t|_____________________________________________________________________________|\n")
                        else:
                            clear_screen()
                            print("\t _____________________________________________________________________________")
                            print("\t|____________________________NOTIFICATION MESSAGE:____________________________|")
                            print("\t|                              Changes discarded.                             |")
                            print("\t|_____________________________________________________________________________|\n")
                    except Exception as e:
                        clear_screen()
                        print("\t _____________________________________________________________________________")
                        print("\t|____________________________NOTIFICATION MESSAGE:____________________________|")
                        print(f"\t|              Error occurred while reading/editing the file: {e}             |")
                        print("\t|_____________________________________________________________________________|\n")
                else:
                    clear_screen()
                    print("\t _____________________________________________________________________________")
                    print("\t|____________________________NOTIFICATION MESSAGE:______________________|_|-|X|")
                    print("\t|                   Invalid choice. Please choose a file.                     |")
                    print("\t|_____________________________________________________________________________|\n")
            else:
                clear_screen()
                print("\t _____________________________________________________________________________")
                print("\t|____________________________NOTIFICATION MESSAGE:______________________|_|-|X|")
                print("\t|                Invalid choice. Please choose a valid number.                |")
                print("\t|_____________________________________________________________________________|\n")
        else:
            clear_screen()
            print("\t _____________________________________________________________________________")
            print("\t|____________________________NOTIFICATION MESSAGE:______________________|_|-|X|")
            print("\t|                   Invalid input. Please enter a number.                     |")
            print("\t|_____________________________________________________________________________|\n")


            

# Function to view file contents
def view_file(directory):
    items = list_directories_and_files(directory)
    if not items:
        clear_screen()
        print("\t _____________________________________________________________________________")
        print("\t|____________________________NOTIFICATION MESSAGE:______________________|_|-|X|")
        print("\t|                           The directory is empty.                           |")
        print("\t|_____________________________________________________________________________|\n")
        return

    while True:
        print("\t|                                                                             |")
        choice = input("\t Enter the number of the file you want to view (0 to cancel): ")
        if choice.isdigit():  # Check if input is a digit
            choice = int(choice)
            if choice == 0:
                return 
            elif 1 <= choice <= len(items):
                file_name = items[choice - 1]
                file_path = os.path.join(directory, file_name)
                if os.path.isfile(file_path):
                    try:
                        os.startfile(file_path)  # Open file with associated application
                    except Exception as e:
                        clear_screen()
                        print("\t _____________________________________________________________________________")
                        print("\t|____________________________NOTIFICATION MESSAGE:______________________|_|-|X|")
                        print(f"\t Error occurred while opening the file: {e}                                  |")
                        print("\t|_____________________________________________________________________________|\n")
                        return
                else:
                    clear_screen()
                    print("\t _____________________________________________________________________________")
                    print("\t|____________________________NOTIFICATION MESSAGE:____________________________|")
                    print("\t Invalid choice. Please choose a file.                                        |")
                    print("\t|_____________________________________________________________________________|\n")
                    return
            else:
                clear_screen()
                print("\t _____________________________________________________________________________")
                print("\t|____________________________NOTIFICATION MESSAGE:______________________|_|-|X|")
                print("\t Invalid choice. Please choose a valid number.                                |")
                print("\t|_____________________________________________________________________________|\n")
                return
        else:
            clear_screen()
            print("\t _____________________________________________________________________________")
            print("\t|____________________________NOTIFICATION MESSAGE:______________________|_|-|X|")
            print("\t Invalid input. Please enter a number.                                        |")
            print("\t|_____________________________________________________________________________|\n")
            return

# Function to rename a file
def rename_file(directory):
    
    items = list_directories_and_files(directory)
    if not items:
        clear_screen()
        print("\t _____________________________________________________________________________")
        print("\t|____________________________NOTIFICATION MESSAGE:______________________|_|-|X|")
        print("\t| The directory is empty.                                                     |")
        print("\t|_____________________________________________________________________________|\n")
        return

    while True:
        print("\t|                                                                             |")
        choice = input("\n\t| Enter the number of the file you want to rename (0 to cancel): ")
        if choice.isdigit():  # Check if input is a digit
            choice = int(choice)
            if choice == 0:
                return
            elif 1 <= choice <= len(items):
                old_file_name = items[choice - 1]
                old_file_path = os.path.join(directory, old_file_name)
                new_file_name = input("\t| Enter the new file name with extension: ")
                new_file_path = os.path.join(directory, new_file_name)
                if os.path.exists(new_file_path):
                    clear_screen()
                    print("\t _____________________________________________________________________________")
                    print("\t|____________________________NOTIFICATION MESSAGE:______________________|_|-|X|")
                    print("\t| A file with the same name already exists.                                   |")
                    print("\t|_____________________________________________________________________________|\n")
                    return
                try:
                    # Ask for confirmation before renaming the file
                    confirm_rename = input("\t Are you sure you want to rename the file? [y/n]: ")
                    if confirm_rename.lower() == 'y':
                        os.rename(old_file_path, new_file_path)
                        clear_screen()
                        print("\t _____________________________________________________________________________")
                        print("\t|____________________________NOTIFICATION MESSAGE:______________________|_|-|X|")
                        print("\t| File renamed successfully!                                                  |")
                        print("\t|_____________________________________________________________________________|\n")
                        return
                    else:
                        clear_screen()
                        print("\t _____________________________________________________________________________")
                        print("\t|____________________________NOTIFICATION MESSAGE:______________________|_|-|X|")
                        print("\t| Renaming canceled.                                                          |")
                        print("\t|_____________________________________________________________________________|\n")
                        return
                except Exception as e:
                    clear_screen()
                    print("\t _____________________________________________________________________________")
                    print("\t|____________________________NOTIFICATION MESSAGE:______________________|_|-|X|")
                    print(f"\t| Error occurred while renaming the file: {e}                                 |")
                    print("\t|_____________________________________________________________________________|\n")
                    return
            else:
                clear_screen()
                print("\t _____________________________________________________________________________")
                print("\t|____________________________NOTIFICATION MESSAGE:______________________|_|-|X|")
                print("\t|                Invalid choice. Please choose a valid number.                |")
                print("\t|_____________________________________________________________________________|\n")
                return
                
        else:
            clear_screen()
            print("\t _____________________________________________________________________________")
            print("\t|____________________________NOTIFICATION MESSAGE:______________________|_|-|X|")
            print("\t|                     Invalid input. Please enter a number.                   |")
            print("\t|_____________________________________________________________________________|\n")
            return
            

# Function to rename a folder
def rename_folder(directory):
    folders = [item for item in os.listdir(directory) if os.path.isdir(os.path.join(directory, item))]
    if not folders:
        clear_screen()
        print("\t _____________________________________________________________________________")
        print("\t|____________________________NOTIFICATION MESSAGE:______________________|_|-|X|")
        print("\t| No folders found in this directory.                                         | ")
        print("\t|_____________________________________________________________________________|\n")
        return

    while True:
        print("\t|_____________________________________________________________________________|")
        print("\t|_Rename Folder\s:____________________________________________________________|\n\t|")
        for i, folder_name in enumerate(folders, 1):
            print(f"\t| [{i}] {folder_name}")

        choice = input("\t|_____________________________________________________________________________|\n\t|\n\t| Enter the number of the folder you want to rename [0 to cancel]: ")
        if choice.isdigit():  # Check if input is a digit
            choice = int(choice)
            
            if choice == 0:
                clear_screen()
                return
            elif 1 <= choice <= len(folders):
                old_folder_name = folders[choice - 1]
                old_folder_path = os.path.join(directory, old_folder_name)
                new_folder_name = input("\t\n\t Enter the new folder name: ")
                new_folder_path = os.path.join(directory, new_folder_name)
                if new_folder_name == old_folder_name:
                    clear_screen()
                    print("\t _____________________________________________________________________________")
                    print("\t|____________________________NOTIFICATION MESSAGE:______________________|_|-|X|")
                    print("\t| New folder name is the same as the old one.                                 |")
                    print("\t|_____________________________________________________________________________|\n")
                    return
                elif os.path.exists(new_folder_path):
                    clear_screen()
                    print("\t _____________________________________________________________________________")
                    print("\t|____________________________NOTIFICATION MESSAGE:______________________|_|-|X|")
                    print("\t| A folder with the same name already exists.                                 |")
                    print("\t|_____________________________________________________________________________|\n") 
                    return

                confirm = input("\n\t______________________________________________________________________________|\n\t| Are you sure you want to rename this folder? [y/n]: ")
                if confirm.lower() == 'y':
                    try:
                        os.rename(old_folder_path, new_folder_path)
                        clear_screen()
                        print("\t _____________________________________________________________________________")
                        print("\t|____________________________NOTIFICATION MESSAGE:______________________|_|-|X|")
                        print("\t| Folder renamed successfully!                                                |")
                        print("\t|_____________________________________________________________________________|\n")
                        return
                        
                    except Exception as e:
                        clear_screen()
                        print("\t _____________________________________________________________________________")
                        print("\t|____________________________NOTIFICATION MESSAGE:______________________|_|-|X|")
                        print(f"\t| Error occurred while renaming the folder: {e}                               |")
                        print("\t|_____________________________________________________________________________|\n")
                        return
                    
                elif confirm.lower() == 'n':
                    clear_screen()
                    print("\t _____________________________________________________________________________")
                    print("\t|____________________________NOTIFICATION MESSAGE:______________________|_|-|X|")
                    print("\t| Rename operation canceled.                                                  |")
                    print("\t|_____________________________________________________________________________|\n")                    
                    return
                else:
                    clear_screen()
                    print("\t _____________________________________________________________________________")
                    print("\t|____________________________NOTIFICATION MESSAGE:______________________|_|-|X|")
                    print("\t| Invalid choice. Please enter 'y' or 'n'.                                    |")
                    print("\t|_____________________________________________________________________________|\n")
                    
            else:
                clear_screen()
                print("\t _____________________________________________________________________________")
                print("\t|____________________________NOTIFICATION MESSAGE:______________________|_|-|X|")
                print("\t|                 Invalid choice. Please choose a valid number.               |")
                print("\t|_____________________________________________________________________________|\n")
                return
                
        else:
            clear_screen()
            print("\t _____________________________________________________________________________")
            print("\t|____________________________NOTIFICATION MESSAGE:______________________|_|-|X|")
            print("\t|                     Invalid input. Please enter a number.                   |")
            print("\t|_____________________________________________________________________________|\n")
            return
            


# Function to navigate to a sub-folder
def navigate_to_sub_folder(current_directory):
    folder_names = [item for item in os.listdir(current_directory) if os.path.isdir(os.path.join(current_directory, item))]

    while True:
        display_current_directory(current_directory)
        print("\t|_Folder Management:__________________________________________________________|")
        print("\t|									      |")
        print("\t| [1] Create Folder							      |")
        print("\t| [2] Delete Folder							      |")
        print("\t| [3] Rename Folder							      |")
        print("\t| [4] Go to Directory/Sub-folders					      |")
        print("\t| [5] Go back to Parent Directory/Folder				      |")
        print("\t| [6] Go back to Main Menu					    	      |")
        print("\t|_____________________________________________________________________________|\n")

        choice = input("\t| Enter the number of the folder you want to navigate : ")
        if choice.isdigit():  # Check if input is a digit
            choice = int(choice)
            if choice == 6:
                return current_directory
            elif 1 <= choice <= 5:
                if choice == 1:
                    create_folder(current_directory)
                elif choice == 2:
                    clear_screen()
                    display_current_directory(current_directory)
                    delete_folder(current_directory)
                elif choice == 3:
                    clear_screen()
                    display_current_directory(current_directory)
                    rename_folder(current_directory)
                elif choice == 4:
                    if folder_names:
                        clear_screen()
                        display_current_directory(current_directory)
                        for i, folder_name in enumerate(folder_names, 1):
                        
                            print(f"\t| [{i}] {folder_name}")
                        
                        print("\t|_____________________________________________________________________________|")
                        sub_choice = input("\t| Enter the number of the sub-folder you want to navigate to [0 to cancel]: ")
                        if sub_choice.isdigit():
                            sub_choice = int(sub_choice)
                            if 1 <= sub_choice <= len(folder_names):
                                folder_name = folder_names[sub_choice - 1]
                                folder_path = os.path.join(current_directory, folder_name)
                                if os.path.isdir(folder_path):
                                    return folder_path
                                else:
                                    clear_screen()
                                    print("\t _____________________________________________________________________________ ")
                                    print("\t|____________________________NOTIFICATION MESSAGE:______________________|_|-|X|")
                                    print("\t|                   Invalid choice. Please choose a folder.                   |")
                                    print("\t|_____________________________________________________________________________|\n")
                            else:
                                clear_screen()
                                print("\t _____________________________________________________________________________ ")
                                print("\t|____________________________NOTIFICATION MESSAGE:______________________|_|-|X|")
                                print("\t|                 Invalid choice. Please choose a valid number.               |")
                                print("\t|_____________________________________________________________________________|\n")
                        else:
                            clear_screen()
                            print("\t _____________________________________________________________________________ ")
                            print("\t|____________________________NOTIFICATION MESSAGE:______________________|_|-|X|")
                            print("\t|                    Invalid input. Please enter a number.                    |")
                            print("\t|_____________________________________________________________________________|\n")
                    else:
                        clear_screen()
                        print("\t _____________________________________________________________________________ ")
                        print("\t|____________________________NOTIFICATION MESSAGE:______________________|_|-|X|")
                        print("\t| No sub-folders found in this directory.                                     |")
                        print("\t|_____________________________________________________________________________|\n")
                elif choice == 5:
                    return os.path.dirname(current_directory)
            else:
                clear_screen()
                print("\t _____________________________________________________________________________ ")
                print("\t|____________________________NOTIFICATION MESSAGE:______________________|_|-|X|")
                print("\t|                Invalid choice. Please choose a valid number.                |")
                print("\t|_____________________________________________________________________________|\n")
        else:
            clear_screen()
            print("\t _____________________________________________________________________________")
            print("\t|____________________________NOTIFICATION MESSAGE:______________________|_|-|X|")
            print("\t|                     Invalid input. Please enter a number.                   |")
            print("\t|_____________________________________________________________________________|\n")


# Main function
def main():
    current_directory = os.getcwd()  # Set current directory to the working directory

    while True:
        clear_screen()
        display_current_directory(current_directory)
        print("\t|_MAIN MENU___________________________________________________________________|")
        print("\t|                                                                             |")
        print("\t| [1] Folder/Directory Management                                             |")
        print("\t| [2] File Management                                                         |")
        print("\t| [3] Exit                                                                    |")
        print("\t|_____________________________________________________________________________|")
        choice = input("\t| Enter your choice: ")
        print("\t|_____________________________________________________________________________|")

        if choice == '1':
            clear_screen()
            current_directory = navigate_to_sub_folder(current_directory)
        elif choice == '2':
            clear_screen()
            display_current_directory(current_directory)
            print("\t|_File Management: ___________________________________________________________|")
            print("\t|                                                                             |")
            print("\t| [1] Create File                                                             |")
            print("\t| [2] Delete File                                                             |")
            print("\t| [3] Edit File                                                               |")
            print("\t| [4] Rename File                                                             |")
            print("\t| [5] Open file through Windows                                               |")
            print("\t|_____________________________________________________________________________|\n")
            sub_choice = input("\t| Enter your choice \n\t| Double press Enter to go back to Main Menu : ")
            if sub_choice == '1':
                create_file(current_directory)
            elif sub_choice == '2':
                clear_screen()
                display_current_directory(current_directory)
                delete_file(current_directory)
            elif sub_choice == '3':
                clear_screen()
                display_current_directory(current_directory)
                edit_file(current_directory)
            elif sub_choice == '4':
                clear_screen()
                display_current_directory(current_directory)
                rename_file(current_directory)
            elif sub_choice == '5':
                clear_screen()
                display_current_directory(current_directory)
                view_file(current_directory)
            else:
                print("\t You have choose an invalid selection or you didn't choose any option")
            input("\t Press Enter to continue...\n")
        elif choice == '3':
            confirm_exit = input("\t| Are you sure you want to exit? (y/n): ")
            if confirm_exit.lower() == 'y':
                clear_screen()
                print("\n\n\n\n\t _____________________________________________________________________________")
                print("\t|_______________________________________________________________________|_|-|x|")
                print("\t|                                                                             |")
                print("\t|_____________________________ NOTIFICATION MESSAGE: _________________________|")
                print("\t|                                                                             |")
                print("\t|                                                                             |")
                print("\t|                                                                             |")
                print("\t|                                                                             |")
                print("\t|                    You have sucessfully exited the program                  |")
                print("\t|                                                                             |")             
                print("\t|                        Thank you. Have a great day! ...                     |")
                print("\t|                                                                             |")
                print("\t|                                                                             |")
                print("\t|                                                                             |")
                print("\t|_____________________________________________________________________________|")
                break
        else:
            print("\t Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
