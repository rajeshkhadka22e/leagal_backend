from django.contrib import admin
from .models import FAQ,TeamMember

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question',) 
    search_fields = ('question', 'answer')



admin.site.register(TeamMember)
