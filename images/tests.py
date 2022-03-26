from django.test import TestCase
from .models import Location,Image,Category
# Create your tests here.

class LocationTestCase(TestCase):
    def setUp(self):
        self.name = Location(name='London')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.name,Location))

class CategoryTestCase(TestCase):
    def setUp(self):
        self.name = Category(name='Beach')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.name,Category))

class ImageTestClass(TestCase):

    #set up method
    def setUp(self):
        self.location = Location(name='Nairobi')
        self.location.save()

        self.category = Category(name='park')
        self.category.save()

        self.imagee = Image(id=1, image='image.jpg', description='this is a park', location=self.location,category=self.category)
    # Testing instance
    def test_instace(self):
        self.assertTrue(isinstance(self.imagee,Image))

    def test_save_image(self):
        self.imagee.save_image()
        after = Image.objects.all()
        self.assertTrue(len(after) > 0)

    def test_delete_image(self):
        self.imagee.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)
    
    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()

    def test_update_image(self):
        self.imagee.save_image()
        self.imagee.update_image(self.imagee.id, 'photos/test.jpg')
        changed_img = Image.objects.filter(image='photos/test.jpg')
        self.assertTrue(len(changed_img) > 0)
