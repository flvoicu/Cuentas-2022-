# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
import datetime

class tablaInversores(models.Model):

    _name = "cuentas.inversores"

    name = fields.Char('DNI', required=True)
    nombre = fields.Char('Nombre', required=True)
    
class tablaCliente(models.Model):

    _name = "cuentas.clientes"

    name = fields.Char('DNI', required=True)
    nombre = fields.Char('Nombre', required=True)
    email = fields.Char('E-mail', required=True)
    
    def send_email(self):
        import smtplib
        receivers_email= self.email
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login("pruebaemailodoo@gmail.com", "Odoo1234")
        message = "Ha sido dado de alta en Cuentas. Bienvenido" 
        server.sendmail("pruebaemailodoo@gmail.com", receivers_email, message)
        server.quit()

class tablaPlataformas(models.Model):

    _name="cuentas.plataformas"

    name = fields.Char('Plataforma', required=True)  
    
class tablaServicios(models.Model):

    _name = "cuentas.servicios"

    name = fields.Char('Nombre', required=True)
    plataforma = fields.Many2one('cuentas.plataformas', "Nombre plataforma", required=True) 
    inversor = fields.Many2one('cuentas.inversores', "DNI inversor", required=True)
    cliente = fields.Many2one('cuentas.clientes', "DNI cliente", required=True) 
    fecha1 = fields.Date("Fecha Inicio de Subscripción", required=True, default=fields.Date.context_today)  
    fecha2 = fields.Date("Fecha Fin de Subscripción", compute='_fecha', default=fields.Date.context_today)
    
    @api.depends('fecha1', 'fecha2')
    def _fecha(self):
        for record in self:
            record.fecha2 = record.fecha1 + datetime.timedelta(30)  