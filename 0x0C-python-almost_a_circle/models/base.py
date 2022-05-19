#!/usr/bin/python3
"""created class"""
import csv
import json


class Base:

    """class attribute, private"""

    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor, instance attributes"""

        if id is not None:
            """asign  instance attribute, public"""

            self.id = id
        else:
            """increment attribute of class"""

            Base.__nb_objects += 1
            """and assign the new value of __nb...
            to the instance atrribute, public id"""

            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """@staticmethod or class.function = staticmethod(class.function)"""

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation"""

        tmp = []
        tmptwo = "{}.json".format(cls.__name__)
        if list_objs is not None:
            for i in range(len(list_objs)):
                tmp.append(cls.to_dictionary(list_objs[i]))
        with open(tmptwo, mode='w', encoding="utf-8") as json_file:
            json_file.write(cls.to_json_string(tmp))

    @staticmethod
    def from_json_string(json_string):
        """stactic method  that returb lists  of the json string"""

        if json_string is None or json_string == '':
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """function create method"""
        if cls.__name__ == "Rectangle":
            tmp_create = cls(4, 5)
        else:
            tmp_create = cls(6)

        tmp_create.update(**dictionary)
        return tmp_create

    @classmethod
    def load_from_file(cls):
        """function load method"""

        tmp_load = cls.__name__ + '.json'
        try:
            tmp_file = []
            with open(tmp_load, mode='r', encoding='utf-8') as tmp_from_file:
                tmp_three = Base.from_json_string(tmp_from_file.read())
                for i in tmp_three:
                    tmp_file += [cls.create(**i)]
                return tmp_file
        except:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """"""

        tmp_save = '{}.csv'.format(cls.__name__)
        with open(tmp_save, mode='w+', newline='') as tmp_file_saves:
            if list_objs is None or list_objs == []:
                tmp_file_saves.write('[]')
            else:
                if cls.__name__ == 'Square':
                    tm = ['id', 'size', 'x', 'y']
                else:
                    tm = ['id', 'width', 'height', 'x', 'y']
                t_csv = csv.DictWriter(tmp_file_saves, fieldnames=tm)
                ty = []
                for j in list_objs:
                    ty += [t_csv.writerow(j.to_dictionary())]

    @classmethod
    def load_from_file_csv(cls):
        """create load method"""

        tmp_save = '{}.csv'.format(cls.__name__)
        try:
            with open(tmp_save, mode='r', newline='') as tmp_file_saves:
                if cls.__name__ == 'Square':
                    tm = ['id', 'size', 'x', 'y']
                else:
                    tm = ['id', 'width', 'height', 'x', 'y']
                t_csv = csv.DictReader(tmp_file_saves, fieldnames=tm)
                tys = [{key: int(value) for key, value in dict.items()}
                       for dict in t_csv]
                return [cls.create(**dics) for dics in tys]
        except IOError:
            return []

    @classmethod
    def reset(cls):
        cls.__nb_objects = 0
