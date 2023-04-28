from lesson_19.database_repository.products_repository import ProductsRepository


def test_create_products_table(create_db_connection):
    my_columns = [('id', 'serial primary key'), ('name', 'varchar(50)'), ('price', 'int')]
    repo = ProductsRepository(create_db_connection[0], create_db_connection[1])
    repo.create_product_table(my_columns)


def test_add_many_products(create_db_connection):
    products_json = [{'name': 'TV', 'price': 100},
                {'name': 'T-shirt', 'price': 5},
                {'name': 'Table', 'price': 15},
                {'name': 'Chair', 'price': 35},
                {'name': 'Phone', 'price': 50}]
    repo = ProductsRepository(create_db_connection[0], create_db_connection[1])
    repo.insert_many(products_json)


def test_get_all_products_from_table(create_db_connection):
    repo = ProductsRepository(create_db_connection[0], create_db_connection[1])
    for product in repo.get_all():
        print(product)
