from odoo import api, fields, models


class Bayar(models.Model):
    _name = 'wikulaundry.bayar'
    _description = 'Penerimaan Pembayaran Cucian'

    name = fields.Many2one(
        comodel_name='wikulaundry.order', 
        string='Customer',
        domain="[('sudah_bayar','=',False)]",   
        )
        
    tgl_masuk = fields.Char(
        compute='_compute_tgl_masuk', 
        string='Tanggal Masuk')
    
    @api.depends('name')
    def _compute_tgl_masuk(self):
        for record in self:
            record.tgl_masuk = record.name.tanggal_masuk
       
    tgl_bayar = fields.Datetime(        
        string='Tanggal Bayar', 
        default=fields.Datetime.now())
    
    tagihan = fields.Integer(
        compute='_compute_tagihan', 
        string='Total Pembayaran',
        store=True
        )
    
    @api.depends('name')
    def _compute_tagihan(self):
        for record in self:
            record.tagihan = record.name.total_harga
            
    
    
    
            
    
    
            
    
    
