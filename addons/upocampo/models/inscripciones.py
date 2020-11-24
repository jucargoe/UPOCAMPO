# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Inscripciones(models.Model):
    _name = 'upocampo.inscripciones'
    _description = 'Inscripciones de las actividades del hotel rural'

    #name = fields.Integer('Identificacion:')
    name = fields.Many2one('upocampo.clientes', string='Cliente:')
    actividad_id = fields.Many2one('upocampo.actividades', string='ID de Actividad:')
    fecha = fields.Datetime('Fecha:', autodate=True)