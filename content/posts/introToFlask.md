title: Making your first website with Flask
subtitle: How hard could it be to make a website with Python?
date: 2018-11-05
author: Eric Zhang
image: post-bg.jpg

### Setting up your environment
----

If you are running Windows, go to [link](http://timmyreilly.azurewebsites.net/python-flask-windows-development-environment-setup/) to set up all the tools you will need for this tutorial. 

Now that your environment is set up. We can begin to write the code.

### Getting Started
----

1. First, create a directory that will contain all of your files for the website. This ensures that the other files on your computer will not interfere. 

2. Inside your directory, you will need to create another directory titled `templates`, which will contain all of your html       code.

An example of an index html can look like this:

<pre>
    &lt;html&gt;
    &lt;body&gt;
      &lt;header&gt;
        &lt;div class="containter"&gt;
            &lt;h1 class="logo"&gt;Your First Website&lt;/h1&gt;
            &lt;strong&gt;&lt;nav&gt;
              &lt;ul class="menu"&gt;
                &lt;li&gt;&lt;a href="{{ url_for('home') }}"&gt;Home&lt;/a&gt;&lt;/li&gt;
              &lt;/ul&gt;
            &lt;/nav&gt;&lt;/strong&gt;
        &lt;/div&gt;
      &lt;/header&gt;
      &lt;div class="container"&gt;
          {% block content %}
          {% endblock %}
      &lt;/div&gt;
    &lt;/body&gt;
    &lt;/html&gt;
</pre>

### Writing the Driver Code
----

The `{%  %}` characters indicates that there are parameters being passed in to the function. This is a simple template for our navigating system where the middle block will be replaced with different html blocks depending on the URL that the user chose.

To instruct the html that you are continuing from the index html, add the following block:

    {% extends "index.html" %}
    {% block content %}
      <div class="home">
       <h1>My home page</h1>
       <p>These middle sections can always change</p>
      </div>
    {% endblock %}

The `{% extends %}` characteers basically tells the compiler to pass into the index html, and the ``{% block content %}`` and the `{% endblock %}` indicates the part that will be passed on.

### Using Flask

Now that all of the the basic html for the website is set up, you can begin to start implementing Flask. 

Outside of the template directory, create a python file that will create the website for you. In this case, I will call it `app.py`.

A simple website can have a python file look something like this:

    from flask import Flask, render_template
    app = Flask(__name__)
    @app.route('/')
    def index()
        return render_template('index.html')
    if __name__ = '__main__':
        app.run(debug=True)

It is very important that you _do not_ import **everything** from flask, as it is a very big library. The third line tells Flask where to look for templates, static files, and so on. The `@app.route` is a decorator, which allows you to implement the html.

You can do a lot of neat things with html, flask and css. This is only the tip of the iceberg.
