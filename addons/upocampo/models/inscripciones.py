# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Inscripciones(models.Model):
    _name = 'upocampo.inscripciones'
    _description = 'Inscripciones de las actividades del hotel rural'

    name = fields.Many2one('upocampo.clientes', string='Cliente:')
    actividad_id = fields.Many2one('upocampo.actividades', string='ID de Actividad:')
    fecha = fields.Datetime(compute='_fechaHoy', string="Fecha:", store=True)

    def _fechaHoy(self):
        self.fecha = fields.Datetime.now()