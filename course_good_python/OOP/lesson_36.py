class Meta(type):
    def create_local_attrs(self, *args, **kwargs):
        for key, value in self.class_attrs.items():
            self.__dict__[key] = value

    def __init__(cls, name, bases, attrs):
        cls.class_attrs = attrs
        cls.__init__ = Meta.create_local_attrs


class Women(metaclass=Meta):
    title = "heading"
    content = "content"
    photo = "path to photo"


# class Women:
#     class_attrs = {
#         'title': 'heading',
#         'content': 'content',
#         'photo': 'path to photo'
#     }
#     title = "heading"
#     content = "content"
#     photo = "path to photo"
#
#     def __init__(self, *args, **kwargs):
#         for key, value in self.class_attrs.items():
#             self.__dict__[key] = value


w = Women()
print(w.__dict__)