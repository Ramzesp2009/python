class BankAccount:
    def __init__(self, summa):
        self.summa = summa

    def __eq__(self, other):
        # ==
        return self.summa == other.summa

    def __gt__(self, other):
        # >
        return self.summa > other.summa

    def __lt__(self, other):
        # <
        return self.summa < other.summa

    def __iadd__(self, other):
        # +=
        self.summa += other
        return self.summa

    def __add__(self, other):
        # +
        return self.summa + other.summa