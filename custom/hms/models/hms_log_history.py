from odoo import models, fields


class HmsLogHistory(models.Model):
    _name = 'hms.log_history'

    description = fields.Text()
    patient_id = fields.Many2one('hms.patient')
