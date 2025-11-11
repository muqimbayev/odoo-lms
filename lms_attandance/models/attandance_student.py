from odoo import fields, models


class Attendance(models.Model):
    _name = "attandance.attendance_student"
    _description = "Student Attendance"

    student_id = fields.Many2one("users.student", required=True)
    date = fields.Date(default=fields.Date.today, required=True)
    status = fields.Selection([
        ('present', "Present"),
        ('absent', "Absent"),
        ('late', "Late"),
    ], default='present')
    reason = fields.Text(string="Reason")


