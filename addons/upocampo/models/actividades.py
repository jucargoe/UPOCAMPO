# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Actividades(models.Model):
    _name = 'upocampo.actividades'
    _description = 'Actividades del hotel rural'

    name = fields.Char('Nombre de Actividad:')
    descripcion = fields.Text('Descripcion:')
    duracion = fields.Float('Duracion:')
    inscripciones_ids = fields.One2many('upocampo.inscripciones', 'actividad_id', 'Inscripciones:')
    empleado_id = fields.Many2one('upocampo.empleados', 'Empleado:')