# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Descuentos(models.Model):
    _name = 'upocampo.descuentos'
    _description = 'Descuento de una habitación del hotel rural'

    name = fields.Char('Nombre:', required=True, help='Campo nombre requerido')
    porcentaje = fields.Float('Porcentaje:')
    reservas_id = fields.One2many('upocampo.reservas', 'descuento_id', 'Reservas:')

    _sql_constraints = [('descuentos_name_unique','UNIQUE (name)','El nombre del descuento tiene que debe ser único')]

    @api.onchange('porcentaje')
    def onchange_porcentaje(self):
        if self.porcentaje != False and self.porcentaje < 10:
            raise models.ValidationError('El porcentaje de descuento tiene que ser mayor a 10 minutos')
