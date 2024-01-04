import data_processing
import models
import emails
import logging
import os

logging.basicConfig(level=logging.INFO)


def main():
    logging.info('Running data transactions summary process')
    # Data processing
    file_path = 'resources/transactions.csv'
    transactions_df = data_processing.read_transactions(file_path)
    summary = data_processing.summarize_transactions(transactions_df)

    # Creating db session and inserting transactions into db
    database_url = os.environ.get('DATABASE_URL')
    session = models.create_session(database_url)
    data_processing.insert_transactions(session, transactions_df)

    # Email generation
    email_content = emails.generate_email_content(summary)
    logging.info('Sending transaction summary email')
    try:
        emails.send_email('[Stori] Summary of transactions', email_content)
    except Exception as e:
        logging.error(f'Error trying to send email, error: {e}')


if __name__ == "__main__":
    main()

