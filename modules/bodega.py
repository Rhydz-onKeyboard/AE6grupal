#DATA
productos={ 'ZAPATILLAS':20,'POLERAS':10,'ZAPATOS':15,'POLERÓN':3,'CHAQUETA':5,'GUANTES':4 }


def agregar_producto():
    #agrega un producto a la DATA
    key = input('Ingresa el producto: ')
    value = int(input('Ingresa el stock: '))
    productos.update({ key: value })

def actualizar_stock(key, unidades_venta = 1):
    #actualiza el stock de la DATA
    productos[key] -= unidades_venta
        
def mostrar_productos():
    #muestra por consola los productos y su stock disponible
    for key, value in productos.items():
        print(f'Tenemos {value} unidades/pares del {key}')
        #return key

def mostrar_producto(producto):
    #busca un producto en especifico en la DATA segun el argumento y los muestra 
    for key, value in productos.items():
        if key == producto.upper():
            print(key, value)
            #return producto

def mostrar_solo_productos():
    #muestra todos los productos
    for key in productos.keys():
        print(f'Tenemos disponibles: {key} ')

def mostrar_producto_condicional():
    #muestra los producto que cumplen con la condicion de stock
    unidades = int(input('Indique el numero de unidades y le diremos los productos que tienen ese stock: '))
    for key, value in productos.items():
        if value > unidades:
            print(f'Tenemos {value} unidades/pares del {key}')