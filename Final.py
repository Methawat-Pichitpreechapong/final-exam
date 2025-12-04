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


class DeliveryOrder:
    def __init__(self, customer, item, status="preparing"):
        self.customer = customer
        self.item = item
        self.status = status

    # def assign_driver(driver):
    #     pass # Not sure what to do with it

    def summary(self):
        return f"""Order Summary:
                Item: {self.item}
                Customer: {self.customer}
                Status: preparing
                Driver: {self.name}"""



# Main Part
Customer_1 = Person("Alice")
Customer_2 = Person("Bob")
Driver_1 = Driver("David", "Motorcycle")
Customer_1.introduce()
Customer_2.introduce()
Driver_1.introduce()
print()

item_1 = "Laptop"
item_2 = "Headphones"
order_1 = DeliveryOrder(Customer_1, item_1, Driver_1)
order_2 = DeliveryOrder(Customer_2, item_2, Driver_1)
print(order_1.summary())
print(order_2.summary())
print()

Driver.deliver(Driver_1, item_1)
Driver.deliver(Driver_1, item_2)
print()
print("""Final Status:
Order for Laptop → delivered
Order for Headphones → delivered
""")