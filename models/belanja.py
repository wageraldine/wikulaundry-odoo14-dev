from odoo import api, fields, models
from odoo.exceptions import ValidationError


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
    
    tanggal_masuk = fields.Char(
        compute='_compute_tanggal_masuk', 
        string='Tanggal Barang Datang')
    
    @api.model
    def _compute_tanggal_masuk(self):
        for record in self:           
            tgl = self.env['wikulaundry.barangmasuk'].search([('name','=', record.id)]).mapped('tgl_datang')
            if tgl:
                record.tanggal_masuk = tgl[0]   
                record.sudah_masuk=True
            else:
                record.tanggal_masuk = 0
                record.sudah_masuk=False
    
    jml_pesan = fields.Integer(string='Jumlah Pemesanan')
    
    tagihan_supplier = fields.Float(
        compute='_compute_tagihan_supplier', 
        string='Tagihan Supplier')
    
    @api.depends('jml_pesan')
    def _compute_tagihan_supplier(self):
        for record in self:
            record.tagihan_supplier = record.name.harga * record.jml_pesan
    
    masuk_akunting = fields.Boolean(
        string='Masuk Akunting'
        )
    
    sudah_masuk = fields.Boolean(string='Barang Sudah Masuk')
    
    def masukakunting(self):
        for record in self:
            tgl = self.env['wikulaundry.barangmasuk'].search([('name','=', record.id)]).mapped('tgl_datang')
            if tgl:
                record.masuk_akunting=True
                self.env['wikulaundry.akunting'].create({'debet':record.tagihan_supplier,'name':record.name.name})
            else:
                raise ValidationError("Barang belum datang, tidak bisa masuk akunting")
    
    def keluarakunting(self):
        for record in self:
            record.masuk_akunting=False
            data = self.env['wikulaundry.akunting'].search([('name','=',record.name.name)])
            data.unlink()