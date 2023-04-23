import random
import json
from datetime import datetime

from lesson_19.utilities.decorators import allure_step


@allure_step
class Store:
    def __init__(self, **kwargs):
        self.__store_id = random.randint(1, 10000)
        self.__pet_id = random.randint(1, 900000)
        self.__quantity = 1 if 'quantity' not in kwargs.keys() else kwargs['quantity']
        self.__ship_date = datetime.utcnow().isoformat() + "Z"
        self.__status = 'placed' if 'status' not in kwargs.keys() else kwargs['status']
        self.__complete = False if 'complete' not in kwargs.keys() else kwargs['complete']

    def get_json(self):
        return json.dumps(self.__dict__)

    def update_data(self, **kwargs):
        self.__dict__.update(**kwargs)
