from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
from django.core.validators import MaxValueValidator,MinValueValidator
from django.db.models.signals import post_delete
from django.dispatch import receiver

caragories = (
    ('Goat','Goat'),
    ('Cow','Cow'),
    ('Birds','Birds'),
    ('Fishes','Fishes'),
    ('Farm Equipments','Farm Equipments'),
    ('Vegetables','Vegetables'),
    ('Flowers','Flowers'),
    ('Others..','Others..'),
    )

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=2000)

    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    state = models.CharField(max_length=15,null=True,blank=True)
    Catagory = models.CharField(max_length=15,null=True,blank=True,choices=caragories)
    district = models.CharField(max_length=15,null=True,blank=True)
    phonenumber = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(999999999999)],null=False,blank=False)
    price = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(990000000)],null=False,blank=False)
    userimage = models.ImageField(default='default1.jpg', upload_to='postimage',blank=True,null=True)
    userimage2 = models.ImageField(default='default1.jpg', upload_to='postimage',blank=True,null=True)
    userimage3 = models.ImageField(default='default1.jpg', upload_to='postimage',blank=True,null=True)

    def save(self, *args, **kwargs):
        super(*args, **kwargs).save(*args, **kwargs)

        img1 = Image.open(self.userimage.path)
        img2 = Image.open(self.userimage2.path)
        img3 = Image.open(self.userimage3.path)

        if img1:
            output_size = (300, 300)
            img1.thumbnail(output_size)
            img1.save(self.userimage.path)

        if img2:
            output_size = (300, 300)
            img2.thumbnail(output_size)
            img2.save(self.userimage2.path)

        if img3:
            output_size = (300, 300)
            img3.thumbnail(output_size)
            img3.save(self.userimage3.path)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.id})
#above code helps to assign all kinds of url to post model
#reverse code reverses the code to same string, ie if I create a new post
#it will be directed to post details page specifically
    class Meta:
        ordering = ['-date_posted']

@receiver(post_delete, sender=Post)
def submission_delete(sender, instance, **kwargs):
    if instance.userimage == 'default1.jpg':
        pass
    else:
        instance.userimage.delete(False)
    if instance.userimage2 == 'default1.jpg':
        pass
    else:
        instance.userimage2.delete(False)
    if instance.userimage3 == 'default1.jpg':
        pass
    else:
        instance.userimage3.delete(False)

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

    