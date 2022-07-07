from pywebio.input import *
from pywebio.output import *
from pywebio.platform.flask import webio_view
from pywebio.session import run_js
from flask import Flask
import json

from newsdataapi import NewsDataApiClient

app = Flask(__name__)


def generate_guid():
    put_html("<h1>BREAKING NEWS!<h1>")
    put_text(
        "Get the last news about your subject"
    )
    country = select("Choose your country", ["br", "us", "ca"])
    category = select("Choose your language", ["business", "food", "technology"])
    query = input('Search Terms', type=TEXT)

    get_breaking_news(query, category, country)

def get_breaking_news(query, category, country):
    # API key authorization, Initialize the client with your API key
    api = NewsDataApiClient(apikey="pub_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    # You can pass empty or with request parameters {ex. (country = "us")}
    response = api.news_api(q=query, category=category,country = country)

    json_data = response["results"]
    if json_data:
        get_map_table(json_data)

def get_map_table(str_json):
    
    put_html('<ul>')
    for item in str_json:
        put_html('<li><a href="'+item["link"]+'" target="_blank">'+item["title"]+'</a></li>')        
    put_html('</ul>')
    put_button("RESET", onclick=lambda: run_js("window.location.reload()"))
    # Use `put_xxx()` in `put_table()`
    # put_table([
    #     ['Description'],
    #     [put_html(jsn_loads["title"])]
    # ])


app.add_url_rule(
    "/", "webio_view", webio_view(generate_guid), methods=["GET", "POST", "OPTIONS"]
)
app.run(host="0.0.0.0", port=80)
