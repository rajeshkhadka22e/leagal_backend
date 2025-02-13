from django.contrib import admin
from .models import FAQ,TeamMember,services,publication
from django.utils.html import mark_safe
from django.utils.html import format_html

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question','answer') 
    search_fields = ('question', 'answer')



@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    # inlines = [TeamMemberDescriptionInline]
    list_display = ('image_tag', 'name', 'position', 'number')  
    ordering = ('number',) 
    prepopulated_fields = {"slug": ("name",)}
    fields = ("name", "slug", "number", "position", "description", "lawyer_image")

    def description_display(self, obj):
        return mark_safe(obj.position)
    description_display.short_description = 'Description'
    def image_tag(self, obj):
        if obj.lawyer_image:  
            return format_html('<img src="{}" width="150" height="100" style="border-radius:5px; object-fit:cover;"/>', obj.lawyer_image)
        return "No Image"

    image_tag.short_description = 'Image'



@admin.register(services)
class services(admin.ModelAdmin):
    list_display = ('image_tag', 'title', 'is_services')  # Use 'image_tag' instead of 'image'

    def image_tag(self, obj):
        if obj.image:  
            return format_html('<img src="{}" width="150" height="100" style="border-radius:5px;"/>', obj.image)
        return "No Image"

    image_tag.short_description = 'Image'

    def get_queryset(self, request):
        return super().get_queryset(request).filter(is_services=True)




@admin.register(publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag', 'is_services')
    def image_tag(self, obj):
        if obj.image:  
            return format_html('<img src="{}" width="150" height="100" style="border-radius:5px;"/>', obj.image)
        return "No Image"

    image_tag.short_description = 'Image'

    def get_queryset(self, request):
        return super().get_queryset(request).filter(is_services=False)
    