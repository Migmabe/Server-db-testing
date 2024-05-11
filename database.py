from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String
import datetime
import logging

app = Flask(__name__)
# Create a logger for debugging purposes
logger = logging.getLogger(__name__)
logging.basicConfig(filename='sql_query.log', level=logging.INFO)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///users.db"

logger.info("Create extension")
# Create the extension
db = SQLAlchemy(model_class=Base)
# Initialise the app with the extension
db.init_app(app)

logger.info("Create table")


# -----------------CREATE TABLES---------------------------#
class Users(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    accountType: Mapped[str] = mapped_column(nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<User: {self.username}>'


class SystemLogon(db.Model):
    """Logs system logins into the database"""
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(250), nullable=False)
    time: Mapped[datetime.datetime] = mapped_column(nullable=False)


# ---------------END TABLE CREATION-------------------#

# Create the tables produced in my database file (Users and SystemLogon)
with app.app_context():
    db.create_all()
