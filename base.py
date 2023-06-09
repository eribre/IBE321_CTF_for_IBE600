from main import (
    app,
    render_template,
    re,
)


# from dotenv import load_dotenv

# load_dotenv()


sqladmin = re.compile(
    "^([a-zA-Z0-9]*('|\") (or|OR) (')?(([a-zA-Z0-9]*)(\\4)?=(\\4)?\\6\\b)(\\4)?(;)?--)$"
)
sqlroot = re.compile("^(admin('|\")(;)?--)$")


# Level imports
# from Level1 import *
# from Level2 import *
# from Level3 import *


@app.route("/")
def index():
    return render_template("index.j2")


# hidden password and steganography
@app.route("/about")
def about():
    return render_template("about.j2")


# Base64 Decoding
@app.route("/base64")
def base64():
    return render_template("base64.j2")


# BAD PATH
@app.route("/admin")
def admin():
    return render_template("admin.j2")
