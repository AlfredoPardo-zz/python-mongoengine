from mongoengine import Document
from mongoengine.fields import (StringField)

class CloudProvider(Document):

    meta = {'collection': 'cloud_provider'}
    uid = StringField()
    name = StringField()
    abbreviation = StringField()