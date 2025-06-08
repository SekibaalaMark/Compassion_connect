# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [("Regional_Director","Regional Director"),
        ("Country_Director","Country Director"),
        ("Project_director","Project Director"),
                    ("PF","PF"),("CDO_SDR","CDO SDR"),
                    ("CDO_HEALTH","CDO Health")]
    GENDER_CHOICES=[("Female","Female"),("Male","Male")]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    first_name= models.CharField(max_length=25)
    last_name= models.CharField(max_length=25)
    username= models.CharField(max_length=50,unique=True)
    email=models.EmailField(unique=True)
    gender=models.CharField(max_length=10,choices=GENDER_CHOICES)
    region=models.CharField(max_length=30,null=True,blank=True)
    country=models.CharField(max_length=50,null=True,blank=True)
    project_code=models.CharField(max_length=20,null=True,blank=True)
    cluster=models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return self.username


class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    caption = models.TextField(blank=True)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username}'s post"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)



class Message(models.Model):
    sender = models.ForeignKey(CustomUser, related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(CustomUser, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)



class Notification(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)




from django.utils import timezone
from django.conf import settings

class EmailVerificationCode(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    verified = models.BooleanField(default=False)

    def is_expired(self):
        return (timezone.now() - self.created_at).seconds > 3600  # 1 hour expiry
