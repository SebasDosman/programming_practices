class DisplayMenuView:
    def __init__(self):
        pass
    
    def display_main_menu(self):
        """
        Displays the main menu of the application.
        Allows navigation through different modules.
        """
        try:
            from views import MenuView
            
            while True:
                menu = MenuView("Eurocopa 2024", ["Gestión de Partidos y Estadios", "Gestión de Ventas de Entradas", "Gestión de Asistencia a Partidos", "Gestión de Restaurantes", "Gestión de Venta de Restaurantes", "Indicadores de Gestión", "Salir"])
                menu.display()
                
                option = menu.get_option()
                
                if option == 1:
                    self.display_first_menu()
                elif option == 2:
                    self.display_second_menu()
                elif option == 3:
                    self.display_third_menu()
                elif option == 4:
                    self.display_fourth_menu()
                elif option == 5:
                    self.display_fifth_menu()
                elif option == 6:
                    self.display_sixth_menu()
                elif option == len(menu.options):
                    break 
        except Exception as e:
            print(f"Error al mostrar el menú principal: {e}")
    
    def display_first_menu(self):
        """
        Displays the menu for managing matches and stadiums.
        Allows filtering matches by country, stadium, or date.
        """
        try:
            from views import MenuView, MatchesFilterView
            
            menu = MenuView("Gestión de Partidos y Estadios", ["Filtrar Partidos por País", "Filtrar Partidos por Estadio", "Filtrar Partidos por Fecha", "Salir"])
            matches_filter = MatchesFilterView()
            
            while True:
                menu.display()
                
                option = menu.get_option()
                
                if option == 1:
                    matches_filter.filter_matches_by_country()
                elif option == 2:
                    matches_filter.filter_matches_by_stadium()
                elif option == 3:
                    matches_filter.filter_matches_by_date()
                elif option == len(menu.options):
                    break
        except Exception as e:
            print(f"Error al mostrar el primer menú: {e}")
    
    def display_second_menu(self):
        """
        Displays the ticket management menu.
        """
        try:
            from views import TicketsManagementView
            
            ticket = TicketsManagementView()
            ticket.show_principal_menu()
        except Exception as e:
            print(f"Error al filtrar las coincidencias por fecha: {e}")
    
    def display_third_menu(self):
        """
        Displays the match management menu.
        """
        try:
            from views import MatchesManagementView
            
            match = MatchesManagementView()
            match.show_principal_menu()
        except Exception as e:
            print(f"Error al mostrar el tercer menú: {e}")
    
    def display_fourth_menu(self):
        """
        Displays the menu for managing restaurants.
        Allows filtering products by name, type, or price.
        """
        try:
            from views import MenuView, ProductsFilterView
            
            menu = MenuView("Gestión de Restaurantes", ["Filtrar Productos por Nombre", "Filtrar Productos por Tipo", "Filtrar Productos por Precio", "Salir"])
            products_filter = ProductsFilterView()
            
            while True:
                menu.display()
                
                option = menu.get_option()
                
                if option == 1:
                    products_filter.filter_products_by_name()
                elif option == 2:
                    products_filter.filter_products_by_type()
                elif option == 3:
                    products_filter.filter_products_by_price()
                elif option == len(menu.options):
                    break
        except Exception as e:
            print(f"Error al mostrar el cuarto menú: {e}")
    
    def display_fifth_menu(self):
        """
        Displays the restaurant management menu.
        """
        try:
            from views import RestaurantsManagementView
            
            restaurant = RestaurantsManagementView()
            restaurant.show_principal_menu()
        except Exception as e:
            print(f"Error al mostrar el quinto menú: {e}")
    
    def display_sixth_menu(self):
        """
        Displays the statistics management menu.
        """
        try:
            from views import StatisticsManagementView
            
            statistics = StatisticsManagementView()
            statistics.show_principal_menu()
        except Exception as e:
            print(f"Error al mostrar el sexto menú: {e}")
