from collections import defaultdict
from utils import FiltersUtil, GraphicsUtil
from views import MenuView


class StatisticsManagementView:
    def __init__(self):
        self._tickets = FiltersUtil.get_preload_data_model("tickets_data_model.txt")
        self._line = "-" * 40

    def show_principal_menu(self):
        """
        Displays the main menu for statistics management.
        """
        while True:
            menu = MenuView("Indicadores de Gestión", [
                "Promedio de Gasto de Clientes VIP",
                "Tabla Con Asistencia a Partidos (Mejor a Peor)",
                "Partido Con Mayor Asistencia",
                "Partido Con Mayor Cantidad de Boletos Vendidos",
                "Top 3 Productos Vendidos",
                "Top 3 Clientes Con Más Boletos Comprados",
                "Salir"
            ])
            menu.display()

            option = menu.get_option()

            if option == 1:
                self.average_vip_client_spend()
            elif option == 2:
                self.assistance_statistics()
            elif option == 3:
                self.max_assistance_match()
            elif option == 4:
                self.max_tickets_sold_match()
            elif option == 5:
                self.top_three_products()
            elif option == 6:
                self.top_three_clients()
            elif option == len(menu.options):
                break

    def average_vip_client_spend(self):
        """
        Calculates and displays the average spending of VIP clients.
        """
        total_spent = 0
        vip_sales_count = 0
        sales = FiltersUtil.get_preload_data_model("sales_data_model.txt")

        for sale in sales:
            total_spent += float(sale["total"])
            vip_sales_count += 1

        if vip_sales_count > 0:
            average_spend = total_spent / vip_sales_count
        else:
            average_spend = 0

        if sales:
            print(self._line)
            print(f"Gasto promedio de clientes VIP: {average_spend:.2f}")

            clients = {"Clientes VIP": average_spend}
            GraphicsUtil.plot_bar_chart_dict(clients, "Gasto Promedio de Clientes VIP", "Clientes", "Gasto Promedio")
        else:
            print(self._line)
            print("No hay boletos VIP registrados")

    def assistance_statistics(self):
        """
        Displays statistics related to match attendance.
        """
        assistance = [ticket for ticket in self._tickets if ticket["available"] == "false"]

        attendance = defaultdict(lambda: [0, []])
        for ticket in assistance:
            attendance[ticket["id_match"]][0] += 1
            attendance[ticket["id_match"]][1].append(ticket["id"])

        sorted_attendance = sorted(attendance.items(), key=lambda x: x[1][0], reverse=True)

        if assistance:
            print(self._line)

            for id_match, count in sorted_attendance:
                match = FiltersUtil.get_full_match_info(id_match)
                people = [FiltersUtil.search_item_by_id("tickets_data_model.txt", ticket_id) for ticket_id in count[1]]
                people_formatted = ", ".join([f"{person['name_client']}" for person in people])

                print(f"{match['home_team']['name']} vs {match['away_team']['name']} - {match['date']} - {match['stadium']['name']} - Asistencia: {count[0]} - Personas: {people_formatted}")

            first_elements_list = [sublist[0] for sublist in attendance.values()]
            GraphicsUtil.plot_bar_chart_list(list(attendance.keys()), first_elements_list, "Asistencia a Partidos", "Partidos", "Asistencia")
        else:
            print(self._line)
            print("No hay asistencias registradas")

    def max_assistance_match(self):
        """
        Finds and displays the match with the highest attendance.
        """
        assistance = [ticket for ticket in self._tickets if ticket["available"] == "false"]

        attendance = defaultdict(lambda: 0)
        for ticket in assistance:
            attendance[ticket["id_match"]] += 1

        if assistance:
            max_attendance = max(attendance.items(), key=lambda x: x[1])
            match = FiltersUtil.get_full_match_info(max_attendance[0])

            print(self._line)
            print(f"{match['home_team']['name']} vs {match['away_team']['name']} - {match['date']} - {match['stadium']['name']} - Asistencia: {max_attendance[1]}")

            GraphicsUtil.plot_bar_chart_dict(dict(attendance), "Partidos Con Mayor Asistencia", "Partidos", "Asistencia")
        else:
            print(self._line)
            print("No hay asistencias registradas")

    def max_tickets_sold_match(self):
        """
        Finds and displays the match with the highest number of tickets sold.
        """
        attendance = defaultdict(lambda: 0)
        for ticket in self._tickets:
            attendance[ticket["id_match"]] += 1

        if self._tickets:
            max_attendance = max(attendance.items(), key=lambda x: x[1])
            match = FiltersUtil.get_full_match_info(max_attendance[0])

            print(self._line)
            print(f"{match['home_team']['name']} vs {match['away_team']['name']} - {match['date']} - {match['stadium']['name']} - Boletos: {max_attendance[1]}")

            GraphicsUtil.plot_bar_chart_dict(dict(attendance), "Partidos Con Mayor Cantidad de Boletos Vendidos", "Partidos", "Boletos")
        else:
            print(self._line)
            print("No hay boletos registrados")

    def top_three_products(self):
        """
        Finds and displays the top three products by sales volume.
        """
        products = defaultdict(lambda: 0)
        sales = FiltersUtil.get_preload_data_model("sales_data_model.txt")

        for sale in sales:
            products[sale["name_product"]] += 1

        if sales:
            top_products = sorted(products.items(), key=lambda x: x[1], reverse=True)[:3]

            print(self._line)
            for name_product, count in top_products:
                print(f"{name_product} - Cantidad: {count}")

            GraphicsUtil.plot_bar_chart_dict(dict(top_products), "Top 3 Productos Vendidos", "Productos", "Cantidad de Ventas")
        else:
            print(self._line)
            print("No hay productos registrados")

    def top_three_clients(self):
        """
        Finds and displays the top three clients by number of tickets bought.
        """
        clients = defaultdict(lambda: 0)
        for ticket in self._tickets:
            clients[ticket["dni_client"]] += 1

        if self._tickets:
            top_clients = sorted(clients.items(), key=lambda x: x[1], reverse=True)[:3]

            print(self._line)
            for client, count in top_clients:
                client_info = FiltersUtil.get_ticket_with_dni(client)
                print(f"{client_info['name_client']} - Boletos: {count}")

            GraphicsUtil.plot_bar_chart_dict(dict(top_clients), "Top 3 Clientes Con Más Boletos Comprados", "Clientes", "Cantidad")
        else:
            print(self._line)
            print("No hay clientes registrados")
