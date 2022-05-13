from cgi import test
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.db import transaction
from django.db.models import Avg,Count,F,Q
# Create your views here.

def SelectRelatedQuery(request):
    employees = Employee.objects.all().select_related('department')
    for employe in employees:
        print(employe.name , employe.department.name)

    #Annotate and Aggregate
    test1 = Book.objects.aggregate(totalcount=Count('price'))
    test2 = Book.objects.annotate(totalcount=Count('price'))
    print("------------------------------------------------------------------")
    print("sfdgsgfdgsd",test1)
    print("------------------------------------------------------------------")
    print("sdsdhshdghsdh",test2)

    #values

    test3 = Book.objects.values('name').annotate(totalcount=Count('price'))
    print("Values " , test3)
    print("------------------------------------------------------------------")
    test4 = Book.objects.annotate(count=Count('price')).values('name', 'count')
    print("test4 " , test4)
    print("------------------------------------------------------------------")
    

    #Q anf F
    test5 = Employee.objects.filter(Q(id=1) & Q(age=121) | Q(id=2) & Q(age=12))
    print("test5",test5)
    return HttpResponse("ok")


def PrefetchRelatedQuery(request): 
    books = Book.objects.all().prefetch_related('store_set')
    for book in books:
        print(book.store_set.all())
    return HttpResponse("ok")

    #  store_set Means Reverse Manager That Means Fetch Many TO Many Field Datas From Base Model ( Fetch store from Books) , store => model name , modelname_set


# @transaction.atomic
def Transaction_AtomicQuery(request):
    data = True
    if data:
        user1 = "user1"
        user2 = "user2"
        amount = 50
        try :
            with transaction.atomic():
                payor = TransactionAtomicityModel.objects.get(user = user1)
                payor.amount = int(payor.amount) - int(amount)
                payor.save()


                receiver = TransactionAtomicityModel.objects.get(user = user2)
                receiver.amount = int(receiver.amount) + int(amount)
                receiver.save()

                return HttpResponse("OK")
        except Exception as e:
            return HttpResponse("!OK,, "+str(e))

    else:
        return HttpResponse("False Message")



# @transaction.atomic
def Transaction_AtomicQuerySelectforupdate(request):
    data = True
    if data:
        user1 = "user1"
        user2 = "user2"
        amount = 50

        payor = TransactionAtomicityModel.objects.select_for_update().get(user=user1)
        # payor2 = TransactionAtomicityModel.objects.get(user=user1)
        receiver = TransactionAtomicityModel.objects.select_for_update().get(user=user2)
        print(payor)
        # print(payor2)

        with transaction.atomic():
            
            payor.amount = int(payor.amount) - int(amount)
            payor.save()

           
            receiver.amount = int(receiver.amount) + int(amount)
            receiver.save()

            return HttpResponse("OK")
    else:
        return HttpResponse("False Message")


def ReverseRelation(request):
    data = Group.objects.get(id=1)
    relation = data.profiles.filter(id=1)
    print("relation",relation)
    return HttpResponse("ok")

def postcreate(request):
    # Post.objects.bulk_create(
    # [   Post(title='Django bulk_create example 1.0'),
    #     Post(title='Django bulk_create example 2.0'), 
    #     Post(title='Django bulk_create example 3.0')
    # ])

     # Post.objects.bulk_create([Post(title=f"Post {i}") for i in range(5)])



    datas = [ {"title" : "Title 1"} , {"title" : "Title 2"} , {"title" : "Title 3"} , {"title" : "Title 4"} , {"title" : "Title 5"}]
    
    with transaction.atomic():
        for x in datas:
            Post.objects.bulk_create([Post(title=x['title'])])
        return HttpResponse("Post Create")



def updatepost(request):
    posts = list(Post.objects.all())
    for index, post in enumerate(posts):
        if post.title == "Title 4":
            posts[index].title = f"Post 4 and 5 Is changed"
        # print("INDEX" , index)
        # print("POST" , post.title)
        else:
            pass
    Post.objects.bulk_update(posts, ['title'])
    return HttpResponse("Update ")

def deferfunction(request):
    datas = [ {"title" : "Title 1"} , {"title" : "Title 2"} , {"title" : "Title 3"} , {"title" : "Title 4"} , {"title" : "Title 5"}]
    k = Post.objects.defer('id')
    for x in k:
        print(x.title)
        print(x.time_published)
        print(x.id)
    return HttpResponse("defer")



def Home(request):
    datasmallerthan = Post2.objects.smaller_than(2)
    alldata = Post2.objects.all()
    print(datasmallerthan)
    print(alldata)
    return HttpResponse("ok")


def Ffunction(request):
    # product.objects.update(price = F('price') * 2)
    product.objects.filter(name = "A").update(price = F('price') * 2)
    #Update The Price
    return HttpResponse("ok") 