from pathlib import Path
from utils import FileManagerUtil
import itertools as it


class FiltersUtil:
    @staticmethod
    def get_preload_data_model(file_name):
        """
        Returns a list of dictionaries with preload data from a file.
        
        :param file_name: Name of the file to load.
        :return: List of dictionaries with the preload data.
        """
        from utils import MappersUtil
        
        try:
            current_dir = Path(__file__).parent.resolve()
            data_dir = current_dir.parent / "data_models" / file_name

            if not data_dir.exists():
                raise FileNotFoundError(f"The directory '{data_dir}' does not exist.") 

            data_from_file = FileManagerUtil.read_txt(data_dir)
            dict_list_data = MappersUtil.list_strings_to_json(data_from_file)
            return dict_list_data        
        except FileNotFoundError as fn:
            print(f"{fn}")
        except Exception as e:
            print(f'Error al cargar datos para el filtro: {e}')

    @staticmethod
    def matches_by_country(id_country):
        """
        FiltersUtil matches by country ID.
        
        :param id_country: ID of the country to filter.
        :return: List of matches filtered by country.
        """
        matches_not_filtered = FiltersUtil.get_preload_data_model("matches_data_model.txt")
        matches_filtered = [match for match in matches_not_filtered if (match['idHomeTeam'] == id_country or match['idAwayTeam'] == id_country)]
        
        return matches_filtered
    
    @staticmethod
    def matches_by_stadium(id_stadium):
        """
        FiltersUtil matches by stadium ID.
        
        :param id_stadium: ID of the stadium to filter.
        :return: List of matches filtered by stadium.
        """
        matches_not_filtered = FiltersUtil.get_preload_data_model("matches_data_model.txt")
        matches_filtered = [match for match in matches_not_filtered if match['idStadium'] == id_stadium]

        return matches_filtered
    
    @staticmethod
    def matches_by_date(day_number):
        """
        FiltersUtil matches by date (day) within June 2024.
        
        :param day_number: Day to filter.
        :return: List of matches filtered by date.
        """
        matches_not_filtered = FiltersUtil.get_preload_data_model("matches_data_model.txt")
        full_date = f'2024-06-{day_number}'
        matches_filtered = [match for match in matches_not_filtered if match['date'] == full_date]

        return matches_filtered

    @staticmethod
    def validate_vampire_number(number_str):
        """
        Validates if a number is a vampire number.
        
        :param number_str: String representation of the number to validate.
        :return: True if the number is a vampire number, False otherwise.
        """
        try:
            print("-" * 40)
            print("Validando número vampiro, por favor espere...")
            
            if len(number_str) % 2 == 1:
                return False
        
            fangs = FiltersUtil.get_fangs(number_str)
        
            if not fangs:
                return False
        
            return True
        except Exception as e:
            print(f"Error al validar el número de vampiro: {e}")

    @staticmethod
    def get_fangs(num_str):
        """
        Finds the fangs (factor pairs) of a given number string if it is a vampire number.

        :param num_str: String representation of the number to check.
        :return: A tuple of strings representing the fangs if the number is a vampire number, False otherwise.
        """
        try:
            num_iter = it.permutations(num_str, len(num_str))
            
            for num_list in num_iter:
                v = ''.join(num_list)
                x, y = v[:int(len(v)/2)], v[int(len(v)/2):]
                
                if x[-1] == '0' and y[-1] == '0':
                    continue
                if int(x) * int(y) == int(num_str):
                    return x, y
            
            return False
        except Exception as e:
            print(f"Error al obtener colmillos: {e}")

    @staticmethod
    def validate_perfect_number(number_str):  
        """
        Validates if a number is a perfect number.
        
        :param number_str: String representation of the number to validate.
        :return: True if the number is a perfect number, False otherwise.
        """
        try:
            num_int = int(number_str)
            sum1 = 0

            for i in range(1, num_int):
                if (num_int % i == 0):
                    sum1 = sum1 + i

            if (sum1 == num_int):
                return True
            
            return False
        except Exception as e:
            print(f"Error al validar el número perfecto: {e}")

    @staticmethod
    def search_product_by_name(id_stadium, restaurant_name, product_name):
        """
        Searches for a product by name in a specific restaurant of a stadium.
        
        :param id_stadium: ID of the stadium.
        :param restaurant_name: Name of the restaurant.
        :param product_name: Name of the product to search.
        :return: Dictionary with the product data if found, None otherwise.
        """
        try:
            restaurants = FiltersUtil.get_preload_data_model("restaurants_data_model.txt")
            product = {}

            for restaurant in restaurants:
                if restaurant['stadium_id'] == id_stadium:
                    if restaurant['name'] == restaurant_name:
                        for product_data in restaurant['products']:
                            if product_data['name'] == product_name:
                                product = product_data
                                break
            
            return product
        except Exception as e:
            print(f"Error al buscar producto por su nombre: {e}")

    @staticmethod
    def search_product_by_type(id_stadium, restaurant_name, product_type):
        """
        Searches for products by type in a specific restaurant of a stadium.
        
        :param id_stadium: ID of the stadium.
        :param restaurant_name: Name of the restaurant.
        :param product_type: Type of the product to search.
        :return: List of dictionaries with the product data if found, empty list otherwise.
        """
        try:
            restaurants = FiltersUtil.get_preload_data_model("restaurants_data_model.txt")
            products = []

            for restaurant in restaurants:
                if restaurant['stadium_id'] == id_stadium:
                    if restaurant['name'] == restaurant_name:
                        for product_data in restaurant['products']:
                            if product_data['adicional'] == product_type:
                                products.append(product_data)
            
            return products
        except Exception as e:
            print(f"Error al buscar producto por tipo: {e}")
    
    @staticmethod
    def search_stadium_by_match(id_match):
        """
        Searches for a stadium by match ID.
        
        :param id_match: ID of the match.
        :return: Dictionary with the stadium data if found, None otherwise.
        """
        try:
            matches = FiltersUtil.get_preload_data_model("matches_data_model.txt")
            stadium = {}

            for match in matches:
                if match['id'] == id_match:
                    stadium = FiltersUtil.search_item_by_id("stadiums_data_model.txt", match['idStadium'])
                    break
            
            return stadium
        except Exception as e:
            print(f"Error al buscar estadio por id de partido: {e}")

    @staticmethod
    def search_restaurant_by_stadium(id_stadium):
        """
        Searches for restaurants by stadium ID.
        
        :param id_stadium: ID of the stadium.
        :return: List of dictionaries with the restaurant data if found, empty list otherwise.
        """
        try:
            restaurants = FiltersUtil.get_preload_data_model("restaurants_data_model.txt")
            restaurants_found = []

            for restaurant in restaurants:
                if restaurant['stadium_id'] == id_stadium:
                    restaurants_found.append(restaurant)
            
            return restaurants_found
        except Exception as e:
            print(f"Error al buscar restaurante por el id del estadio: {e}")

    @staticmethod
    def search_item_by_id(file_preload_data_path, id_item):
        """
        Searches for an item (stadium or team) by ID in preload data.
        
        :param file_preload_data_path: Path of the file with the preload data.
        :param id_item: ID of the item to search.
        :return: Dictionary with the item data if found, empty dictionary otherwise.
        """
        try:
            preload = FiltersUtil.get_preload_data_model(file_preload_data_path)
            item_found = {}

            for item in preload:
                if item['id'] == id_item:
                    item_found = item
                    break
            
            return item_found
        except Exception as e:
            print(f"Error al buscar artículo por su id: {e}")

    @staticmethod
    def search_product_by_price(id_stadium, restaurant_name, max_price):
        """
        Searches for products within a maximum price range in a specific restaurant of a stadium.

        :param id_stadium: ID of the stadium.
        :param restaurant_name: Name of the restaurant.
        :param max_price: Maximum price of the products to search.
        :return: List of dictionaries with the product data if found, empty list otherwise.    
        """
        try:
            restaurants = FiltersUtil.get_preload_data_model("restaurants_data_model.txt")
            products = []

            for restaurant in restaurants:
                if restaurant['stadium_id'] == id_stadium:
                    if restaurant['name'] == restaurant_name:
                        for product_data in restaurant['products']:
                            if float(product_data['price']) <= float(max_price):
                                products.append(product_data)
            
            return products
        except Exception as e:
            print(f"Error al buscar producto por precio: {e}")

    @staticmethod
    def get_seats_used_in_match(id_match):
        """
        Gets the seats used in a match.
        
        :param id_match: ID of the match.
        :return: List of seats used in the match.
        """
        try:
            tickets = FiltersUtil.get_preload_data_model("tickets_data_model.txt")
            seats_used = [ticket['seat'] for ticket in tickets if ticket.get('id_match') == id_match]
            return seats_used
        except Exception as e:
            print(f"Error al obtener los asientos utilizados en el partido: {e}")

    @staticmethod
    def search_ticket_by_match(id_match):
        """
        Searches for a ticket by match ID.
        
        :param id_match: ID of the match.
        :return: Dictionary with the ticket data if found, None otherwise.
        """
        try:
            tickets = FiltersUtil.get_preload_data_model("tickets_data_model.txt")
            ticket_found = next((ticket for ticket in tickets if ticket['idMatch'] == id_match), None)
            return ticket_found
        except Exception as e:
            print(f"Error en la búsqueda de entradas por el id del partido: {e}")   

    @staticmethod
    def get_full_match_info(id_match):
        """
        Gets the full information of a match.
        
        :param id_match: ID of the match.
        :return: Dictionary with the full information of the match.
        """
        try:
            match_data_model = FiltersUtil.search_item_by_id("matches_data_model.txt", id_match)
            match_info = {}

            if match_data_model:
                match_info['id'] = match_data_model['id']
                match_info['home_team'] = FiltersUtil.search_item_by_id("teams_data_model.txt", match_data_model['idHomeTeam'])
                match_info['away_team'] = FiltersUtil.search_item_by_id("teams_data_model.txt", match_data_model['idAwayTeam'])
                match_info['stadium'] = FiltersUtil.search_item_by_id("stadiums_data_model.txt", match_data_model['idStadium'])
                match_info['date'] = match_data_model['date']
            
            return match_info
        except Exception as e:
            print(f"Error al obtener la información completa del partido: {e}")
    
    @staticmethod
    def get_ticket_with_dni(client_dni):
        """
        Gets the ticket with the given DNI.
        
        :param client_dni: DNI of the user.
        :return: Dictionary with the user data if found, None otherwise.
        """
        try:
            tickets = FiltersUtil.get_preload_data_model("tickets_data_model.txt")
            ticket_found = next((ticket for ticket in tickets if ticket.get('dni_client') == client_dni), None)
            return ticket_found
        except Exception as e:
            print(f"Error al obtener usuario con dni: {e}")
