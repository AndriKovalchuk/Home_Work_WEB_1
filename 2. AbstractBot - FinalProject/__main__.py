from Bot import AddBot, ExitBot, SearchBot, ViewBot, SaveBot, LoadBot, EditBot, RemoveBot, CongratulateBot
from AddressBook import AddressBook


if __name__ == "__main__":
    book = AddressBook()
    choice = {
        'add': AddBot(book),
        'search': SearchBot(book),
        'view': ViewBot(book),
        'save': SaveBot(book),
        'load': LoadBot(book),
        'edit': EditBot(book),
        'remove': RemoveBot(book),
        'congratulate': CongratulateBot(book),
        'exit': ExitBot()
    }

    while True:
        action = input('Choose an action: ')
        if action in choice:
            choice[action].handle()
        else:
            print('There is no such command!')
