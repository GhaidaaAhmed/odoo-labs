from datetime import datetime
from odoo import models, fields, api


class VcaCertificate(models.Model):
    _name = 'vca.certificate'

    serial_number = fields.Char(default=lambda self: self.env['ir.sequence'].next_by_code('vca.certificate.serial_no'))
    vehicle_type = fields.Selection([("Car", "Car"),
                                     ("Bus", "Bus"),
                                     ("Minibus", "Minibus"),
                                     ("Microbus", "Microbus")])
    certificate_type_id = fields.Many2one('vca.certificate.type')
    traffic_department_id = fields.Many2one('vca.traffic.department')
    customer_id = fields.Many2one('res.partner')
    price = fields.Float()
    motor_number = fields.Char()
    chassis_number = fields.Char()
    brand_id = fields.Many2one('vca.brand')
    is_printed = fields.Boolean(default=0)
    print_date = fields.Date()

    @api.model
    def car_model_selection(self):
        year_list = []
        for y in range(datetime.now().year - 20, datetime.now().year):
            year_list.append((str(y), str(y)))
        return year_list

    car_model = fields.Selection(car_model_selection)

    def print_report(self):
        if self.create_uid == self.env.uid:
            self.is_printed = True
            self.print_date = datetime.today()

        return self.env.ref('vca.vca_certificate_card_report').report_action(self)
