from django.db import models
from django.contrib.auth.models import User
from PIL import Image
#importing from pillow

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return {self.user.username}

    def save(self, *args, **kwargs):#adding functionality to save method
        super().save(*args, **kwargs)
#super is calling the parent class save method
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:#checking if image is above 300px
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)#overrides the image 



