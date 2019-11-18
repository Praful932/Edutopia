from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from app.models import User,Domain,Student,Mentor,Post

admin.site.register(User,UserAdmin)
admin.site.register(Domain)
admin.site.register(Student)
admin.site.register(Mentor)
admin.site.register(Post)
# Register your models here.
