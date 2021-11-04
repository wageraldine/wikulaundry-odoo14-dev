from odoo import api, fields, models


class Suppliernya(models.Model):
    _name = 'wikulaundry.suppliernya'
    _description = 'Supplier bahan dan alat cuci wikulaundry'

    name = fields.Char(
        string='Name',
        required=True)
    
    alamat = fields.Char(string='Alamat')
    
    cp = fields.Char(string='Contact Person')
    
    telp = fields.Char(string='Nomor Telepon')
    
    bahanalat = fields.One2many(
        comodel_name='wikulaundry.bahanalatcuci', 
        inverse_name='suppliernya', 
        string='Bahan Supply')
    
