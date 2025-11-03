from odoo import fields, models


class Payment(models.Model):
    _inherit = "payment.course_payment"

    group_id = fields.Many2one("education.group", required=True)
