# class provides a way to store and retrieve a locator for an element in a web page.
# The "method" attribute represent the method used to locate the element (e.g., "id", "name", "class name", "xpath"),
# while the "locator_string" attribute represents the value used to locate the element based on the chosen method.


class Locator:
    def __init__(self, method: str, locator_string: str):
        self.__method = method
        self.__locator_string = locator_string

    def get_locator(self) -> tuple:
        return self.__method, self.__locator_string
