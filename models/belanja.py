from odoo import api, fields, models


class PemesananBarang(models.Model):
    _name = 'wikulaundry.pesan'
    _description = 'Purchasing Wiku Laundry'

    name = fields.Many2one(
        comodel_name='wikulaundry.bahanalatcuci', 
        string='Nama Barang'
        )
    
    supplier = fields.Char(
        compute='_compute_supplier', 
        string='Supplier')
    
    @api.depends('name')
    def _compute_supplier(self):
        for record in self:
            record.supplier = record.name.suppliernya.name
    
    contact = fields.Char(
        compute='_compute_contact',
        string='No. Telp Supplier'
        )
    
    @api.depends('name')
    def _compute_contact(self):
        for record in self:
            record.contact = record.name.suppliernya.telp
    
    tanggal_pesan = fields.Date(
        string='Tanggal Pesan', 
        default=fields.Datetime.now
        )
    
    tanggal_masuk = fields.Date(
        string='Tanggal Masuk Barang'
        )
    
    jml_pesan = fields.Integer(string='Jumlah Pemesanan')
    
    masuk_akunting = fields.Boolean(
        string='Masuk Akunting'
        )
    

class PenerimaanBarang(models.Model):
    _name = 'wikulaundry.terima'
    _description = 'Penerimaan Barang Gudang'

    name = fields.Many2one(
        comodel_name='wikulaundry.pesan', 
        string='Nama Barang'
        )
    
    tanggal_pesan = fields.Char(
        compute='_compute_tanggal_pesan', 
        string='Tanggal Pemesanan'
        )
    
    @api.depends('name')
    def _compute_tanggal_pesan(self):
        for record in self:
            record.tanggal_pesan = record.name.tanggal_pesan
    
    tgl_terima = fields.Datetime(        
        string='Tanggal Terima', 
        default=fields.Datetime.now())
    

    
    