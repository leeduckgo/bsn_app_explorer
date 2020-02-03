# -*- coding:utf-8  -*-

from app import db


class Transactions(db.Model):
    '''定义Transactions 模型类'''
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    txid = db.Column(db.String(100), unique=True)
    key = db.Column(db.String(100), unique=True)
    operation = db.Column(db.String(100))
    value = db.Column(db.String(100))
    timestamp = db.Column(db.String(100))

    def to_dict(self):
        transcation_dict = {
            "key": self.key,
            "operation": self.operation,
            "timestamp": self.timestamp,
        }
        return transcation_dict


class Data_on_chain(db.Model):
    '''定义Data_on_chain模型类'''
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    txid = db.Column(db.String(100), unique=True)
    key = db.Column(db.String(100), unique=True)
    value = db.Column(db.String(100))
    last_updatetime = db.Column(db.String(100))

    def to_dict(self):
        Data_on_chain_dict = {
            "key": self.key,
            "value": self.value,
            "last_updatetime": self.last_updatetime,
        }
        return Data_on_chain_dict
