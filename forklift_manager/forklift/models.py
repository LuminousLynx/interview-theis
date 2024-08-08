from django.db import models
import datetime

# Create your models here.
class Forklift(models.Model):

    serial_no = models.CharField(max_length=30, unique=True)

    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    type = models.CharField(max_length=30)

    max_load = models.IntegerField(default=800)
    hours_run = models.FloatField(default=0)
    next_check = models.DateField(null=True, blank=True, default=None,)         

    can_operate = models.BooleanField(default=True)
    allowed_operators = models.JSONField(default=list)

    location = models.CharField(max_length=50, default="Münster")
    workshops = models.JSONField(default=list)
    fastest_workshop = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.serial_no}'

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Forklift'
        verbose_name_plural = 'Forklifts'



class Workshop(models.Model):
    name = models.CharField(max_length=80, unique=True)

    mail = models.CharField(max_length=80)
    operates_in = models.CharField(max_length=50)

    can_fix_brands = models.JSONField(default=dict)
    
    fastest_repair_times = models.JSONField(default=dict, null=True)
    lowest_mean_price = models.JSONField(default=dict, null=True)
    reliability_rating = models.IntegerField(default=5, null=True)         

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Workshop'
        verbose_name_plural = 'Workshops'



class Repair(models.Model):

    active = models.BooleanField(default=True)
    
    model_id = models.CharField(max_length=30, null=True)
    workshop_id_id = models.CharField(max_length=50, null=True)

    start_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField(default=datetime.date(year=2024, month=12, day=31))
    
    message = models.CharField(max_length=2000, default="Sehr geehrtes Werkstatt-Team!\nWir möchten einen unserer Stapler bei Ihnen reparieren lassen. Wann wäre dies möglich? \nMfG \nflaschenpost-Warehouse")

    repair_time = models.IntegerField(null=True)
    repair_cost = models.FloatField(null=True)
    
    def __str__(self):
        return f'{self.model_id}'

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Repair'
        verbose_name_plural = 'Repairs'