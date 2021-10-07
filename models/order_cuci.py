from odoo import api, fields, models


class OrderCuci(models.Model):
    _name = 'wikulaundry.order'
    _description = 'Daftar Order Cuci WikuLaundry'

    name = fields.Char(
        string='No.Order',
        required=True
        )
    customer_id = fields.Many2one(
        comodel_name='res.partner', 
        string='Customer',
        domain="[('is_customernya','=',True)]",
        delegate=True
        )
    
    tanggal_masuk = fields.Datetime(
        default=fields.Datetime.now,
        )
    
    models_id = fields.Many2one(
        comodel_name='wikulaundry.jeniscucian', 
        string='Bahan Cucian')
    
    
    
    
    
