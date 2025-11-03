from odoo import fields, models


class Teacher(models.Model):
   _inherit = "users.teacher"

   payment_ids = fields.One2many(comodel_name="payment.payment")
  