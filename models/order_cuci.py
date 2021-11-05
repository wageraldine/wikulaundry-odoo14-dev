from odoo import api, fields, models
from odoo.exceptions import ValidationError
class OrderCuci(models.Model):
    _name = 'wikulaundry.order'
    _description = 'Daftar Order Cuci WikuLaundry'
    _order = 'id desc'

    name = fields.Many2one(
        comodel_name='res.partner', 
        string='Customer',
        domain="[('is_customernya','=',True)]",
        delegate=True
        )  
    
    phone = fields.Char(
        compute='_compute_phone', 
        string='No. Telepon')
    
    @api.depends('name')
    def _compute_phone(self):
        for record in self:
            record.phone = record.name.phone
    
    tanggal_masuk = fields.Datetime(
        default=fields.Datetime.now,
        )
    
    tanggal_bayar = fields.Datetime(
        compute='_compute_tanggal',
        string='Tanggal Selesai'
        )      
            
    detailcucian_ids = fields.One2many(
        comodel_name='wikulaundry.detailcucian', 
        inverse_name='order_id', 
        string='Detail Order'
        )
    
    bayar_ids = fields.One2many(
        comodel_name='wikulaundry.bayar', 
        inverse_name='name', 
        string='Pembayaran'
        )    
        
    jml_pesanan = fields.Char(
        compute='_compute_jml_pesanan', 
        string='Jumlah Pesanan'
        )
    
    sudah_bayar = fields.Boolean(
        string='Sudah Bayar'
        )
    
    masuk_akunting = fields.Boolean(string='Masuk Akunting')
    
    @api.depends('detailcucian_ids')
    def _compute_jml_pesanan(self):        
        for record in self:
            record.jml_pesanan +=len(record.detailcucian_ids)
            
    total_harga = fields.Integer(
        compute='_compute_total_harga', 
        string='Total Tagihan'
        )
   
    @api.model
    def _compute_total_harga(self):        
        for record in self:           
                total = sum(self.env['wikulaundry.detailcucian'].search([('order_id','=', record.id)]).mapped('jumlah_harga'))
                record.total_harga = total           
    
    @api.model
    def _compute_tanggal(self):        
        for record in self:           
            tgl = self.env['wikulaundry.bayar'].search([('name','=', record.id)]).mapped('tgl_bayar')
            if tgl:
                record.tanggal_bayar = tgl[0]   
                record.sudah_bayar=True
            else:
                record.tanggal_bayar = 0
                record.sudah_bayar=False
   
    def confirm(self):
        for record in self:
            if record.tanggal_bayar:
                record.masuk_akunting=True
                self.env['wikulaundry.akunting'].create({'kredit':record.total_harga,'name':record.name.display_name})
            else:
                raise ValidationError("Yang belum selesai dicuci tidak bisa masuk")
    def cancel(self):
        for record in self:
            record.masuk_akunting=False
            data = self.env['wikulaundry.akunting'].search([('name','=',record.name.display_name)])
            data.unlink()
                   
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
            
    
    
    
    
    
    
    
