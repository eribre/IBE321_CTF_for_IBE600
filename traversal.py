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


# Directory/Path Traversal
@app.route("/traversal")
def traversal():
    return render_template("traversal/traversal.j2")


@app.route("/traversal/confirm", methods=["get"])
def traversal_confirm():
    inp_path = request.args["file"]

    count_dots = inp_path.count("../")
    count_path = inp_path.count("/etc/shadow")

    if count_dots >= 3 and count_path == 1:
        return render_template("traversal/directory.j2", usrInp=inp_path)
    else:
        return render_template("traversal/dir_fail.j2", usrInp=inp_path)


# TODO: Make it so user input that includes valid base paths like /home/ or /etc/
# TODO: will return costumized fail return message.
# TODO: Example: /home/ will return "You may have found something in /home/ but..."

# ! Old directory/path traversal code

# DT redirector
# @app.route("/traversal/redirect", methods=["get"])
# def traversal_redirect():
#    directory = request.args["file"]
#    return redirect(url_for("traversal_conf", directory=directory))

# Directory Traversal Results
# @app.route("/traversal/file/<path:directory>")
# def traversal_conf(directory):
#    if directory == "etc/shadow":
#        return render_template("traversal/directory.j2", usrInp=directory)
#    else:
#        return render_template("traversal/dir_fail.j2", usrInp=directory)
