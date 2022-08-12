from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(null=False, max_length=50)
    description = models.CharField(max_length=500)

    def __str__(self):
        return "Name: " + self.name + "," + \
            "Description: " + self.description

# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    maker = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    dealerId = models.IntegerField()
    name = models.CharField(null=False, max_length=50)
    SEDAN = 'Sedan'
    SUV = 'SUV'
    WAGON = 'Wagon'
    TYPES_CHOICES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon')
    ]
    type = models.CharField(
        max_length=20,
        choices = TYPES_CHOICES
    )
    year = models.DateField(default=now)

    def __str__(self):
        return "Name: " + self.name + "," + \
            "Dealer: " + str(self.dealerId) + "," + \
            "Type: " + self.type + "," + \
            "Year: " + str(self.year)

# <HINT> Create a plain Python class `CarDealer` to hold dealer data
class CarDealer:

    def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip, state):
        # Dealer address
        self.address = address
        # Dealer city
        self.city = city
        # Dealer Full Name
        self.full_name = full_name
        # Dealer id
        self.id = id
        # Location lat
        self.lat = lat
        # Location long
        self.long = long
        # Dealer short name
        self.short_name = short_name
        # Dealer short state
        self.st = st
        # Dealer state
        self.state = state
        # Dealer zip
        self.zip = zip

    def __str__(self):
        return "Dealer name: " + self.full_name

# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview:

    def __init__(self, car_make, car_model, car_year, dealership, id, name, purchase, purchase_date, review):
        # DealerReview car_make
        self.car_make = car_make
        # DealerReview car_model
        self.car_model = car_model
        # DealerReview car_year
        self.car_year = car_year
        # DealerReview dealership
        self.dealership = dealership
        # DealerReview id
        self.id = id
        # DealerReview name
        self.name = name
        # DealerReview purchase
        self.purchase = purchase
        # DealerReview purchase_date
        self.purchase_date = purchase_date
        # DealerReview purchase_date
        self.review = review
        # DealerReview purchase_date
        self.sentiment = ''

    def __str__(self):
        return "Dealer name: " + self.full_name + ", Review: " + self.review
