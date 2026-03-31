# tests/integration/test_fastapi_calculator.py

import pytest  # Import the pytest framework for writing and running tests
from fastapi.testclient import TestClient  # Import TestClient for simulating API requests
from main import app  # Import the FastAPI app instance from your main application file

# ---------------------------------------------
# Pytest Fixture: client
# ---------------------------------------------

@pytest.fixture
def client():
    """
    Pytest Fixture to create a TestClient for the FastAPI application.

    This fixture initializes a TestClient instance that can be used to simulate
    requests to the FastAPI application without running a live server.
    """
    with TestClient(app) as client:
        yield client  # Provide the TestClient instance to the test functions


# ==============================================
# Tests for the GET / (Root) Endpoint
# ==============================================

def test_root_endpoint(client):
    """
    Test the Root Endpoint.

    Verifies that the GET / endpoint returns a 200 status code and serves
    the HTML template containing the calculator interface.
    """
    response = client.get('/')
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    assert "Hello World" in response.text, "Homepage should contain 'Hello World'"
    assert "Calculator" in response.text, "Homepage should contain the Calculator section"


# ==============================================
# Tests for the POST /add Endpoint
# ==============================================

def test_add_api(client):
    """
    Test the Addition API Endpoint with positive integers.
    """
    response = client.post('/add', json={'a': 10, 'b': 5})
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    assert response.json()['result'] == 15, f"Expected result 15, got {response.json()['result']}"


def test_add_api_negative_numbers(client):
    """
    Test the Addition API Endpoint with negative numbers.
    """
    response = client.post('/add', json={'a': -10, 'b': -5})
    assert response.status_code == 200
    assert response.json()['result'] == -15


def test_add_api_floats(client):
    """
    Test the Addition API Endpoint with floating-point numbers.
    """
    response = client.post('/add', json={'a': 2.5, 'b': 3.7})
    assert response.status_code == 200
    assert response.json()['result'] == pytest.approx(6.2)


def test_add_api_zeros(client):
    """
    Test the Addition API Endpoint with zeros.
    """
    response = client.post('/add', json={'a': 0, 'b': 0})
    assert response.status_code == 200
    assert response.json()['result'] == 0


# ==============================================
# Tests for the POST /subtract Endpoint
# ==============================================

def test_subtract_api(client):
    """
    Test the Subtraction API Endpoint with positive integers.
    """
    response = client.post('/subtract', json={'a': 10, 'b': 5})
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    assert response.json()['result'] == 5, f"Expected result 5, got {response.json()['result']}"


def test_subtract_api_negative_result(client):
    """
    Test the Subtraction API Endpoint producing a negative result.
    """
    response = client.post('/subtract', json={'a': 5, 'b': 10})
    assert response.status_code == 200
    assert response.json()['result'] == -5


def test_subtract_api_floats(client):
    """
    Test the Subtraction API Endpoint with floating-point numbers.
    """
    response = client.post('/subtract', json={'a': 10.5, 'b': 3.2})
    assert response.status_code == 200
    assert response.json()['result'] == pytest.approx(7.3)


# ==============================================
# Tests for the POST /multiply Endpoint
# ==============================================

def test_multiply_api(client):
    """
    Test the Multiplication API Endpoint with positive integers.
    """
    response = client.post('/multiply', json={'a': 10, 'b': 5})
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    assert response.json()['result'] == 50, f"Expected result 50, got {response.json()['result']}"


def test_multiply_api_by_zero(client):
    """
    Test the Multiplication API Endpoint multiplying by zero.
    """
    response = client.post('/multiply', json={'a': 999, 'b': 0})
    assert response.status_code == 200
    assert response.json()['result'] == 0


def test_multiply_api_negative(client):
    """
    Test the Multiplication API Endpoint with a negative number.
    """
    response = client.post('/multiply', json={'a': -4, 'b': 5})
    assert response.status_code == 200
    assert response.json()['result'] == -20


