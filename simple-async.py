from sanic import Sanic
from sanic.response import json
import asyncpg
import os

app = Sanic()


@app.route('/')
async def count(request):
    conn = await asyncpg.connect(os.getenv('CN_STRING'))
    result = await conn.fetchrow("SELECT COUNT(*) FROM pgbench_accounts")
    return  json({'count': str(result[0])})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
