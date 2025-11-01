from odoo import fields, models


class Expense(models.Model):
    _name = "payment.expense"
    _description = "Expenses"

    name = fields.Char(required=True)
    category = fields.Selection([
        ('rent', "Rent"),
        ('utilities', "Utilities"),
        ('equipment', "Equipment"),
        ('salary', "Salaries"),
        ('marketing', "Marketing"),
        ('other', "Other")
    ])
    amount = fields.Float(required=True)
    date = fields.Date(default=fields.Date.today)
    branch_id = fields.Many2one("res.company")
    description = fields.Text()
