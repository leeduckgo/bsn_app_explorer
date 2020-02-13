# -*- coding:utf-8  -*-

from app import db


class Transactions(db.Model):
    """定义Transactions 模型类"""
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    tx_id = db.Column(db.String, unique=True)
    key = db.Column(db.String, unique=True)
    operation = db.Column(db.String)
    value = db.Column(db.String)
    timestamp = db.Column(db.String)

    def to_dict(self):
        item = self.__dict__
        item.pop('_sa_instance_state', None)
        return item


class Data_on_chain(db.Model):
    """定义Data_on_chain模型类"""
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    tx_id = db.Column(db.String, unique=True)
    key = db.Column(db.String, unique=True)
    value = db.Column(db.String)
    last_update_time = db.Column(db.String)

    def to_dict(self):
        item = self.__dict__
        item.pop('_sa_instance_state', None)
        return item

