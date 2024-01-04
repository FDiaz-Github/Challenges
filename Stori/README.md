# Stori Challenge

## Description

This application processes and summarizes financial transactions, storing the results in a PostgreSQL database and sends a summary via email.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Docker and Docker Compose are installed on your system.
- Python and pip are installed for local development and running Alembic migrations.

## Setup and Installation

1. **Clone the Repository**:
   ```bash
   cd Challenges/Stori
   ```
2. **Set up env variables**:
In the .env file, make sure to setup your mail password, as well as modifying as needed the settings.py for the sender and receiver mail addresses. If your mail has 2FA enabled, you might need additional steps, for gmail for example, you will need to [add an app password](https://support.google.com/mail/answer/185833?hl=en) 
3. **Build and run the app with Docker Compose**:
   ```bash
   docker-compose up --build
   ```
4. **Install Alembic for migrations**:
   ```bash
   pip install alembic
   ```
   You can install alembic or if you prefer you can have a virtual environment for the entire project by creating a virtual environment, activating it and running:
   ```bash
   pip install -r requirements.txt
   ```

## Considerations

This application is mainly developed to solve a challenge, therefore the transactions stored in the database can be duplicated if you run the app several times. Since the csv generated is simple, we dont have enough details to add unique constraints on our Transaction model.

To connect to the database you can find the database URL on the env file.
