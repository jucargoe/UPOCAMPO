# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Empleados(models.Model):
    _name = 'upocampo.empleados'
    _description = 'Empleados del hotel rural'

    dni = fields.Integer('DNI:')
    name = fields.Char('Nombre:')
    apellidos = fields.Char('Apellidos:')
    id_puesto = fields.Integer('ID de Puesto de Trabajo:')
    sueldo = fields.Float('Sueldo:')
    genero = fields.Selection([('hombre', 'Hombre'), ('mujer', 'Mujer')], 'Género:')