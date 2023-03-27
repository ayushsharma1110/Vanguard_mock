from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass

db = SQLAlchemy()

# Modeling the database
# Model for UserDetails.csv


@dataclass
class Userdetails(db.Model):
    UserId: str
    Username: str
    DOB: str
    Address: str
    Email: str

    UserId = db.Column(db.String(8), primary_key=True, nullable=False)
    Username = db.Column(db.String(45), nullable=False)
    DOB = db.Column(db.String(50), nullable=False)
    Address = db.Column(db.String(45), nullable=False)
    Email = db.Column(db.String(45), nullable=False)

    def print(self):
        return f'{self.UserId} {self.Username} {self.DOB} {self.Address} {self.Email}\n'

    def __repr__(self):
        return f'<user {self.UserId}>'


# Model for UserAccountDetails.csv
@dataclass
class Useraccountdetails(db.Model):
    UserId:str
    AccountNumber:int
    AccountBalance:int



    UserId = db.Column(db.String(50), primary_key=True, nullable=False)
    AccountNumber = db.Column(db.Integer, nullable=False)
    AccountBalance = db.Column(db.Integer, nullable=False)



    def print(self):
        return f'{self.UserId} {self.AccountNumber} {self.AccountBalance}\n'

    def __repr__(self):
        return f'<user {self.UserId}>'


# Model for UserTansactionDetails.csv
@dataclass
class Usertransactiondetails(db.Model):
    AccountNumber: int
    TransactionDate: str
    Description: str
    Withdrawl: int
    Deposit: int
    Balance: int



    AccountNumber = db.Column(db.Integer, primary_key=True, nullable=False)
    TransactionDate = db.Column(db.String(45), nullable=False)
    Description = db.Column(db.String(45), nullable=False)
    Withdrawl = db.Column(db.Integer, nullable=False)
    Deposit = db.Column(db.Integer, nullable=False)
    Balance = db.Column(db.Integer, nullable=False)



    def print(self):
        return f'{self.AccountNumber} {self.TransactionDate} {self.Description} {self.Withdrawl} {self.Deposit} {self.Balance}\n'

    def __repr__(self):
        return f'<user {self.AccountNumber}>'




