from django.db import models
from filehub.fields import ImagePickerField
from django.utils.text import slugify
from tinymce.models import HTMLField
from django.utils import timezone
import bleach


class practicearea(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = ImagePickerField()
    class Meta:
        verbose_name = "practice Area"
        verbose_name_plural = "Practice Area"
class FAQ(models.Model):
    CATEGORY_CHOICES = [
        ('Home', 'Home'),
        ('About', 'About'),
    ]
    category = models.CharField(
        max_length=20, choices=CATEGORY_CHOICES, default='Home'
    )
    question = models.CharField("Question", max_length=255)
    answer = models.CharField(max_length=255)

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"

    def __str__(self):
        return self.question


class TeamMember(models.Model):
    name = models.CharField("Name", max_length=100)
    position =models.CharField(max_length=200)
    lawyer_image = ImagePickerField()
    description = HTMLField("description")
    slug = models.SlugField("Slug", blank=True, null=True)
    number = models.IntegerField("order", null=True)
    class Meta:
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"
        ordering = ['number', '-id']

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
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



class about(models.Model):
    title = models.CharField("Title", max_length=255)
    description = HTMLField("Description")
    image = ImagePickerField("Image")
    CATEGORY_CHOICES = [
        ('vision', 'vision'),
        ('About', 'About'),
        ('exit','exit'),
    ]
    category = models.CharField(
        max_length=20, choices=CATEGORY_CHOICES, default='About'
    )
    class Meta:
        verbose_name = "about"
        verbose_name_plural = "about"

    def __str__(self):
        return self.title



class services(models.Model):
    title = models.CharField("Title", max_length=255)
    description = HTMLField("Description")
    image = ImagePickerField("Image")

    class Meta:
        verbose_name = "services"
        verbose_name_plural = "services"


    def __str__(self):
        return self.title

class publication(models.Model):
    title = models.CharField("Title", max_length=255)
    description = HTMLField("Description")
    image = ImagePickerField("Image")
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)

    class Meta:
        verbose_name = "publication"
        verbose_name_plural = "publications"

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            count = 1
            while publication.objects.filter(slug=slug).exists():
                print(f"Slug {slug} already exists, trying next...")
                slug = f"{base_slug}-{count}"
                count += 1
                if count > 100:
                    raise ValueError("Too many slug conflicts!")
            self.slug = slug
        super().save(*args, **kwargs)


class ContactMessage(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"
    class Meta:
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Message"