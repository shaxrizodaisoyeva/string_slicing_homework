def main(s):
    """
    The s string variable is given. return the characters in the odd position.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    a=len(s)
    return s[1:(a-1):2]