from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Create an empty list to store registration data
registration_data = []

# Route to the home page
@app.route('/')
def home():
    return render_template('home.html')

# Route to the registration page
@app.route('/registration')
def registration():
    return render_template('registration.html')

# Route to display info page
@app.route('/display_info')
def display_info():
    return render_template('display_info.html', data=registration_data)

# Handle form submission for registration
@app.route('/register', methods=['POST'])
def register():
    name = request.form.get('name')
    address = request.form.get('address')
    phone = request.form.get('phone')
    email = request.form.get('email')
    
    # Store registration data in a dictionary
    registration_data.append({'name': name, 'address': address, 'email': email})

    # Redirect to the display_info page
    return redirect(url_for('display_info'))

if __name__ == '__main__':
    app.run(host="0.0.0.0")