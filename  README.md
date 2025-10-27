## Selenium Tests — Python + Pytest Framework

## Este proyecto contiene una suite de pruebas automatizadas desarrolladas en **Python** con **Pytest** y **Selenium**, organizada bajo el patrón **Page Object Model (POM)**.

<!-- │selenium-tests/
├── pages/ # Clases Page Object (mapean pantallas)
│ └── login_page.py
│
├── mimod/ # Clientes o módulos auxiliares
│ └── api_client.py
│
├── tests/ # Casos de prueba
│ ├── test_login.py # Pruebas UI
│ ├── test_api_httpbin.py # Ejemplo API
│ └── test_api_client_mock.py
│
├── .github/workflows/ # Integración CI/CD (GitHub Actions)
│ └── python-tests.yml
│
├── requirements.txt # Dependencias del entorno virtual
├── pytest.ini # Configuración de pytest
└── README.md # Este archivo -->

## ⚙️ Instalación y configuración

 1️⃣ Crear entorno virtual
```bash
python -m venv .venv
source .venv/bin/activate    # Mac/Linux
# .venv\Scripts\activate     # Windows
pip install -r requirements.txt

### Pruebas locales
pytest -v

### Generar reporte HTML
pytest --html=reports/report.html --self-contained-html

### Pruebas específicas
pytest tests/test_login.py::test_login_exitoso -v

# Integración continua (CI/CD)
# El pipeline de GitHub Actions se ejecuta automáticamente en cada push o pull request.

# Incluye:
# Instalación de dependencias.
# Ejecución de pruebas Pytest.
# Generación de reportes.
# Archivo: .github/workflows/python-tests.yml

# Tecnologías principales

# Python 3.12
# Pytest
# Selenium WebDriver
# Requests / Mock
# GitHub Actions

## Autor

# Sergio Ávila Espinosa
# QA Automation Engineer / SDET
# 📧 sergioavilaespinosa@gmail.com