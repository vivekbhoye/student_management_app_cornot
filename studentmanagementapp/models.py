from django.db import models
from django.utils.translation import gettext as _
from django.urls import reverse

class Student(models.Model):
    GENDER = [
        ("Male","Male"),
        ("Female","Female")
    ]
    first_name = models.CharField(_("first_name"),max_length=50,null=False)
    last_name = models.CharField(_("last_name"),max_length=50,null=True,blank=True)
    email = models.EmailField(_("email"),max_length=100,null=False)
    gender = models.CharField(_("gender"),max_length=6,choices=GENDER,null=True,blank=True)
    # school = models.CharField(_("school"),null=True,blank=True,max_length=150)
    # books = models.CharField(_("book"),null=True,blank=True,max_length=150)
    school = models.ForeignKey(_("school"),db_constraint=False,on_delete=models.SET_NULL,null=True,blank=True)
    books = models.ForeignKey(_("book"),db_constraint=False,on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse('student-detail', kwargs={'pk': self.pk})

    
class School(models.Model):
    
    regionid = models.IntegerField(_("REGIONID"),null=False,unique=False)
    school = models.CharField(_("school"),max_length=150,null=False,primary_key=True)
    email = models.EmailField(_("email"),max_length=100,null=False)
    principal = models.CharField(_("principal"),max_length=50,null=False)
    phone = models.CharField(_("phone"),max_length=8)
    address2 = models.CharField(_("address2"),max_length=100,null=True)

    def __str__(self) -> str:
        return f'{self.school}'

    def get_absolute_url(self):
        return reverse('student-create')

    
class Book(models.Model):
    
    title = models.CharField(_("title"),null=False,max_length=100,primary_key=True)
    author_name = models.CharField(_("Author Name"),max_length=150,null=True,blank=True)
    date_of_publication = models.DateField(_("Date of Publication"),null=True,blank=True)
    number_of_pages = models.IntegerField(_("Number of Pages"),null=False)

    def __str__(self) -> str:
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('student-create')

    