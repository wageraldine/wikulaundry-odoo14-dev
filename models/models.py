# -*- coding: utf-8 -*-


from odoo import models, fields, api
from odoo.exceptions import ValidationError

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
    
    deskrip = fields.Char(
        compute='_compute_deskrip', 
        string='Teknik Pencucian')
    
    @api.depends('teknik_id')
    def _compute_deskrip(self):
        for record in self:
            record.deskrip = record.teknik_id.deskripsicuci
    
    @api.onchange('tipe')
    def _onchange_field_name(self):
        if self.tipe == 'katun':
            return {
                'warning' : {
                    'title' : "Teknik Pencucian",
                    'message' : "Rubah teknik pencucian ke golongan B"
                },
            }
        elif self.tipe == 'polyester':
            return {
                'warning' : {
                    'title' : "Teknik Pencucian",
                    'message' : "Rubah teknik pencucian ke golongan A"
                }
            }
    
    @api.constrains('name')
    def _check_name(self):
        for record in self:
            bahan = self.env['wikulaundry.jeniscucian'].search([('name', '=',record.name), ('id', '!=',record.id)])
            if bahan:
                raise ValidationError("Bahan %s sudah ada" % record.name)
    
    
    
    
    
    
