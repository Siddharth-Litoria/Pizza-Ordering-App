from django import forms
from .models import Pizza
# class Pizzaform(forms.Form):
#     topping1=forms.CharField(label="Topping 1",max_length=100)
#     topping2=forms.CharField(label="Topping 2",max_length=100)
#     size=forms.ChoiceField(label="size",choices=[('Small','Small'),('Medium','Medium'),('Large','Large')])

class Pizzaform(forms.ModelForm):
    class Meta:
        model=Pizza
        fields=['topping1','topping2','size']

class MultiplePizzaForm(forms.Form):
    number=forms.IntegerField(min_value=2,max_value=10)