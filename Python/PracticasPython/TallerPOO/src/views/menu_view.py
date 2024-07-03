class MenuView:
    def __init__(self, title, options):
        """
        Initializes a menu instance with a title and a list of options.

        :param title: Title of the menu.
        :param options: List of options to display in the menu.
        """
        self._title = title
        self._options = options
        self._line = "-" * 40

    @property
    def title(self):
        return self._title

    @property
    def options(self):
        return self._options

    def display(self):
        """
        Displays the menu title and options.
        """
        print(self._line)
        print(self._title)
        
        for i, option in enumerate(self._options):
            print(f"{i + 1}. {option}")
        
        print(self._line)

    def get_option(self):
        """
        Prompts the user to input an option and validates the input.

        :return: The chosen option (1-based index).
        """
        while True:
            try:
                choice = int(input("Ingrese una opción: "))
                
                if choice < 1 or choice > len(self._options):
                    raise ValueError
                
                return choice
            except ValueError:
                print(self._line)
                print("Opción inválida. Por favor ingrese otra opción.")
                print(self._line)
