from argparse import ArgumentParser
import json
import xmltodict


class Human:
    def __init__(self, name, age, gender, birth_year):
        self.name = name
        self.age = age
        self.gender = gender
        self.birth_year = birth_year

    def get_dict(self):
        return self.__dict__

    def convert_to_json(self, filename='test.json'):
        data = {"human": self.get_dict()}
        with open(filename, "w") as file:
            json.dump(data, file, indent=3)

    def convert_to_xml(self, filename='test.xml'):
        xml_dict = {"human": self.get_dict()}
        with open(filename, "w") as file:
            file.write(xmltodict.unparse(xml_dict, pretty=True))

    def parse_args(self):
        parser = ArgumentParser()
        parser.add_argument('--format', type=lambda format_string: format_string.lower(), help='Select format JSON/XML',
                            default='xml')
        args = parser.parse_args()
        if args.format == 'json':
            self.convert_to_json()
        elif args.format == 'xml':
            self.convert_to_xml()
        else:
            print('Not available format')


if __name__ == '__main__':
    human_data = Human('test_default', '29', 'f', '1993')
    human_data.parse_args()
    # human_data_xml = Human('test', '29', 'f', '1993')
    # human_data_xml.convert_to_xml('test.xml')
    # human_data_json = Human('test', '29', 'f', '1993')
    # human_data_json.convert_to_json('test.json')
