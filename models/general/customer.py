from mongoengine import Document
from mongoengine.fields import (StringField)

class Customer(Document):

    meta = {'collection': 'customer'}
    uid = StringField()
    name = StringField()