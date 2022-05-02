def is_alphanumeric(v):
    if not v.isalnum():
        raise ValueError('Value should be numeric')
    return v

def is_username_length_valid(v):
    if 20 < len(v) < 3:
        raise ValueError('Username should be from 3 to 20 characters long')

def is_password_length_valid(v):
    if len(v) < 8:
        raise ValueError('Password should contain at least 8 symbols')
