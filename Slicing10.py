def main(s,n,k):
    """
    The s string variable is given. return from index n to index k.
    Args:
        s(str): parameter
        n(int): parameter
        k(int): parameter
    Returns:
        str: answer
    """
    if n==k:
        a=s[n]
    elif s=="":
        a=""
    else:
        a=s[n:k]
    return a