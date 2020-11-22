# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Reservas(models.Model):
    _name = 'upocampo.reservas'
    _description = 'Reserva de habitación de hotel rural'

    name = fields.Integer('Identificacion:', help='Auto Generate')
    descuento_id = fields.Many2one('upocampo.descuentos', string='Descuento:')
    precio = fields.Float('Precio:')
    importeTotal = fields.Float('Importe total:')
    numHabitacion = fields.Integer('Numero De Habitacion:')
    checkIn = fields.Datetime('Check In:', autodate=True)
    checkOut = fields.Datetime('Check Out:', autodate=True)
    habitaciones_ids = fields.Many2many('upocampo.habitaciones', string='Habitaciones asociadas:')
    cliente_id = fields.Many2one('upocampo.clientes', string='Cliente:')