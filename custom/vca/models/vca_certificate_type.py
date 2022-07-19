from odoo import models, fields


class VcaCertificateType(models.Model):
    _name = 'vca.certificate.type'

    name = fields.Char()
    certificate_ids = fields.One2many('vca.certificate', 'certificate_type_id')
