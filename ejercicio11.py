producto=input('como se llama su producto:')
precio=float(input('El precio del producto:'))
unidades=int(input('Cuantas unidades del producto desea:'))
precio_unidades=precio*unidades
print('El {} que tiene precio {:6.2f}€ la unidad hemos cogido {} por lo cual el total son {:8.2f} €'.format(
      producto,precio,unidades,precio_unidades))
