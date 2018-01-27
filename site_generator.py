import json
import os

from jinja2 import Template
import markdown


def load_file(filename):
    with open(filename, 'r') as file:
        return file.read()


def render_index_page(json_data, html):
    articles = json_data['articles']
    topics = json_data['topics']
    template = Template(html)
    return template.render(articles=articles, topics=topics)


if __name__ == '__main__':
    json_data = json.loads(load_file('config.json'))
    html = load_file('templates/index.html')
    render = render_index_page(json_data, html)
