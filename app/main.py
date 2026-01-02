from flask import Flask, render_template
import mysql.connector
import os

app = Flask(__name__)

def get_db_connection():
    # این متغیرها باید از .env بیایند
    return mysql.connector.connect(
        host="db_services", # نام سرویس در داکر کمپوز
        user="root",
        password=os.getenv("MYSQL_ROOT_PASSWORD"),
        database="task_db"
    )

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    # ساخت جدول اگر وجود نداشت (برای راحتی تمرین)
    cursor.execute("CREATE TABLE IF NOT EXISTS tasks (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255))")
    
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    
    cursor.close()
    conn.close()
    return render_template('index.html', tasks=tasks)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)