import pandas as pd
from data_processing import read_transactions, summarize_transactions


def test_read_transactions(tmp_path, transactions_data):
    # Given a file with some data
    file_path = tmp_path / "transactions.csv"
    transactions_data.to_csv(file_path, index=False)

    # When reading the file
    df = read_transactions(file_path)

    # Then the df should be created successfully
    assert not df.empty


def test_summarize_transactions(read_transactions_data):
    # Given a dataframe, when summarizing the transaction
    total_balance = read_transactions_data['Amount'].sum()
    transactions_per_month = read_transactions_data.groupby(read_transactions_data['Date'].dt.to_period('M')).size()
    avg_credit = read_transactions_data[read_transactions_data['Amount'] > 0]['Amount'].mean()
    avg_debit = read_transactions_data[read_transactions_data['Amount'] < 0]['Amount'].mean()
    summary = summarize_transactions(read_transactions_data)

    # Then a dictionary should be created
    assert summary['total_balance'] == total_balance
    assert summary['transactions_per_month'].equals(transactions_per_month)
    assert summary['avg_credit_amount'] == avg_credit
    assert summary['avg_debit_amount'] == avg_debit
