# -*- coding: utf-8 -*-

 from odoo import models, fields, api


# class final(models.Model):
#     _name = 'final.final'
#     _description = 'final.final'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100


 class residencia(models.Model):
     _name = 'final.residencia'
     _description = 'model residencia'
     name = fields.Char('Nombre', required=True)

     enfermeros_id = fields.One2many('final.enfermeros','residencia_id', string='Enfermeros')
     ancianos_id = fields.One2many('final.ancianos', 'residencia_id', string='Ancianos')
     habitaciones_id = fields.One2many('final.habitaciones', 'residencia_id',string='habitaciones')

class enfermeros(models.Model):
     _name = 'final.enfermeros'
     _description = 'model enfermeros'

     name = fields.Char('Nombre', required=True)
     residencia_id = fields.Many2one('final.residencia',string ='residencia')
     ancianos_id = fields.Many2one('final.ancianos',string ='ancianos')

 class ancianos(models.Model):
     _name = 'final.ancianos'
     _description = 'model ancianos'

     name = fields.Char('Nombre', required=True)
     residencia_id = fields.Many2one('final.residencia',string ='residencia')
     enfermeros_id = fields.Many2one('final.ancianos',string ='enfermeros')

 class comida(models.Model):
     _name = 'final.comida'
     _description = 'model comida'

     name = fields.Char('Nombre', required=True)


 class medicina(models.Model):
     _name = 'final.medicina'
     _description = 'model medicina'

     name = fields.Char('Nombre', required=True)


 class enfermedades(models.Model):
     _name = 'final.enfermedades'
     _description = 'model enfermedades'

     name = fields.Char('Nombre', required=True)



 class habitaciones(models.Model):
     _name = 'final.habitaciones'
     _description = 'model habitaciones'

     name = fields.Char('Nombre', required=True)
     residencia_id = fields.Many2one('final.habitaciones',string ='residencia')


 class mascotas(models.Model):
     _name = 'final.mascotas'
     _description = 'model mascotas'

     name = fields.Char('Nombre', required=True)


 class visitas(models.Model):
     _name = 'final.visitas'
     _description = 'model visitas'

     name = fields.Char('Nombre', required=True)


 class familiar(models.Model):
     _name = 'final.familiar'
     _description = 'model residencia'

     name = fields.Char('Nombre', required=True)