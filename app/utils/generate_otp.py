import secrets


def generate_otp() -> int:
    return secrets.randbelow(900000) + 100000
