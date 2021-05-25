from django.db import models

# Create your models here.

class VisitorModel(models.Model):
    name = models.CharField(max_length=128)
    phone_no = models.CharField(max_length=128)
    in_time = models.DateTimeField(max_length=128)
    out_time = models.DateTimeField(max_length=128)
    def __str__(self):
        return self.name

class PreferenceModel(models.Model):
    description = models.CharField(max_length=128)
    extra_charges = models.CharField(max_length=128)
    def __str__(self):
        return self.description

class RoomTypeModel(models.Model):
    description = models.CharField(max_length=128)
    fees = models.CharField(max_length=128)
    def __str__(self):
        return self.description

class StaffModel(models.Model):
    name = models.CharField(max_length=128)
    salary = models.CharField(max_length=128) 
    def __str__(self):
        return self.name

class RoomModel(models.Model):
    room_no = models.CharField(max_length=128,default=None)
    floor = models.CharField(max_length=128)
    availablity = models.CharField(max_length=128)
    staff = models.ForeignKey(StaffModel,on_delete=models.CASCADE)
    room_type = models.ForeignKey(RoomTypeModel,on_delete=models.CASCADE)
    def __str__(self):
        return self.room_no

class FeesModel(models.Model):
    amount = models.CharField(max_length=128)
    date = models.DateTimeField(max_length=128)
    status = models.CharField(max_length=128)

class MessFeesModel(models.Model):
    amount = models.CharField(max_length=128)
    date = models.DateTimeField(max_length=128)
    status = models.CharField(max_length=128)

class StudentModel(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    date_of_birth = models.DateField(max_length=128)
    phone_no = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    visitor = models.ManyToManyField(VisitorModel,blank=True)
    fees = models.ManyToManyField(FeesModel,blank=True)
    mess_fees = models.ManyToManyField(MessFeesModel,blank=True)
    blood_group = models.CharField(max_length=128)
    room = models.ForeignKey(RoomModel,on_delete=models.CASCADE,default=None)
    join_date = models.DateField(max_length=128)
    availed_till = models.DateField(max_length=128)
    preference = models.ForeignKey(PreferenceModel,on_delete=models.CASCADE)
    def __str__(self):
        return self.first_name+" "+self.last_name
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        try:
            hostel_fee = 0
            for fee in self.fees.all():
                hostel_fee = hostel_fee + int(fee.amount)

            self.hostel_fee = hostel_fee
            self.preference_fee = int(self.preference.extra_charges)

            mess_fee = 0
            for fee in self.mess_fees.all():
                mess_fee = mess_fee + int(fee.amount)
            self.mess_fee = mess_fee

            self.total_fee = hostel_fee + mess_fee + int(self.preference.extra_charges)
        except:
            pass

