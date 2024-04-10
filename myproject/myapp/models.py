from django.db import models
from django.urls import reverse
from django.utils import timezone
# Create your models here.
class Bus(models.Model):
    bus_no = models.CharField(max_length=100)
    driver = models.CharField(max_length=100)
    route_name = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('bus-update', kwargs={'pk': self.pk})

    def __str__(self):
        return f"{self.bus_no} {self.driver}"


class Seat(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.PROTECT)
    seat_no = models.CharField(max_length=100)
    price = models.PositiveIntegerField(default=0)
    status = models.PositiveIntegerField(default=1)
    customer = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.seat_no


