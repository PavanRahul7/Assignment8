# tests/e2e/test_e2e.py

import pytest  # Import the pytest framework for writing and running tests

# The following decorators and functions define E2E tests for the FastAPI calculator application.
# Each test is marked with @pytest.mark.e2e so they can be selectively run with: pytest -m e2e


@pytest.mark.e2e
def test_hello_world(page, fastapi_server):
    """
    Test that the homepage displays "Hello World".

    This test verifies that when a user navigates to the homepage of the application,
    the main header (<h1>) correctly displays the text "Hello World". This ensures
    that the server is running and serving the correct template.
    """
    # Navigate the browser to the homepage URL of the FastAPI application.
    page.goto('http://localhost:8000')
    
    # Use an assertion to check that the text within the first <h1> tag is exactly "Hello World".
    assert page.inner_text('h1') == 'Hello World'


@pytest.mark.e2e
def test_page_title(page, fastapi_server):
    """
    Test that the browser page title is correct.
    """
    page.goto('http://localhost:8000')
    assert 'Hello World' in page.title() or 'Calculator' in page.title()


@pytest.mark.e2e
def test_calculator_heading_visible(page, fastapi_server):
    """
    Test that the Calculator heading is visible on the page.
    """
    page.goto('http://localhost:8000')
    assert page.inner_text('h2') == 'Calculator'


# ==============================================
# Addition E2E Tests
# ==============================================

@pytest.mark.e2e
def test_calculator_add(page, fastapi_server):
    """
    Test the addition functionality of the calculator.

    Simulates a user performing an addition operation: fills in two numbers,
    clicks the "Add" button, and verifies the result displayed is correct.
    """
    page.goto('http://localhost:8000')
    page.fill('#a', '10')
    page.fill('#b', '5')
    page.click('button:text("Add")')
    # Wait for the result to appear
    page.wait_for_selector('#result:not(:empty)')
    assert page.inner_text('#result') == 'Calculation Result: 15'


@pytest.mark.e2e
def test_calculator_add_floats(page, fastapi_server):
    """
    Test addition with floating-point numbers.
    """
    page.goto('http://localhost:8000')
    page.fill('#a', '2.5')
    page.fill('#b', '3.5')
    page.click('button:text("Add")')
    page.wait_for_selector('#result:not(:empty)')
    assert page.inner_text('#result') == 'Calculation Result: 6'


@pytest.mark.e2e
def test_calculator_add_negative(page, fastapi_server):
    """
    Test addition with negative numbers.
    """
    page.goto('http://localhost:8000')
    page.fill('#a', '-10')
    page.fill('#b', '5')
    page.click('button:text("Add")')
    page.wait_for_selector('#result:not(:empty)')
    assert page.inner_text('#result') == 'Calculation Result: -5'


# ==============================================
# Subtraction E2E Tests
# ==============================================

@pytest.mark.e2e
def test_calculator_subtract(page, fastapi_server):
    """
    Test the subtraction functionality of the calculator.

    Simulates a user subtracting 5 from 10 and verifies the result is 5.
    """
    page.goto('http://localhost:8000')
    page.fill('#a', '10')
    page.fill('#b', '5')
    page.click('button:text("Subtract")')
    page.wait_for_selector('#result:not(:empty)')
    assert page.inner_text('#result') == 'Calculation Result: 5'


@pytest.mark.e2e
def test_calculator_subtract_negative_result(page, fastapi_server):
    """
    Test subtraction that produces a negative result.
    """
    page.goto('http://localhost:8000')
    page.fill('#a', '3')
    page.fill('#b', '10')
    page.click('button:text("Subtract")')
    page.wait_for_selector('#result:not(:empty)')
    assert page.inner_text('#result') == 'Calculation Result: -7'


# ==============================================
# Multiplication E2E Tests
# ==============================================

@pytest.mark.e2e
def test_calculator_multiply(page, fastapi_server):
    """
    Test the multiplication functionality of the calculator.

    Simulates a user multiplying 10 by 5 and verifies the result is 50.
    """
    page.goto('http://localhost:8000')
    page.fill('#a', '10')
    page.fill('#b', '5')
    page.click('button:text("Multiply")')
    page.wait_for_selector('#result:not(:empty)')
    assert page.inner_text('#result') == 'Calculation Result: 50'


@pytest.mark.e2e
def test_calculator_multiply_by_zero(page, fastapi_server):
    """
    Test multiplying by zero yields zero.
    """
    page.goto('http://localhost:8000')
    page.fill('#a', '999')
    page.fill('#b', '0')
    page.click('button:text("Multiply")')
    page.wait_for_selector('#result:not(:empty)')
    assert page.inner_text('#result') == 'Calculation Result: 0'


# ==============================================
# Division E2E Tests
# ==============================================

@pytest.mark.e2e
def test_calculator_divide(page, fastapi_server):
    """
    Test the division functionality of the calculator.

    Simulates a user dividing 10 by 2 and verifies the result is 5.
    """
    page.goto('http://localhost:8000')
    page.fill('#a', '10')
    page.fill('#b', '2')
    page.click('button:text("Divide")')
    page.wait_for_selector('#result:not(:empty)')
    assert page.inner_text('#result') == 'Calculation Result: 5'


@pytest.mark.e2e
def test_calculator_divide_by_zero(page, fastapi_server):
    """
    Test the divide by zero functionality of the calculator.

    Simulates a user attempting to divide a number by zero and verifies
    that the appropriate error message is displayed.
    """
    page.goto('http://localhost:8000')
    page.fill('#a', '10')
    page.fill('#b', '0')
    page.click('button:text("Divide")')
    page.wait_for_selector('#result:not(:empty)')
    assert page.inner_text('#result') == 'Error: Cannot divide by zero!'


# ==============================================
# Sequential Operations E2E Test
# ==============================================

@pytest.mark.e2e
def test_calculator_sequential_operations(page, fastapi_server):
    """
    Test performing multiple operations in sequence on the same page.

    Verifies that the calculator correctly updates the result when different
    operations are performed one after another without refreshing the page.
    """
    page.goto('http://localhost:8000')
    
    # First operation: Add 10 + 5 = 15
    page.fill('#a', '10')
    page.fill('#b', '5')
    page.click('button:text("Add")')
    page.wait_for_selector('#result:not(:empty)')
    assert page.inner_text('#result') == 'Calculation Result: 15'
    
    # Second operation: Multiply 4 * 3 = 12 (clear and re-fill)
    page.fill('#a', '4')
    page.fill('#b', '3')
    page.click('button:text("Multiply")')
    page.wait_for_selector('#result')
    # Small wait for the result to update
    page.wait_for_timeout(500)
    assert page.inner_text('#result') == 'Calculation Result: 12'
