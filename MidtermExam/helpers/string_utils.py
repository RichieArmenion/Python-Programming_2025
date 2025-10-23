# Converts string to uppercase
def shout(s):
    if not isinstance(s, str):
        return "Invalid input"
    return s.upper()
