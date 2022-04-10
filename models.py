# Models go here
from asyncio.windows_events import NULL
from unicodedata import name
import peewee
from faker import Faker
import random

db = peewee.SqliteDatabase("webshop.db")


class User(peewee.Model):
    id = peewee.BigAutoField()
    user_name = peewee.CharField()
    adress = peewee.CharField()
    email = peewee.CharField()
    phone = peewee.IntegerField()
    iban = peewee.CharField()

    class Meta:
        database = db


class Product(peewee.Model):
    id = peewee.BigAutoField()
    product_name = peewee.CharField()
    description = peewee.CharField()
    price = peewee.FloatField()
    quantity = peewee.IntegerField()
    product_owner = peewee.ForeignKeyField(User, backref="get_products")

    class Meta:
        database = db


class ProductTag(peewee.Model):
    id = peewee.BigAutoField()
    product_id = peewee.ForeignKeyField(Product, backref="get_tags")
    tag_name = peewee.CharField()

    class Meta:
        database = db


class Transaction(peewee.Model):
    id = peewee.BigAutoField()
    user_id = peewee.ForeignKeyField(User, backref="get_user")
    product_id = peewee.ForeignKeyField(Product, backref="get_product")
    quantity = peewee.IntegerField()

    class Meta:
        database = db


db.connect()
db.create_tables([User, ProductTag, Product, Transaction])


def db_seed():
    fake = Faker()
    # User SEED
    for number in range(10):
        random_user = User(
            user_name=fake.name(),
            adress=fake.address(),
            email=fake.email(),
            phone=fake.phone_number(),
            iban=fake.iban(),
        )
        random_user.save()

        # Product SEED
        for number in range(3):
            user_products = Product(
                product_name=fake.word(),
                description=fake.sentence(),
                price=round(random.uniform(00.33, 66.66), 2),
                quantity=random.randint(1, 10),
                product_owner=random_user.id,
            )
            user_products.save()

            # ProductTag SEED
            for number in range(2):
                product_tags = ProductTag(
                    product_id=user_products.id, tag_name=fake.word()
                )
                product_tags.save()

        # Transactions SEED
        for number in range(2):
            user_transactions = Transaction(
                user_id=random_user.id,
                product_id=random.randint(1, 30),
                quantity=random.randint(1, 3),
            )
            user_transactions.save()


db_seed()
