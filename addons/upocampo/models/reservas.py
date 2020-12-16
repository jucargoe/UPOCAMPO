# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Reservas(models.Model):
    _name = 'upocampo.reservas'
    _description = 'Reserva de habitación de hotel rural'

    name = fields.Many2one('upocampo.clientes', string='Cliente:')
    descuento_id = fields.Many2one('upocampo.descuentos', string='Descuento:')
    precio = fields.Float('Precio:')
    importeTotal = fields.Float(compute='_calcularDescuento', string='Importe total:', store=True)    
    habitaciones_ids = fields.Many2many('upocampo.habitaciones', string='Habitaciones asociadas:')
    checkIn = fields.Datetime('Check In:', require=True, help="El campo checkin es requerido", autodate=True)
    checkOut = fields.Datetime('Check Out:', require=True, help="El campo checkout es requerido", autodate=True)

    @api.onchange('checkIn')
    def onchange_checkIn(self):
        if self.checkIn != False and self.checkIn > self.checkOut:
            raise models.ValidationError('La fecha de entrada no puede ser posterior a la de salida')

    @api.onchange('checkOut')
    def onchange_checkOut(self):
        if self.checkOut != False and self.checkIn > self.checkOut:
            raise models.ValidationError('La fecha de entrada no puede ser posterior a la de salida')
    
    @api.depends('descuento_id')
    def _calcularDescuento(self):
        if self.descuento_id != False:
            self.importeTotal = self.precio - self.precio * (self.descuento_id.porcentaje / 100)
        else:
            self.importeTotal = self.precio
        