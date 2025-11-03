from odoo import fields, models


class StudentCertification(models.Model):
    _name = "education.certification"
    _description = "Student Certification"

    student_id = fields.Many2one('users.students', required=True, string="Student")
    file = fields.Binary(string="Certification")
    