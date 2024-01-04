from emails import generate_email_content


def test_generate_email_content(summary_data):
    # Given the email template, when filling it with summary data
    email_html = generate_email_content(summary_data)

    # Then that data should be in the template
    assert str(summary_data['total_balance']) in email_html
    assert str(summary_data['avg_credit_amount']) in email_html
    assert str(summary_data['avg_debit_amount']) in email_html
