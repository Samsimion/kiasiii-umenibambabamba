from django.db import models

class SchoolCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


SCHOOL_TYPE_CHOICES = [
    ('national', 'National School'),
    ('county', 'County School'),
    ('sub_county', 'Sub-county School'),
    ('private', 'Private School'),
]


class PrimarySchool(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(SchoolCategory, on_delete=models.CASCADE)
    school_type = models.CharField(max_length=20, choices=SCHOOL_TYPE_CHOICES)
    address = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class HighSchool(models.Model): 
    name = models.CharField(max_length=200)
    category = models.ForeignKey(SchoolCategory, on_delete=models.CASCADE)
    school_type = models.CharField(max_length=20, choices=SCHOOL_TYPE_CHOICES)
    address = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    

