from odoo import api, fields, models


class BahanAlatCuci(models.Model):
    _name = 'wikulaundry.bahanalatcuci'
    _description = 'New Description'

    name = fields.Char(string='Name')
    harga = fields.Integer(string='Harga Satuan')
    unit = fields.Char(string='Unit Pengguna')
    suppliernya = fields.Many2one(
        comodel_name='wikulaundry.suppliernya', 
        string='Supplier')
    
