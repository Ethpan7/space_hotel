from flask import render_template, request
from flask import *
import sqlite3

app = Flask(__name__)
app.debug = True

#connecting to sqlite
conn = sqlite3.connect('data.db')

#establishing cursor
c = conn.cursor()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        name = request.form['name']
        surname = request.form['surname']
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        c.execute("INSERT INTO users (email, name, surname, username, password) VALUES (?,?,?,?,?)", (email, name, surname, username, password))
        conn.commit()
        conn.close()

        return 'Sign-up successful'
    return render_template('signup.html')



@app.route('/signin', methods=['GET', 'POST'], endpoint='signin')
def signin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(password)

        conn = sqlite3.connect('data.db')
        c = conn.cursor()

        # Retrieve user with the matching username
        select_query = "SELECT * FROM users WHERE username = ?"
        c.execute(select_query, (username,))
        user = c.fetchone()
        print(user[5])

        if user is not None:
            # if password matches, allow sign-in
            if user[5] == password:
                return 'Sign-in successful'
            else:
                return 'Incorrect password'
        else:
            return 'User does not exist'

    return render_template('signin.html')



@app.route('/data-entry', methods=['GET', 'POST'], endpoint='data_entry')
def data_entry():
    if request.method == 'POST':
        creditcard_info = request.form['credit_card_info']
        name = request.form['name']
        last_name = request.form['last_name']
        payment_choice = request.form['payment_choice']
        passport_number = request.form['passport_number']
        medical_record = request.form['medical_record']
        return 'Data submitted successfully!'
    return render_template('data_entry.html')

if __name__ == '__main__':
    app.run(port=5001)