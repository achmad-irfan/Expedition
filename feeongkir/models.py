from django.db import models

class Province(models.Model):
    class Meta:
        managed = False  # Django tidak mengubah tabe
        
    id= models.IntegerField(primary_key=True, unique=True,db_column='id')
    name= models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class City(models.Model):
    id=models.IntegerField(unique=True, primary_key=True)
    province_id= models.ForeignKey(
        Province,
        on_delete=models.CASCADE,
        related_name= "cities",
        db_column='province_id',
    )
    name = models.CharField(max_length=100)
    rajaongkir_id= models.IntegerField(unique=True)
    
    def __str__(self):
        return f"{self.name}"