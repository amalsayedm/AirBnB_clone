#!/usr/bin/python3
"""Module for the entry point of the command interpreter."""
import cmd
import sys
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Contains the entry point of the command interpreter."""
    prompt = "(hbnb) "  # if sys.__stdin__.isatty() else " "

    classes_names = {'BaseModel': BaseModel,
                     'User': User,
                     'Place': Place,
                     'State': State,
                     'City': City,
                     'Amenity': Amenity,
                     'Review': Review}
    types = {'number_rooms': int,
             'number_bathrooms': int,
             'max_guest': int,
             'price_by_night': int,
             'latitude': float,
             'longitude': float}
    # dot_cmds = ['all', 'count', 'show', 'destroy', 'update']

    '''
    def preloop(self):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    def precmd(self, line):
        """Reformat command line for advanced command syntax.

        Usage: <class name>.<command>([<id> [<*args> or <**kwargs>]])
        (Brackets denote optional fields in usage example.)
        """
        _cmd = _cls = _id = _args = ''  # initialize line elements

        # scan for general formating - i.e '.', '(', ')'
        if not ('.' in line and '(' in line and ')' in line):
            return line

        try:  # parse line left to right
            pline = line[:]  # parsed line

            # isolate <class name>
            _cls = pline[:pline.find('.')]

            # isolate and validate <command>
            _cmd = pline[pline.find('.') + 1:pline.find('(')]
            if _cmd not in HBNBCommand.dot_cmds:
                raise Exception

            # if parantheses contain arguments, parse them
            pline = pline[pline.find('(') + 1:pline.find(')')]
            if pline:
                # partition args: (<id>, [<delim>], [<*args>])
                pline = pline.partition(', ')  # pline convert to tuple

                # isolate _id, stripping quotes
                _id = pline[0].replace('\"', '')
                # possible bug here:
                # empty quotes register as empty _id when replaced

                # if arguments exist beyond _id
                pline = pline[2].strip()  # pline is now str
                if pline:
                    # check for *args or **kwargs
                    if pline[0] == '{' and pline[-1] == '}'\
                            and type(eval(pline)) is dict:
                        _args = pline
                    else:
                        _args = pline.replace(',', '')
                        # _args = _args.replace('\"', '')
            line = ' '.join([_cmd, _cls, _id, _args])

        except Exception as mess:
            pass
        finally:
            return line

    def postcmd(self, stop, line):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb) ', end='')
        return stop
        '''

    def do_quit(self, args):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, args):
        """Ending char handler."""
        print()
        return True

    def emptyline(self):
        """shouldn’t execute anything"""
        pass

    def do_create(self, args):
        """ Create an object of any class"""
        if not args:
            print("** class name missing **")
            return
        elif args not in HBNBCommand.classes_names:
            print("** class doesn't exist **")
            return
        new_object = HBNBCommand.classes_names[args]()
        storage.save()
        print(new_object.id)
        storage.save()  # 1

    def do_show(self, args):
        """ Method to show an individual object """
        new_args = args.partition(" ")
        class_name = new_args[0]
        class_id = new_args[2]

        # guard against trailing args
        if class_id and ' ' in class_id:
            class_id = class_id.partition(' ')[0]

        if not class_name:
            print("** class name missing **")
            return

        if class_name not in HBNBCommand.classes_names:
            print("** class doesn't exist **")
            return

        if not class_id:
            print("** instance id missing **")
            return

        key = class_name + "." + class_id
        try:
            print(storage._FileStorage__objects[key])
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, args):
        """ Destroys a specified object """
        new_args = args.partition(" ")
        class_name = new_args[0]
        class_id = new_args[2]

        if class_id and ' ' in class_id:
            class_id = class_id.partition(' ')[0]

        if not class_name:
            print("** class name missing **")
            return

        if class_name not in HBNBCommand.classes_names:
            print("** class doesn't exist **")
            return

        if not class_id:
            print("** instance id missing **")
            return

        key = class_name + "." + class_id

        try:
            del(storage.all()[key])
            storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, args):
        """ Shows all objects, or all objects of a class"""
        print_list = []

        if args:
            args = args.split(' ')[0]
            if args not in HBNBCommand.classes_names:
                print("** class doesn't exist **")
                return
            """for key, val in storage.all().items():"""
            for key, val in storage._FileStorage__objects.items():
                if key.split('.')[0] == args:
                    print_list.append(str(val))
        else:
            """for key, val in storage.all().items():"""
            for key, val in storage._FileStorage__objects.items():
                print_list.append(str(val))

        print(print_list)

    def do_update(self, args):
        """ Updates a certain object with new information """
        class_name = class_id = attribute_name = attribute_val = kwargs = ''

        args = args.partition(" ")
        if args[0]:
            class_name = args[0]
        else:
            print("** class name missing **")
            return
        if class_name not in HBNBCommand.classes_names:
            print("** class doesn't exist **")
            return

        # gets id from args
        args = args[2].partition(" ")
        if args[0]:
            class_id = args[0]
        else:
            print("** instance id missing **")
            return

        # generate the key
        key = class_name + "." + class_id

        # checks if key is present
        if key not in storage.all():
            print("** no instance found **")
            return

        # check if kwargs or args
        if '{' in args[2] and '}' in args[2] and type(eval(args[2])) is dict:
            kwargs = eval(args[2])
            args = []
            for key, val in kwargs.items():
                args.append(key)
                args.append(val)
        else:  # get args
            args = args[2]
            if args and args[0] == '\"':  # check for quoted arg
                second_quote = args.find('\"', 1)
                attribute_name = args[1:second_quote]
                args = args[second_quote + 1:]

            args = args.partition(' ')

            if not attribute_name and args[0] != ' ':
                attribute_name = args[0]
            if args[2] and args[2][0] == '\"':
                attribute_val = args[2][1:args[2].find('\"', 1)]

            if not attribute_val and args[2]:
                attribute_val = args[2].partition(' ')[0]

            args = [attribute_name, attribute_val]
            # data = [attribute_name, attribute_val]

        dict = storage.all()[key]

        for i, attribute_name in enumerate(args):
            # block only runs on even iterations
            if (i % 2 == 0):
                attribute_val = args[i + 1]  # following item is value
                if not attribute_name:  # check for att_name
                    print("** attribute name missing **")
                    return
                if not attribute_val:  # check for att_value
                    print("** value missing **")
                    return
                # type cast as necessary
                if attribute_name in HBNBCommand.types:
                    attribute_val = HBNBCommand.types
                    [attribute_name](attribute_val)

                # update dictionary with name, value pair
                dict.__dict__.update({attribute_name: attribute_val})

        dict.save()  # save updates to file

        """for i, attribute_name in enumerate(data):
            # block only runs on even iterations
            if (i % 2 == 0):
                att_val = data[i + 1]  # following item is value
                if not attribute_name:  # check for att_name
                    print("** attribute name missing **")
                    return
                if not att_val:
                    print("** value missing **")
                    return
                # type cast as necessary
                if attribute_name in HBNBCommand.types:
                    att_val = HBNBCommand.types[attribute_name](att_val)

                # update dictionary
                dict.__dict__.update({attribute_name: att_val})

        storage.save()  # save updates to jason file
        """
    '''
    def do_count(self, args):
        """Count current number of class instances"""
        count = 0
        for key, val in storage._FileStorage__objects.items():
            if args == key.split('.')[0]:
                count += 1
        print(count)
    '''
    def default(self, line):
        """handle class commands"""
        li = line.split('.', 1)
        if len(li) < 2:
            print('*** Unknown syntax:', li[0])
            return False
        class_name, line = li[0], li[1]
        if class_name not in list(self.classes_names.keys()):
            print('*** Unknown syntax: {}.{}'.format(class_name, line))
            return False
        li = line.split('(', 1)
        if len(li) < 2:
            print('*** Unknown syntax: {}.{}'.format(class_name, l[0]))
            return False
        mthname, args = li[0], li[1].rstrip(')')
        if mthname not in ['all', 'count', 'show', 'destroy', 'update']:
            print('*** Unknown syntax: {}.{}'.format(class_name, line))
            return False
        if mthname == 'all':
            self.do_all(class_name)
        elif mthname == 'count':
            print(self.count_class(class_name))
        elif mthname == 'show':
            self.do_show(clsname + " " + args.strip('"'))
        elif mthname == 'destroy':
            self.do_destroy(clsname + " " + args.strip('"'))
        elif mthname == 'update':
            lb, rb = args.find('{'), args.find('}')
            d = None
            if args[lb:rb + 1] != '':
                d = eval(args[lb:rb + 1])
            li = args.split(',', 1)
            objid, args = li[0].strip('"'), li[1]
            if d and type(d) is dict:
                self.handle_dict(class_name, objid, d)
            else:
                from shlex import shlex
                args = args.replace(',', ' ', 1)
                li = list(shlex(args))
                li[0] = l[0].strip('"')
                self.do_update(" ".join([class_name, objid, li[0], li[1]]))

    def handle_dict(self, class_name, objid, d):
        """handle dictionary update"""
        for key, val in d.items():
            self.do_update(" ".join([class_name, objid, str(key), str(val)]))

    def postloop(self):
        """print new line after each loop"""
        print()

    @staticmethod
    def count_class(class_name):
        """count number of objects of type clsname"""
        c = 0
        for key, val in storage.all().items():
            if type(val).__name__ == class_name:
                c += 1
        return (c)

    @staticmethod
    def getType(attribute_val):
        """return the type of the input string"""
        try:
            int(attribute_val)
            return (int)
        except ValueError:
            pass
        try:
            float(attrval)
            return (float)
        except ValueError:
            return (str)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
