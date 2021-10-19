
from odoo import http, models, fields
from odoo.http import request
import json


class Wikulaundry(http.Controller):
    @http.route('/bahancuci', auth='public')
    def get_models(self, **kwargs):
        order = request.env['wikulaundry.jeniscucian'].search([])
        value = []
        for ord in order:
            value.append({
                'nama' : ord.name,
                'ukuran' : ord.ukuran,
                'tipe' : ord.tipe                
            })
        return json.dumps(value)

    @http.route('/caracuci', auth='public')
    def get_caracuci(self, **kwargs):
        caracuci = request.env['wikulaundry.caracuci'].search([])
        value = []
        for cc in caracuci:
            value.append({
                'nama' : cc.name,
                'tingkat_kotoran' : cc.kotoran,
                'jenis_air' : cc.air,
                'harga_per_kg' : cc.harga                
            })
        return json.dumps(value)
