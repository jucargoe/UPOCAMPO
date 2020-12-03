# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Clientes(models.Model):
    _name = 'upocampo.clientes'
    _description = 'Clientes del hotel rural'

    name = fields.Char('DNI:', required=True, help="El DNI es requerido") 
    nombre = fields.Char('Nombre:')
    apellidos = fields.Char('Apellidos:')
    reservas_ids = fields.One2many('upocampo.reservas', 'name', 'Reservas:')
    inscripciones_ids = fields.One2many('upocampo.inscripciones', 'name', 'Inscripciones:')

    _sql_constraints = [('clientes_name_unique','UNIQUE (name)','El DNI debe ser único')]

    @api.constrains('nombre')
    def _check_nombre(self):
        if self.nombre == False:
            raise models.ValidationError('Campo nombre requerido')

    @api.constrains('apellidos')
    def _check_apellidos(self):
        if self.apellidos == False:
            raise models.ValidationError('Campo apellidos requerido')