from django.db import models

# Create your models here.

class Subject(models.Model):
    """Model definition for Subject."""

    # TODO: Define fields here
    subject_name = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)


    # standar

    statut = models.BooleanField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Subject."""

        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'

    def __str__(self):
        """Unicode representation of Subject."""
        return self.subject_name



class Teacher(models.Model):
    """Model definition for Teacher."""

    # TODO: Define fields here
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=254)
    profile_picture = models.ImageField(upload_to="Teachers/Profile_Picture", default="default.png")
    phone_number = models.CharField(max_length=50)
    room_number = models.CharField(max_length=10)
    subjects_taught = models.ManyToManyField(Subject, blank=True)


    statut = models.BooleanField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Teacher."""

        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'

    def __str__(self):
        """Unicode representation of Teacher."""
        return self.last_name + ' ' + self.last_name + '(' + self.email + ')'

