from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe

# Register your models here.


class SubjectAdmin(admin.ModelAdmin):

    list_display = ('subject_name','statut', 'date_add', 'date_update',)
        
    list_filter = ('statut', 'date_add', 'date_update',)
    
    search_fields = ('subject_name',)
    
    date_hierarchy = 'date_add'
    
    actions = ('active','deactive')
    def active(self, request, queryset):
        queryset.update(produit_collections_is_view=False)
        self.message_user(request, 'La selection a été deactivé avec succès')

    active.short_description = 'Desactiver'

    def deactive(self, request, queryset):
        queryset.update(produit_collections_is_view=True)
        self.message_user(request, 'La selection a été activé avec succès')

    deactive.short_description = 'Activer'
    
    list_display_links = ['subject_name',]
    
    ordering = ['subject_name',]
    
    list_per_page = 20
    
    fieldsets = (
        ('Subject infos', 
            {'fields': ('subject_name', 'description',)
        }),
        ('Standar', 
            {'fields': ('statut',)
        })
    )




class TeacherAdmin(admin.ModelAdmin):

    list_display = (
        'profile_picture_preview',
        'last_name',
        'first_name',
        'email',
        'phone_number',
        'room_number',
    )
        
    list_filter = (
        'statut', 
        'date_add', 
        'date_update',
        'subjects_taught',
    )
    
    search_fields = (
        'last_name',
        'first_name',
    )
    
    date_hierarchy = 'date_add'
    
    
    actions = ('active','deactive')
    def active(self, request, queryset):
        queryset.update(produit_collections_is_view=False)
        self.message_user(request, 'La selection a été deactivé avec succès')

    active.short_description = 'Desactiver'

    def deactive(self, request, queryset):
        queryset.update(produit_collections_is_view=True)
        self.message_user(request, 'La selection a été activé avec succès')

    deactive.short_description = 'Activer'
    
    list_display_links = ['last_name' ,'first_name',]
    
    ordering = ['last_name' ,'first_name',]
    
    list_per_page = 20


    readonly_fields = ['profile_picture_preview',]

    filter_horizontal = ('subjects_taught',)

    fieldsets = (
        ('Teacher Personnal infos', 
            {
                'fields': ('last_name', 'first_name', 'email', 'profile_picture',)
            }
        ), 
        ('Contacts and address', 
            {'fields': 
                ('phone_number', 'room_number',)
            }
        ), 
        ('Subject Taught', 
            {'fields': 
                ('subjects_taught',)
            }
        )
    )
    

    #cette fonction nous pemmet d'avoir une vue d'image
    def profile_picture_preview(self, obj):
        return mark_safe('<img src="{url}" width="100px" height="100px" />'.format(url = obj.profile_picture.url))


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Teacher, TeacherAdmin)
_register(models.Subject, SubjectAdmin)
