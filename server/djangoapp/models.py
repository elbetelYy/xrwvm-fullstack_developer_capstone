from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# -----------------------------
# CAR MAKE MODEL
# -----------------------------
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.name


# -----------------------------
# CAR MODEL
# -----------------------------
class CarModel(models.Model):

    CAR_TYPES = [
        ('Sedan', 'Sedan'),
        ('SUV', 'SUV'),
        ('Wagon', 'Wagon'),
        ('Hatchback', 'Hatchback'),
        ('Coupe', 'Coupe'),
    ]

    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    car_type = models.CharField(max_length=20, choices=CAR_TYPES)

    year = models.IntegerField(
        validators=[
            MinValueValidator(2015),
            MaxValueValidator(2023)
        ]
    )

    dealer_id = models.IntegerField(default=0)

    price = models.FloatField(default=0.0)

    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.car_make.name} - {self.name}"