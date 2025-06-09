from flask import Flask, request, redirect, url_for, render_template

# This list stores the to-do items. Because this list is in memory, it will
# reset every time the application restarts. A production-grade application
# would use another medium to store to-do items, like a database.
todos = []

app = Flask(__name__)

@app.route("/")
def index():
    # A template is identified by its path relative from the `templates`
    # directory. Usually, a template needs extra data to correctly render. In
    # this case, we pass the to-do list to the template. Inside the template,
    # the to-do list is accessible through the `todos` variable.  Flask handles
    # the HTTP GET request and returns the rendered HTML as the response.
    return render_template("index.html", todos=todos)


@app.route("/add", methods=["POST"])
def add():
    # This route only responds to POST requests. Accessing this route from the
    # web browser, which generates a GET request to "http://localhost:5000/add",
    # will result in a 405 Method Not Allowed response.
    #
    # The special variable `request`, imported from the `flask` module,
    # represents the current request processed by your application. This
    # variable contains all kinds of information about the request, including
    # the form data that a web `<form>` sends. The `request.form` is a
    # dictionary that maps the form fields to their corresponding values.
    #
    # This function performs just a minimal validation of its input: if the
    # to-do item is empty, nothing is added to the list. In more complex
    # applications, validation on the server-side is very important and usually
    # a great source of bugs. Always pay attention to how you validate user
    # input on the server!
    #
    # Finally, whether we add a to-do item to the list or not, this handler
    # responds with a 302 Found response, commonly known as a "redirect". When
    # the browser receives a 302 response, it makes another HTTP request to the
    # path provided in the Location header. In this example, we are using the
    # url_for() function to retrieve the path of the handler for the `"index"`
    # function. This mechanism allows us to change the path associated to a
    # handler without rewriting every part of the application that hardcodes
    # that path.
    #
    # We use a redirect after handling the POST request (the post/redirect/get
    # pattern). This prevents duplicate submissions if the user refreshes the
    # page, because the browser will perform a GET request to the main page
    # instead of resubmitting the form data. See more about this pattern:
    #
    # https://en.wikipedia.org/wiki/Post/Redirect/Get
    item = request.form.get("item")
    if item:
        todos.append(item)
    return redirect(url_for("index"))


@app.route("/done/<int:index>", methods=["POST"])
def done(index):
    # This is another handler that only responds to POST requests. This time,
    # though, the handler is responsible for marking a to-do item as "done". In
    # this application, this means removing the to-do item from the list.
    #
    # The index of the to-do item is passed as part of the request path. Every
    # string in a path in the form `<index>` is used as a wildcard to match
    # multiple requests with similar paths. In this example, this handler is
    # invoked when the request path is `/done/0`, `/done/99`, etc. Flask gives
    # the value of the placeholder `<index>` to the parameter with the same
    # name. For more information, see:
    #
    # https://flask.palletsprojects.com/en/stable/quickstart/#variable-rules
    #
    # After validating the index and maybe removing a to-do item from the list,
    # we issue a redirect to the index page of the application.
    if 0 <= index < len(todos):
        todos.pop(index)
    return redirect(url_for("index"))
