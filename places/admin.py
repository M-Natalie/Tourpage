from django.contrib import admin

# Register your models here.
from .models import Place 
from .models import Feedback


admin.site.register(Place)

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['text', 'place', 'user', 'checked' ]
    list_editable = ['checked']
    list_filter = ['checked']
    search_fields = ['text', 'place__name', 'place__location', 'place__description']

    fields = ['user', 'place', 'text']
    readonly_fields = ['place', 'text']


admin.site.register(Feedback, FeedbackAdmin)
