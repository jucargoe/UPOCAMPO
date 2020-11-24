# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Habitaciones(models.Model):
    _name = 'upocampo.habitaciones'
    _description = 'Habitación del hotel rural'

    name = fields.Integer('Numero de habitacion:')
    #estado = fields.Selection([('ocupado', 'Ocupado'), ('libre', 'Libre')], 'Estado:')
    foto = fields.Binary('Foto:')
    reservas_ids = fields.Many2many('upocampo.reservas', string='Reserva asociada:')