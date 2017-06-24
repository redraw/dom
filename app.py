from sanic import Sanic
from sanic.log import log
from sanic.response import json, text
from sanic_cors import CORS

import dom

app = Sanic()
CORS(app)


@app.route("/")
async def help(request):
    return text("Use /parse?url=<URL>&selector=<CSS selector>")


@app.route("/parse")
async def parse(request):
    log.info(request.args)

    url = request.args.get('url')
    selector = request.args.get('selector')

    result = await dom.parse(url, selector)

    return text(result, headers={
        "content-type": "application/json"
    })


app.static('/favicon.ico', 'favicon.ico')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)