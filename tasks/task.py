def check_str(s: str):
    """
    Add your code here
    """
    new_s = ''
    for i in s.lower():
        if i.isalnum():
            new_s += i

    new_str = new_s[::-1]
    if new_s == new_str:
        return True
    else:
        return False
