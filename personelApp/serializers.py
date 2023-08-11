from rest_framework import serializers

from .models import Departman,Personel

from django.utils.timezone import now





class DepartmanSerializer(serializers.ModelSerializer):
    count = serializers.SerializerMethodField()
    
    class Meta:
        model = Departman
        fields = (
            'id',
            'name',
            'count',
            
        )
        
    def get_count(self,giris):
        return giris.personel.count()
    
  
        
class PersonelSerializer(serializers.ModelSerializer):
    
    departman =serializers.StringRelatedField()
    departman_id=serializers.IntegerField()
    total = serializers.SerializerMethodField()
    
    class Meta :
        model =  Personel
        fields = (
            'id',
            'first_name',
            'last_name',
            'title',
            'gender',
            'salary',
            'departman',
            'departman_id',
            'start_date',
            'total'
            
        )
    def get_total(self,toplam):
    
        return (now()- toplam.start_date).days