class Image:
    def __init__(self, resolution, title, extension):
        self.resolution = resolution
        self.title = title
        self.extension = extension

    def resize(self, new_resolution):
        self.resolution = new_resolution

    def __str__(self):
        return self.title + self.extension

my_image = Image('800x600', "My first image", '.png')
print(my_image.resolution)
print(my_image.title)
print(my_image.extension)
print(my_image)
print()
my_image.resize('1920x1020')
print(my_image.title + my_image.extension)
print(my_image.resolution)
print()

second_image = Image(title="My second image", extension='.jpeg', resolution='800*600')
second_image.resize('1270x768')
print(second_image.title + second_image.extension)
print(second_image.resolution)
print()

# third_image = Image()
# third_image.title = "Kaka"
# third_image.extension = '.gif'
# print(third_image.title + third_image.extension)
# print(third_image.resolution)

