from odoo import api, fields, models


class SelesaiCuci(models.Model):
    _name = 'wikulaundry.selesaicuci'
    _description = 'Penyelesaian Cucian'

    name = fields.Many2one(
        comodel_name='wikulaundry.order', 
        string='Customer',
        domain="[('selesai_cuci','=',False)]",   
        )
        
    tgl_masuk = fields.Char(
        compute='_compute_tgl_masuk', 
        string='Tanggal Masuk')
    
    @api.depends('name')
    def _compute_tgl_masuk(self):
        for record in self:
            record.tgl_masuk = record.name.tanggal_masuk
       
    tgl_selesai = fields.Datetime(        
        string='Tanggal Selesai', 
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
            
    
    
    
            
    
    
            
    
    
