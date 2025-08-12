import re

def class_number_validator(code):
    if re.match(r"^[a-zA-Z\d\s]{3,30}$",code):
        return True
    else:
        return False

def title_validator(title):
    if re.match(r"^[a-zA-Z\s]{3,30}$",title):
        return True
    else:
        return False