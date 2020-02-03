from app import app, db
from bsn_sdk import Operator
from app.models import Transactions,Data_on_chain
import json
import configparser

config = configparser.ConfigParser()

config.read('config.ini')
user_code = config['bsn_info']["user_code"]
app_code = config["bsn_info"]["app_code"]
chain_code = config["bsn_info"]["chain_code"]
url = config["bsn_info"]["url"]
cert_path = config["bsn_info"]["cert_path"]

op = Operator(user_code, app_code, chain_code, url, cert_path)
transactions = op.get_history('WNB')
data_on_chain=op.get_data('WNB')
transactions_list=[]
data_on_chain_list=[]
if transactions.get("payload").get("context"):
    for i in transactions.get("payload").get("context"):
        try:
            time = i.get("txTime")
            transactions_dict = json.loads(i.get('dataInfo'))
            transactions_dict["timestamp"] = i.get("txTime")
            transactions_dict["txid"] = i.get("txId")
        except:
            transactions_dict = {"txid": i.get("txId"),
                                 "BaseKey": None,
                                 "BaseInfo": None,
                                 "timestamp": i.get("txTime")}
        transactions_list.append(transactions_dict)
    for i in transactions_list:
        trans = Transactions(txid=i.get("txid"),
                             key=i.get("BaseKey"),
                             operation=None,
                             value=i.get("BaseInfo"),
                             timestamp=i.get("timestamp"))
        db.session.add(trans)
        db.session.commit()
if data_on_chain.get("payload").get("context"):
    data_on_chain_dict = {"txid": data_on_chain.get("payload").get("txId"),
                          "BaseKey": i.get("BaseKey"),
                          "Value": data_on_chain.get("payload").get("context"),
                          "Last UpdateTime": i.get("timestamp")}
    data_on_chain_list.append(data_on_chain_dict)
    print(data_on_chain_dict)
    data = Data_on_chain(txid=data_on_chain_dict.get("txid"),
                         key=data_on_chain_dict.get("BaseKey"),
                         value=data_on_chain_dict.get("Value"),
                         last_updatetime=data_on_chain_dict.get("Last UpdateTime"))
    db.session.add(data)
    db.session.commit()