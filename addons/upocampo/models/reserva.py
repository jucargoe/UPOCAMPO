# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Reserva(models.Model):
    _name = 'upocampo.reserva'
    _description = 'Hotel rural'

    name = fields.Char(string="Title", required=True, help="name of the gym")
    description = fields.Text()
    #start = fields.Datetime('Starts',required=True, autodate = True)
    #end = fields.Datetime('Ends',required=True, autodate = True)
    capacity = fields.Integer("Capacity")
    activityType = fields.Selection([('dance','Dance'),
                                ('aerobic','Aerobic'),
                                ('anaerobic','Anaerobic'),
                                ('relax','Relax'),],
                                'Type of activity')
