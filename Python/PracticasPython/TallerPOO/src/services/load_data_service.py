from services import APIService


class LoadDataService:
    @staticmethod
    def load_data_to_txt():
        """
        Fetches data from various API endpoints and saves the filtered data to TXT files.
        
        The method fetches data for teams, stadiums, and matches from predefined API URLs,
        processes the data using the appropriate filters, and saves it to corresponding
        TXT files.
        """
        try:
            api_service = APIService()
            
            teams = APIService.get_data_from_api("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json")
            if teams:
                api_service.filter_team_data_model(teams)
            
            stadiums = APIService.get_data_from_api("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/stadiums.json")
            if stadiums:
                api_service.filter_stadium_data_model(stadiums)
            
            matches = APIService.get_data_from_api("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/matches.json")
            if matches:
                api_service.filter_match_data_model(matches)
        except Exception as e:
            print(f"Ocurrió un error: {e}")
