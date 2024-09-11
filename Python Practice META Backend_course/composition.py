class Car:
    def __init__(self, make, model, year, price) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.price = price

    def __str__(self) -> str:
        return f"Make: {self.make} Model: {self.model}, Year: {self.year}, Price: {self.price}"


class Salesperson:
    def __init__(self, name, emp_id) -> None:
        self.name = name
        self.employee_id = emp_id
        self.cars_sold = []
        self.assigned_customer = None

    def add_car(self, car):
        self.cars_sold.append(car)

    def __str__(self) -> str:
        return f"Name: {self.name} Employee_id: {self.employee_id} Sold cars: {self.cars_sold}"


class Customer:
    def __init__(self, name, cust_id) -> None:
        self.name = name
        self.customer_id = cust_id
        self.purchased_car = []
        self.assigned_salesperson = None

    def purchase(self, car):
        self.purchased_car.append(car)

    def __str__(self) -> str:
        return f"Customer Name: {self.name} Customer Id: {self.customer_id} Purchased Cars are: {self.purchased_car}"


class Dealership:
    def __init__(self, name, location) -> None:
        self.name = name
        self.location = location
        self.salespersons = []
        self.inventory = []

    def add_car(self, car):
        self.inventory.append(car)

    def add_salesperson(self, salesperson):
        self.salespersons.append(salesperson)

    def assign_salesperson(self, customer, salesperson):
        if salesperson in self.salespersons:
            customer.assigned_salesperson = salesperson
            salesperson.assigned_customer = customer
            return f"Salesperson {salesperson.name} assigned to customer {customer.name}"
        else:
            return "Salesperson not found in the dealership"

    def track_sales(self):
        for salesperson in self.salespersons:
            total_sales = sum(car.price for car in salesperson.cars_sold)
            print(f"Salesperson {salesperson.name} has sold cars worth: {total_sales}")

    def find_most_sold_model(self):
        car_models = {}
        for salesperson in self.salespersons:
            for car in salesperson.cars_sold:
                if car.model in car_models:
                    car_models[car.model] += 1
                else:
                    car_models[car.model] = 1
        most_sold_model = max(car_models, key=car_models.get)
        return most_sold_model


dealership = Dealership("Fast Cars Auto", "New York")

car1 = Car("Toyota", "Corolla", 2020, 20000)
car2 = Car("Honda", "Civic", 2021, 25000)

salesperson1 = Salesperson("John", "E123")
salesperson2 = Salesperson("Jane", "E456")

customer1 = Customer("Bob", "C123")
customer2 = Customer("Alice", "C456")

dealership.add_car(car1)
dealership.add_car(car2)

dealership.add_salesperson(salesperson1)
dealership.add_salesperson(salesperson2)

dealership.assign_salesperson(customer1, salesperson1)
dealership.assign_salesperson(customer2, salesperson2)

customer1.purchase(car1)
customer2.purchase(car2)

salesperson1.add_car(car1)
salesperson2.add_car(car2)

dealership.track_sales()
print(dealership.find_most_sold_model())