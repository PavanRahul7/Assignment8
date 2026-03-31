# Module 8 — FastAPI Calculator: Testing, Logging & CI

## Project Overview

A FastAPI-based calculator application with comprehensive **unit**, **integration**, and **end-to-end (E2E)** tests, **structured logging**, and **GitHub Actions CI/CD**.

## Project Structure

```
module8_is601/
├── .github/
│   └── workflows/
│       └── ci.yml                  # GitHub Actions CI workflow
├── app/
│   └── operations/
│       └── __init__.py             # Arithmetic functions (add, subtract, multiply, divide) with logging
├── templates/
│   └── index.html                  # Frontend calculator UI
├── tests/
│   ├── conftest.py                 # Shared fixtures (Playwright browser, FastAPI server)
│   ├── unit/
│   │   └── test_calculator.py      # 42 unit tests for operations.py
│   ├── integration/
│   │   └── test_fastapi_calculator.py  # 23 integration tests for API endpoints
│   └── e2e/
│       └── test_e2e.py             # 14 E2E tests using Playwright
├── main.py                         # FastAPI application with structured logging
├── Dockerfile                      # Docker image definition
├── docker-compose.yml              # Docker Compose configuration
├── pytest.ini                      # Pytest configuration
├── requirements.txt                # Python dependencies
└── README.md                       # This file
```

## Setup & Installation

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd module8_is601
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
# venv\Scripts\activate         # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Playwright Browsers (for E2E tests)

```bash
playwright install --with-deps chromium
```

### 5. Run the Application

```bash
python main.py
```

Then open [http://localhost:8000](http://localhost:8000) in your browser.

## Running Tests

### Run All Unit + Integration Tests

```bash
pytest tests/unit/ tests/integration/ -v --cov=app --cov-report=term-missing
```

### Run Only Unit Tests

```bash
pytest tests/unit/ -v
```

### Run Only Integration Tests

```bash
pytest tests/integration/ -v
```

### Run E2E Tests (Playwright)

```bash
pytest tests/e2e/ -v -m e2e
```

## Test Summary

| Category     | File                                      | Count | Description                                              |
|-------------|-------------------------------------------|-------|----------------------------------------------------------|
| **Unit**     | `tests/unit/test_calculator.py`           | 42    | Direct function tests: add, subtract, multiply, divide   |
| **Integration** | `tests/integration/test_fastapi_calculator.py` | 23 | API endpoint tests via FastAPI TestClient               |
| **E2E**      | `tests/e2e/test_e2e.py`                  | 14    | Browser-based tests via Playwright                       |
| **Total**    |                                           | **79**| **100% coverage on `app/operations`**                    |

### Unit Test Highlights
- Parametrized tests for all four operations (positive/negative/float/zero/large numbers)
- Floating-point precision tests (`0.1 + 0.2 ≈ 0.3`)
- Mathematical property tests (commutativity, identity, inverse)
- Return type assertions
- Division by zero (int and float variants)

### Integration Test Highlights
- All four API endpoints: `/add`, `/subtract`, `/multiply`, `/divide`
- Root endpoint (`GET /`) serves the HTML template
- Validation error handling: missing fields, invalid input types, empty body, no JSON
- Response structure verification (`result` key on success, `error` key on failure)
- Edge cases: negative numbers, floats, large numbers, zero

### E2E Test Highlights
- Homepage renders with correct headings
- All four calculator operations via browser interaction
- Division by zero displays error message
- Sequential operations on the same page
- Float and negative number inputs

## Logging

Structured logging is implemented at two levels:

1. **`app/operations/__init__.py`** — Logs every operation result at `INFO` level and division-by-zero at `ERROR` level.
2. **`main.py`** — Logs incoming requests, results, and errors for every API route with timestamps.

Log format:
```
2025-01-15 10:30:45 - __main__ - INFO - Add request received: a=10.0, b=5.0
2025-01-15 10:30:45 - app.operations - INFO - add(10.0, 5.0) = 15.0
2025-01-15 10:30:45 - __main__ - INFO - Add result: 15.0
```

## GitHub Actions CI

The workflow (`.github/workflows/ci.yml`) runs automatically on every push/PR to `main` or `master`:

- **Job 1: `unit-and-integration-tests`** — Installs dependencies, runs unit + integration tests with coverage
- **Job 2: `e2e-tests`** — Installs dependencies + Playwright browsers, runs E2E tests

Screenshot
<img width="1915" height="978" alt="Screenshot 2026-03-31 183054" src="https://github.com/user-attachments/assets/90fd92dc-ba30-4c48-b792-7deb5c6dd3e7" />


