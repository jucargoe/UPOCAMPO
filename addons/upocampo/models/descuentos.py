# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Descuentos(models.Model):
    _name = 'upocampo.descuentos'
    _description = 'Descuento de una habitación del hotel rural'

    identificacion = fields.Integer('Identificacion:')
    name = fields.Char('Nombre:')
    porcentaje = fields.Float('Porcentaje:')