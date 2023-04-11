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
from helper import dropProtection, orProtection, antiPassCrack


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

    # Block DROP
    if dropProtection(inpUser):
        return "Naughty naughty!  :D"

    if orProtection(inpUser):
        return "'or' statements aren't needed quite yet.  ;D"

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

            # * password cracking challenge
            if ans := antiPassCrack(result[0][1]):
                return ans
            # elif result[0][1] == "Jonathan":
            #    return 'You\'ve the right idea, but maybe try a more "admin"-like username?'
            # elif result[0][1] == "Roger":
            #    return 'You\'ve the right idea, but maybe try a more "rooted" username?'
            # elif result[0][1] == "secUsr":
            #    return 'You\'ve the right idea, but maybe try a more "admin"-like or "rooted" username?'

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

    # Block DROP
    if dropProtection(inpUser):
        return "Naughty naughty!  :D"

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
                # checkList2 = any("admin" in x for x in result)
                if checkList:  # 1 and checkList2:
                    return render_template("sql_injection/sql_return.j2", result=result)
            except:
                pass

            # try:
            #    if result[0][1] == "admin" and result[1][1] == "secUsr":
            #        return render_template("sql_injection/sql_return.j2", result=result)
            # except:
            #    pass

            if result is None:
                return render_template("fail.j2")

            # * password cracking challenge
            if ans := antiPassCrack(result[0][1]):
                return ans

            # * root'-- or admin'-- sql injection challenge
            elif result[0][1] == "root" or result[0][1] == "admin":
                return "You've got the right idea, but you're not quite there yet. :D"

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
