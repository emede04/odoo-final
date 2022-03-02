# -*- coding: utf-8 -*-

# from odoo import models, fields, api


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


from odoo import models, fields, api


class Anciano(models.Model):
    _name = 'final.Anciano'
    _description = 'model Anciano'

    name = fields.Char('Nombre',required=True)
    nombre_enfermero = fields.Char('Nombre',required=True)
    edad = fields.Char('Nombre',required=True)
    enfermedades = fields.Char('Nombre',required=True)




class Enfermeros(models.Model):
    _name = 'final.Enfermeros'
    _description = 'model Enfermeros'

    name = fields.Char('Nombre',required=True)




class Residencia(models.Model):
    _name = 'final.Enfermeros'
    _description = 'model Enfermeros'

    name = fields.Char('Nombre',required=True)


