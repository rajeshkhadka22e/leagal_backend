from django.contrib import admin
from .models import FAQ,TeamMember,publication
from django.utils.html import mark_safe
from django.utils.html import format_html

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question','answer') 
    search_fields = ('question', 'answer')



@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    # inlines = [TeamMemberDescriptionInline]
    list_display = ('name', 'position','image_tag', 'number')  
    ordering = ('number',) 
    prepopulated_fields = {"slug": ("name",)}
    fields = ("name", "slug", "number", "position", "description", "lawyer_image")

    def description_display(self, obj):
        return mark_safe(obj.position)
    description_display.short_description = 'Description'
    def image_tag(self, obj):
        if obj.lawyer_image:  
            return format_html('<img src="{}" width="250" height="150" style="border-radius:5px;"/>', obj.lawyer_image)
        return "No Image"

    image_tag.short_description = 'Image'



@admin.register(publication)
class publication(admin.ModelAdmin):
    list_display = ('title', 'image_tag')  # Use 'image_tag' instead of 'image'

    def image_tag(self, obj):
        if obj.image:  
            return format_html('<img src="{}" width="250" height="150" style="border-radius:5px;"/>', obj.image)
        return "No Image"

    image_tag.short_description = 'Image'

