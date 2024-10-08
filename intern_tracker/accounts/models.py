from django.contrib.auth.models import User, Group
from django.db import models
from resources.models import Department

class Profile(models.Model):
    intern = models.OneToOneField(User, on_delete=models.CASCADE)
    matric_number = models.CharField(max_length=20)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    whatsapp = models.CharField(max_length=15)

    class Meta:
        verbose_name = "Intern Profile"
        verbose_name_plural = "Intern Profiles"

    def __str__(self):
        return self.intern.username

class Team(Group):
    lead = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="lead_team")

    class Meta:
        verbose_name = "Project Team"
        verbose_name_plural = "Project Teams"

    def __str__(self):
        return self.name

