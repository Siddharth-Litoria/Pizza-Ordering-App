from django.urls import path
from . import views
urlpatterns=[
    path('home/',views.home,name="home"),
    path('order/',views.order,name="order"),
    path('pizzas/',views.pizzas,name="pizzas"),
    path('editorder/<int:pk>',views.editorder,name="editorder")
]