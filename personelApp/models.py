from django.db import models



# Create your models here.

class Departman(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    

GENDER = [
    ('E','ERKEK'),
    ('K','KADIN')
]

TITLE = [
    ('TM','Team Lead'),
    ('MD', 'Mid Lead'),
    ('JN','Junior'),
]

class Personel(models.Model):
    first_name = models.CharField(max_length=43) #Türkiyedeki en uzun isim 43 karakter olarak kayıt edilmiş.."Haşim Ahmet Abdulbaki Buğra Bahadır Nebioğulları"
    last_name = models.CharField(max_length=42) # Türkiyedeki en uzun soyisim 42 karakter olarak "Ayyıldızlı Kırmızı Bayrak Taşıyan Kahramanoğlu'"
    title = models.CharField(max_length=100,choices=TITLE,default=3)
    gender = models.CharField(max_length=50, choices=GENDER)
    salary = models.PositiveIntegerField()
    departman = models.ForeignKey(Departman,on_delete=models.PROTECT,related_name='personel')
    start_date = models.DateTimeField(auto_now_add=True)
   
    
    
    
    def __str__(self):
        return f"{self.first_name} - {self.last_name}  - {self.title} - {self.departman.name}"
    
   


