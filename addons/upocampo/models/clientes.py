# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Clientes(models.Model):
    _name = 'upocampo.clientes'
    _description = 'Clientes del hotel rural'

    name = fields.Char('DNI:')
    nombre = fields.Char('Nombre:')
    apellidos = fields.Char('Apellidos:')
    reservas_ids = fields.One2many('upocampo.reservas', 'cliente_id', 'Reservas:')
    inscripciones_ids = fields.One2many('upocampo.inscripciones', 'cliente_id', 'Inscripciones:')