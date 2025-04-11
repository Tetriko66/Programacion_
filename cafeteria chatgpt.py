class Cafeteria:
    def __init__(self):
        self.menu = {
            'Café Americano': 2.50,
            'Café Latte': 3.00,
            'Café Cappuccino': 3.50,
            'Té Verde': 2.00,
            'Donut': 1.50,
            'Croissant': 2.00
        }
        self.pedido = []

    def mostrar_menu(self):
        print("----- Menú Cafetería -----")
        for item, precio in self.menu.items():
            print(f"{item}: ${precio:.2f}")
        print("-------------------------")

    def agregar_a_pedido(self):
        while True:
            item = input("Introduce el nombre del producto que deseas agregar (o escribe 'terminar' para finalizar): ").title()
            if item == 'Terminar':
                break
            elif item in self.menu:
                self.pedido.append(item)
                print(f"{item} ha sido agregado a tu pedido.")
            else:
                print("Producto no disponible, por favor elige del menú.")
                
    def mostrar_pedido(self):
        if not self.pedido:
            print("No has agregado productos a tu pedido.")
        else:
            print("----- Tu Pedido -----")
            for item in self.pedido:
                print(f"- {item}")
            print("----------------------")

    def calcular_total(self):
        total = sum(self.menu[item] for item in self.pedido)
        return total

    def realizar_pago(self):
        total = self.calcular_total()
        print(f"Total a pagar: ${total:.2f}")
        while True:
            try:
                pago = float(input("Introduce el monto que deseas pagar: $"))
                if pago < total:
                    print("El monto ingresado es insuficiente. Inténtalo nuevamente.")
                else:
                    cambio = pago - total
                    print(f"Pago recibido. Tu cambio es: ${cambio:.2f}")
                    break
            except ValueError:
                print("Por favor, ingresa un número válido.")

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            self.agregar_a_pedido()
            self.mostrar_pedido()
            
            continuar = input("¿Te gustaría realizar otro pedido? (si/no): ").lower()
            if continuar != 'si':
                break
        
        self.realizar_pago()
        print("¡Gracias por tu compra! Que disfrutes tu día.")