# -*- coding: utf-8 -*-

from odoo import models, fields, api


class kedatech(models.Model):
    _name = 'kedatech.material'
    _description = 'kedatech.material'

    code = fields.Char()
    name = fields.Char()
    type = fields.Selection([('fabric','Fabric'),('jeans','Jeans'),('cotton','Cotton')])
    buy_price = fields.Monetary()
