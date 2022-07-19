from odoo import models, fields


class VcaBrand(models.Model):
    _name = 'vca.brand'

    name = fields.Char()
    certificate_ids = fields.One2many('vca.certificate', 'brand_id')
