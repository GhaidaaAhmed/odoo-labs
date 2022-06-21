from odoo import models, fields


class HmsDoctor(models.Model):
    _name = 'hms.doctor'

    first_name = fields.Char()
    last_name = fields.Char()
    image = fields.Binary()
    department_id = fields.Many2one('hms.department')
    patient_id = fields.Many2one('hms.patient')
