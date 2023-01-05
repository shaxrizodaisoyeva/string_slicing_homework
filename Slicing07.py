def main(s,n):
    """
    The s string variable is given. return all characters except n characters at the end.
    Args:
        s(str): parameter
        n(int): parameter
    Returns:
        str: answer
    """
    a=len(s)
    if a==n:
        x="" 
    else:
        x=s[0:(a-n)]
    return x