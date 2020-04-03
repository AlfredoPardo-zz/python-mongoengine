from bson import json_util
from mongoengine import Document
from mongoengine.fields import (StringField, ReferenceField)

from models.cloud.cloud_provider import CloudProvider
from models.general.customer import Customer

class CloudAccount(Document):

    meta = {'collection': 'cloud_account'}
    uid = StringField()
    name = StringField()
    customer = ReferenceField(Customer)
    cloud_provider = ReferenceField(CloudProvider)

    def to_dict(self):

        data = self.to_mongo().to_dict()
        data["customer"] = {key:self.customer[key] for key in Customer._fields if key != "id"}
        data["cloud_provider"] = {key:self.cloud_provider[key] for key in CloudProvider._fields if key != "id"}

        return data