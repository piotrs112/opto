from django.db import models


# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    birthdate = models.DateField('birthday', null=True, blank=True)
    added_date = models.DateTimeField('date when added')

    def __repr__(self):
        return f"{self.name} {self.surname}"


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    value = models.FloatField()


    def __repr__(self):
        return f"{self.client.name} {self.client.surname}: {self.value} PLN"


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    unit = models.CharField(max_length=10)


    def __repr__(self):
        return f"{self.name}: {self.price} PLN/{self.unit}"


class Parameters(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    op = models.FloatField()
    ol = models.FloatField()
    op_astigm = models.FloatField()
    ol_astigm = models.FloatField()
    op_axis = models.FloatField()
    ol_axis = models.FloatField()
    pd = models.FloatField()


    def __repr__(self):
        return f'''
            PD: <--{self.pd}-->
            D: {self.op}                {self.ol}
            A: {self.op_astigm}         {self.ol_astigm}
            Ax: {self.op_axis}          {self.ol_axis}
            
        '''


class Appointment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField('date of appointment')
    parameters = models.ForeignKey(Parameters, on_delete=models.SET_NULL, null=True)


    def __repr__(self):
        return f"{self.client.name} {self.client.surname} on {self.client.date}"
