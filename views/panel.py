#!/usr/bin/env python
import sys

from feedparser import parse
from jinja2 import Environment, PackageLoader, select_autoescape
from sanic import Blueprint
from sanic.response import html, text
from test.ssctest import circle_area
from config import CONFIG

sys.path.append('../')

# enable async 3.6+
enable_async = sys.version_info >= (3, 6)

panel_bp = Blueprint('ssc_user_panel', url_prefix='panel')
panel_bp.static('/statics/html', CONFIG.BASE_DIR + '/statics/html')

# jinjia2 config
env = Environment(
    loader=PackageLoader('views.panel', '../templates/html'),
    autoescape=select_autoescape(['html', 'xml', 'tpl']),
    enable_async=enable_async)


async def template(tpl, **kwargs):
    template = env.get_template(tpl)
    rendered_template = await template.render_async(**kwargs)
    return html(rendered_template)

@panel_bp.route("/", methods=["POST", "GET"])
async def index(request):
    flash_text = ""
    if request.method == "POST":
        radius_text = request.form.get('radius')
        if radius_text.isdigit():
            radius = int(radius_text)
            area = circle_area(radius)
            flash_text = "circle area for radius " + str(radius) + " is " + str(area)
        else:
            flash_text = radius_text + " is not a valid radius"

    return await template('index.html', flash_text=flash_text)

