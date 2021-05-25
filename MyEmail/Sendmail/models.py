from django.db import models
from django.db.models.deletion import CASCADE



class Publication(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Article(models.Model):
    topic = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    def __str__(self):
        return self.topic

# class Author(models.Model):
#     first_name = models.CharField(max_length = 30)
#     last_name = models.CharField(max_length=30)
#     email = models.EmailField()

#     def __str__(self):
#         return "%s %s" % (self.first_name, self.last_name)
    

# class Post(models.Model):
#     topic = models.CharField(max_length=100)
#     publish_date = models.DateField()
#     author = models.ForeignKey(Author, on_delete= models.CASCADE)

#     def __str__(self):
#         return self.topic


# # # Create your models here.
# # class RollNumber(models.Model):
# #     rollno = models.IntegerField(blank = True, null=True)

# #     # def __str__(self):
# #     #     return self.rollno
    

# # class Student(models.Model):
# #     name = models.CharField(max_length=255)
# #     rollno = models.OneToOneField(
# #         RollNumber,
# #         on_delete=models.CASCADE,
# #         related_name='Student'
# #     )

# #     subject = models.CharField(max_length=25)

# #     def __str__(self):
# #        return self.name
   
