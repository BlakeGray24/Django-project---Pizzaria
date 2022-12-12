from django.db import models

# Create your models here.

class Pizza(models.Model):
    pizza_name = models.CharField(max_length=200)

    def __str__(self):
        return self.pizza_name


class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    topping_name = models.TextField()

    class Meta:
        verbose_name_plural = 'toppings'

    def __str__(self):
        return f"{self.topping_name[:50]}..."


class Comment(models.Model):
    comment = models.ForeignKey(Pizza,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)