from odoo import fields, models
from datetime import date

class EmployeeSalary(models.Model):
    _name = "payment.employee.salary"
    _description = "Employee Monthly Salary"

    employee_id = fields.Many2one("res.users", required=True)
    month = fields.Selection([
            ('jan', "January"), ('feb', "February"), ('mar', "March"), ('apr', "April"),
            ('may', "May"), ('jun', "June"), ('jul', "July"), ('aug', "August"),
            ('sep', "September"), ('oct', "October"), ('nov', "November"), ('dec', "December")
        ])    
    base_salary = fields.Float(required=True)
    bonus = fields.Float(default=0)
    deductions = fields.Float(default=0)
    total_salary = fields.Float(compute="_compute_total_salary", store=True)
    payment_state = fields.Selection([
        ('unpaid', "Unpaid"), ('paid', "Paid")
    ], default='unpaid')
    year = fields.Integer(string="Year", default=lambda self: date.today().year)
