from django.db import models
from filehub.fields import ImagePickerField
from django.utils.text import slugify
from tinymce.models import HTMLField
import bleach

class FAQ(models.Model):
    question = models.CharField("Question", max_length=255)
    answer =models.CharField(max_length=255)

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"

    def __str__(self):
        return self.question
    

class TeamMember(models.Model):
    name = models.CharField("Name", max_length=100)
    position =models.CharField(max_length=200)
    lawyer_image = ImagePickerField()
    description = HTMLField()
    slug = models.SlugField("Slug", blank=True, null=True)
    number = models.IntegerField("order", null=True) 
    class Meta:
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"
        ordering = ['number', '-id']

    def save(self, *args, **kwargs):
        if not self.slug:  # Only generate slug if it does not exist
            base_slug = slugify(self.name)  # Convert name to slug
            slug = base_slug
            count = 1
            while TeamMember.objects.filter(slug=slug).exists():
                slug = f"{base_slug}{count}"
                count += 1
            self.slug = slug
        super().save(*args, **kwargs)
    def save(self, *args, **kwargs):
  
        self.description = bleach.clean(self.description, tags=['p', 'strong', 'em', 'ul', 'ol', 'li', 'a', 'img', 'br'], attributes={'a': ['href', 'title'], 'img': ['src', 'alt']})
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name




class publication(models.Model):
    title = models.CharField("Title", max_length=255)
    description = HTMLField("Description")
    image = ImagePickerField("Image")

    class Meta:
        verbose_name = "publication"
        verbose_name_plural = "publications"

    def __str__(self):
        return self.title
