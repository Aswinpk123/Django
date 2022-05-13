from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    department = models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return self.name    

class Book(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Store(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name


class TransactionAtomicityModel(models.Model):
    user = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)

    def __str__(self):
        return self.user


# class QandFmodel(models.Model):
#     order = models.CharField(max_length=100)
#     product = models.CharField(max_length=100)
#     quantity = models.IntegerField(null=False)




class Group(models.Model):
    name = models.CharField(max_length=100)

class Profile(models.Model):
    name = models.CharField(max_length=100,default='')
    group = models.ForeignKey(Group,on_delete=models.CASCADE,related_name='profiles')
    

class Post(models.Model):
    title = models.CharField(max_length=512)
    time_published = models.DateTimeField(auto_now_add=True)


class PostManager(models.Manager):
    def smaller_than(self,size):
        return self.filter(comments__lt=size)

class Post2(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
    comments = models.IntegerField()

    objects = PostManager()

    


# The Above code is same as the below code 

# class PostManager(models.Queryset):
#     def smaller_than(self,size):
#         return self.filter(comments__lt=size)

# class Post(models.Model):
#     title = models.CharField(max_length=100)
#     desc = models.CharField(max_length=100)
#     comments = models.IntegerField()

#     objects = PostManager.as_manager()


class product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()