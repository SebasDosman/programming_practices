import json
import os


class FileManager:
    @staticmethod
    def create_file_if_not_exists(file_path, default_content=None):
        """
        Creates a file if it does not exist and writes default content to it.
        
        :param file_path: Path to the file.
        :param default_content: Default content to write (JSON or text).
        """
        if not os.path.exists(file_path):
            if default_content is not None:
                if file_path.endswith('.json'):
                    FileManager.write_json(file_path, default_content)
                else:
                    FileManager.write_txt(file_path, default_content)
            else:
                open(file_path, 'w').close()

    @staticmethod
    def read_json(file_path):
        """
        Reads a JSON file and returns its content as a dictionary.
        
        :param file_path: Path to the JSON file.
        :return: Content of the JSON file as a dictionary.
        """
        FileManager.create_file_if_not_exists(file_path, default_content={})
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return data
        except json.JSONDecodeError:
            print(f"Error decoding the JSON file: {file_path}")
        return None

    @staticmethod
    def write_json(file_path, data):
        """
        Writes a dictionary to a JSON file.
        
        :param file_path: Path to the JSON file.
        :param data: Dictionary to write.
        """
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
        except IOError:
            print(f"Error writing to the JSON file: {file_path}")

    @staticmethod
    def read_txt(file_path):
        """
        Reads a text file and returns its content as a list of lines.
        
        :param file_path: Path to the text file.
        :return: List of lines from the text file.
        """
        FileManager.create_file_if_not_exists(file_path, default_content=[])
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                return [line.strip() for line in lines]
        except IOError:
            print(f"Error reading the text file: {file_path}")
        return []

    @staticmethod
    def write_txt(file_path, lines):
        """
        Writes a list of lines to a text file.
        
        :param file_path: Path to the text file.
        :param lines: List of lines to write.
        """
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                for line in lines:
                    file.write(line + '\n')
        except IOError:
            print(f"Error writing to the text file: {file_path}")