# SVBurger Automation Tests

UI automation testing project for the SVBurger web application using Python and Playwright.

## Covered Scenarios

- User registration (Sign Up)
- Product selection
- Order creation
- Order summary popup validation

## Tech Stack

- Python
- Playwright
- pytest
- Page Object Model (POM)
- Git & GitHub

## Key Features

- Structured test framework using Page Object Model
- Reusable page objects and methods
- Validation of core user flows and UI behavior

## Project Structure

pages/
- home_page.py
- registration_page.py
- products_page.py

tests/
- test_registration.py
- test_order.py

utils/
- browser_factory.py

## How to Run

Install dependencies:

pip install -r requirements.txt

Run tests:

pytest tests/

## Status

Work in progress – expanding test coverage and improving test scenarios.
