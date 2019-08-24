from flask import Flask, jsonify
from psycopg2.pool import SimpleConnectionPool
import os

app = Flask(__name__)
pool = SimpleConnectionPool(3, 20, os.getenv('CNN_STRING'))

@app.route('/')
def count():
    conn = pool.getconn()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM pgbench_accounts LIMIT 1')
    result = str(cursor.fetchone()[0])
    cursor.close()
    pool.putconn(conn)
    return jsonify({'count': result})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
