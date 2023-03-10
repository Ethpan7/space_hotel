from flask import *

app = Flask(__name__)
app.debug = True

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/data-entry', methods=['GET', 'POST'])
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
    app.run()