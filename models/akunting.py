from odoo import api, fields, models


class Akunting(models.Model):
    _name = 'wikulaundry.akunting'
    _description = 'Keluar masuk uang' 
    _order = 'id asc' 
    
    name = fields.Char(string='NAMA')    
    date = fields.Datetime(
        string='WAKTU TRANSAKSI',
        default=fields.Datetime.now
        )
    debet = fields.Float(string='DEBET')
    kredit = fields.Float(string='KREDIT')  
    saldo = fields.Float(compute='_compute_saldo', string='SALDO', required=False)
    
    @api.depends('debet','kredit')
    def _compute_saldo(self):
        for record in self:
            prev = self.search_read([('id','<',record.id)],limit=1,order='date desc')
            prev_saldo = prev[0]['saldo'] if prev else 0
            record.saldo = prev_saldo + record.kredit - record.debet
    
    
    
    
    
