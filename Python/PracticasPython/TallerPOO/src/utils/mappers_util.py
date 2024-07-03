import json


class MappersUtil:
    @staticmethod
    def list_strings_to_json(data_list_string):
        """
        Converts a list of strings to a list of dictionaries.

        :param data_list_string: List of strings to convert.
        :return: List of dictionaries.
        """
        try:
            dict_list = [json.loads(item.replace("'", '"')) for item in data_list_string]
            return dict_list
        except Exception as e:
            print(f"Error al convertir una lista de cadenas a JSON: {e}")
