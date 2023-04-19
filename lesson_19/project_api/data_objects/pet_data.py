import random
import json


class Pet:
    def __init__(self, pet_id: int, name: str, photo_url=None, tags_id=None, tags_name=None, status=None):
        self.__pet_id = pet_id
        self.__category_id = random.randint(1, 10)
        self.__category_name = ["cats", "dogs", "rats", "turtles", "other"]
        self.__name = name
        self._photo_url = photo_url
        self.__tags_id = tags_id
        self.__tags_name = tags_name
        self.__status = status if status is not None else "available"

    def create_payload(self):
        data = {
            "id": self.__pet_id,
            "category": {
                "id": self.__category_id,
                "name": random.choice(self.__category_name)
            },
            "name": self.__name,
            "photoUrls": [self._photo_url] if self._photo_url is not None else [],
            "tags": [{"id": self.__tags_id, "name": self.__tags_name}] if self.__tags_id is not None and
                                                                          self.__tags_name is not None else [],
            "status": self.__status
        }
        json_data = json.dumps(data)
        return json_data

    def update_data(self, **kwargs):
        self.__dict__.update(**kwargs)
        return self
