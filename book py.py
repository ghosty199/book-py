class Book():
    def __init__(self, name, author, price, year, yearold ):
        self.citizen_name=name
        self.citizen_author=author
        self.citizen_price=price
        self.citizen_year=year
        self.citizen_yearold=yearold
        
    def add_citizen(self):
        print("name=",self.citizen_name)
        print("author=",self.citizen_author)
        print("price=",self.citizen_price)
        print("year=",self.citizen_year)
        print("yearold=", self.citizen_yearold)
object1=Book(" Harry Potter and the Philosophers Stone", "J.K Rowling", 1928, 1997, 23)
object1.add_citizen()
     