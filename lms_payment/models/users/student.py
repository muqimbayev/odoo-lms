from odoo import fields, models, api


class Students(models.Model):
    _inherit = "users.students"

    payment_ids = fields.One2many(comodel_name="payment.cousrse_payment", inverse_name="student_id")





