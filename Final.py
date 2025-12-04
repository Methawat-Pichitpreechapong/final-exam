class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hi, I'm {self.name}.")


class Customer(Person):
    def __init__(self, name, address):
        super().__init__(name)
        self.address = address

    def place_order(self, item):
        return item


class Driver(Person):
    def __init__(self, name, vehicle):
        super().__init__(name)
        self.vehicle = vehicle

    def deliver(self, order):
        print(f"{self.name} is delivering {order} to {self.name} using {self.vehicle}.")


class DeliveryOrder(Driver):
    def __init__(self, customer, item, status="preparing", driver):
        self.customer = customer
        self.item = item
        self.status = status
        super().__init__(driver)

    def assign_driver(driver):
        pass # Not sure what to do with it

    def summary(self):
        return f"""Order Summary:
                Item: {self.item}
                Customer: {self.customer}
                Status: preparing
                Driver: {self.name}"""



# Main Part
Customer_1 = Person("Alice")
Customer_2 = Person("Bob")
Driver_1 = Person("David")
print(DeliveryOrder(Customer_1, "Laptop"))
print(DeliveryOrder(Customer_2, "Headphones"))
