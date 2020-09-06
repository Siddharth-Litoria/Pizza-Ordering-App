from django.shortcuts import render
from .forms import Pizzaform,MultiplePizzaForm
from django.forms import formset_factory
from .models import Pizza

def home(request):
    return render(request,"order/home.html")

def order(request):
    multiple_form=MultiplePizzaForm()
    if request.method=="POST":
        filled_form=Pizzaform(request.POST)
        if filled_form.is_valid():
            created_pizza=filled_form.save()
            created_pizza_pk=created_pizza.id
            note='Thanks for ordering!. Your %s %s and %s pizza is on its way' %(filled_form.cleaned_data['size'],
                                                                                 filled_form.cleaned_data['topping1'],
                                                                                 filled_form.cleaned_data['topping2'])
            filled_form = Pizzaform()
        else:
            created_pizza_pk=None
            note="Pizza order failed"
        return render(request, "order/order.html", {"created_pizza_pk":created_pizza_pk,"pizzaform": filled_form,"note":note,"multiple_form":multiple_form})
    else:
        form = Pizzaform()
        return render(request,"order/order.html",{"pizzaform":form,"multiple_form":multiple_form})

def pizzas(request):
    number_of_pizzas=2
    filled_multiple_pizza_form=MultiplePizzaForm(request.GET)
    if filled_multiple_pizza_form.is_valid():
        number_of_pizzas=filled_multiple_pizza_form.cleaned_data['number']
    PizzaformSet=formset_factory(Pizzaform,extra=number_of_pizzas)
    formset=PizzaformSet()
    if request.method=="POST":
        filled_formset=PizzaformSet(request.POST)
        if filled_formset.is_valid():
            for form in filled_formset:
                print(form.cleaned_data['topping1'])
            note1="pizza have been ordered"
        else:
            note1="Order was not successfull please try again"

        return render(request,'order/pizzas.html',{"note":note1,"formset":formset})
    else:
        return render(request, 'order/pizzas.html', {"formset": formset})


def editorder(request,pk):
    pizza=Pizza.objects.get(pk=pk)
    form =Pizzaform(instance=pizza)
    if request.method=='POST':
        filled_form=Pizzaform(request.POST,instance=pizza)
        if filled_form.is_valid():
            filled_form.save()
            form=filled_form
            note="Order has been updated"
            return render(request,'order/editorder.html',{"pizzaform":form,"pizza":pizza,"note":note})
    return render(request,'order/editorder.html',{"pizzaform":form,"pizza":pizza})