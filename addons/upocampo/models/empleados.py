# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Empleados(models.Model):
    _name = 'upocampo.empleados'
    _description = 'Empleados del hotel rural'

    name = fields.Char('DNI:')
    nombre = fields.Char('Nombre:')
    apellidos = fields.Char('Apellidos:')
    puesto_id = fields.Many2one('upocampo.puestos', 'Puesto de Trabajo:')
    sueldo = fields.Float('Sueldo:')
    genero = fields.Selection([('hombre', 'Hombre'), ('mujer', 'Mujer')], 'Género:')
    actividades_ids = fields.One2many('upocampo.actividades', 'empleado_id', 'Actividades:')

    _sql_constraints = [('empleados_name_unique','UNIQUE (name)','El DNI del empleado ya está en uso')]

    @api.constrains('nombre')
    def _check_nombre(self):
        if self.nombre == False:
            raise models.ValidationError('Campo nombre requerido')

    @api.constrains('apellidos')
    def _check_apellidos(self):
        if self.apellidos == False:
            raise models.ValidationError('Campo apellidos requerido')

    def btn_eliminarActividades(self):
        self.write({'actividades_ids':[(5,)]})