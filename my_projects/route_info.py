def route_info(info):
    if info.get('distance') and type(info['distance']) is int:
        return f"Distance to your destination is {info['distance']}"

    if info.get('speed') and info.get('time'):
        if type(info['speed']) is int and type(info['time']) is int:
            return f"Distance to your destination is {info['speed'] * info['time']}"

    return "No distance info is available"


print(route_info({'distance': 1200}))
print(route_info({'speed': 120, 'time': 10}))
print(route_info({}))