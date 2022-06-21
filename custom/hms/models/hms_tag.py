from odoo import models, fields


class HmsTag(models.Model):
    _name = 'hms.tag'

    name = fields.Char()