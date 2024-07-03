from pathlib import Path
import re
from utils import FiltersUtil, FileManagerUtil


class RestaurantsManagementView:
    def __init__(self):
        self._line = "-" * 40

    def show_principal_menu(self):
        """
        Displays the principal menu for restaurant sales management.
        """
        print(self._line)
        print("Gestión de Venta de Restaurantes")

        ticket_data = self.get_client_dni()
        stadium = FiltersUtil.search_stadium_by_match(ticket_data["id_match"])
        restaurants_per_game = FiltersUtil.search_restaurant_by_stadium(stadium['id'])

        print(self._line)
        print(f"{stadium['name']} - {stadium['id']}")

        for restaurant in restaurants_per_game:
            print(f"Restaurante: {restaurant['name']}")

        choice = self.options_to_search_products(stadium["name"])
        restaurants_selected = self.choose_product_to_buy(choice, stadium['id'], restaurants_per_game)

        validate_age = True
        product_selected = {}

        while validate_age:
            product_selected = self.choose_restaurant_product(restaurants_selected)

            if product_selected[1]["adicional"] == "alcoholic" and int(ticket_data["age_client"]) < 18:
                validate_age = True
                print(self._line)
                print("No puede comprar productos alcohólicos, es menor de edad, vuelva a intentar")
            else:
                validate_age = False

        old_stock = product_selected[1]["stock"]
        base_price = product_selected[1]["price"]

        product_updated = self.get_quantity(product_selected)
        product_final = self.update_product_price(ticket_data, product_updated, old_stock - product_updated[1]["stock"])
        discount = product_final[0]
        product_final = product_final[1]
        
        print(self._line)
        print(f"El producto es: {product_final[1]['name']} - Precio(+IVA): {str(product_final[1]['price'])} - Cantidad: {old_stock - product_final[1]['stock']} - Precio por Unidad: {base_price}")

        if self.ask_last_question(product_final[1]):
            print(self._line)
            print(f"Se realizó la compra de: {product_final[1]['name']} con un descuento de: ${discount} y un precio final de: ${product_final[1]['price']} cantidad: {old_stock - product_final[1]['stock']} y precio base por unidad: {base_price}")

            name_restaurant = product_final[0]
            date = self.get_data_match(ticket_data["id_match"])
            product_final_to_register = product_final[1]

            data_to_register = { 
                "id_stadium": stadium['id'], 
                "name_restaurant": name_restaurant['name'], 
                "name_product": product_final[1]["name"], 
                "total": str(product_final_to_register['price']), 
                "quantity": str(old_stock - product_final_to_register['stock']), 
                "date": date, 
                "dni_client": ticket_data["dni_client"]
            }

            self.register_sale(data_to_register, old_stock)

    @staticmethod
    def get_data_match(match_id):
        """
        Get the date of the match.

        :param match_id: The match id.
        :return: The date of the match.
        """
        matches = FiltersUtil.get_preload_data_model("matches_data_model.txt")
        for match in matches:
            if match["id"] == match_id:
                return match["date"]

    @staticmethod
    def get_quantity(product_updated):
        """
        Get the quantity of the product to buy.

        :param product_updated: The product information.
        :return: The product with the updated stock.
        """
        while True:
            try:
                quantity = int(input("Ingrese la cantidad del producto a comprar: "))
                if 0 < quantity <= product_updated[1]['stock']:
                    product_updated[1]['stock'] -= quantity
                    return product_updated
                else:
                    raise ValueError
            except ValueError:
                print("Ingrese una cantidad válida (mayor a 0 y menor o igual al stock disponible)")

    def update_product_price(self, ticket, product, quantity):
        """
        Update the product price based on the client's VIP status.

        :param ticket: The ticket information.
        :param product: The product information.
        :param quantity: The quantity of the product.
        :return: The updated product with price and any discounts applied.
        """
        try:
            price = float(product[1]['price']) * quantity
            print(self._line)
            print("Validando que es un número perfecto...")
            is_perfect = FiltersUtil.validate_perfect_number(ticket['dni_client'])
            discount = 0

            if is_perfect:
                print(self._line)
                print("Felicitaciones, usted ha ganado un descuento del 15% en su compra porque su cédula es un número perfecto.")
                discount = price * 0.15

            price = price - discount
            price = price + (price * 0.16)
            product[1]['price'] = price

            return [discount, product]

        except Exception as e:
            print(self._line)
            print(f"Error al actualizar el precio del producto: {str(e)}")

    def register_sale(self, product_selected, old_stock):
        """
        Register the sale of the product and update restaurant stock.

        :param product_selected: The product information.
        :param old_stock: The previous stock of the product.
        """
        try:
            current_dir = Path(__file__).parent.resolve()
            data_dir = current_dir.parent / "data_models" / "sales_data_model.txt"
            preload_data = FiltersUtil.get_preload_data_model("sales_data_model.txt")

            sales = []
            for sale in preload_data:
                sales.append(str(sale))

            sales.append(str(product_selected))
            FileManagerUtil.write_txt(data_dir, sales)

            self.update_restaurant_stock(product_selected, old_stock)

        except Exception as e:
            print(self._line)
            print(f"Error al cargar los datos de ventas: {str(e)}")

    def update_restaurant_stock(self, product_selected, old_stock):
        """
        Update the stock of the restaurant after a sale.

        :param product_selected: The product information.
        :param old_stock: The previous stock of the product.
        """
        try:
            current_dir = Path(__file__).parent.resolve()
            data_dir_restaurant = current_dir.parent / "data_models" / "restaurants_data_model.txt"
            preload_data = FiltersUtil.get_preload_data_model(data_dir_restaurant)

            restaurants = []
            for restaurant in preload_data:
                if restaurant["name"] == product_selected["name_restaurant"]:
                    for product in restaurant['products']:
                        if product['name'] == product_selected['name_product']:
                            product['stock'] = old_stock - int(product_selected['quantity'])
                    restaurants.append(str(restaurant))

            FileManagerUtil.write_txt(data_dir_restaurant, restaurants)

        except Exception as e:
            print(self._line)
            print(f"Error al actualizar los datos del restaurante: {str(e)}")

    def ask_last_question(self, product_final):
        """
        Ask the client if they want to finalize the purchase.

        :param product_final: The final product information.
        :return: True if the client confirms, False otherwise.
        """
        while True:
            try:
                print(self._line)
                print("¿Desea efectuar la compra del producto?")
                print("1. Si")
                print("2. No")
                answer = int(input("Ingrese la opción: "))
                if answer == 1:
                    return True
                elif answer == 2:
                    return False
                else:
                    raise ValueError

            except ValueError:
                print(self._line)
                print("Ingrese una opción correcta (1 o 2)")

    def choose_product_to_buy(self, choice, stadium_id, restaurants_available):
        """
        Choose a product to buy based on user choice.

        :param choice: The user's choice of product search option.
        :param stadium_id: The id of the stadium.
        :param restaurants_available: The list of available restaurants.
        :return: The chosen product information.
        """
        try:
            print(self._line)
            if choice == 1:
                restaurant_products = self.search_from_product_name(stadium_id, restaurants_available)
                self.print_products_available_from_differents_searches(restaurant_products)
                return restaurant_products

            elif choice == 2:
                restaurant_products = self.search_from_product_type(stadium_id, restaurants_available)
                self.print_products_available_from_differents_searches(restaurant_products)
                return restaurant_products

            elif choice == 3:
                restaurant_products = self.search_from_price_range(stadium_id, restaurants_available)
                self.print_products_available_from_differents_searches(restaurant_products)
                return restaurant_products

            elif choice == 4:
                self.print_restaurants_available(restaurants_available)
                return self.convert_restaurants_to_format(restaurants_available)

        except Exception as e:
            print(self._line)
            print(f"Error al buscar productos ya cargados. Intente de nuevo: {str(e)}")

    @staticmethod
    def convert_restaurants_to_format(restaurants_available):
        """
        Convert the available restaurants to a specific format.

        :param restaurants_available: The list of available restaurants.
        :return: The list of restaurants in a formatted matrix.
        """
        restaurants = []
        for rest in restaurants_available:
            products = []
            for product in rest["products"]:
                products.append(product)
            restaurants.append([rest, products])
        return restaurants

    def choose_restaurant_product(self, restaurants_available):
        """
        Choose the restaurant and product to buy.

        :param restaurants_available: The list of available restaurants.
        :return: The chosen restaurant and product information.
        """
        print(self._line)
        print("Seleccione el restaurante y el producto a comprar: ")

        while True:
            try:
                restaurant = int(input("Ingrese la opción del restaurante: "))
                if restaurants_available[restaurant - 1][0] == []:
                    raise Exception

                product = int(input("Ingrese la opción del producto: "))
                if restaurants_available[restaurant - 1][1][product - 1] == {}:
                    raise Exception

                return [restaurants_available[restaurant - 1][0], restaurants_available[restaurant - 1][1][product - 1]]

            except Exception as e:
                print(self._line)
                print("Error al seleccionar el producto, ingrese ids correctos")

    def search_from_price_range(self, stadium_id, restaurants_available):
        """
        Search products by price range.

        :param stadium_id: The stadium id.
        :param restaurants_available: The list of available restaurants.
        :return: A matrix with [restaurant, list of product dictionaries].
        """
        while True:
            try:
                max_price = input("Ingrese el precio máximo: ")
                all_the_info = []

                for rest in restaurants_available:
                    product = FiltersUtil.search_product_by_price(stadium_id, rest['name'], max_price)
                    if product and product != {}:
                        all_the_info.append([rest, product])

                if all_the_info != []:
                    return all_the_info
                else:
                    raise KeyError

            except KeyError:
                print(self._line)
                print("No se encontraron productos en ese rango de precios. Intente de nuevo...")

    def search_from_product_type(self, stadium_id, restaurants_available):
        """
        Search products by type.

        :param stadium_id: The stadium id.
        :param restaurants_available: The list of available restaurants.
        :return: A matrix with [restaurant, list of product dictionaries].
        """
        while True:
            try:
                print("Tipos de productos disponibles: 3. package, 4. plate")
                print("1. Alcoholic")
                print("2. Non-alcoholic")
                print("3. Package")
                print("4. Plate")
                
                print(self._line)
                product_type = input("Ingrese el código para el tipo del producto (Del 1 al 4): ")
                id_type = ""

                if product_type == "1":
                    id_type = "alcoholic"
                elif product_type == "2":
                    id_type = "non-alcoholic"
                elif product_type == "3":
                    id_type = "package"
                elif product_type == "4":
                    id_type = "plate"
                else:
                    raise KeyError

                all_the_info = []

                for rest in restaurants_available:
                    product = FiltersUtil.search_product_by_type(stadium_id, rest['name'], id_type)
                    if product and product != {}:
                        all_the_info.append([rest, product])

                if all_the_info != []:
                    return all_the_info
                else:
                    raise ValueError

            except KeyError:
                print(self._line)
                print("Ingrese un código válido (Del 1 al 4)")

            except ValueError:
                print(self._line)
                print("No se encontraron productos de ese tipo. Intente de nuevo...")

    def search_from_product_name(self, stadium_id, restaurants_available):
        """
        Search products by name.

        :param stadium_id: The stadium id.
        :param restaurants_available: The list of available restaurants.
        :return: A matrix with [restaurant, product dictionary].
        """
        while True:
            try:
                product_name = input("Ingrese el nombre del producto: ")

                for rest in restaurants_available:
                    product = FiltersUtil.search_product_by_name(stadium_id, rest['name'], product_name)
                    if product and product != {}:
                        return [[rest, [product]]]

                raise ValueError

            except ValueError:
                print(self._line)
                print("No se encontró ningún producto con ese nombre. Intente de nuevo...")

    def options_to_search_products(self, stadium_name):
        """
        Display options to search products.

        :param stadium_name: The name of the stadium.
        :return: The chosen option (1 to 4).
        """
        print(self._line)
        print(f"Seleccione una opción para buscar productos en el estadio {stadium_name}:")
        print("1. Buscar por Nombre de Producto")
        print("2. Buscar por Tipo de Producto (alcoholic, non-alcoholic, package, plate)")
        print("3. Buscar por Precio Máximo (rango de precios)")
        print(f"4. Buscar por Restaurantes Disponibles en el Estadio {stadium_name}")

        while True:
            try:
                print(self._line)
                option = int(input("Ingrese una opción: "))
                if 1 <= option <= 4:
                    return option
                else:
                    raise ValueError

            except ValueError:
                print(self._line)
                print("Ingrese una opción válida (Del 1 al 4)")

    def get_client_dni(self):
        """
        Get the client's DNI for ticket validation.

        :return: The ticket information.
        """
        while True:
            try:
                dni = input("Ingrese su número de identificación: ")

                if re.match("^\d{4,10}$", dni):
                    ticket = FiltersUtil.get_ticket_with_dni(dni)
                    if self.validate_client_dni_is_vip(ticket, dni):
                        return ticket
                    else:
                        raise ValueError
                else:
                    raise ValueError

            except ValueError:
                print(self._line)
                print("Ingrese un número de DNI válido (de 4 a 10 caracteres, sin letras, sin caracteres especiales)")

    @staticmethod
    def validate_client_dni_is_vip(ticket, client_dni):
        """
        Validate if the client is VIP based on ticket information.

        :param ticket: The ticket information.
        :param client_dni: The client's DNI.
        :return: True if the client is VIP, False otherwise.
        """
        if ticket != {}:
            if ticket["type"] == "VIP":
                return True
        return False

    @staticmethod
    def print_products_available_from_differents_searches(restaurant_products):
        """
        Print the available products based on different search criteria.

        :param restaurant_products: The matrix of products available.
        """
        for index_restaurant, tuple_ in enumerate(restaurant_products):
            restaurant = tuple_[0]
            restaurant_products = tuple_[1]

            print("-" * 40)
            print(f"{index_restaurant + 1}. Restaurante: {restaurant['name']}")

            for index_product, product in enumerate(restaurant_products):
                print(f"{index_product + 1}. Producto: {product['name']} - Precio (NO-IVA): {product['price']} USD - Tipo: {product['adicional']} - Stock: {product['stock']}")

    @staticmethod
    def print_restaurants_available(restaurants_available):
        """
        Print the available restaurants.

        :param restaurants_available: The list of available restaurants.
        """
        for index_restaurant, rest in enumerate(restaurants_available):
            print("-" * 40)
            print(f"{index_restaurant + 1}. Restaurante: {rest['name']}")

            for index_product, product in enumerate(rest['products']):
                print(f"{index_product + 1}. Producto: {product['name']} - Precio (NO-IVA): {product['price']} USD - Tipo: {product['adicional']} - Stock: {product['stock']}")

