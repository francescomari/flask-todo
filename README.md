# To-Do List in Flask

This is a simple web application for managing a to-do list, built using
[Flask](https://flask.palletsprojects.com/). The application demonstrates the
basics of handling web requests, rendering HTML templates, and serving static
files. All to-do items are stored in memory, so they will be lost when the
server restarts.

## Prerequisites

This repository builds on the concepts explained in [Introduction to
Flask](https://github.com/francescomari/flask-introduction), which will not be
repeated here. Moreover, you can set up and run the application in the same way,
so this tutorial doesn't explain how to install the dependencies or run this
application.

## Directory structure

The to-do application introduces some new concepts and expands on the typical
structure of the Flask application:

- `app.py`: Contains the Python code for the web application, including route
  handlers and logic for managing the to-do list.
- `templates/`: This folder contains HTML files that are used as templates. Flask
  uses these templates to generate the web pages you see in your browser. The
  `index.html` file uses Jinja syntax (e.g., `{{ ... }}` and `{% ... %}`) to
  insert dynamic content.
- `static/`: This folder is for static files like images, icons, or CSS. The
  favicon for the site is stored here. Flask automatically serves files from this
  directory at the `/static/` URL path.

## The rest of the code

Pay attention to both [the application code](app.py) and the [web application
template](templates/index.html). The application code defines all the routes
that the application responds to, while the template is responsible for
dynamically rendering the HTML of the web application depending on the to-do
list. Read those files for many more comments!
