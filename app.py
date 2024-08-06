from flask import Flask, request, redirect, url_for, render_template
import psycopg2

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        port = 5433,
        user="postgres",
        password="root"
    )
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    age = request.form['age']

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO users (name, age) VALUES (%s, %s)', (name, age))
    conn.commit()
    cur.close()
    conn.close()

    return redirect(url_for('display'))

@app.route('/display')
def display():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM users')
    users = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('display.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
