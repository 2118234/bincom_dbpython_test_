from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Function to fetch data from the database
def get_data(query=None):
    conn = sqlite3.connect("bincom_test.sqlite", check_same_thread=False)
    cursor = conn.cursor()

    if query:
        cursor.execute("SELECT * FROM sample_table WHERE name LIKE ?", ('%' + query + '%',))  # Filter results
    else:
        cursor.execute("SELECT * FROM sample_table")  # Show all data

    data = cursor.fetchall()
    conn.close()
    return data

# Route for homepage (displaying table & form)
@app.route('/')
def index():
    data = get_data()
    return render_template('index.html', data=data)

# Route to handle form submission
@app.route('/add', methods=['POST'])
def add_entry():
    name = request.form['name']  

    # Insert into database
    conn = sqlite3.connect("bincom_test.sqlite", check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO sample_table (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()

    return redirect('/')  

# Route for search functionality
@app.route('/search')
def search():
    query = request.args.get('query', '')  # Get search query
    data = get_data(query)  # Filter results
    return render_template('index.html', data=data)  # Show filtered table

if __name__ == '__main__':
    app.run(debug=True)
