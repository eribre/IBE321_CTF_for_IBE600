from __main__ import re


# Individual protection functions


def dropProtection(inp):
    """Checks for DROP statement in user input."""
    if re.search("drop", inp, re.IGNORECASE) is not None:
        print("'DROP' DETECTED")
        return True


def insertProtection(inp):
    """Checks for INSERT statement in user input."""
    if re.search("insert", inp, re.IGNORECASE) is not None:
        print("'INSERT' DETECTED")
        return "INSERT"


def selectProtection(inp):
    """Checks for SELECT statement in user input."""
    if re.search("select", inp, re.IGNORECASE) is not None:
        print("'SELECT' DETECTED")
        return "SELECT"


def updateProtection(inp):
    """Checks for UPDATE statement in user input."""
    if re.search("update", inp, re.IGNORECASE) is not None:
        print("'UPDATE' DETECTED")
        return "UPDATE"


def orProtection(inp):
    """Checks for 'or' statement in user input."""
    if re.search(" or ", inp, re.IGNORECASE) is not None:
        print("'OR' DETECTED")
        return "OR"


# Main protection functions


def uauthProtect(inp):
    """Checks for sql statements in user input. Returns touple of
    True/False and the statement if True."""
    if drop := dropProtection(inp):
        return True, drop
    elif insert := insertProtection(inp):
        return True, insert
    elif update := updateProtection(inp):
        return True, update
    elif or_ := orProtection(inp):
        return True, or_
    else:
        return False, None


def sql2Protection(inp):
    """Checks for banned sql statement in user input. Returns touple of
    True/False and the banned statement if True."""
    if drop := dropProtection(inp):
        return True, drop
    elif insert := insertProtection(inp):
        return True, insert
    elif update := updateProtection(inp):
        return True, update
    else:
        return False, None


# Other functions


def antiPassCrack(inp):
    """Points the user in the right direction during the
    SQL injection challenges. While user would be able to access
    using SQL injection, this is not the intended solution, an
    would give them the wrong flag."""
    match inp:
        case "Jonathan":
            ans = "You've the right idea, but maybe try a more 'admin'-like username?"
            return ans
        case "Roger":
            ans = "You've the right idea, but maybe try a more 'rooted' username?"
            return ans
        case "secUsr":
            ans = "You've the right idea, but maybe try a more 'admin'-like or 'rooted' username?"
            return ans
