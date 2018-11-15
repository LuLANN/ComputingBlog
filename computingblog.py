#! usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Manages all the routes for the website

Author: ndesai (Nishkrit)
"""

from constants import *
from external_redirects import slack_invite
from process_posts import *

import sys
import os

from flask import Flask, render_template, send_from_directory, redirect
from flask_flatpages import FlatPages, pygments_style_defs
from flask_frozen import Freezer

app = Flask(__name__)
flatpages = FlatPages(app)
freezer = Freezer(app)
app.config.from_object(__name__)


@app.route('/')
@app.route("/posts/")
def index():
    posts = process_articles(flatpages)
    return render_template('index.html', posts=posts)


@app.route('/posts/<name>/')
def post(name):
    path = '{}/{}'.format(POST_DIR, name)
    post = flatpages.get_or_404(path)
    #Find out if there is a notebook included with the markdown file. If so, include it with the webpage
    #Must have a way of giving the needed notebook to the page, if needed
    try:
        return render_template('postNotebook.html', post=post)
    except:
        return render_template('post.html', post=post)


@app.route('/about')
def about():
    post = get_about_post(flatpages)
    return render_template('about.html', post=post)


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                            'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/content/notebooks/<path:filename>')
def getNotebook(filename):
    return send_from_directory(os.path.join(app.root_path, 'content/notebooks'), filename)


@app.route('/slack')
def slack_link():
    link = slack_invite()
    return redirect(link)


@app.route('/content/images/<path:filename>')
def get_banner_image(filename):
    return send_from_directory(MEDIA_DIRECTORY, filename)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(ssl_context='adhoc')
