from flask import Blueprint, jsonify
from models import Userdetails , Useraccountdetails, Usertransactiondetails

# Initializing Blueprint

simple_page = Blueprint('simple_page', __name__,
                        template_folder='templates')

# Initializing Route endpoints

@simple_page.route('/readud')
def index():
    users = Userdetails.query.all()
    return jsonify(users)


@simple_page.route('/readuad')
def index1():
    users = Useraccountdetails.query.all()
    return jsonify(users)


@simple_page.route('/readutd')
def index2():
    users = Usertransactiondetails.query.all()
    return jsonify(users)


# Account Balance for leass than Rs.800
@simple_page.route('/read800')
def index3():
    users = Useraccountdetails.query.filter(Useraccountdetails.AccountBalance < 800).all()
    return jsonify(users)


# Account Balance for top 10 Richest Users
@simple_page.route('/readtt')
def index4():
    users = Useraccountdetails.query.order_by(Useraccountdetails.AccountBalance.desc()).limit(10).all()
    return jsonify(users)


# Account Balance check for al the users
@simple_page.route('/readbc')
def index5():
    users = Usertransactiondetails.query.filter(Usertransactiondetails.Balance).all()
    return jsonify(users)
