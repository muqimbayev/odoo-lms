from odoo import fields, models

class StudentPayment(models.Model):
    _name = "payment.course_payment"
    _description = "Monthly Student Payment"

    student_id = fields.Many2one("education.student", required=True)
    group_id = fields.Many2one("education.group", required=True)
    amount_due = fields.Float(string="Amount Due", compute="_compute_amount_due")
    amount_paid = fields.Float(string="Amount Paid", default=0)
    payment_date = fields.Date(default=fields.Date.today)
    state = fields.Selection([
        ('pending', "Pending"),
        ('paid', "Paid"),
        ('overdue', "Overdue")
    ], default="pending")

    month = fields.Selection([
            ('jan', "January"), ('feb', "February"), ('mar', "March"), ('apr', "April"), ('may', "May"), ('jun', "June"), ('jul', "July"), ('aug', "August"),
            ('sep', "September"), ('oct', "October"), ('nov', "November"), ('dec', "December")
        ])

    year = fields.Integer(string="Year", default=fields.Date.year)
        