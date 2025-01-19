class DataBase:
    __instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        DataBase.__instance = None
    
    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f"Connect with DB: {self.user}, {self.psw}, {self.port}")

    def close(self):
        print("Closing a connection with a DB")

    def read(self):
        return "data from DB"

    def write(self, data):
        print(f"Writing in DB {data}")


db = DataBase('root', '1234', 80)
db2 = DataBase('root1', '1111', 90)
print(id(db), id(db2))

db.connect()
db2.connect()