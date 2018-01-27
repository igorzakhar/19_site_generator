import json
import os

from jinja2 import Environment, FileSystemLoader
import markdown


def load_file(filename):
    with open(filename, 'r') as file:
        return file.read()


def save_file(data):
    with open('index_render.html', 'w') as file:
        file.write(data)


def render_index_page(json_data, template):
    articles = json_data['articles']
    topics = json_data['topics']
    return template.render(articles=articles, topics=topics)


def get_templates():
    env = Environment(loader=FileSystemLoader('templates'))
    index_template = env.get_template('index.html')
    artice_template = env.get_template('article.html')
    return index_template, artice_template


if __name__ == '__main__':
    json_data = json.loads(load_file('config.json'))
    html = load_file('templates/index.html')
    index_html, article_html = get_templates()
    render = render_index_page(json_data, index_html)
    save_file(render)
