#!/usr/bin/python3


import models
import uuid
import sys
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.review import Review


class HBNBCommand(cmd.Cmd):
    def __init__(self):
        self.__objects = {
                'User': User,
                'BaseModel': BaseModel,
                'City': City,
                'Place': Place,
                'Amenity': Amenity,
                'State': State,
                'Review': Review
                }
        self.completekey = None
        self.cmdqueue = []
        self.stdout = sys.stdout
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program..."""
        return True

    def do_EOF(self, arg):
        """Handle EOF (Ctrl + D)"""
        print("Exiting...")

    def emptyline(self):
        """Do nothing on an empty line"""
        pass

    def do_create(self, arg):
        """Create a new class instance"""
        if not arg:
            print("** class name missing **")
            return
        class_name = arg.split()[0]
        try:
            cls = globals()[class_name]
        except KeyError:
            print("** class doens't exist **")
            return
        instance = cls()
        instance.id = str(uuid.uuid4())
        instance.save()
        print(instance.id)

    def do_show(self, arg):
        """Print the string representation of an instance"""

        args = arg.split()
        if not args:
            print("** classs name missing **")
            return
        class_name = args[0]
        try:
            cls = globals()[class_name]
        except KeyError:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id is missing **")
            return
        instance_id = args[1]
        objects = storage.all()

        is_not_found = False
        for key, value in objects.items():
            if key == f"{class_name}.{instance_id}":
                print(value)
                is_not_found = False
                return
            else:
                is_not_found = True

        if is_not_found:
            print("** instance not found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        try:
            cls = globals()[class_name]
        except KeyError:
            print("** class doesen't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        objects = storage.all()

        if f"{class_name}.{instance_id}" in objects:
            del objects[f"{class_name}.{instance_id}"]
            storage.save()
            return
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        if not arg:
            instances = models.storage.all().values()
            print([str(instance) for instance in instances])
        else:
            class_name = arg.split()[0]
            try:
                cls = globals()[class_name]
            except KeyError:
                print("** class doesn't exist **")
                return
            instances = [
                    str(instance) for key,
                    instance in models.storage.all().items()
                    if key.split('.')[0] == class_name
                    ]
            print(instances)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        try:
            cls = globals()[class_name]
        except KeyError:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        objects = models.storage.all()
        print(objects)

        if key not in objects.keys():
            print("** key-value missing **")
            return
        if len(args) < 3:
            print("** attribute missing **")
            return

        attr_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return

        attr_value = args[3].strip('""')

        instance = objects[key]
        setattr(instance, attr_name, attr_value)
        storage.save()


if __name__ == '__main__':
    try:
        HBNBCommand().cmdloop()
    except KeyboardInterrupt:
        print("Program interrupted by User")
