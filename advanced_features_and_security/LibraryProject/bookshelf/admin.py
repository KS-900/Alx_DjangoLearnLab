from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)

    def create_groups():
        editors, _ = Group.objects.get_or_create(name="Editors")
        viewers, _ = Group.objects.get_or_create(name="Viewers")
        admins, _ = Group.objects.get_or_create(name="Admins")

        content_type = ContentType.objects.get_for_model(Book)
        can_create = Permission.objects.get(codename="can_create", content_type=content_type)
        can_edit = Permission.objects.get(codename="can_edit", content_type=content_type)
        can_delete = Permission.objects.get(codename="can_delete", content_type=content_type)

        viewers.permissions.add(can_create)
        editors.permissions.add(can_edit)
        admins.permissions.add(can_delete,can_create,can_edit)

    create_groups()

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')})
    )
    add_fieldsets = UserAdmin.add_fieldsets +(
        (None, {'fields': ('date_of_birth', 'profile_photo')})
    )
    
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Book, BookAdmin)