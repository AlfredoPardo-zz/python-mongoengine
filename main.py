import yaml
import json
import click

from mongoengine import connect
from models import CloudAccount, \
    CloudProvider, Customer

def get_connection():

    with open("config.yaml") as f:
    
        CONFIG = yaml.load(f, Loader=yaml.FullLoader)
    
    if CONFIG:
        
        return connect(db=CONFIG["mongodb"]["db_name"],
            username=CONFIG["mongodb"]["username"],
            password=CONFIG["mongodb"]["password"],
            host=CONFIG["mongodb"]["host"],
            port=CONFIG["mongodb"]["port"],
            authentication_source=CONFIG["mongodb"]["auth_source"])

    else:

        return None

@click.group()
def cli():
    pass

@cli.command()
def add_records():

    db = get_connection()

    # Adding Customers
    customer_1 = Customer(uid="netflix", name="Netflix")
    customer_1.save()
    
    customer_2 = Customer(uid="apv", name="Amazon Prime Video")
    customer_2.save()

    # Adding Cloud Providers
    cloud_provider_1 = CloudProvider(uid="aws", abbreviation="AWS", name="Amazon Web Services")
    cloud_provider_1.save()

    cloud_provider_2 = CloudProvider(uid="azure", abbreviation="Azure", name="Azure")
    cloud_provider_2.save()

    cloud_provider_3 = CloudProvider(uid="gcp", abbreviation="GCP", name="Google Cloud")
    cloud_provider_3.save()

    # Adding Cloud Accounts
    cloud_account = CloudAccount(uid="netflix-dev",
    name="Netflix Dev",
    customer=customer_1,
    cloud_provider=cloud_provider_1)
    cloud_account.save()

@cli.command()
def show_records():

    db = get_connection()

    print("\n*** CUSTOMERS ***\n")

    for customer in Customer.objects():
        print("UID:\t\t{}".format(customer.uid))
        print("Name:\t\t{}\n".format(customer.name))

    print("\n*** CLOUD PROVIDERS ***\n")

    for cloud_provider in CloudProvider.objects():
        print("Uid:\t\t{}".format(cloud_provider.uid))
        print("Name:\t\t{}".format(cloud_provider.name))
        print("Abbreviation:\t{}\n".format(cloud_provider.abbreviation))

    print("\n*** CLOUD ACCOUNTS ***\n")

    for raw_cloud_account in CloudAccount.objects():
        
        cloud_account = raw_cloud_account.to_dict()

        print("Uid:\t\t{}".format(cloud_account["uid"]))
        print("Name:\t\t{}".format(cloud_account["name"]))
        print("Customer:")
        for k, v in cloud_account["customer"].items():
            print("\t\t{}: {}".format(k.capitalize(),v))
        print("Cloud Provider:")
        for k, v in cloud_account["cloud_provider"].items():
            print("\t\t{}: {}".format(k.capitalize(),v))
        
@cli.command()
def delete_records():

    db = get_connection()
    
    [cloud_account.delete() for cloud_account in CloudAccount.objects()]
    [cloud_provider.delete() for cloud_provider in CloudProvider.objects()]
    [customer.delete() for customer in Customer.objects()]
        
    


if __name__ == '__main__':
    cli()