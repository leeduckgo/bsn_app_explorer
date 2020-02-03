# -*- coding:utf-8 -*-

from flask import (
    request, render_template)
from app.models import Transactions, Data_on_chain
from app import app, db


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    data_on_chain_dict = "no data on chain"
    transactions_list = []
    if request.method == "POST":
        if request.form.get("keyword"):
            basekey = request.form.get("keyword")
            data_on_chain = Data_on_chain.query.filter_by(key=basekey).first()
            try:
                data_on_chain_dict = data_on_chain.to_dict()
            except:
                data_on_chain_dict="no data on chain"
            tran = Transactions.query.filter_by(key=basekey).all()
            if tran:
                try:
                    for i in tran:
                        transactions_list.append(i.to_dict())
                except:
                    transactions_list.append("no transaction")
            else:
                transactions_list.append("no transaction")
    else:
        transactions_list.append("no transaction")
        return render_template("main.html", data_on_chain=data_on_chain_dict, transcations_list=transactions_list)
    return render_template("main.html", data_on_chain=data_on_chain_dict, transcations_list=transactions_list)


@app.route('/nodes')
def nodes():
    return render_template('nodes.html')


@app.route("/transactions")
def transactions():
    transactions_list=[]
    tran =Transactions.query.all()
    if tran:
        try:
            for i in tran:
                transactions_list.append(i.to_dict())
        except:
            transactions_list.append("no transaction")
    else:
        transactions_list.append("no transaction")

    return render_template('transactions.html',transactions_list=transactions_list)

@app.route('/')
def main():
    return render_template('main.html')

@app.route("/data_on_chain")
def data_on_chain():
    data_on_chain_list=[]
    data = Data_on_chain.query.all()
    if data:
        try:
            for i in data:
                data_on_chain_list.append(i.to_dict())
        except:
            data_on_chain_list.append("no transaction")
    else:
        data_on_chain_list.append("no transaction")
    return render_template('data_on_chain.html',data_on_chain_list=data_on_chain_list)
