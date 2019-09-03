from django.db import models


# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    birthdate = models.DateField('birthday', null=True, blank=True)
    added_date = models.DateTimeField('date when added', auto_now_add=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    unit = models.CharField(max_length=10)
    quantity = models.IntegerField()


    def __str__(self):
        return f"{self.name}: {self.price} PLN/{self.unit}"

    def is_available(self):
        if self.quantity > 0:
            return True
        else: return False


class Parameters(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    op = models.FloatField(blank=True)
    ol = models.FloatField(blank=True)
    op_astigm = models.FloatField(blank=True)
    ol_astigm = models.FloatField(blank=True)
    op_axis = models.FloatField(blank=True)
    ol_axis = models.FloatField(blank=True)
    pd = models.FloatField(blank=True)


    def __str__(self):
        return f'''
            PD: <--{self.pd}-->
            D: {self.op}                {self.ol}
            A: {self.op_astigm}         {self.ol_astigm}
            Ax: {self.op_axis}          {self.ol_axis}
            
        '''


class Order(models.Model):
    CHOICES = (
        ('n', 'new'),
        ('w', 'waiting for parts'),
        ('l', 'lab'),
        ('r', 'ready'),
        ('p', 'picked up'),
    )


    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    value = models.FloatField()
    order_date = models.DateTimeField('order date', auto_now_add=True)
    comment = models.TextField(max_length=250, null=True, blank=True)
    parameters = models.ForeignKey(Parameters, on_delete=models.SET_NULL, null=True, blank=True)
    parts = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(
        max_length=1,
        choices=CHOICES,
        default='n'
    )


    def __str__(self):
        return f"{self.client.name} {self.client.surname}: {self.value} PLN"


class Appointment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField('date of appointment')
    parameters = models.ForeignKey(Parameters, on_delete=models.SET_NULL, null=True, blank=True)
    comment = models.TextField(max_length=400, null=True, blank=True)

    def __str__(self):
        return f"{self.client.name} {self.client.surname} on {self.date}"
