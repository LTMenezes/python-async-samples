from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)


@app.route('/')
def count():
    conn = psycopg2.connect(os.getenv('CNN_STRING'))
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM pgbench_accounts')
    return jsonify({'count': str(cursor.fetchone()[0])})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
