from flask import Flask, render_template, request, redirect, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='T$bvth45',
        database='crud'
    )

# Route for rendering the login page
@app.route('/', methods=['GET'])
def login():
    return render_template('login.html')

# Route to handle login form submission
@app.route('/login', methods=['POST'])
def do_login():
    email = request.form['email']
    password = request.form['password']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT password FROM users WHERE email = %s', (email,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()

    if result and check_password_hash(result[0], password):
        session['user'] = email
        flash('Login successful!')
        return redirect('/students')  # Redirect to students page upon successful login
    else:
        flash('Invalid email or password.')
        return redirect('/')

@app.route('/signup', methods=['GET'])
def signup_page():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def do_signup():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    phone = request.form['phone']
    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['confirm_password']

    if password != confirm_password:
        flash('Passwords do not match!')
        return redirect('/signup')

    hashed_password = generate_password_hash(password)

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (first_name, last_name, email, phone, password) VALUES (%s, %s, %s, %s, %s)',
                       (first_name, last_name, email, phone, hashed_password))
        conn.commit()
        cursor.close()
        conn.close()
        return render_template('signup_confirmation.html', email=email)
    except mysql.connector.Error as err:
        flash('Error: ' + str(err))
        return redirect('/signup')

# Forgot password route
@app.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form['email']
        phone = request.form['phone']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE email = %s AND phone = %s', (email, phone))
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        if user:
            session['email'] = email  # Store email in session for password reset
            return redirect('/reset-password')
        else:
            flash('Email or phone number is incorrect.')

    return render_template('forgot_password.html')

# Reset password route
@app.route('/reset-password', methods=['GET', 'POST'])
def reset_password():
    if request.method == 'POST':
        new_password = request.form['new_password']
        hashed_password = generate_password_hash(new_password)

        email = session.get('email')
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('UPDATE users SET password = %s WHERE email = %s', (hashed_password, email))
        conn.commit()
        cursor.close()
        conn.close()

        flash('Password has been reset successfully!')
        return redirect('/')

    return render_template('reset_password.html')

# Students page route
@app.route('/students')
def index():
    if 'user' not in session:
        return redirect('/')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', students=students)

# Insert student route
@app.route('/insert', methods=['POST'])
def insert():
    if 'user' not in session:
        return redirect('/')

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    phone = request.form['phone']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO students (first_name, last_name, email, phone) VALUES (%s, %s, %s, %s)',
                   (first_name, last_name, email, phone))
    conn.commit()
    cursor.close()
    conn.close()

    flash('Student added successfully!')
    return redirect('/students')

# Update student route
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    if 'user' not in session:
        return redirect('/')

    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        phone = request.form['phone']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('UPDATE students SET first_name = %s, last_name = %s, email = %s, phone = %s WHERE id = %s',
                       (first_name, last_name, email, phone, id))
        conn.commit()
        cursor.close()
        conn.close()

        flash('Student updated successfully!')
        return redirect('/students')

    else:  # GET method
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM students WHERE id = %s', (id,))
        student = cursor.fetchone()
        cursor.close()
        conn.close()

        if student:
            return render_template('update_student.html', student=student)
        else:
            flash('Student not found.')
            return redirect('/students')

# Delete student route
@app.route('/delete/<int:id>')
def delete(id):
    if 'user' not in session:
        return redirect('/')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM students WHERE id = %s', (id,))
    conn.commit()
    cursor.close()
    conn.close()

    flash('Student deleted successfully!')
    return redirect('/students')

# Logout route
@app.route('/logout', methods=['GET'])
def logout():
    session.pop('user', None)  # Remove user from session
    flash('You have been logged out.')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
