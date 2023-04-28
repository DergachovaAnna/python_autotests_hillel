from psycopg2 import sql
from psycopg2.extras import Json


class BaseRepository:
    def __init__(self, connection, cursor):
        self._cursor = cursor
        self._connection = connection
        self._connection.set_session(autocommit=True)  # use instead of self.__connection.commit() in called methods
        self.table_name = None

    def create_table(self, table_name, columns, constraints=None):
        columns_str = ', '.join([f'{name} {data_type}' for name, data_type in columns])
        constraints_str = ', '.join(constraints) if constraints else ''
        query = f"Create table {table_name} ({columns_str} {constraints_str})"
        self._cursor.execute(query)

    def insert_many(self, table_lines_json):
        """
        :param table_lines_json: e.g: json = [{'name': 'name1', 'price': 10}, {'name': 'name2', 'price': 10}]
        """
        placeholders = ', '.join(['%s'] * len(table_lines_json[0])) # '%s' string represents a placeholder for a
        # single value in a SQL query. Bby multiplying it by the length of the dictionary, the resulting list will
        # have one placeholder for each key-value pair in the dictionary
        columns = ', '.join(table_lines_json[0].keys()) # create a string with the column names of the table

        values = []  # iterate over given json (list) and take values from each dictionary (line)
        for line in table_lines_json:
            value_tuple = tuple(line.values())
            values.append(value_tuple)

        query = f"Insert into {self.table_name} ({columns}) values ({placeholders})"
        self._cursor.executemany(query, values) # executemany() method automatically replaces placeholders in
        # the SQL query with the corresponding values in each tuple

    def get_all(self):
        self._cursor.execute(f'select * from {self.table_name};')
        return self._cursor.fetchall()

    def delete_all(self):
        self._cursor.execute(f'delete * from {self.table_name};')

    def inner_join(self):
        query = '''
            select p.name, p.price, o.quantity, p.price * o.quantity as total
            from products as p
            join orders as o
            on p.id = o.product_id
        '''
        self._cursor.execute(query)
        return self._cursor.fetchall()
