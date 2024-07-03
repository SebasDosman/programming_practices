from pathlib import Path
from utils import FiltersUtil, FileManagerUtil
from models import Ticket
import re


class TicketsManagementView:
    def __init__(self):
        self._line = "-" * 40
        self._search_seat_title = "A continuación, se mostrarán los asientos disponibles"
        self._select_option_seat_prompt = "Ingrese una opción de asiento: "
        self._put_name_prompt = "Ingrese su nombre: "
        self._put_DNI_prompt = "Ingrese su número de identificación: "
        self._put_age_prompt = "Ingrese su edad: "
        self._coords_seats_x = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        self._coords_seats_y = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    def get_client_age(self):
        """
        Obtiene la edad del cliente

        :return: La edad del cliente
        """
        while True:
            try:
                age = int(input(self._put_age_prompt))
                
                if 6 <= age <= 100:
                    return age
                else:
                    raise ValueError
            except ValueError:
                print(self._line)
                print(f"Ingrese un número válido (entre 6 y 100 años)")
                print(self._line)
    
    def get_client_DNI(self):
        """
        Obtiene el DNI del cliente

        :return: El DNI del cliente
        """
        while True:
            try:
                dni = input(self._put_DNI_prompt)
                
                if re.match("^\d{4,10}$", dni):
                    return dni
                else:
                    raise ValueError
            except ValueError:
                print(self._line)
                print(f"Ingrese un número de identificación válido (de 4 a 10 caracteres, sin letras ni caracteres especiales)")
                print(self._line)
    
    def get_client_name(self):
        """
        Obtiene el nombre del cliente

        :return: El nombre del cliente
        """
        while True:
            try:
                print(self._line)
                print("Gestión de Ventas de Entradas")
                name = input(self._put_name_prompt)
                if 6 <= len(name) <= 50 and re.match("^[A-Za-z ]+$", name):
                    return name
                else:
                    raise ValueError
            except ValueError:
                print(self._line)
                print(f"Ingrese un nombre válido (entre 6 y 50 caracteres, sin números ni caracteres especiales)")
                print(self._line)
    
    def show_principal_menu(self):
        """
        Muestra el menú principal para la gestión de entradas.
        """
        selected_name = self.get_client_name()
        selected_dni_client = self.get_client_DNI()
        selected_age_client = self.get_client_age()
        selected_id_match = self.select_match()
        selected_type = self.get_type_ticket()

        selected_seat = self.search_seat(selected_id_match)
        price_info = self.show_ticket_final_price(selected_dni_client, selected_type)
        buy_ticket = self.ask_for_register_ticket(price_info, selected_seat)

        if buy_ticket:
            id_ticket = self.generate_id_ticket()
            purchased_ticket = Ticket(id_ticket, selected_dni_client, selected_name, selected_age_client, selected_type, selected_seat, True, selected_id_match, str(price_info["total"]))
            self.save_register_ticket(purchased_ticket)

    @staticmethod
    def generate_id_ticket():
        """
        Genera un ID de ticket

        :return: El ID del ticket
        """
        tickets_in_file = FiltersUtil.get_preload_data_model("tickets_data_model.txt")
        
        if not tickets_in_file or len(tickets_in_file) == 0:
            return "1"
        return str(len(tickets_in_file) + 1)

    def save_register_ticket(self, ticket_info):
        """
        Guarda el ticket en el archivo txt
        """
        data_dir = Path(__file__).parent.resolve().parent / "data_models" / "tickets_data_model.txt"
        old_tickets = FileManagerUtil.read_txt(data_dir)

        str_tickets = [str(ticket) for ticket in old_tickets]
        str_tickets.append(str(ticket_info.to_dict()).replace("'", '"'))
        FileManagerUtil.write_txt(data_dir, str_tickets)

        print(self._line)
        print("Registro exitoso...")
    
    def ask_for_register_ticket(self, prices_info, seat):
        """
        Pregunta al usuario si desea registrar la compra del ticket

        :param prices_info: Información del precio del ticket
        :param seat: Asiento seleccionado
        :return: True si el usuario desea registrar la compra, False si no
        """
        print(self._line)
        print(f"Información del ticket -> IVA 16%: {round(prices_info['IVA'], 1)} - Monto inicial {prices_info['base']} - Descuento {prices_info['discount']} - Total {prices_info['total']} - Asiento {seat}")   
        print(self._line)
        print("¿Desea registrar la compra del ticket?")
        print("1. Si")
        print("2. No")

        while True:
            try:
                print(self._line)
                choice = int(input("Ingrese una opción: "))
                if choice == 1:
                    return True
                elif choice == 2:
                    return False
                else:
                    raise ValueError
            except ValueError:
                print(self._line)
                print("Opción inválida. Por favor ingrese una opción válida.\n")
                print(self._line)

    @staticmethod
    def show_ticket_final_price(client_dni, selected_type):
        """
        Muestra el precio final del ticket

        :param client_dni: DNI del cliente
        :param selected_type: Tipo de ticket seleccionado
        :return: Un diccionario con la información del IVA, descuento, base y TOTAL
        """
        filtersUtil = FiltersUtil()

        price_base = 0
        if selected_type == "General":
            price_base = 35
        elif selected_type == "VIP":
            price_base = 75
        discount = 0
        original_price = price_base
        if filtersUtil.validate_vampire_number(client_dni):
            print("Felicidades, su identificación es un número vampiro. Obtuviste un 50% de descuento")
            price_base *= 0.5
            discount = original_price * 0.5
        value_iva = price_base * 0.16
        total = price_base + value_iva
        return {"IVA": value_iva, "discount": discount, "base": original_price, "total": total}

    def get_type_ticket(self):
        """
        Obtiene el tipo de ticket

        :return: El tipo de ticket
        """
        print(self._line)
        print("Seleccione el tipo de entrada (IVA no incluido)")
        print("1. General - $35")
        print("2. VIP - $75")
        
        while True:
            try:
                choice = int(input("Ingrese una opción: "))
                if choice == 1:
                    return "General"
                elif choice == 2:
                    return "VIP"
                else:
                    raise ValueError
            except ValueError:
                print(self._line)
                print("Opción inválida. Por favor ingrese una opción válida.\n")
                print(self._line)

    def select_match(self):
        """
        Selecciona un partido

        :return: El ID del partido seleccionado
        """
        print(self._line)
        print("Seleccione un partido")
        
        matches = FiltersUtil.get_preload_data_model("matches_data_model.txt")
        matches_filtered = [FiltersUtil.get_full_match_info(match["id"]) for match in matches]

        for i, match in enumerate(matches_filtered):
            print(f"{i + 1}. {match['home_team']['name']} vs {match['away_team']['name']} - {match['date']} - {match['stadium']['name']}")
        print(self._line)
        
        while True:
            try:
                choice = int(input("Ingrese una opción: "))
                if 1 <= choice <= len(matches_filtered):
                    return matches_filtered[choice - 1]["id"]
                else:
                    raise ValueError
            except ValueError:
                print("Opción inválida. Por favor ingrese un número de partido válido.\n")

    def search_seat(self, id_match):
        """
        Busca un asiento disponible para el cliente

        :param id_match: ID del partido
        :return: El asiento seleccionado
        """
        print(self._search_seat_title)
        used_seats = FiltersUtil.get_seats_used_in_match(id_match)

        if used_seats is None:
            used_seats = []

        self.print_seats(used_seats)
        selected_seat = self.select_seat(used_seats)
        return selected_seat

    def select_seat(self, used_seats):
        """
        Permite al cliente seleccionar el asiento que desea comprar

        :param used_seats: Lista de asientos ocupados
        :return: El asiento seleccionado
        """
        while True:
            try:
                choice = input(self._select_option_seat_prompt)
                if len(choice) == 2 and choice[0] in self._coords_seats_x and choice[1] in self._coords_seats_y and choice not in used_seats:
                    return choice
                else:
                    raise ValueError
            except ValueError:
                print(self._line)
                print("Opción inválida. Por favor ingrese un código de asiento válido (Formato Letra y Número).\n")
                print(self._line)
    
    def print_seats(self, used_seats):
        """
        Imprime los asientos disponibles

        :param used_seats: Lista de asientos ocupados
        """
        for x in self._coords_seats_x:
            print('| ', end="")
            for y in self._coords_seats_y:
                if f"{x}{y}" in used_seats:
                    print(f"[X]", end=" ")
                else:
                    print(f"[{x}{y}]", end=" ")
            print(" |", end="")
            print("\n")
