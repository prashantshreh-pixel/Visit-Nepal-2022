from django.db import models
from django.conf import settings
# Create your models here.


class RoomCategory(models.Model):
    Category = models.CharField(max_length=50)
    rate = models.FloatField()

    def __str__(self):
        return self.Category


class Room(models.Model):
    Room_number = models.IntegerField()
    Beds = models.IntegerField()
    Price = models.IntegerField()
    description = models.TextField(max_length=2000, null=False)
    image = models.ImageField(upload_to='room_image')
    Capacity = models.IntegerField()
    Category = models.ForeignKey(
        RoomCategory, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'Room no ={self.Room_number} Price = {self.Price} Beds = {self.Beds} Capacity = {self.Capacity} Category = {self.Category}  '


class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

    def __str__(self):
        return f'{self.user} has booked From = {self.check_in.strftime("%d-%b-%Y %H:%M")} To = {self.check_out.strftime("%d-%b-%Y %H:%M")}{self.room}'
