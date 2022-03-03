# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class odoo_final_md(models.Model):
#     _name = 'odoo_final_md.odoo_final_md'
#     _description = 'odoo_final_md.odoo_final_md'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
  

class empresa(models.Model):
    _name = 'odoo_final_md.empresa'
    _description = 'model empresa'

    name = fields.Char('Nombre',required=True)

    residencias_id = fields.One2many('odoo_final_md.residencias','empresa_id',string='residencias')

class residencias(models.Model):
    _name = 'odoo_final_md.residencias'
    _description = 'model residencias'

    name = fields.Char('ID',required=True)
    lugar = fields.Char(String='Lugar',required=True)

    empresa_id = fields.Many2one('odoo_final_md.empresa',string='Empresa')
    profesionales_salud_id = fields.One2many('odoo_final_md.profesionales_salud','residencias_id',string='profesionales_salud')

class profesionales_salud(models.Model):
    _name = 'odoo_final_md.profesionales_salud'
    _description = 'model profesionales_salud'

    name = fields.Char('Nombre',required=True)
    sector_de_la_salud = fields.Char('Sector: ')
    residencias_id = fields.Many2one('odoo_final_md.residencias',string='residencias')

class ancianos(models.Model):
    _name = 'odoo_final_md.ancianos'
    _description = 'model ancianos'

    name = fields.Char('Nombre del residente',required=True)
    numero = fields.Integer(String='DNI',required=True)

    factura_id = fields.One2many('odoo_final_md.factura','ancianos_id',string='factura')

class factura(models.Model):
    _name = 'odoo_final_md.factura'
    _description = 'model factura'

    name = fields.Char('factura a: ',required=True)

    ancianos_id = fields.Many2one('odoo_final_md.ancianos',string='ancianos')
    recibo_id = fields.Many2one('odoo_final_md.recibo',string='recibo')

class recibo(models.Model):
    _name = 'odoo_final_md.recibo'
    _description = 'model recibo'

    name = fields.Char('recibo a: ',required=True)

    enfermeria_id = fields.One2many('odoo_final_md.enfermeria','recibo_id',string='enfermeria')
    fisoterapia_id = fields.One2many('odoo_final_md.fisoterapia','recibo_id',string='fisoterapia')
    servicios_limpieza_id = fields.One2many('odoo_final_md.servicios_limpieza','recibo_id',string='servicios_limpieza')
    hospedaje_id = fields.One2many('odoo_final_md.hospedaje','recibo_id',string='hospedaje')
    factura_id = fields.One2many('odoo_final_md.factura','recibo_id',string='factura')


class enfermeria(models.Model):
    _name = 'odoo_final_md.enfermeria'
    _description = 'model enfermeria'

    name = fields.Char('Nombre de la empresa encargda de enfemeria ',required=True)
    empresa = fields.Char(String='empresa',required=True)
    precio = fields.Integer(String='Precio del servicio de enfermeria',required=True)

    recibo_id = fields.Many2one('odoo_final_md.recibo',string='recibo')

class fisoterapia(models.Model):
    _name = 'odoo_final_md.fisoterapia'
    _description = 'model fisoterapia'

    name = fields.Char('Nombre de la empresa encargda de fisoterapia ',required=True)
    empresa = fields.Char(String='empresa',required=True)
    precio = fields.Integer(String='Precio',required=True)

    recibo_id = fields.Many2one('odoo_final_md.recibo',string='recibo')

class servicios_limpieza(models.Model):
    _name = 'odoo_final_md.servicios_limpieza'
    _description = 'model servicios_limpieza'

    name = fields.Char('nombre de servicios de limpieza',required=True)
    empresa = fields.Char(String='empresa de limpieza',required=True)
    precio = fields.Integer(String='Precio del servicio de limpieza',required=True)

    recibo_id = fields.Many2one('odoo_final_md.recibo',string='recibo')

class hospedaje(models.Model):
    _name = 'odoo_final_md.hospedaje'
    _description = 'model hospedaje'

    name = fields.Char('Nombre del hospedaje',required=True)
    tipo = fields.Char(String='tipo de hospicio',required=True)
    precio = fields.Integer(String='Precio',required=True)

    recibo_id = fields.Many2one('odoo_final_md.recibo',string='recibo')

