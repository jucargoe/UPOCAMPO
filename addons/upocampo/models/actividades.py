# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Actividades(models.Model):
    _name = 'upocampo.actividades'
    _description = 'Actividades del hotel rural'

    name = fields.Char('Nombre de Actividad:', required=True, help="Nombre requerido")
    descripcion = fields.Text('Descripcion:', required=True, help="Descripcion requerida")
    duracion = fields.Float('Duracion:')
    inscripciones_ids = fields.One2many('upocampo.inscripciones', 'actividad_id', 'Inscripciones:')
    empleado_id = fields.Many2one('upocampo.empleados', 'Empleado:')
    fecha = fields.Datetime('Fecha:')

    @api.onchange('duracion')
    def onchange_duracion(self):
        if self.descripcion != False and self.duracion < 10:
            raise models.ValidationError('La duración de la actividad tiene que ser mayor a 10 minutos')

    @api.constrains('empleado_id')
    def _check_empleado_id(self):
        valido = False
        for empleado in self.empleado_id:
            valido = True

        if valido == False:
            raise models.ValidationError('Tienes que asignar un empleado')
        
    @api.constrains('fecha')
    def _check_fecha(self):
        if self.fecha == False or (self.fecha != False and self.fecha < fields.Datetime.now()):
            raise models.ValidationError('La fecha no puede ser anterior a la actual')
    
    def btn_eliminarInscripciones(self):
          self.write({'inscripciones_ids':[(5,)]})

    