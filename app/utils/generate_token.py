import jwt


def generate_token(payload: dict, secret: str) -> str:
    token = jwt.encode(payload, secret, algorithm="HS256")
    return token
