from lesson_19.utilities.base_db_repo import BaseRepository


class ProductsRepository(BaseRepository):
    def __init__(self, connection, cursor):
        super().__init__(connection, cursor)
        self.table_name = 'products'

    def create_product_table(self, columns: list):
        """
        :param columns: example my_columns = [('id', 'serial primary key'), ('quantity', 'int')]
        """
        self.create_table(self.table_name, columns)
