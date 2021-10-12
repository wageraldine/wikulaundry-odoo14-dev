from odoo import api, fields, models


class OrderCuci(models.Model):
    _name = 'wikulaundry.order'
    _description = 'Daftar Order Cuci WikuLaundry'

    name = fields.Many2one(
        comodel_name='res.partner', 
        string='Customer',
        domain="[('is_customernya','=',True)]",
        delegate=True)  
    
    tanggal_masuk = fields.Datetime(
        default=fields.Datetime.now,
        )
    
    detailcucian_ids = fields.One2many(
        comodel_name='wikulaundry.detailcucian', 
        inverse_name='order_id', 
        string='Detail Order')
    
    jml_pesanan = fields.Char(
        compute='_compute_jml_pesanan', 
        string='Jumlah Pesanan')
    
    @api.depends('detailcucian_ids')
    def _compute_jml_pesanan(self):        
        for record in self:
            record.jml_pesanan +=len(record.detailcucian_ids)
            
    
            
            
class DetailCucian(models.Model):
    _name = 'wikulaundry.detailcucian'
    _description = 'Detail Cucian Wiku Laundry'
    
    name = fields.Char(string='Kode Order')    
    
    order_id = fields.Many2one(
        comodel_name='wikulaundry.order', 
        string='Kode Order')
         
    jenis = fields.Many2one(
        comodel_name='wikulaundry.jeniscucian',
        string='Bahan Cucian')
    
    harga = fields.Integer(
        compute='_compute_harga', 
        string='Harga per Kg')
    
    @api.depends('jenis')
    def _compute_harga(self):
        for record in self:
            record.harga = record.jenis.harga
    
    berat = fields.Integer(
        string='Berat Cucian')
        
    jumlah_harga = fields.Integer(
        compute='_compute_field_name', 
        string='Jumlah Harga')
    
    @api.depends('berat')
    def _compute_field_name(self):
        for record in self:
            record.jumlah_harga = record.berat * record.harga
            
   
           
   
    
    
    
    
    
    
    
    
    
