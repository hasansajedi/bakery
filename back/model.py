class Bakery:
    instances = []

    def __init__(self, name, code, packs):
        self.instances.append(self)

        self.name = name
        self.code = code
        self.packs = packs

    def __get__(self, instance, owner):
        for inst_ref in self.__refs__[self]:
            inst = inst_ref()
            if inst is not None:
                yield inst
