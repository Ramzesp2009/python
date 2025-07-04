class SingleTon:

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
        
    
    


if __name__ == "__main__":
    singleton = SingleTon()
    singleton2 = SingleTon()
    singleton3 = SingleTon()
    print(singleton)
    print(singleton2)
    print(singleton3)
    print(singleton == singleton2)
    print(singleton == singleton3)
