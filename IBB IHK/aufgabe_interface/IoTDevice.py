from abc import ABC, abstractmethod

class IoTDevice(ABC):

    @abstractmethod
    def connect(self): pass

    @abstractmethod
    def send_command(self, command): pass

    @abstractmethod
    def disconnect(self): pass


class Smartlight(IoTDevice):
    def connect(self):
        print(f"It'll be connected with {self.__class__.__name__}")

    def send_command(self, command):
        print(f"The Light will be turn {command}.")

    def disconnect(self):
        print(f"It'll be disconnected with {self.__class__.__name__}")


class SmartThermostat(IoTDevice):
    def connect(self):
        print(f"It'll be connected with {self.__class__.__name__}")

    def send_command(self, command):
        print(f"The Light will be turn {command}.")

    def disconnect(self):
        print(f"It'll be disconnected with {self.__class__.__name__}")


def use_equipment(equip, command):
    equip.connect()
    equip.send_command(command)
    equip.disconnect()


light = Smartlight()
use_equipment(light, 'on')
print()
use_equipment(light, 'off')