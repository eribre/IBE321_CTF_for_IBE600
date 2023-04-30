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
from helper import (
    dropProtection,
    orProtection,
    antiPassCrack,
    uauthProtect,
    sql2Protection,
)


# * Sql injection level 1
@app.route("/uauth1")
def uauth1():
    return render_template("sql_injection/uauth1.j2")


@app.route("/confirm1", methods=["post"])
def confirm1():
    # Get user input
    inpUser = request.form["username"]
    inpPass = request.form["passwd"]
    print(f"{inpUser} as input for sql injection level 1.")

    # * Block DROP and OR (and more dangerous sql statements)
    ret = uauthProtect(inpUser)
    if ret[0]:
        return f"{ret[1]} statements aren't needed here.  ;D"

    # Connect to DB
    try:
        with Database() as db:
            # * Verify input / Give user their result
            result = db(
                f"SELECT * FROM users WHERE name='{inpUser}' AND password='{inpPass}'"
            )
            result = result.fetchall()
            print(result)

            if result is None:
                return render_template("fail.j2")

            # * password cracking challenge blocker
            if ans := antiPassCrack(result[0][1]):
                return ans

            # * root'-- or admin'-- sql injection challenge
            elif result[0][1] == "root" or result[0][1] == "admin":
                if result[0][1] == "root":
                    return render_template("sql_injection/root.j2", username="root")
                elif result[0][1] == "admin":
                    return render_template("sql_injection/root.j2", username="admin")
                else:
                    return render_template("fail.j2")

            # * fail condition
            else:
                return render_template("fail.j2")

        # All this is very messy, but it makes it so that users can perform basic SQL injection
        # using "username' -- " without double quotes

    # incase kind of break
    except IndexError as indErr:
        print(indErr)
        return render_template("fail.j2")
    except Exception as ex:
        # if user tries invalid SQL injection syntax
        if str(ex) == "'OperationalError' object has no attribute 'fetchall'":
            return "You've got the right idea, but you're not quite there yet. :D"
        else:
            # incase things REALLY break
            print(ex)
            return "Congrats! You crashed the server..."


# * Sql injection level 2
@app.route("/uauth2")
def uauth2():
    return render_template("sql_injection/uauth2.j2")


@app.route("/confirm2", methods=["post"])
def confirm2():
    # Get user input
    inpUser = request.form["username"]
    inpPass = request.form["passwd"]
    print(f"{inpUser} as input for sql injection level 2.")

    # * Block DROP (and more dangerous sql statements)
    ret = sql2Protection(inpUser)
    if ret[0]:
        return f"{ret[1]} statements aren't needed here.  ;D"

    # Connect to DB
    try:
        with Database() as db:
            # * Verify input / Give user their result
            result = db(
                f"SELECT * FROM users WHERE name='{inpUser}' AND password='{inpPass}'"
            )
            result = result.fetchall()
            print(result)

            # * Return the flag if user successfully returns all user info
            try:
                checkList = any("root" in x for x in result) and any(
                    "admin" in x for x in result
                )
                if checkList:
                    return render_template("sql_injection/sql_return.j2", result=result)
            except:
                pass

            if result is None:
                return render_template("fail.j2")

            # * password cracking challenge blocker
            if ans := antiPassCrack(result[0][1]):
                return ans

            # * root'-- or admin'-- sql injection challenge
            elif result[0][1] == "root" or result[0][1] == "admin":
                return "You've got the right idea, but you're not quite there yet. :D"

            # * fail condition
            else:
                return render_template("fail.j2")

    # incase kind of break
    except IndexError as indErr:
        print(indErr)
        return render_template("fail.j2")

    except Exception as ex:
        # if user tries invalid SQL injection syntax
        if str(ex) == "'OperationalError' object has no attribute 'fetchall'":
            return "You've got the right idea, but you're not quite there yet. :D"
        else:
            # incase things REALLY break
            print(ex)
            return "Congrats! You crashed the server..."
