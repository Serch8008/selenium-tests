from unittest.mock import patch, Mock
import requests

def obtener_datos_usuario(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()
    return None


@patch("tests.test_api_mock.requests.get")
def test_mock_api_exitoso(mock_get):
    # Simular respuesta exitosa
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"id": 1, "username": "sergio", "email": "sdet@test.com"}

    mock_get.return_value = mock_response

    result = obtener_datos_usuario(1)
    assert result["username"] == "sergio"
    assert result["email"] == "sdet@test.com"
    print("✅ Mock API exitoso")


@patch("tests.test_api_mock.requests.get")
def test_mock_api_falla(mock_get):
    # Simular error 404
    mock_response = Mock()
    mock_response.status_code = 404
    mock_get.return_value = mock_response

    result = obtener_datos_usuario(99)
    assert result is None
    print("⚠️ Mock API falló correctamente (404)")
