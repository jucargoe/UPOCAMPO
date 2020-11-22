# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Empleados(models.Model):
    _name = 'upocampo.empleados'
    _description = 'Empleados del hotel rural'

    name = fields.Integer('DNI:')
    nombre = fields.Char('Nombre:')
    apellidos = fields.Char('Apellidos:')
    puesto_id = fields.Many2one('upocampo.puestos', 'Puesto de Trabajo:')
    sueldo = fields.Float('Sueldo:')
    genero = fields.Selection([('hombre', 'Hombre'), ('mujer', 'Mujer')], 'Género:')
    actividades_ids = fields.One2many('upocampo.actividades', 'empleado_id', 'Actividades:')