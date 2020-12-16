# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Puestos(models.Model):
    _name = 'upocampo.puestos'
    _description = 'Puestos de trabajo del hotel rural'

    name = fields.Char('Nombre del Puesto:')
    descripcion = fields.Text('Descripcion:')
    empleado_id = fields.Many2one('upocampo.empleados', string='Empleados:')

    _sql_constraints = [('puestos_name_unique','UNIQUE (name)','El nombre del puesto ya está en uso')]