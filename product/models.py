
from django.db import models

from django.core.files import File

from PIL import Image
from io import BytesIO

class Category(models.Model):
    name=models.CharField(max_length=120)
    slug=models.SlugField()
    
    class Meta:
        ordering = ('name',)
        
    def __str__(self):
        return self.name
    
class Product(models.Model):
    category=models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    slug=models.SlugField()
    name=models.CharField(max_length=120)
    description=models.TextField(blank=True, null=True)
    price=models.DecimalField(max_digits=8, decimal_places=2)
    image= models.ImageField(upload_to='uploads/',blank=True, null=True)
    thumbnail=models.ImageField(upload_to='uploads/',null=True, blank=True)
    creat_at=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-creat_at',)
        
    def __str__(self):
        return self.name
    
    def get_thumbnails(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail=self.make_thumbnail(self.image)
                self.save()
                
                return self.thumbnail.url
            else:
                return 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pngegg.com%2Fen%2Fsearch%3Fq%3Dnot%2BFound&psig=AOvVaw2UBU5dS4eg1UKzSrD_rZ51&ust=1704998730503000&source=images&cd=vfe&opi=89978449&ved=0CBMQjRxqFwoTCLCfga6904MDFQAAAAAdAAAAABAf'
    
    def make_thumbnail(self,image,size=(400,400)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)
        
        thumb_io=BytesIO()
        img.save(thumb_io,'JPEG',quality=85)
        
        thumbnail=File(thumb_io,name=image.name)
        
        return thumbnail