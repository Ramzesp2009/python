cmd = 14.5

match cmd:
    case str() as command:
        print(f"str {command}")
    case bool() as command:
        print(f"bool {command}")
    case int() as command if 0 <= 9:
        print(f"int {command}")
    case float() as command if 0 <= 9:
        print(f"float {command}")
    case _:
        print('other')


# print("end check")