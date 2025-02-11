from django.contrib import admin
from .models import FAQ,TeamMember,TeamMemberDescription,ContentSection

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question',) 
    search_fields = ('question', 'answer')


class TeamMemberDescriptionInline(admin.TabularInline):
    model = TeamMemberDescription
    extra = 1  
class TeamMemberAdmin(admin.ModelAdmin):
    inlines = [TeamMemberDescriptionInline]
    list_display = ('name', 'position')  


@admin.register(ContentSection)
class ContentSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')

admin.site.register(TeamMember, TeamMemberAdmin)
admin.site.register(TeamMemberDescription)
