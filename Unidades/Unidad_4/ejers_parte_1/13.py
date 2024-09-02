'''
Se tiene un ticket de supermercado que se puede
representar como una lista de tuplas (producto,
precio).
a. Hacer una función que reciba la lista, calcule y devuelva el total que hay que pagar.
b. Ahora se tienen dos tickets. Juntar ambos y volver a calcular el total.
Un ejemplo de lista puede ser: [(“Detergente”, 123),
(“Jabón Líquido”, 456)] y nos tendría que devolver
579. (No copien y peguen la lista de la guía,
porque hay caracteres que no los va a reconocer el editor
de texto).
'''
producto_1 = ("cereal", 32)
producto_2 = ("carne", 532)
producto_3 = ("leche", 62)

compras_1 = [producto_1, producto_2]
compras_2 =[producto_3]

def coste(ticket):
    total = 0
    for item in ticket:
        total += item[1]
    return total

def combinar_tickets(ticket_1, ticket_2):
    total = coste(ticket_1) + coste(ticket_2)
    return total

print(f"el coste del ticket es: {coste(compras_1)} y el de los dos tickets combinados es de: {combinar_tickets(compras_1, compras_2)}")