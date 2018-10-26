from django.contrib import admin
from . import models
from django.conf import settings

# Register your models here.

# Cette classe me permet de definir l'affichage de mes donnes davs la partie admin
# list_display permet de choisir les elements ke je souhaite dans ma liste 
# list_filter permet d'assigner des filtres 
# search_fields me permettra dans le champ de recherche d'effectuer une recherche sur les 
# elements choisies
# fieldsets permettra d'inserer les champs du formulaire de creation ou de modification
class EtablissementAdmin(admin.ModelAdmin):
    list_display   = ('nom', 'ville', 'quartier', 'repere', 'telephone', 
    	'email', 'adresse', 'longitude', 'latitude',)
    list_filter    = ('nom', 'ville', 'quartier', 'repere', 
    	'telephone', 'email', 'adresse', 'longitude', 'latitude', )
    search_fields  = ('nom', 'ville', 'quartier',)

    fieldsets = (
        (None, {
            'fields': ('nom', 'ville', 'quartier', 'repere', 'telephone', 
            	'email', 'adresse', 'longitude', 'latitude', )
        }),
    )


admin.site.register(models.Etablissement, EtablissementAdmin)