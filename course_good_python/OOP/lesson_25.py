class Goods:
    def __init__(self, name, weight, price):
        super().__init__()
        print("init Goods")
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f"name: {self.name}, weight: {self.weight}, price: {self.price}")


class MixinLog:
    ID = 0

    def __init__(self):
        print("init MixinLog")
        self.ID += 1
        self.id = self.ID

    def save_sell_log(self):
        print(f"{self.id} good was sold at 00:00 clock")

    def print_info(self):
        print("print_info MixinLog")





class NoteBook(Goods, MixinLog):

    def print_info(self):
        print("print_info from MixinLog")
        # super().print_info()


n = NoteBook("Acer", 1.5, 30000)
# MixinLog.print_info(n)
n.print_info()

