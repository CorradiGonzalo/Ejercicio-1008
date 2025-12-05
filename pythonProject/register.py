class Interno:
    def __init__(self, dni, nombre, servicio, pago, edad, cobro):
        self.dni = dni
        self.nombre = nombre
        self.servicio = servicio
        self.pago = pago
        self.edad = edad
        self.cobro = cobro

    def __str__(self):
        cad = '{:<10} | {:<10} | {:>4} | {:>4} | {:>3} | {:<6}'
        return cad.format(self.dni, self.nombre, self.servicio, self.pago, self.edad, self.cobro)