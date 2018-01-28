import json
import os

from jinja2 import Environment, FileSystemLoader
import markdown


BASE_DIR = 'articles/'
SITE_DIR = 'site/'


def load_file(filename):
    with open(filename, 'r') as file:
        return file.read()


def save_file(filename, data):
    path_for_save = os.path.dirname(filename)
    if not os.path.exists(path_for_save):
        os.makedirs(path_for_save)
    with open(filename, 'w') as file:
        file.write(data)


def get_templates():
    env = Environment(loader=FileSystemLoader('templates'))
    index_template = env.get_template('index.html')
    artice_template = env.get_template('article.html')
    return index_template, artice_template


def render_index_page(json_data, template):
    articles = json_data['articles']
    topics = json_data['topics']
    return template.render(articles=articles, topics=topics)


def render_article_page(content, template):
    return template.render(content)


def main():
    json_data = json.loads(load_file('config.json'))
    index_template, article_template = get_templates()

    index_html = render_index_page(json_data, index_template)
    save_file('./index.html', index_html)

    for article in json_data['articles']:
        article_file = BASE_DIR + article['source']
        html = markdown.markdown(load_file(article_file))
        article_html = render_article_page(
            {'title': article['title'], 'html': html},
            article_template
        )
        save_path = SITE_DIR + article['source'].replace('md', 'html')
        save_file(save_path, article_html)


if __name__ == '__main__':
    main()
