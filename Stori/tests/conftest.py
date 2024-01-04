import pytest
import pandas as pd
from datetime import datetime


@pytest.fixture
def transactions_data():
    data = {
        'Id': [1, 2, 3, 4],
        'Date': [datetime(2023, 7, 1), datetime(2023, 7, 15), datetime(2023, 8, 10), datetime(2023, 8, 20)],
        'Transaction': ['+60.5', '-20.46', '-10.3', '+15.0']
    }
    return pd.DataFrame(data)


@pytest.fixture
def read_transactions_data():
    data = {
        'Id': [1, 2, 3, 4],
        'Date': [datetime(2023, 7, 1), datetime(2023, 7, 15), datetime(2023, 8, 10), datetime(2023, 8, 20)],
        'Amount': [60.5, -20.46, -10.3, 15.0]
    }
    return pd.DataFrame(data)


@pytest.fixture
def summary_data():
    """Fixture to provide a summary dictionary for testing email generation."""
    return {
        'total_balance': 44.74,
        'transactions_per_month': {'2023-07': 2, '2023-08': 2},
        'avg_credit_amount': 37.75,
        'avg_debit_amount': -15.38
    }
