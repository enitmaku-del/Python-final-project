class Ticket:
    def __init__(self, name, base_price):
        self.__name = name
        self.__base_price = base_price

   def get_name(self):
       return self._name

   def price(self):
       return self.base_price


class StudentTicket(Ticket):
    def price(self):
        return super ().price()*0.5

class GroupTicket(Ticket):
    def __init__(self, name, base_price, people):
        super().__init__(name, base_price)
        self.__people = people
        


concert = Ticket("Concert, 200")
museum = Ticket("Museum, 150")
print(concert.name, concert.price())
print(museum.name, museum.price())
