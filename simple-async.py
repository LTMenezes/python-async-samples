from sanic import Sanic
from sanic.response import json
import asyncpg
import os

app = Sanic()
pool = None

@app.route('/')
async def count(request):
    global pool
    if pool is None:
        pool = await asyncpg.create_pool(os.getenv('CN_STRING'))

    conn = await pool.acquire()
    result = await conn.fetchrow("SELECT * FROM pgbench_accounts LIMIT 1")
    await pool.release(conn)
    return  json({'count': str(result[0])})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
