from odoo import api, fields, models


class Akunting(models.Model):
    _name = 'wikulaundry.akunting'
    _description = 'Keluar masuk uang'  
    
    name = fields.Char(string='NAMA')    
    debet = fields.Integer(string='DEBET')
    kredit = fields.Integer(string='KREDIT')  
    saldo = fields.Integer(string='SALDO')
    
    
    
    
    
