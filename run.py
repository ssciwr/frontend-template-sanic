# !/usr/bin/env python
import os
import sys

from sanic import Sanic
from sanic.response import html, json, redirect

# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from views import panel_bp

app = Sanic(__name__)
app.config.WEBSOCKET_MAX_SIZE = 2 ** 20
app.config.WEBSOCKET_MAX_QUEUE = 32
app.config.WEBSOCKET_READ_LIMIT = 2 ** 16
app.config.WEBSOCKET_WRITE_LIMIT = 2 ** 16
app.config.WEBSOCKET_PING_INTERVAL = 20
app.config.WEBSOCKET_PING_TIMEOUT = 20

app.blueprint(panel_bp)


@app.route('/', methods=["POST", "GET"])
async def index(request):
    # generate a URL for the endpoint `post_handler`
    return redirect('/panel')


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)
