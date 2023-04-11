from __main__ import re


def dropProtection(inp):
    """Checks for DROP statement in user input."""
    if re.search("drop", inp, re.IGNORECASE) is not None:
        print("'DROP' DETECTED")
        return True


def orProtection(inp):
    """Checks for 'or' statement in user input."""
    if re.search(" or ", inp, re.IGNORECASE) is not None:
        print("'OR' DETECTED")
        return True


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
