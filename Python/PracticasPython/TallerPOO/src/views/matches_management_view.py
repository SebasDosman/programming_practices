from pathlib import Path
from utils import FileManagerUtil, FiltersUtil


class MatchesManagementView:
    def __init__(self):
        self._line = "-" * 40
    
    def show_principal_menu(self):
        """
        Displays the main menu for managing match attendance.
        Allows verifying and updating ticket status.
        """
        try:
            print(self._line)
            print("Gestión de Asistencia a Partidos")

            current_dir = Path(__file__).parent.resolve()
            data_dir = current_dir.parent / "data_models" / "tickets_data_model.txt"
            
            id_boleto = input("Ingrese el id del boleto: ")
            print(self._line)
            
            if not self.verify_ticket(id_boleto):
                raise Exception("El boleto no es válido o no está disponible.")

            tickets = FiltersUtil.get_preload_data_model("tickets_data_model.txt")

            if tickets is not None:
                for ticket in tickets:
                    if ticket["id"] == id_boleto:
                        ticket["available"] = "false"

                        tickets_str = [str(i) for i in tickets]
                        FileManagerUtil.delete_data_txt(data_dir)
                        FileManagerUtil.write_txt(data_dir, tickets_str)
                        
                        print("El boleto es válido. Actualizando su estado a no disponible.")
                        break
            else:
                raise Exception("Error al cargar los datos de los boletos.")

        except Exception as e:
            print(f"Error: {e}")
    
    @staticmethod
    def verify_ticket(ticket):
        """
        Verifies if the ticket is valid and available.

        :param ticket: Ticket ID to verify.
        :return: True if the ticket is valid and available, False otherwise.
        """
        try:
            ticket_saved = FiltersUtil.search_item_by_id("tickets_data_model.txt", ticket)

            if not ticket_saved or ticket_saved["available"] == "false":
                return False
            return True
        except Exception as e:
            print(f"Error verifying ticket: {e}")
            return False
