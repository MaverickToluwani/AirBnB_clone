#!/usr/bin/python3
# python console 

"""project concole module"""

import cmd
import sys  


class HBNBCommand(cmd.Cmd):
    """simple console class """

    def do_EOF(self, arg):
        """Exits program"""
        return True

    def do_quit(self, arg):
        sys.exit(1)

    def help_quit(self):
        print('Quit command to exit the program')
    
    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
