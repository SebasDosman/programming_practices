from views import DisplayMenuView
from services import LoadDataService


if __name__ == "__main__":
    try: 
        LoadDataService.load_data_to_txt()
        
        menu = DisplayMenuView()
        menu.display_main_menu()
    except Exception as e:
        print(f"Error: {e}")