class Apple:
    manufacturer = "Apple INC."
    contactWebsite = "www.Apple.com/contact"

    def contactDetails(self):
        print("To contact us, log on to ", self.contactWebsite)

class MacBook(Apple):
    def __init__(self):
        self.yearOfManufacture = 2017

    def manufactureDetails(self):
        print("this Macbook was manufactured in the year {} by {}".format(self.yearOfManufacture, self.manufacturer))

macBook = MacBook()
macBook.manufactureDetails()
macBook.contactDetails()