from odoo import fields, models

class Group(models.Model):
    _name = "lms.group"
    _description = "Group"

    name = fields.Char(string="Name", required=True)
    teacher_ids = fields.Many2many(comodel_name="lms.teacher", string="Teacher")
    student_ids = fields.Many2many(comodel_name="lms.students")
    branch_id = fields.Many2one(comodel_name="res.company", required=True, string="Branch")

    
