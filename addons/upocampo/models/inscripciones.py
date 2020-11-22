# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Inscripciones(models.Model):
    _name = 'upocampo.inscripciones'
    _description = 'Inscripciones de las actividades del hotel rural'

    name = fields.Integer('Identificacion:')
    actividad_id = fields.Many2one('upocampo.actividades', string='Actividad:')
    cliente_id = fields.Many2one('upocampo.clientes', string='Cliente:')
    fecha = fields.Datetime('Fecha:', autodate=True)