import random


class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        if isinstance(memory, int):
            self.__memory = memory

    def __str__(self):
        return f'{self.cpu} {self.memory}'

    @property
    def cpu(self):
        return self.__cpu

    @property
    def memory(self):
        return self.__memory

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        self.__memory *= 2


class Phone:
    def __init__(self, sim_cards_list):
        if isinstance(sim_cards_list, list):
            self.__sim_cards_list = sim_cards_list

    def __str__(self):
        return f'{self.__sim_cards_list}'

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_cards_number, call_to_number):
        if isinstance(sim_cards_number, int):
            sim = self.__sim_cards_list[sim_cards_number]
            return f'C симки {sim} звонит к {call_to_number}'


class SmartPhone(Computer, Phone):
    def __str__(self):
        return f'{self.cpu},{self.memory}'

    def use_gps(self, location):
        list1 = random.randint(1, 100)
        return f'До {location} осталось {(list1)} метров '


comp1 = Computer('M1', 1024)
smart1 = Phone(['Beeline,O'])
smart2 = SmartPhone('intel', 128)
print(comp1.__str__())
print(smart1.__str__())
print(smart2.__str__())
print(smart1.call(0, '0555839747'))
print(smart2.use_gps('цум'))
