from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Set up MySQL database connection
mydb = mysql.connector.connect(
  host="localhost",
  user="soub",
  password="password",
  database="my_db"
)
mycursor = mydb.cursor()

@app.route('/')
def index():

    """
     - Shows all available items present in database
    """

    mycursor.execute('SELECT * FROM items')
    items = mycursor.fetchall()
    return render_template('index.html', items=items)

@app.route('/add_item', methods=['POST'])
def add_item():
    """
    - Adds a specific item in database
    - Uses form data from HTML
    """
    if request.method == 'POST':
        item_name = request.form['item_name']
        mycursor.execute('INSERT INTO items (name) VALUES (%s)', (item_name,))
        mydb.commit()
    return redirect(url_for('index'))

@app.route('/update_item/<int:item_id>', methods=['GET', 'POST'])
def update_item(item_id):
    if request.method == 'POST':
        new_name = request.form['new_name']
        # Update the item in the MySQL database
        update_query = "UPDATE items SET name = %s WHERE id = %s"
        update_data = (new_name, item_id)
        mycursor.execute(update_query, update_data)
        mydb.commit()
        return redirect(url_for('index'))
    else:
        # Handle the GET request to show the item's details and edit form
        select_query = "SELECT * FROM items WHERE id = %s"
        select_data = (item_id,)
        mycursor.execute(select_query, select_data)
        item = mycursor.fetchone()
        mydb.commit()
        return render_template('edit_item.html', item=item)

@app.route('/delete_item/<int:item_id>')
def delete_item(item_id):
    mycursor.execute('DELETE FROM items WHERE id = %s', (item_id,))
    mydb.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