def test_multiply_api_large_numbers(client):
    """
    Test the Multiplication API Endpoint with large numbers.
    """
    response = client.post('/multiply', json={'a': 100000, 'b': 100000})
    assert response.status_code == 200
    assert response.json()['result'] == 10000000000


# ==============================================
# Tests for the POST /divide Endpoint
# ==============================================

def test_divide_api(client):
    """
    Test the Division API Endpoint with positive integers.
    """
    response = client.post('/divide', json={'a': 10, 'b': 2})
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    assert response.json()['result'] == 5, f"Expected result 5, got {response.json()['result']}"


def test_divide_api_float_result(client):
    """
    Test the Division API Endpoint where the result is a non-integer float.
    """
    response = client.post('/divide', json={'a': 7, 'b': 2})
    assert response.status_code == 200
    assert response.json()['result'] == 3.5


def test_divide_by_zero_api(client):
    """
    Test the Division by Zero API Endpoint.

    Verifies that dividing by zero returns a 400 status code
    and an appropriate error message.
    """
    response = client.post('/divide', json={'a': 10, 'b': 0})
    assert response.status_code == 400, f"Expected status code 400, got {response.status_code}"
    assert 'error' in response.json(), "Response JSON does not contain 'error' field"
    assert "Cannot divide by zero!" in response.json()['error'], \
        f"Expected error message 'Cannot divide by zero!', got '{response.json()['error']}'"


def test_divide_api_negative_numbers(client):
    """
    Test the Division API Endpoint with negative numbers.
    """
    response = client.post('/divide', json={'a': -10, 'b': -2})
    assert response.status_code == 200
    assert response.json()['result'] == 5.0


# ==============================================
# Validation Error Tests
# ==============================================

def test_add_api_missing_field(client):
    """
    Test the Addition API Endpoint with a missing field.

    Verifies that omitting a required field ('b') returns a 400 status code
    and an appropriate validation error message.
    """
    response = client.post('/add', json={'a': 10})
    assert response.status_code == 400 or response.status_code == 422, \
        f"Expected 400 or 422 for missing field, got {response.status_code}"


def test_subtract_api_missing_field(client):
    """
    Test the Subtraction API Endpoint with a missing field.
    """
    response = client.post('/subtract', json={'b': 5})
    assert response.status_code == 400 or response.status_code == 422, \
        f"Expected 400 or 422 for missing field, got {response.status_code}"


def test_multiply_api_invalid_input(client):
    """
    Test the Multiplication API Endpoint with non-numeric string input.

    Verifies that sending a string instead of a number returns an error.
    """
    response = client.post('/multiply', json={'a': 'abc', 'b': 5})
    assert response.status_code == 400 or response.status_code == 422, \
        f"Expected 400 or 422 for invalid input, got {response.status_code}"


def test_divide_api_empty_body(client):
    """
    Test the Division API Endpoint with an empty JSON body.
    """
    response = client.post('/divide', json={})
    assert response.status_code == 400 or response.status_code == 422, \
        f"Expected 400 or 422 for empty body, got {response.status_code}"


def test_add_api_no_json(client):
    """
    Test the Addition API Endpoint with no JSON body at all.
    """
    response = client.post('/add')
    assert response.status_code == 400 or response.status_code == 422, \
        f"Expected 400 or 422 for no body, got {response.status_code}"


# ==============================================
# Response Structure Tests
# ==============================================

def test_response_contains_result_key(client):
    """
    Test that a successful response always contains the 'result' key.
    """
    response = client.post('/add', json={'a': 1, 'b': 1})
    assert response.status_code == 200
    data = response.json()
    assert 'result' in data, "Successful response should contain 'result' key"


def test_error_response_contains_error_key(client):
    """
    Test that an error response always contains the 'error' key.
    """
    response = client.post('/divide', json={'a': 1, 'b': 0})
    assert response.status_code == 400
    data = response.json()
    assert 'error' in data, "Error response should contain 'error' key"
