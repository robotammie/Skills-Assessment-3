from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index_page():
    """Show an index page."""

    return render_template("application-form.html")

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")


@app.route("/application", methods=["POST"])
def application_page():
    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    salary = int(request.form.get("salary"))
    job_title = request.form.get("position")

    return render_template("application-response.html",
                           firstname=firstname,
                           lastname=lastname,
                           salary=salary,
                           job_title=job_title)


if __name__ == "__main__":
    app.run(debug=True)
