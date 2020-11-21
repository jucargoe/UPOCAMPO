# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Actividades(models.Model):
    _name = 'upocampo.actividades'
    _description = 'Actividades del hotel rural'

    identificacion = fields.Integer('Identificacion:')
    name = fields.Char('Nombre de Actividad:')
    descripcion = fields.Text('Descripcion:')
    duracion = fields.Float('Duracion:')
    id_empleado = fields.Integer('ID de Empleado:')