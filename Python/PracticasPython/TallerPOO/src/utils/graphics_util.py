import matplotlib.pyplot as plt
import numpy as np


class GraphicsUtil:
    @staticmethod
    def plot_bar_chart_dict(data, title, xlabel, ylabel):
        """
        Generates a bar chart from a dictionary of data.

        :param data: Dictionary with data to plot. Keys are categories and values are quantities.
        :param title: Title of the chart.
        :param xlabel: Label for the X-axis.
        :param ylabel: Label for the Y-axis.
        """
        try:
            categories = list(data.keys())
            values = list(data.values())
            colors = plt.cm.viridis(np.linspace(0, 1, len(categories)))

            plt.figure(figsize=(10, 5))
            plt.bar(categories, values, color=colors)

            plt.title(title)
            plt.xlabel(xlabel)
            plt.ylabel(ylabel)

            plt.xticks(rotation=45, ha='right')

            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"Error al trazar el gráfico de barras desde el diccionario: {e}")

    @staticmethod
    def plot_bar_chart_list(categories, values, title, xlabel, ylabel):
        """
        Generates a bar chart from a list of data.

        :param categories: List of categories for the X-axis.
        :param values: List of values for the Y-axis.
        :param title: Title of the chart.
        :param xlabel: Label for the X-axis.
        :param ylabel: Label for the Y-axis.
        """
        try:
            colors = plt.cm.viridis(np.linspace(0, 1, len(categories)))

            plt.figure(figsize=(10, 5))
            plt.bar(categories, values, color=colors)

            plt.title(title)
            plt.xlabel(xlabel)
            plt.ylabel(ylabel)

            plt.xticks(rotation=45, ha='right')

            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"Error al trazar el gráfico de barras a partir de una lista: {e}")
