from odoo import models, fields, api
from datetime import datetime
from odoo.exceptions import ValidationError
import re


class HmsPatient(models.Model):
    _name = 'hms.patient'

    first_name = fields.Char()
    last_name = fields.Char()
    birth_date = fields.Date()
    age = fields.Integer(compute="_cal_age", store="True")
    history = fields.Html()
    cr_ratio = fields.Float()
    blood_type = fields.Selection([("A", "A"),
                                   ("B", "B"),
                                   ("AB", "AB"),
                                   ("O", "O")])
    pcr = fields.Boolean()
    address = fields.Text()
    image = fields.Binary()
    department_id = fields.Many2one('hms.department')
    log_history = fields.One2many('hms.log_history', 'patient_id')
    doctor_ids = fields.One2many('hms.doctor', 'patient_id')
    department_capacity = fields.Integer(related='department_id.capacity')
    state = fields.Selection([("undetermined", "Undetermined"),
                                   ("good", "Good"),
                                   ("fair", "Fair"),
                                   ("serious", "Serious")], default="undetermined")
    tags_ids = fields.Many2many("hms.tag")
    email = fields.Char()
    _sql_constraints = [("email_duplicated", "UNIQUE(email)", "Duplicated Email")]

    @api.depends('birth_date')
    def _cal_age(self):
        for record in self:
            if record.birth_date:
                record.age = datetime.today().year - datetime.strptime(str(record.birth_date), '%Y-%m-%d').year

    @api.constrains('email')
    def _validate_email(self):
        for record in self:
            if not re.match('(\w+[.|\w])*@(\w+[.])*\w+', record.email):
                raise ValidationError("Email Not Valid")

    @api.onchange('state')
    def _onchange_state(self):
        self.ensure_one()
        description = f"State changed to {self.state}"
        self.env['hms.log_history'].create([{'description': description,
                                             "patient_id": self.ids[0]}])

    @api.onchange('age')
    def _onchange_age(self):
        if self.age < 30:
            self.pcr = True
            return {
                'warning': {
                    'title': 'Warning!',
                    'message': "PCR has been checked"}
            }

    # @api.onchange('department_id')
    # def _onchange_department_id(self):
    #     if self.department_id:
    #         return {
    #             'tags_ids': {
    #                 'readonly': False}
    #         }


