import requests

def test_get_public_api():
    """
    Prueba un endpoint público: GET y validación básica del JSON.
    """
    url = "https://jsonplaceholder.typicode.com/users/1"
    response = requests.get(url)

    # Validaciones básicas
    assert response.status_code == 200, f"❌ Status inesperado: {response.status_code}"
    data = response.json()
    assert "username" in data, "❌ No se encontró la clave 'username'"
    assert "email" in data, "❌ No se encontró la clave 'email'"

    print(f"✅ Usuario: {data['username']} | Email: {data['email']}")


def test_post_api():
    """
    Simula creación de un recurso (POST).
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {"title": "pytest demo", "body": "API post test", "userId": 1}
    response = requests.post(url, json=payload)

    assert response.status_code == 201, f"❌ Status inesperado: {response.status_code}"
    data = response.json()
    assert data["title"] == "pytest demo"
    print(f"✅ POST creado con ID: {data['id']}")
