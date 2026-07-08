# ➔ ⚠️ Logistics aur baaki Projects add karne ke liye:
from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

class Profile(models.Model):
    name = models.CharField(max_length=100, default="Talha")
    profile_picture = models.ImageField(upload_to='profile_pics/')
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    tag = models.CharField(max_length=100, default="Django Backend")
    description = models.TextField()
    image = models.ImageField(upload_to='project_pics/')
    project_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

# ➔ ⚠️ Is section ko check karein aur 'models' sahi karein:
class Skill(models.Model):
    name = models.CharField(max_length=100)  # Yahan 'models' hona chahiye, 'model' nahi
    percentage = models.IntegerField(default=80)

    def __str__(self):
        return self.name


