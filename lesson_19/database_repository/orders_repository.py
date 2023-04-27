from lesson_19.utilities.base_db_repo import BaseRepository


class OrdersRepository(BaseRepository):
    def __init__(self, connection, cursor):
        super().__init__(connection, cursor)
        self.table_name = 'orders'

    def create_orders_table(self, columns: list, constraints=None):
        """
        :param columns: example my_columns = [('id', 'serial primary key'), ('quantity', 'int')]
        """
        self.create_table(self.table_name, columns, constraints)

