from django.shortcuts import render,redirect
from .models import *
from .forms import *

# Create your views here.
def index(request):
    """The home page for Pizzeria"""
    return render(request, 'pizzas/index.html')


def pizzas(request):
    pizzas = Pizza.objects.order_by('pizza_name')

    context = {'all_pizzas':pizzas}

    return render(request, 'pizzas/pizzas.html',context)


def pizza(request,pizza_id):

    p = Pizza.objects.get(id=pizza_id)

    toppings = Topping.objects.filter(pizza=p)

    context = {'pizza':p, 'toppings':toppings}

    return render(request, 'pizzas/pizza.html',context)



def comments(request,pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    if request.method != 'POST':
        form = CommentForm()
    else:
        print(request.POST)
        form = CommentForm(data=request.POST)
        if form.is_valid():
            comments = form.save(commit=False)
            comments.pizza = pizza
            comments.save()
            return redirect('pizzas:pizza', pizza_id=pizza_id)

    context = {'form':form, 'pizza': pizza}
    return render(request, 'pizzas/comments.html', context)



