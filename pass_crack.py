from __main__ import (
    app,
    render_template,
    request,
    Database,
    storedUser,
    storedPass,
    secUser,
    secPass,
    hintUser,
    hintPass,
)

from helper import dropProtection, orProtection, uauthProtect


# Password-Breaking Challenge
@app.route("/uauth")
def uauth():
    return render_template("pass_crack/uauth.j2")


# Confirms uauth input
@app.route("/confirm", methods=["post"])
def confirm():
    # Get user input
    inpUser = request.form["username"]
    inpPass = request.form["passwd"]
    print(f"{inpUser} as input for password cracking challenge.")

    # Block DROP
    # if re.search("drop", inpUser, re.IGNORECASE) is not None:
    #    return "Naughty naughty!  :D"

    # * Block DROP and OR (and more dangerous sql statements)
    # if dropProtection(inpUser):
    #    return "Naughty naughty!  :D"
    # if orProtection(inpUser):
    #    return "'or' statements aren't needed quite yet.  ;D"
    ret = uauthProtect(inpUser)
    if ret[0]:
        return f"{ret[1]} statements aren't needed here.  ;D"

    # Connect to DB
    try:
        with Database() as db:
            # * Verify input / Give user their result
            # Secure against SQL injection
            result = db(
                "SELECT * FROM users WHERE name=? AND password=?", (inpUser, inpPass)
            )
            result = result.fetchall()
            print(result)

            if result is None:
                return render_template("fail.j2")

            # * password cracking challenge
            elif result[0][1] == "Jonathan":
                return render_template("pass_crack/hintUser.j2", username=hintUser)
            elif result[0][1] == "Roger":
                return render_template("pass_crack/success.j2", username=storedUser)
            elif result[0][1] == "secUsr":
                return render_template("pass_crack/super_secret.j2", username=secUser)

            # * fail condition
            else:
                return render_template("fail.j2")

        # All this is very messy, but it makes it so that users can perform basic SQL injection
        # using "username' -- " without double quotes

    # incase kind of break
    except IndexError as indErr:
        print(indErr)
        return render_template("fail.j2")
    # incase things REALLY break
    except Exception as ex:
        print(ex)
        return "Congrats! You crashed the server..."
