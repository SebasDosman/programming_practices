class MatchesFilterView:
    def __init__(self):
        self._line = "-" * 40
    
    def filter_matches_by_country(self):
        """
        Filters matches by country based on user input.
        Displays filtered matches information.
        """
        try:
            from utils import FiltersUtil
            
            print(self._line)
            country_id = input("Ingrese el id del país: ")
            print(self._line)
            
            matches = FiltersUtil.matches_by_country(country_id)
            matches_filtered = [FiltersUtil.get_full_match_info(match["id"]) for match in matches]
            
            for i, match in enumerate(matches_filtered):
                print(f"{i + 1}. {match['home_team']['name']} vs {match['away_team']['name']} - {match['date']} - {match['stadium']['name']}")
        except Exception as e:
            print(f"Error al filtrar los partidos por país: {e}")
    
    def filter_matches_by_stadium(self):
        """
        Filters matches by stadium based on user input.
        Displays filtered matches information.
        """
        try:
            from utils import FiltersUtil
            
            print(self._line)
            stadium_id = input("Ingrese el id del estadio: ")
            print(self._line)
            
            matches = FiltersUtil.matches_by_stadium(stadium_id)
            matches_filtered = [FiltersUtil.get_full_match_info(match["id"]) for match in matches]
            
            for i, match in enumerate(matches_filtered):
                print(f"{i + 1}. {match['home_team']['name']} vs {match['away_team']['name']} - {match['date']} - {match['stadium']['name']}")
        except Exception as e:
            print(f"Error al filtrar los partidos por estadio: {e}")
    
    def filter_matches_by_date(self):
        """
        FiltersUtil matches by date based on user input.
        Displays filtered matches information.
        """
        try:
            from utils import FiltersUtil
            
            print(self._line)
            date = input("Ingrese la fecha (dd): ")
            print(self._line)
            
            matches = FiltersUtil.matches_by_date(date)
            matches_filtered = [FiltersUtil.get_full_match_info(match["id"]) for match in matches]
            
            for i, match in enumerate(matches_filtered):
                print(f"{i + 1}. {match['home_team']['name']} vs {match['away_team']['name']} - {match['date']} - {match['stadium']['name']}")
        except Exception as e:
            print(f"Error filtering matches by date: {e}")