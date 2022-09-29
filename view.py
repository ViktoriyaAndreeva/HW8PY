import utils

def menu_select(title, menu):
    while True:
        utils.print_delimiter()
        print(title)
        utils.print_delimiter()
        for index, item in enumerate(menu):
            print(f"{index + 1}: {item['title']}")
        
        index = utils.input_number("Выберите пункт меню: ", 1, len(menu))
        if index:
            return menu[index - 1]
            