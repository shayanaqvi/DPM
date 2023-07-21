from browse import browse
from current import current
from inform import inform_user
from messages import messages
from pl_browse import pl_browse
from pl_settings import pl_settings
from search import search
from shuffle import shuffle

import sys
import os

from rich.console import Console


console = Console()


if __name__ == "__main__":
    user_arguments = sys.argv
    match len(user_arguments):
        case 1:
            inform_user("dpm: No arguments provided\nInput 'dpm h' for more information", "error")
        case 2:
            match user_arguments[1]:
                case "b":
                    browse()
                case "p":
                    pl_browse()
                case "f":
                    search()
                case "c":
                    current()
                case "o":
                    pl_settings(None, "app")
                case "s":
                    shuffle()
                case "h":
                    os.system('%s %s' % (os.getenv('EDITOR'), "HELP.md"))
                case _:
                    inform_user(messages["Invalid option"], "error")
        case 3:
            match user_arguments[1]:
                case "o":
                    pl_settings(user_arguments[2], "cli")
                case _:
                    inform_user(messages["Invalid option"], "error")
