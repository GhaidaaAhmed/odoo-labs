from odoo import fields, models, api
from odoo.exceptions import ValidationError, UserError


class PartnerInherit(models.Model):
    _inherit = 'res.partner'

    related_patient_id = fields.Many2one('hms.patient')

    @api.constrains('email')
    def _validate_email(self):
        for record in self:
            if record.related_patient_id:
                patient = self.env['hms.patient'].search([('email', '=', record.email)])
                if record.email != patient.email:
                    raise ValidationError("Email Not Valid")

    def unlink(self):
        for record in self:
            if record.related_patient_id:
                raise UserError("Can't delete Patient")
        return super(PartnerInherit, self).unlink()

