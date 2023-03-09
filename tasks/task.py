def check_str(s: str):
    """
    Add your code here
    """
    new_str = s[::-1]
    if s == new_str:
        return True
    else:
        return False
