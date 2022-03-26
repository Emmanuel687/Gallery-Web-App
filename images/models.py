from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name



class Category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Image(models.Model):
    image = CloudinaryField('image', default='')
    name = models.CharField(max_length = 30)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.name
    
    @classmethod
    def search_by_name(cls,search_term):
        images = cls.objects.filter(title__icontains = search_term)
        return images
    
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
    
    @classmethod
    def update_image(cls, id, value):
        cls.objects.filter(id=id).update(image=value)

    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.filter(id=id).all()
        return image
