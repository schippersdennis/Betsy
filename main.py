__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

import models
from rich.console import Console
from rich.table import Table

console = Console()

# (Cast to string only for printing out results.)


def search(term) -> models.Product:
    # Query
    product = models.Product.get(models.Product.product_name == term)

    # Render table.
    table = Table(title="Search Products")
    for key in models.Product._meta.fields.keys():
        table.add_column(key)
    table.add_row(
        str(product.id),
        product.product_name,
        product.description,
        str(product.price),
        str(product.quantity),
        str(product.product_owner_id),
    )
    console.print(table)


def list_user_products(user_id) -> models.User:
    # Query
    user = models.User.select().where(models.User.id == user_id).get()

    # Render table.
    table = Table(title=f"{user.user_name} products")
    for key in models.Product._meta.fields.keys():
        table.add_column(key)
    table.add_column("user_name")
    for item in user.get_products:
        print(item.product_name)
        table.add_row(
            str(item.id),
            item.product_name,
            item.description,
            str(item.price),
            str(item.quantity),
            str(item.product_owner_id),
            user.user_name,
        )
    console.print(table)


def list_products_per_tag(tag_id) -> models.ProductTag:
    # Query
    products = (
        models.Product.select()
        .join(models.ProductTag, on=(models.Product.id == models.ProductTag.product_id))
        .where(models.ProductTag.tag_name == tag_id)
    )

    # Render table.
    table = Table(title=f"Products with tag:{tag_id}")
    for key in models.Product._meta.fields.keys():
        table.add_column(key)
    table.add_column("tag_name")

    for item in products:
        table.add_row(
            str(item.id),
            item.product_name,
            item.description,
            str(item.price),
            str(item.quantity),
            str(item.product_owner_id),
            tag_id,
        )
    console.print(table)


def add_product_to_catalog(user_id, product):
    ...


def update_stock(product_id, new_quantity):
    ...


def purchase_product(product_id, buyer_id, quantity):
    ...


def remove_product(product_id):
    ...


# search("single")
# list_user_products(9)
list_products_per_tag("drop")
