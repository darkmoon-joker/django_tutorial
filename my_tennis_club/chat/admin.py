from django.contrib import admin
from .models import ChatLog

# Register your models here.
class ChatLogAdmin(admin.ModelAdmin):
  list_display = ("user_id", "chat_id", "chat_date", "chat_title", "header", "role", "prompt")
  
admin.site.register(ChatLog, ChatLogAdmin)
