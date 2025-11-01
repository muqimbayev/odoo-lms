from odoo import fields, models


class KPI(models.Model):
    _name = "payment.kpi"
    _description = "KPI"

    department_ids = fields.Many2many("users.department", required=True)
    employee_id = fields.Many2many('res.users')
    period_start = fields.Date(required=True)
    period_end = fields.Date(required=True)
    kpi_description = fields.Text(required=True)
    