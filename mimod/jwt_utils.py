import jwt
from datetime import datetime, timedelta, timezone

def generar_token_hs256(payload_base: dict, secret: str, exp_seconds: int = 300) -> str:
    payload = {
        **payload_base,
        "iat": datetime.now(timezone.utc),
        "exp": datetime.now(timezone.utc) + timedelta(seconds=exp_seconds),
    }
    return jwt.encode(payload, secret, algorithm="HS256")

def validar_token_hs256(token: str, secret: str) -> dict | None:
    try:
        return jwt.decode(token, secret, algorithms=["HS256"])
    except jwt.exceptions.ExpiredSignatureError:
        # Token expirado
        return None
    except jwt.exceptions.InvalidTokenError:
        # Firma inválida, token mal formado, etc.
        return None
