
from django.urls import path
from Notesapp import views
urlpatterns = [
    path('selectrelated',views.SelectRelatedQuery),
    path('prefetchrelated',views.PrefetchRelatedQuery),
    path('atomicity',views.Transaction_AtomicQuery),
    path('test',views.Transaction_AtomicQuerySelectforupdate),
    path('reverserelation',views.ReverseRelation),
    path('postcreate',views.postcreate),
    path('updatepost',views.updatepost),
    path('defer',views.deferfunction),
    path('Home', views.Home),
    path('F', views.Ffunction),
]
