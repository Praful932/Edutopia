from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from app.models import User,Domain,Student,Mentor,Post

admin.site.register(Domain)
admin.site.register(Student)
admin.site.register(Mentor)
admin.site.register(Post)
# Register your models here.
ADDITIONAL_USER_FIELDS = (
    (None, {'fields': ('is_student','is_mentor','lat','lng')}),
)

class MyUserAdmin(UserAdmin):
    model = User

    add_fieldsets = UserAdmin.add_fieldsets + ADDITIONAL_USER_FIELDS
    fieldsets = UserAdmin.fieldsets + ADDITIONAL_USER_FIELDS

admin.site.register(User,MyUserAdmin)