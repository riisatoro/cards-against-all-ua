import hashlib
import hmac
import os


def hash_password(v):
    """
    Hash the provided password with a pepper salt and return the
    hash to store in the database.
    """
    pepper = os.getenv('SECRET_KEY')
    if not pepper:
        raise ValueError('SECRET_KEY is required')
    pw_hash = hashlib.pbkdf2_hmac('sha256', v.encode(), pepper.encode(), 100000)
    return pw_hash


def is_passwords_match(pw_hash: bytes, password: str) -> bool:
    """
    Check whether the password is correct.
    """
    pepper = os.getenv('SECRET_KEY')
    return hmac.compare_digest(
        pw_hash,
        hashlib.pbkdf2_hmac('sha256', password.encode(), pepper.encode(), 100000)
    )
