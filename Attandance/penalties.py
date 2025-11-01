from odoo import fields, models


class Penalty(models.Model):
    _name = "attandance.penalty"
    _description = "Penalties"

    person_type = fields.Selection([
        ('student', "Student"),
        ('employee', "Employee")
    ], required=True)
    student_id = fields.Many2one("users.student")
    employee_id = fields.Many2one("res.users")
    date = fields.Date(default=fields.Date.today)
    reason = fields.Text(required=True)

    amount = fields.Float(string="Fine Amount", default=0)
    state = fields.Selection([
        ('draft', "Draft"),
        ('approved', "Approved"),
        ('paid', "Paid")
    ], default='draft')
