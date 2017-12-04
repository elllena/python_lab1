class Extension:
    jpg, jpeg, png, bmp = range(4)

    def __init__(self, Type):
        self.value = Type

    def __str__(self):
        if self.value == Extension.jpg:
            return 'jpg'
        if self.value == Extension.jpeg:
            return 'jpeg'
        if self.value == Extension.png:
            return 'png'
        if self.value == Extension.bmp:
            return 'bmp'


class Photograph:

    def __init__(self, name, extension, width, height):
        self.name = name
        self.extension = extension
        self.width = width
        self.height = height

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_full_name(self):
        return self.name + "." + str(self.extension)

    def get_extension(self):
        #print str(self.extension)
        return self.extension

    def get_size(self):
        return str(self.width) + "x" + str(self.height)


class Photoalbum:

    def __init__(self, name):
        self.photographs = []
        self.name = name

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def add_photo(self, photo):
        self.photographs.append(photo)

    def delete_photo(self, full_name):# exp. full_name = "photo1.jpg"
        for i in range(0, len(self.photographs) + 1):
            if self.photographs[i].get_full_name == full_name:
                self.photographs.pop(i)
                return True
        return False

    def get_all_photos(self):
        return self.photographs

    def change_photo_name(self, previous_full_name, new_name):# previous_full_name = "123.jpg" new_name = "321"
        for i in range(0, len(self.photographs)):
            if self.photographs[i].get_full_name() == previous_full_name:
                self.photographs[i].set_name(new_name)
                return True
        return False

    def is_contain_bmp(self):
        for photo in self.photographs:
            if str(photo.get_extension()) == str(3):
                return True
        return False
