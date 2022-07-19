from odoo import fields, models


class PartnerInherit(models.Model):
    _inherit = 'res.partner'

    certificate_ids = fields.One2many('vca.certificate', 'customer_id')

