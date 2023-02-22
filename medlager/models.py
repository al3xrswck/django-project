from django.db import models

class City(models.Model):
    def __str__(self):
        if self.Parent:
            return "{} {}-{}".format(self.Parent.PLZ, self.Parent.Name, self.Name)
        else:
            return "{} {}".format(self.PLZ, self.Name)

    CityID = models.AutoField(primary_key=True, editable=False, unique=True)
    Name = models.CharField(blank=False, null=False, max_length=64)
    PLZ = models.IntegerField(blank=True, null=True)
    Parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.PROTECT, help_text='Is district of')

class Street(models.Model):
    def __str__(self):
        return self.Name

    StreetID = models.AutoField(primary_key=True, editable=False, unique=True)
    Name = models.CharField(blank=False, null=False, max_length=64)

class Category(models.Model):
    CategoryID = models.AutoField(primary_key=True, editable=False, unique=True)
    CategoryName = models.CharField(blank=False, null=False, max_length=64)

class Product(models.Model):
    ProductID = models.AutoField(primary_key=True, editable=False, unique=True)
    ProductName = models.CharField(blank=False, null=False, max_length=64)
    Description = models.CharField(blank=True, null=True, max_length=255)
    Price = models.DecimalField(max_digits=5, decimal_places=0.1, blank=True, null=True)
    Quantitiy = models.IntegerField(blank=True, null=True)
    ReportingQuantity = models.IntegerField(blank=True, null=True)
    CategoryID = models.IntegerField(blank=True, null=True)