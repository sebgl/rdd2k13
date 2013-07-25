from django.contrib import admin
from insa5an.models import Etudiant


class EtudiantAdmin(admin.ModelAdmin):
    list_display = ('email', 'departement', 'has_info', 'has_portrait', 'nb_photo_group', 'is_valid')
    search_fields = ('email',)

admin.site.register(Etudiant, EtudiantAdmin)
