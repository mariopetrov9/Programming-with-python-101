import json
import xml.etree.ElementTree as ET


class Jsonable:

    def to_json(self):
        return json.\
            dumps({"dict": self.__dict__, "class_name": self.__class__.__name__}, indent=4)

    @classmethod
    def from_json(cls, json_string):
        json_dict = json.loads(json_string)
        class_name2 = eval(json_dict["class_name"])
        args = json_dict["dict"]
        if cls == class_name2:
            return class_name2(**args)
        else:
            raise ValueError


class Xmlable:

    def to_xml(self):
        root = ET.Element(self.__class__.__name__)
        for prop in self.__dict__:
            b = ET.SubElement(root, prop)
            ET.SubElement(b, self.__dict__[prop])
        return ET.tostring(root)

    def from_xml(xml_string):
        cls_name = ET.fromstring(xml_string)
        cls_dict = {}
        for elem in cls_name:
            for child in elem.getchildren():
                cls_dict[elem.tag] = child.tag
        return eval(cls_name.tag)(**cls_dict)


class Panda(Jsonable, Xmlable):
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name


class Person(Jsonable, Xmlable):
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name


# person = Person(name='Rado')
# print(Panda.from_json(person.to_json()))  # ValueError


# p = Panda(name='Ivo')
# json_string = p.to_json()
# xml_string = p.to_xml()
# p1 = Panda.from_json(json_string)
# p2 = Panda.from_xml(xml_string)
# print(p == p1)
# print(p == p2)
# print(p1 == p2)
