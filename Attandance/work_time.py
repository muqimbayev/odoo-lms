from odoo import fields, models


class WorkTime(models.Model):
    _name = "attandance.work.time"
    _description = "Employee Work Time"

    employee_id = fields.Many2one(
        "res.users", required=True, string="Employee")
    date = fields.Date(default=fields.Date.today, required=True)
    start_date = fields.Datetime(string="Check In")
    end_date = fields.Datetime(string="Check Out")
    schedule_type = fields.Selection([
        ('full_time', "Full Time"),
        ('part_time', "Part Time"),
    ], default='full_time')
    work_day_ids = fields.Many2many(comodel_name="education.weekday", string="Weekend Days"
                                    )


class Weekday(models.Model):
    _name = "education.weekday"
    _description = "Week Days"

    name = fields.Selection([
        ('monday', "Monday"),
        ('tuesday', "Tuesday"),
        ('wednesday', "Wednesday"),
        ('thursday', "Thursday"),
        ('friday', "Friday"),
        ('saturday', "Saturday"),
        ('sunday', "Sunday")
    ], string="Day", required=True)
