from sanic import Sanic
from sanic.response import json, text

import dom

app = Sanic()


@app.route("/")
async def help(request):
    return text("Use /parse?url=<URL>&select=<CSS selector>")


@app.route("/parse")
async def parse(request):
    url = request.args.get('url')
    select = request.args.get('select')

    result = await dom.parse(url, select)

    return text(result, headers={
        "content-type": "application/json"
    })


app.static('/favicon.ico', 'favicon.ico')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)