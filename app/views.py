# -*- coding:utf-8 -*-

from flask import (
    request, render_template)
from app.models import Transactions, Data_on_chain
from app import app, db
from app.blockchain import Blockchain
import json
import datetime 

## === global variables ===
blockchain = Blockchain()
## === api ===

@app.route('/api/get_data/<key>', methods=['get'])
def get_data(key):
    data_on_chain = Data_on_chain.query.filter_by(key=key).first()
    if data_on_chain == None:
        return ""
    else:
        return json.dumps(data_on_chain.to_dict(),ensure_ascii=False)

@app.route('/api/get_history/<key>', methods=['get'])
def get_history(key):
    txs_list=[]
    txs = Transactions.query.filter_by(key=key).all()
    for tx in txs:
        txs_list.append(tx.to_dict())
    return json.dumps(txs_list)

@app.route('/api/delete_data/<key>', methods=['get'])
def delete_data(key):
    res = blockchain.delete_data(key)
    if res["success"] == True:
        # delete item in data_on_chain
        item = Data_on_chain.query.filter_by(key=key).first()
        db.session.delete(item)
        db.session.commit()
        # save to transactions
        a_tx = Transactions()
        a_tx.key = key
        a_tx.tx_id = res['payload']['txId']
        a_tx.operation = "delete"
        a_tx.timestamp = datetime.datetime.now() 
        db.session.add(a_tx)
        db.session.commit()
        db.session.refresh(a_tx)      
        return json.dumps(a_tx.to_dict())
    else:
        return "error"     

@app.route('/api/save_data/<key>', methods=['post'])
def save_data(key):
    jsoned = trans(request.get_data())
    value = jsoned["payload"]
    res = blockchain.save_data(key, value)
    if res["success"] == True:
        # save to data_on_chain
        an_item = Data_on_chain()
        an_item.key = key
        an_item.value = value
        an_item.tx_id = res['payload']['txId']
        an_item.last_update_time = datetime.datetime.now() 
        db.session.add(an_item)
        db.session.commit()
        # save to transactions
        a_tx = Transactions()
        a_tx.key = key
        a_tx.value = value
        a_tx.tx_id = res['payload']['txId']
        a_tx.operation = "create"
        a_tx.timestamp = datetime.datetime.now() 
        db.session.add(a_tx)
        db.session.commit()
        db.session.refresh(a_tx)      
        return json.dumps(a_tx.to_dict())
    else:
        return "error"



@app.route('/api/update_data/<key>', methods=['post'])
def update_data(key):
    jsoned = trans(request.get_data())
    value = jsoned["payload"]
    res = blockchain.update_data(key, value)
    if res["success"] == True:
        # update data
        an_item = Data_on_chain.query.filter_by(key=key).first()
        # get last one:
        # obj = session.query(ObjectRes).order_by(ObjectRes.id.desc()).first()
        an_item.value = value
        an_item.tx_id = res['payload']['txId']
        an_item.last_update_time = datetime.datetime.now() 
        db.session.add(an_item)
        db.session.commit()
        # save to transactions
        a_tx = Transactions()
        a_tx.key = key
        a_tx.value = value
        a_tx.tx_id = res['payload']['txId']
        a_tx.operation = "update"
        a_tx.timestamp = datetime.datetime.now() 
        db.session.add(a_tx)
        db.session.commit()
        db.session.refresh(a_tx)
        
        return json.dumps(a_tx.to_dict())
    else:
        return "error"

## === pages ===
@app.route('/', methods=['POST', 'GET'])
def index():
    global blockchain
    node = blockchain.config["url"]
    data_on_chain_list = []
    transactions_list = []
    if request.method == "POST":
        if request.form.get("keyword"):
            basekey = request.form.get("keyword")
            # 链上数据
            data_on_chain = Data_on_chain.query.filter_by(key=basekey).first()
            try:
                data_on_chain_list = [data_on_chain.to_dict()]
            except:
                data_on_chain_list = ["no data you ask for"]
            # 链上交易
            trans = Transactions.query.filter_by(key=basekey).order_by(Transactions.id.desc()).all()
            if trans:
                try:
                    for i in trans:
                        transactions_list.append(i.to_dict())
                except:
                    transactions_list.append("no transaction")
            else:
                transactions_list.append("no transaction")
    else:
        # 默认首页
        data_on_chain = Data_on_chain.query.all()
        for data in data_on_chain:
            data_on_chain_list.append(data.to_dict())
        txs = Transactions.query.order_by(Transactions.id.desc()).all()
        for tx in txs:
            transactions_list.append(tx.to_dict())
    return render_template("index.html", 
    data_on_chain=data_on_chain_list, 
    transcations_list=transactions_list,
    node=node)


@app.route('/nodes')
def nodes():
    return render_template('nodes.html')


@app.route("/transactions")
def transactions():
    transactions_list=[]
    tran =Transactions.query.order_by(Transactions.id.desc()).all()
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

'''pretty json '''
def trans(payload):
    try:
        return json.loads(str(payload, "utf-8"))
        # return json.dumps(a_json, sort_keys=True, indent=4, separators=(',', ':'))
    except:
        print("not json")
        return payload
