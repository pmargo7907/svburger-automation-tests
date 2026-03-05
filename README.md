# SVBurger Automation Tests

Automation testing project for SVBurger web application using Playwright and Python.

## Features covered

- User registration
- Product selection
- Order creation
- Order summary popup validation

## Tech stack

- Python
- Playwright
- PyCharm
- Git & GitHub
- Page Object Model (POM)

## Project structure

pages/
- home_page.py
- registration_page.py
- products_page.py

tests/
- test_registration.py
- test_order.py

utils/
- browser_factory.py

## How to run tests

Install dependencies:

pip install -r requirements.txt

Run tests:

pytest tests/
