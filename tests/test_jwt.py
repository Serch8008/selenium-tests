import time
from mimod.jwt_utils import generar_token_hs256, validar_token_hs256

SECRET = "clave_super_secreta"

def test_jwt_valido():
    token = generar_token_hs256({"user": "sergio", "role": "SDET"}, SECRET, exp_seconds=5)
    data = validar_token_hs256(token, SECRET)
    assert data is not None
    assert data["user"] == "sergio"
    assert data["role"] == "SDET"

def test_jwt_expirado():
    token = generar_token_hs256({"user": "sergio"}, SECRET, exp_seconds=1)
    time.sleep(2)
    data = validar_token_hs256(token, SECRET)
    assert data is None, "Debería ser None cuando expira"

def test_jwt_invalido():
    token = generar_token_hs256({"user": "sergio"}, SECRET, exp_seconds=60)
    # Validar con otra clave
    data = validar_token_hs256(token, "otra_clave")
    assert data is None, "Debería ser None cuando la firma no coincide"
