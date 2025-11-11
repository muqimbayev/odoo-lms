from odoo import fields, models

class TeacherAddCustom(models.Model):
    _inherit = "users.teacher"
       
    course_ids = fields.Many2many(comodel_name="education.course", required=True)
    group_count = fields.Integer(string="Group count", compute="_compute_group_count")
    student_count = fields.Integer(string="Student count", compute="_compute_student_count")
    group_ids = fields.Many2many(comodel_name="education.groups")

    def _compute_group_count(self):
        self.group_count = len(self.group_ids)

    def _compute_student_count(self):
        for record in self:
            for group in record.group_ids:
                record.student_count+=group.student_count




