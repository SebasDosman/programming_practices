class ProductsFilterView:
    def __init__(self):
        self._line = "-" * 40
    
    def filter_products_by_name(self):
        """
        Filters products by name based on user input.
        Displays filtered product information.
        """
        try:
            from utils import FiltersUtil
            
            print(self._line)
            id_stadium = input("Ingrese el id del estadio: ")
            restaurant_name = input("Ingrese el nombre del restaurante: ")
            product_name = input("Ingrese el nombre del producto: ")
            print(self._line)
            
            product = FiltersUtil.search_product_by_name(id_stadium, restaurant_name, product_name)
            product_info = f"Nombre: {product['name']} - Cantidad: {product['quantity']} - Precio: {product['price']}USD - Stock: {product['stock']} - Alcoholica: {'Si' if product['adicional'] else 'No'}"
            
            print(product_info)
        except Exception as e:
            print(f"Error al filtrar productos por nombre: {e}")
    
    def filter_products_by_type(self):
        """
        Filters products by type based on user input.
        Displays filtered product information.
        """
        try:
            from utils import FiltersUtil
            
            print(self._line)
            id_stadium = input("Ingrese el id del estadio: ")
            restaurant_name = input("Ingrese el nombre del restaurante: ")
            product_type = input("Ingrese el tipo de producto (alcoholic, non-alcoholic, package, plate): ")
            print(self._line)
            
            products = FiltersUtil.search_product_by_type(id_stadium, restaurant_name, product_type)
            products_info = [f"Nombre: {product['name']} - Cantidad: {product['quantity']} - Precio: {product['price']}USD - Stock: {product['stock']} - Tipo: {product['adicional']}" for product in products]
            
            for product in products_info:
                print(product)
        except Exception as e:
            print(f"Error al filtrar los productos por tipo: {e}")
    
    def filter_products_by_price(self):
        """
        Filters products by price based on user input.
        Displays filtered product information.
        """
        try:
            from utils import FiltersUtil
            
            print(self._line)
            id_stadium = input("Ingrese el id del estadio: ")
            restaurant_name = input("Ingrese el nombre del restaurante: ")
            price = input("Ingrese el precio: ")
            print(self._line)
            
            products = FiltersUtil.search_product_by_price(id_stadium, restaurant_name, price)
            products_info = [f"Nombre: {product['name']} - Cantidad: {product['quantity']} - Precio: {product['price']}USD - Stock: {product['stock']} - Tipo: {product['adicional']}" for product in products]
            
            for product in products_info:
                print(product)
        except Exception as e:
            print(f"Error al filtrar productos por precio: {e}")