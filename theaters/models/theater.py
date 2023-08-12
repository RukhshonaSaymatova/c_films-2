from django.db import models

class Theater(models.Model):
    title = models.CharField("Name of theater", max_length=25)
    description = models.TextField("Description", default="Description...")
    category = models.CharField("Category", max_length=25)
    address = models.CharField("Address of theater", max_length=50)
    city = models.CharField("City", max_length=50)
    contact = models.CharField("Contact", max_length=12)
    email = models.EmailField("Email", max_length=50)
    working_mode = models.DateTimeField("Working mode")
    image = models.ImageField("Image")

    
    class Meta:
        verbose_name = "Title"
        verbose_name_plural ="Titles"
        
    def __str__(self):
        return f"{self.title}"