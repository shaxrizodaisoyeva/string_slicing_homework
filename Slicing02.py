def main(s):
    """
    The s string variable is given. return four characters from the end.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    a=len(s)
    b=s[(a-4):a]
    return b
s="abcdefaziz"
print(main(s))