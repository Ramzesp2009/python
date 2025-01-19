def image_info(a: dict):
    if 'image_title' not in a:
        raise TypeError("There isn't image_title")
    elif 'image_id' not in a:
        raise TypeError("There isn't image_id")
    return f"Image '{a['image_title']}' has id {a['image_id']}"



my_dict = {
    'image_title': 'my cat',
    'image_id': 5136,
    'image_volume': '13,5Kb'
}

try:
    print(image_info(my_dict))
except Exception as e:
    print(e)