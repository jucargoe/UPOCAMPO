# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Puestos(models.Model):
    _name = 'upocampo.puestos'
    _description = 'Puestos de trabajo del hotel rural'

    identificacion = fields.Integer('Identificacion:')
    name = fields.Char('Nombre de Puesto:')
    descripcion = fields.Text('Descripcion:')