from odoo import fields, models, api


class Operator(models.Model):
    _inherit = "users.operator"

    salary_payment = fields.One2many('payment.employee.salary', inverse_name="employee_id")