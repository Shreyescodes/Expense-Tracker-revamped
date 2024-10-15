# Personal Finance Tracker

A comprehensive web application built with Django to help users manage their personal finances effectively.

## Features

- User authentication system
- Income and expense logging with categorization
- Dashboard with financial overview
- Expense categorization (e.g., food, rent, entertainment)
- Data visualization with pie charts for expense categories
- Monthly budget tracking and visualization
- Expense summary page with category totals and date range filtering
- Search functionality for transactions

## Technologies Used

- Python 3.x
- Django 3.x
- Chart.js for data visualization
- SQLite (default Django database)
- HTML/CSS/JavaScript

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/Shreyescodes/personal-finance-tracker.git
   cd personal-finance-tracker
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```
   python manage.py migrate
   ```

5. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

7. Access the application at `http://127.0.0.1:8000/login/`

## Usage

1. Register a new account or log in with existing credentials.
2. Use the dashboard to get an overview of your financial status.
3. Add new transactions (income or expenses) using the provided form.
4. View and analyze your expenses using the summary page and visualizations.
5. Set and track monthly budgets for different categories.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
