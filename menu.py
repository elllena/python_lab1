import classes
import pickle
import os.path


class Menu:
    photoalbums = []

    def __init__(self):
        if os.path.isfile("photoalbums.txt"):
            with open("photoalbums.txt", "rb") as input_file:
                self.photoalbums = pickle.load(input_file)

    def print_menu(self):
        print 30 * "-", "MENU", 30 * "-"
        print "1. Show all albums"
        print "2. Show all photos in albums"
        print "3. Create new album"
        print "4. Create new photo"
        print "5. Delete album"
        print "6. Delete photo"
        print "7. Change album name"
        print "8. Change photo name"
        print "9. Show albums with \".bmp\" extension photos"
        print "10. Exit"
        print 67 * "-"

    def run_menu(self):
        loop = True

        while loop:  ## While loop which will keep going until loop = False
            self.print_menu()  ## Displays menu
            choice = input("Enter your choice [1-10]: ")

            if choice == 1:
                print "List of albums"
                for album in self.photoalbums:
                    print album.get_name()
            elif choice == 2:
                album_name = raw_input("Album name: ")
                for album in self.photoalbums:
                    if album.get_name() == album_name:
                        for photo in album.get_all_photos():
                            print photo.get_name()
            elif choice == 3:
                print "Creating album"
                album_name = raw_input("Name: ")
                self.photoalbums.append(classes.Photoalbum(album_name))
            elif choice == 4:
                album_name = raw_input("Album name: ")
                for album in self.photoalbums:
                    if album.get_name() == album_name:
                        photo_name = raw_input("Photo name: ")
                        photo_extension = raw_input("Choose extension\n0 - jpg\n1 - jpeg\n"
                                                    "2 - png\n3 - bmp\n")
                        photo_width = 500
                        photo_height = 500
                        album.add_photo(classes.Photograph(photo_name,classes.Extension(photo_extension),
                                                               photo_width,photo_height))
                        print "Added"
            elif choice == 5:
                print "Deleting album"
                album_name = raw_input("Album name: ")
                for i in range(0, len(self.photoalbums) + 1):
                    if self.photoalbums[i].get_name() == album_name:
                        self.photoalbums.pop(i)
                        print "Deleted"

            elif choice == 6:
                print "Deleting photo"
                album_name = raw_input("Album name: ")
                for album in self.photoalbums:
                    if album.get_name() == album_name:
                        photo_full_name = raw_input("Photo full name: ")
                        album.delete_photo(photo_full_name)
                        print "Deleted"
            elif choice == 7:
                album_name = raw_input("Enter name of album: ")
                new_album_name = raw_input("Enter new name of album: ")

                for i in range(len(self.photoalbums)):
                    if self.photoalbums[i].get_name() == album_name:
                        self.photoalbums[i].set_name(new_album_name)
            elif choice == 8:
                album = raw_input("Enter name of album: ")
                old_photo_name = raw_input("Enter name of photo what you like to change: ")
                new_photo_name = raw_input("Enter new name of photo what you like to change: ")

                for photoalbum in self.photoalbums:
                    if photoalbum.get_name() == album:  
                        photoalbum.change_photo_name(old_photo_name, new_photo_name)

            elif choice == 9:
                for photoalbum in self.photoalbums:
                    if photoalbum.is_contain_bmp() == True:
                        print photoalbum.get_name()
            elif choice == 10:
                print "Menu 10 has been selected"
                with open("photoalbums.txt", "wb") as output_file:
                    pickle.dump(self.photoalbums, output_file)
                loop = False  # This will make the while loop to end as not value of loop is set to False
            else:
                # Any integer inputs other than values 1-5 we print an error message
                raw_input("Wrong option selection. Enter any key to try again..")




if __name__ == "__main__":
    menu = Menu()
    print menu.photoalbums
    menu.run_menu()
