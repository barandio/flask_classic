import csv
from . import FICHERO

class Movimiento():
    def __init__(self, fecha, concepto, es_ingreso, cantidad):
        self.fecha = fecha
        self.concepto = concepto
        self.es_ingreso = es_ingreso
        self.cantidad = cantidad
    
class ListaMovimientos():
    def __init__(self):
        self.movimientos = []

    def leer(self):
        self.movimientos = []
        fichero = open(FICHERO, "r")
        dreader = csv.DictReader(fichero)
        for linea in dreader:
            self.movimientos.append(linea)
        fichero.close()

    def escribir(self):
        if len(self.movimientos) == 0:
            return

        fichero = open(FICHERO, "w")
        #nombres_campo = ["fecha", "concepto", "ingreso_gasto", "cantidad"]
        nombres_campo = list(self.movimientos[0].keys())
        dwriter = csv.DictWriter(fichero,fieldnames=nombres_campo)
        for movimiento in self.movimiento:
            dwriter.writerow(movimiento)
        fichero.close()
        