from flask import Flask, render_template, request, url_for, flash, redirect
import re

# from dotenv import load_dotenv

# load_dotenv()


# * Import Database class from dbconnection.py
from dbconnection import Database

# Even though some imports are not used in this specific file, they may be used in other files.

# Easy access variables [Password vars from older versions]
storedUser = "Roger"
storedPass = "Password1"
secUser = "secUsr"
secPass = "blowfish"
hintUser = "Jonathan"
hintPass = "12345"

app = Flask(__name__)

# base file
from base import *

# files separated by category/challenge
from crypto import *
from traversal import *
from pass_crack import *
from sql_injection import *

port = 81
host = "0.0.0.0"
debug = True

if __name__ == "__main__":
    app.run(host, port, debug)

# * All computer IPs
# app.run(host="0.0.0.0", port=port)

# * Localhost
# if __name__ == "__main__":
#    app.run(port=port)
