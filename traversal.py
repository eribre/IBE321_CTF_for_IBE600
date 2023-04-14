from __main__ import (
    app,
    Flask,
    render_template,
    request,
    url_for,
    flash,
    redirect,
    re,
)


# Directory Traversal
@app.route("/traversal")
def traversal():
    return render_template("traversal/traversal.j2")


# DT redirector
@app.route("/traversal/redirect", methods=["post"])
def traversal_redirect():
    directory = request.form["file"]
    return redirect(url_for("traversal_conf", directory=directory))


# Directory Traversal Results
@app.route("/traversal/file/<path:directory>")
def traversal_conf(directory):
    if directory == "etc/shadow":
        return render_template("traversal/directory.j2")
    else:
        return render_template("traversal/dir_fail.j2")
