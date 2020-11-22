# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Descuentos(models.Model):
    _name = 'upocampo.descuentos'
    _description = 'Descuento de una habitación del hotel rural'

    name = fields.Integer('Identificacion:')
    nombre = fields.Char('Nombre:')
    porcentaje = fields.Float('Porcentaje:')
    reservas_id = fields.One2many('upocampo.reservas', 'descuento_id', 'Reservas:')