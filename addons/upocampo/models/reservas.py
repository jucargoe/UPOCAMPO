# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Reservas(models.Model):
    _name = 'upocampo.reservas'
    _description = 'Reserva de habitación de hotel rural'

    name = fields.Integer('Identificacion:')
    id_descuento = fields.Integer('ID Descuento:')
    precio = fields.Float('Precio:')
    importeTotal = fields.Float('Importe total:')
    numHabitacion = fields.Integer('Numero De Habitacion:')
    checkIn = fields.Datetime('Check In:', autodate=True)
    checkOut = fields.Datetime('Check Out:', autodate=True)