from django.db import models

class Province(models.Model):
    province_id= models.IntegerField(unique=True)
    province= models.CharField(max_length=100)
    
    def __str__(self):
        return self.province
    
class City(models.Model):
    city_id=models.IntegerField(unique=True)
    province= models.ForeignKey(
        Province,
        on_delete=models.CASCADE,
        related_name= "cities"
    )
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=30)  
    
    def __str__(self):
        return f"{self.type} {self.name}"