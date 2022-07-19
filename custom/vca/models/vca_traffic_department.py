from odoo import models, fields


class VcaTrafficDepartment(models.Model):
    _name = 'vca.traffic.department'

    name = fields.Char()
    certificate_ids = fields.One2many('vca.certificate', 'traffic_department_id')
