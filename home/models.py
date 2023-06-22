from django.db import models

# Manually Imported Modules
from datetime import datetime
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Institution(models.Model):
    # Default generated Fields
    modifiedOn = models.DateTimeField(default=datetime.now())
    
    # Basic Required Fields
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    address = models.TextField()
    city = models.CharField(max_length=100, default='bangalore')
    state = models.CharField(max_length=50, default='karnataka')
    postal_code = models.IntegerField(default=560045)
    country = models.CharField(max_length=100, default='india')
    
    # Principal Details
    principal_name = models.CharField(max_length=100)
    principal_email = models.CharField(max_length=100)
    principal_phone = models.CharField(max_length=10)
    password = models.CharField(max_length=100)
    
    # Chairman Details
    owner_name = models.CharField(max_length=100)
    owner_email = models.CharField(max_length=100)
    owner_phone = models.CharField(max_length=10)
    password = models.CharField(max_length=100)
    
    # Additional / Misc Fields
    website = models.CharField(max_length=100, null=True)
    logo = models.ImageField(upload_to='database/images', null=True)
    motto = models.TextField()
    mission_statement = models.TextField()

class Department(models.Model):
    # Default generated Fields
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    office_location = models.TextField()
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    
    # Head of the Department Details
    hod_name = models.CharField(max_length=100)
    hod_email = models.CharField(max_length=100)
    hod_phone = models.CharField(max_length=10)
    
    # Additional Misc Fields
    description = models.TextField()
    specialization_area = models.CharField(max_length=100)
    budget_allocation = models.BigIntegerField(null=True)
    facilities_available = ArrayField(models.CharField(max_length=100),
                                      blank=True,null=True)
    research_areas = ArrayField(models.TextField(),
                                      blank=True,null=True)
    
    
    