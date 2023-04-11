from __main__ import (
    app,
    Flask,
    render_template,
    request,
    url_for,
    flash,
    redirect,
    re,
    Database,
    storedUser,
    storedPass,
    secUser,
    secPass,
    hintUser,
    hintPass,
)


# * caesar cipher
@app.route("/cipher")
def cipher():
    return render_template("crypto/cipher.j2")


# * Hash SHA256
@app.route("/hash")
def hash():
    return render_template("crypto/hash.j2")


# * Hash MD5
@app.route("/hash2")
def hash2():
    return render_template("crypto/hash2.j2")
