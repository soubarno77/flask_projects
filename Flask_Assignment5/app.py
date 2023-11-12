from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Simulated user data
"""
-  These are some dummy usernames
- For example, while logging in, use 'user1' as username
- It will store the session of Alice and show their email ID
"""
users = {
    'user1': {'name': 'Alice', 'email': 'alice@example.com'},
    'user2': {'name': 'Bob', 'email': 'bob@example.com'},
}

@app.route('/')
def index():
    if 'username' in session:
        user = users.get(session['username'])
        return render_template('profile.html', user=user)
    return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        if username in users:
            session['username'] = username
            return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
