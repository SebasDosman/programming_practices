import json
import os


class FileManagerUtil:
    @staticmethod
    def create_file_if_not_exists(file_path, default_content=None):
        """
        Creates a file if it does not exist and optionally writes default content to it.
        
        :param file_path: Path to the file.
        :param default_content: Default content to write (optional).
        """
        if not os.path.exists(file_path):
            if default_content is not None:
                if file_path.endswith(".json"):
                    FileManagerUtil.write_json(file_path, default_content)
                else:
                    FileManagerUtil.write_txt(file_path, default_content)
            else:
                open(file_path, "w").close()

    @staticmethod
    def read_json(file_path):
        """
        Reads content from a JSON file and returns it as a dictionary.
        
        :param file_path: Path to the JSON file.
        :return: Dictionary containing the JSON data.
        """
        FileManagerUtil.create_file_if_not_exists(file_path, default_content={})
        
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                return data
        except json.JSONDecodeError:
            print(f"Error al decodificar el archivo JSON: {file_path}") 
        return None

    @staticmethod
    def write_json(file_path, data):
        """
        Writes a dictionary to a JSON file.
        
        :param file_path: Path to the JSON file.
        :param data: Dictionary to write.
        """
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
        except IOError:
            print(f"Error al escribir en el archivo JSON: {file_path}")

    @staticmethod
    def delete_data_txt(file_path):
        """
        Deletes the content of a TXT file.
        
        :param file_path: Path to the TXT file.
        """
        try:
            with open(file_path, 'w') as file:
                file.truncate(0)
        except IOError:
            print(f"Error al eliminar los datos en el archivo TXT: {file_path}")

    @staticmethod
    def read_txt(file_path):
        """
        Reads content from a text file and returns it as a list of lines.
        
        :param file_path: Path to the text file.
        :return: List of lines from the text file.
        """
        FileManagerUtil.create_file_if_not_exists(file_path, default_content=[])
        
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                lines = file.readlines()
                return [line.strip() for line in lines]
        except IOError:
            print(f"Error al leer el archivo de texto: {file_path}")
        return []

    @staticmethod
    def write_txt(file_path, lines):
        """
        Writes a list of lines to a text file.
        
        :param file_path: Path to the text file.
        :param lines: List of lines to write.
        """
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                for line in lines:
                    file.write(line + "\n")
        except IOError:
            print(f"Error al escribir en el archivo de texto: {file_path}")

    @staticmethod
    def append_txt(data, file_path):
        """
        Appends a string representation of data to a text file.
        
        :param data: Data to append (string representation).
        :param file_path: Path to the text file.
        """
        try:
            with open(file_path, "a", encoding="utf-8") as file:
                file.write(str(data) + "\n")
        except IOError:
            print(f"Error al escribir en el archivo JSON: {file_path}")
