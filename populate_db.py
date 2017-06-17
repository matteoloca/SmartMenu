# User
from django.contrib.auth.models import User
User.objects.create_superuser(username='admin', password='admin', email='')

# UoM
from core.models import UoM
uom_kg = UoM.objects.create(name='Kg', readable_name='Chilogrammo')
uom_prz = UoM.objects.create(name='Prz', readable_name='Porzione')
uom_l= UoM.objects.create(name='L', readable_name='Litro')
uom_g = UoM.objects.create(name='g', readable_name='Grammo')

# Shelf
from core.models import Shelf
Shelf.objects.create(id='A1')
Shelf.objects.create(id='A2')
Shelf.objects.create(id='A3')
Shelf.objects.create(id='B1')
Shelf.objects.create(id='B2')
Shelf.objects.create(id='C1')


# Product
from core.models import Product
Product.objects.create(name='Riso', uom=uom_kg, kind=Product.MATERIA_PRIMA)
Product.objects.create(name='Pasta', uom=uom_kg, kind=Product.MATERIA_PRIMA)
Product.objects.create(name='Farina', uom=uom_kg, kind=Product.MATERIA_PRIMA)
Product.objects.create(name='Salsa di pomodoro', uom=uom_l, kind=Product.MATERIA_PRIMA)
Product.objects.create(name='Zafferano', uom=uom_g, kind=Product.MATERIA_PRIMA)
Product.objects.create(name='Farina 00', uom=uom_kg, kind=Product.MATERIA_PRIMA)
Product.objects.create(name='Impasto pizza', uom=uom_kg, kind=Product.PREPARATO)
Product.objects.create(name='Pizza margherita', uom=uom_prz, kind=Product.PIATTO)
Product.objects.create(name='Pizza quattro stagioni', uom=uom_prz, kind=Product.PIATTO)
Product.objects.create(name='Pizza americana', uom=uom_prz, kind=Product.PIATTO)

