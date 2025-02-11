from django.db import models
from filehub.fields import ImagePickerField
from django.utils.text import slugify
from tinymce.models import HTMLField

class FAQ(models.Model):
    question = models.CharField("Question", max_length=255)
    answer = models.TextField("Answer")

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"

    def __str__(self):
        return self.question
    

class TeamMember(models.Model):
    name = models.CharField("Name", max_length=100)
    position = models.CharField("Position", max_length=100)
    lawyer_image = ImagePickerField("Lawyer Image")
    description = models.TextField("Description")
    is_list_item = models.BooleanField("Is List Item", default=False)  # Whether the description is a list item
    slug = models.SlugField("Slug", blank=True, null=True)

    class Meta:
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"

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

    def __str__(self):
        return self.name


class TeamMemberDescription(models.Model):
    team_member = models.ForeignKey(
        TeamMember, related_name='descriptions', on_delete=models.CASCADE, verbose_name="Team Member"
    )
    topic = HTMLField("Topic", max_length=100)  
    description = HTMLField("Description")  
    is_list_item = models.BooleanField("Is List Item", default=False) 

    class Meta:
        verbose_name = "Team Member Description"
        verbose_name_plural = "Team Member Descriptions"

    def __str__(self):
        return f"{self.topic}: {self.description}"
    


class ContentSection(models.Model):
    title = models.CharField("Title", max_length=255)
    description = HTMLField("Description")
    image = ImagePickerField("Image")

    class Meta:
        verbose_name = "Content Section"
        verbose_name_plural = "Content Sections"

    def __str__(self):
        return self.title
