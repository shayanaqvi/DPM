from Menu import Menu
from cs import cs
from client import client


menu = Menu()


def search():
    menu.generate_menu(["Artist", "Album", "Title", "Return"])
    menu_opt = int(input("Do: "))

    match menu_opt:
        case 1:
            type = "artist"
            artist_name = input("Artist: ")
            menu.return_query_results(type, artist_name)
        case 2:
            type = "album"
            album_name = input("Album: ")
            menu.return_query_results(type, album_name)
        case 3:
            type = "title"
            title_name = input("Title: ")
            menu.return_query_results(type, title_name)
        case 4:
            cs()
            return ""


