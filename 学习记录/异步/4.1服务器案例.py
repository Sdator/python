import asyncio
from aiohttp import web


async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>Index</h1>')


async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>hello, %s!</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'))


async def init():
    loop = asyncio.get_running_loop()
    app = web.Application()
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/hello/{name}', hello)
    srv = await loop.create_server(app(), '127.0.0.1', 8000)
    print('Server started at http://127.0.0.1:8000...')
    return srv


a = asyncio.run(init())    # loop.run_forever()
print(a)
