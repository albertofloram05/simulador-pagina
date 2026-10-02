# VARIABLES Y CONSTANTES
IVA = 0.21
descuento = False

# ENTRADA DE DATOS

nombre_cliente = input("Nombre del cliente: ")
seccion_cliente = input("Sección del cliente: ")
numero_unidades = int(input("Número de artículos: "))
precio_unidad = float(input("Precio por unidad: "))


# OPERACIONES

subtotal = numero_unidades * precio_unidad
importe_total = subtotal * (1+IVA)
descuento = numero_unidades > 5 and importe_total > 50

# SALIDA DE DATOS

print(f"Cliente: {nombre_cliente} | Sección: {seccion_cliente}")
print(f"\nNúmero de artículos: {numero_unidades}")
print(f"Subtotal: {subtotal}")
print(f"Importe total (IVA incluido): {importe_total}")
print(f"Descuento aplicable: {descuento}")
print(f"Puntos acumulados: {(int(importe_total))}")