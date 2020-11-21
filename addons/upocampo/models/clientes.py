# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Clientes(models.Model):
    _name = 'upocampo.clientes'
    _description = 'Clientes del hotel rural'

    dni = fields.Integer('DNI:')
    name = fields.Char('Nombre:')
    apellidos = fields.Char('Apellidos:')