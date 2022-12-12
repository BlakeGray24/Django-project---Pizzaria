from django import forms

from .models import *

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['pizza_name']
        labels = {'pizza_name':'Pizza Name'}

class ToppingForm(forms.ModelForm):
    class Meta:
        model = Topping
        fields = ['topping_name']
        labels = {'topping_name':''}

        widget = {'topping_name': forms.Textarea(attrs={'cols':80})}

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')