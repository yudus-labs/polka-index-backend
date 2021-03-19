import mongoengine as me
from .config import load_db_config


def connect(cfg_path: str):
    cfg = load_db_config(cfg_path)
    me.connect(
        db=cfg['DB'],
        username=cfg['USERNAME'],
        password=cfg['PASSWORD'],
        host=cfg['HOST'],
        port=cfg['PORT'],
    )


class TokenDetails(me.EmbeddedDocument):
    homepage = me.StringField()
    cap = me.IntField()
    diluted_cap = me.IntField()
    supply = me.IntField()
    total_supply = me.IntField()
    max_supply = me.IntField()
    desc = me.StringField()
    links = me.StringField()


class Tokens(me.Document):
    cg_id = me.StringField()
    logo = me.StringField()
    symbol = me.StringField()
    name = me.StringField()
    price = me.FloatField()
    price_change_24h = me.FloatField()
    atl = me.FloatField()
    ath = me.FloatField()
    plo = me.BooleanField()
    tags = me.ListField()
    w3f = me.BooleanField()
    rank = me.IntField()
    details = me.EmbeddedDocumentField(TokenDetails)


def ls_tokens():
    return {'tokens': Tokens.objects()}
