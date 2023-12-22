from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class ChatHeader(models.IntegerChoices):
    HEADER = 1, 'Header'
    CONTENT = 0, 'Content'

class ChatRole(models.IntegerChoices):
    ROLE_NONE = 0, 'none'
    ROLE_USER = 1, 'User'
    ROLE_AI = 2, 'ChatGPT'

class ChatLog(models.Model):
    id = models.AutoField(primary_key=True)
    
    id = models.IntegerField(primary_key=True, validators=[MinValueValidator(1)])
    user_id = models.IntegerField()
    chat_id = models.IntegerField()
    chat_date = models.DateField()
    chat_title = models.CharField(max_length = 255, null=True)
    header = models.SmallIntegerField(choices=ChatHeader.choices, default = ChatHeader.CONTENT)
    role = models.SmallIntegerField(choices=ChatRole.choices, default=ChatRole.ROLE_NONE)
    prompt = models.TextField(null=True)


