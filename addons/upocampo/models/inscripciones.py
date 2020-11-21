# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Inscripciones(models.Model):
    _name = 'upocampo.inscripciones'
    _description = 'Inscripciones de las actividades del hotel rural'

    name = fields.Integer('Identificacion:')
    id_actividad = fields.Integer('ID de Actividad:')
    id_cliente = fields.Integer('ID de Cliente:')
    fecha = fields.Datetime('Fecha:', autodate=True)