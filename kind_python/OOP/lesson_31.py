class ExceptionPrint(Exception):
    """Base class for exceptions in this module."""


class ExceptionPrintSendData(ExceptionPrint):
    """Class Exception for send data to the printer"""
    def __init__(self, *args):
        self.message = args[0] if args else None

    def __str__(self):
        return f"Error: {self.message}"


class PrintData:
    def print(self, data):
        self.send_data(data)
        print(f"print: {str(data)}")

    def send_data(self, data):
        if not self.send_to_print(data):
            raise ExceptionPrintSendData("Printer is not available")

    def send_to_print(self, data):
        return False


p = PrintData()
# p.print("Hello")

try:
    p.print("Hello")
except ExceptionPrintSendData:
    print("Printer is not available")
except ExceptionPrint:
    print("Base error printing")
