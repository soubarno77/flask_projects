from flask import Flask, render_template, abort

app = Flask(__name__)

# Routes
@app.route('/')
def index():
    return render_template('index.html')

# 404 Error Handler
@app.errorhandler(404)
def page_not_found(error):

    """
    - Renders the error.html in case any other route is hit via URL
    - Displays the appropriate 404 error message as a fallback
    """
    return render_template('error.html', error_code=404, error_message='Page Not Found'), 404

@app.route('/simulate_500')
def simulate_error():
    """
    - Simulates 500 internal error by performing invalid division by zero
    - Renders 500.html to see the result
    """
    try:
        div_res = 1/0

        # This return will be unreachable
        return {
            'division_result': 'success'
        }
    
    except Exception as e:
        abort(500)

# 500 Error Handler
@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html', error_code=500, error_message='Internal Server Error'), 500

if __name__ == '__main__':
    app.run(debug=True)
