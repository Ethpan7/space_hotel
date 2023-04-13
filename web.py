from flask import render_template, request, redirect, url_for
from flask import *
import sqlite3

app = Flask(__name__)
app.debug = True

def get_db_connection():
    conn2 = sqlite3.connect('data.db')
    conn2.row_factory = sqlite3.Row
    return conn2

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
        booking_query = "SELECT * FROM booking WHERE username = ?"
        c.execute(booking_query, (username,))
        bookings = c.fetchone()
        print(type(bookings))

        if user is not None:
            # if password matches, allow sign-in
            if user[5] == password and user[4] == 'cozmoz_admin':
                return redirect(url_for('users_list'))
            if user[5] == password:
                return str(bookings)
            else:
                return 'Incorrect password'
        else:
            return 'User does not exist'

    return render_template('signin.html')

@app.route('/users_list')
def users_list():
    conn2 = get_db_connection()
    users = conn2.execute('SELECT * FROM users').fetchall()
    conn2.close()
    return render_template('users_list.html', users=users)

@app.route('/bookings_list')
def bookings_list():
    conn3 = get_db_connection()
    bookings = conn3.execute('SELECT * FROM booking').fetchall()
    conn3.close()
    return render_template('bookings_list.html', bookings=bookings)

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

@app.route('/booking')
def booking():
    return render_template('booking.html')

@app.route('/checkout', methods=['POST','GET'])
def checkout():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(request.form)
        room_type = request.form['room_type']
        bed_type = request.form['bed_type']
        num_nights = request.form['num_nights']
        card_number = request.form['card_number']
        exp_date = request.form['exp_date']
        cvv = request.form['cvv']
        total_price = 500 * int(num_nights)
        print(username, room_type, bed_type, num_nights, card_number, exp_date, cvv, total_price)
        
        conn = sqlite3.connect('data.db')
        c = conn.cursor()

        select_query = "SELECT * FROM users WHERE username = ?"
        c.execute(select_query, (username,))
        user = c.fetchone()

        if user is not None:
            # if password matches, allow sign-in
            if user[5] == password:
                c.execute("INSERT INTO booking (username, room_type, bed_type, num_nights, card_number, exp_date, cvv, total_price) VALUES (?,?,?,?,?,?,?,?)", (username, room_type, bed_type, num_nights, card_number, exp_date, cvv, total_price))
                conn.commit()
                conn.close()
            else:
                return 'Incorrect password'
        else:
            return 'User does not exist'



        return 'Booking complete!'
    return render_template('checkout.html')
if __name__ == '__main__':
    app.run(port=5001)