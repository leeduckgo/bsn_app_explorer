from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
transactions = Table('transactions', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('txid', VARCHAR(length=100)),
    Column('key', VARCHAR(length=100)),
    Column('operation', VARCHAR(length=100)),
    Column('value', VARCHAR(length=100)),
    Column('timestamp', VARCHAR(length=100)),
)

transactions = Table('transactions', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('tx_id', String),
    Column('key', String),
    Column('operation', String),
    Column('value', String),
    Column('timestamp', String),
)

data_on_chain = Table('data_on_chain', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('txid', VARCHAR(length=100)),
    Column('key', VARCHAR(length=100)),
    Column('value', VARCHAR(length=100)),
    Column('last_updatetime', VARCHAR(length=100)),
)

data_on_chain = Table('data_on_chain', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('tx_id', String),
    Column('key', String),
    Column('value', String),
    Column('last_update_time', String),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['transactions'].columns['txid'].drop()
    post_meta.tables['transactions'].columns['tx_id'].create()
    pre_meta.tables['data_on_chain'].columns['last_updatetime'].drop()
    pre_meta.tables['data_on_chain'].columns['txid'].drop()
    post_meta.tables['data_on_chain'].columns['last_update_time'].create()
    post_meta.tables['data_on_chain'].columns['tx_id'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['transactions'].columns['txid'].create()
    post_meta.tables['transactions'].columns['tx_id'].drop()
    pre_meta.tables['data_on_chain'].columns['last_updatetime'].create()
    pre_meta.tables['data_on_chain'].columns['txid'].create()
    post_meta.tables['data_on_chain'].columns['last_update_time'].drop()
    post_meta.tables['data_on_chain'].columns['tx_id'].drop()
