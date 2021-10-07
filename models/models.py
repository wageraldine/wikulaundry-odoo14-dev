# -*- coding: utf-8 -*-


from odoo import models, fields

class ModelDasar(models.Model):
    _name = "wikulaundry.modeldasar"
    _description = "model dasar wiku laundry"
    
    ukuran = fields.Char(
        string='ukuran bahan',
        required=True,
    )
    
    tipe = fields.Selection(
        string='tipe/jenis bahan',
        selection=[('katun', 'Katun'), ('polyester', 'Polyester'), ('twill', 'Twill'), ('sutra', 'Sutra')]
    )
    
    
    
class WikuLaundry(models.Model):
    _name = 'wikulaundry.jeniscucian'
    _description = 'daftar jenis-jenis cucian'
    _inherit = 'wikulaundry.modeldasar'
    
    name=fields.Char(
        string='jenis cucian',
        required=True        
    )
    
    active = fields.Boolean(
        default=True
    )
    
    deskripsi = fields.Char(
        string='Deskripsi'
    )
    
    teknik_id = fields.Many2one(
        comodel_name='wikulaundry.caracuci', 
        string='teknik cuci', 
        required=True,
        delegate=True)
    
    order_cuci_id = fields.One2many(
        comodel_name='wikulaundry.order', 
        inverse_name='models_id', 
        string='Order Cuci')
    
    
    
    
    
    
