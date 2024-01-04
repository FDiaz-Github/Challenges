import pandas as pd
from pandas import DataFrame
from typing import Dict, Any
from models import Transaction


def read_transactions(file_path: str) -> DataFrame:
    """
    Function that returns a dataframe from a csv file, transforms date column into datetime and
    casts transaction column into Amounts (float)

    :param file_path: File path of the csv file
    :return: Dataframe with cleaned csv data
    """
    df = pd.read_csv(file_path)
    df['Date'] = pd.to_datetime(df['Date'])
    df['Amount'] = df['Transaction'].apply(lambda x: float(x))
    return df


def summarize_transactions(df: DataFrame) -> Dict[str, Any]:
    """
    Summarizes transactions by calculating the total balance,
    number of transactions per month and average credit and debit amounts

    :param df: Dataframe of the transactions. Columns: id, Date, Amount
    :return: Dict containing the summary of the transactions by month, credit and debit
    """
    summary = {
        'total_balance': df['Amount'].sum(),
        'transactions_per_month': df.groupby(df['Date'].dt.to_period('M')).size(),
        'avg_credit_amount': df[df['Amount'] > 0]['Amount'].mean(),
        'avg_debit_amount': df[df['Amount'] < 0]['Amount'].mean(),
    }
    return summary


def insert_transactions(session, transactions_df: DataFrame) -> None:
    """
    Inserts the transactions of the dataframe into the Transaction model

    :param session: Db session
    :param transactions_df: Dataframe obtained with the read function
    :return: None
    """
    for _, row in transactions_df.iterrows():
        transaction = Transaction(date=row['Date'], amount=row['Amount'])
        session.add(transaction)
    session.commit()