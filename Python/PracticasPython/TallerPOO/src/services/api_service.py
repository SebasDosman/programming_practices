from pathlib import Path
import requests
from utils import FileManagerUtil


class APIService:
    def __init__(self):
        self._current_dir = Path(__file__).parent.resolve()
        self._data_dir = self._current_dir.parent / 'data_models'
        self._data_dir.mkdir(parents=True, exist_ok=True)
    
    @staticmethod
    def get_data_from_api(url, params=None):
        """
        Makes a GET request to the given URL and returns the response data.
        
        :param url: URL of the API endpoint.
        :param params: Optional parameters for the GET request.
        :return: Response data as JSON or None if an error occurs.
        """
        try:
            response = requests.get(url, params=params)
            response.raise_for_status() 
            return response.json()
        except requests.RequestException as e:
            print(f"Error al obtener datos de la API: {e}")
            return None
    
    @staticmethod
    def save_data_to_txt(data, file_path):
        """
        Saves the data obtained from the API to a TXT file.
        
        :param data: Data to save (list, dict, or other).
        :param file_path: Path to the TXT file.
        """
        if isinstance(data, list):
            lines = [str(item) for item in data]
        elif isinstance(data, dict):
            lines = [f"{key}: {value}" for key, value in data.items()]
        else:
            lines = [str(data)]
        
        FileManagerUtil.write_txt(file_path, lines)

    def filter_team_data_model(self, data):
        """
        Filters the data from the API to the Team data model and saves it to a TXT file.
        
        :param data: Team data from the API in JSON format.
        """
        try:
            path_teams_file = self._data_dir / "teams_data_model.txt"
            FileManagerUtil.delete_data_txt(path_teams_file)
            
            for team_data in data:
                team_data_model = {
                    "id": team_data['id'],
                    "code": team_data['code'],
                    "name": team_data['name'],
                    "group": team_data['group']
                }
                FileManagerUtil.append_txt(team_data_model, path_teams_file)
        except Exception as e:
            print(f"Se produjo un error en el filtro de equipos: {e}")

    def filter_stadium_data_model(self, data):
        """
        Filters the data from the API to the Stadium data model and saves it to a TXT file.
        
        :param data: Stadiums data from the API in JSON format.
        """
        try:
            path_stadiums_file = self._data_dir / "stadiums_data_model.txt"
            path_restaurants_file = self._data_dir / "restaurants_data_model.txt"
            FileManagerUtil.delete_data_txt(path_restaurants_file)
            FileManagerUtil.delete_data_txt(path_stadiums_file)
            
            for stadium_data in data:
                stadium_data_model = {
                    "id": stadium_data['id'],
                    "name": stadium_data['name'],
                    "location": stadium_data['city']
                }
                FileManagerUtil.append_txt(stadium_data_model, path_stadiums_file)

                for restaurant in stadium_data['restaurants']:
                    restaurant_data_model = {
                        "stadium_id": stadium_data['id'],
                        "name": restaurant['name'],
                        "products": restaurant['products']
                    }
                    FileManagerUtil.append_txt(restaurant_data_model, path_restaurants_file)
        except Exception as e:
            print(f"Se produjo un error en el filtro de estadios: {e}")

    def filter_match_data_model(self, data):
        """
        Filters the data from the API to the Match data model and saves it to a TXT file.
        
        :param data: Data of the Match from the API in JSON format.
        """
        try:
            path_matches_file = self._data_dir / "matches_data_model.txt"
            FileManagerUtil.delete_data_txt(path_matches_file)
            
            for match_data in data:
                match_data_model = {
                    "id": match_data['id'],
                    "idHomeTeam": match_data['home']['id'],
                    "idAwayTeam": match_data['away']['id'],
                    "idStadium": match_data['stadium_id'],
                    "date": match_data['date']
                }
                FileManagerUtil.append_txt(match_data_model, path_matches_file)
        except Exception as e:
            print(f"Se produjo un error en el filtro de partidos: {e}")
