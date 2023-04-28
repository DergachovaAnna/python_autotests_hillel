from lesson_19.database_repository.orders_repository import OrdersRepository


def test_create_orders_table(create_db_connection):
    my_columns = [('id', 'serial primary key'), ('product_id', 'int'), ('quantity', 'int')]
    constraints = [', CONSTRAINT fk_product_id FOREIGN KEY(product_id) REFERENCES products(id)']
    repo = OrdersRepository(create_db_connection[0], create_db_connection[1])
    repo.create_orders_table(my_columns, constraints)


def test_add_many_orders(create_db_connection):
    orders_json = [{'product_id': 1, 'quantity': 13},
                {'product_id': 2, 'quantity': 3},
                {'product_id': 3, 'quantity': 8},
                {'product_id': 4, 'quantity': 9},
                {'product_id': 5, 'quantity': 32}]
    repo = OrdersRepository(create_db_connection[0], create_db_connection[1])
    repo.insert_many(orders_json)


def test_get_all_orders_from_table(create_db_connection):
    repo = OrdersRepository(create_db_connection[0], create_db_connection[1])
    for order in repo.get_all():
        print(order)


def test_join_tables(create_db_connection):
    repo = OrdersRepository(create_db_connection[0], create_db_connection[1])
    result = repo.inner_join()
    for row in result:
        print(row)
