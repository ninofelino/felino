# -*- coding: utf-8 -*-

from odoo import models, fields, api
class felino(models.Model):
     _name = 'felino.felino'
     name = fields.Char()
     barcode = fields.Char()
     article = fields.Char()
     ukuran  = fields.Char()
     sale_price = fields.Char()
     list_price = fields.Char()
     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100