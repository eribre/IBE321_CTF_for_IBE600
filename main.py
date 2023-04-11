from flask import Flask, render_template, request, url_for, flash, redirect
import re
from dbconnection import Database
from helper import dropProtection

# Even though some imports are not used in this specific file, they may be used in other files.

# Easy access variables [Password vars from older versions]
storedUser = "Roger"
storedPass = "Password1"
secUser = "secUsr"
secPass = "blowfish"
hintUser = "Jonathan"
hintPass = "12345"

app = Flask(__name__)

from base import *

# from Level1 import *
# from Level2 import *
# from Level3 import *

from crypto import *
from pass_crack import *
from sql_injection import *

port = 81
host = "0.0.0.0"

if __name__ == "__main__":
    app.run(host=host, port=port)
