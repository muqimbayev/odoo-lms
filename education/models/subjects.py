from odoo import fields, models, api


class Subjects(models.Model):
    _name = "education.subjects"
    _description = "Education Subjects"

    name = fields.Char(string="Name", required=True)
    duration = fields.Float(string="Duration")
    category_id = fields.Many2one("education.subjects", string="Category")
    month_price = fields.Float(string="Month price")
    month_lesson = fields.Float(string="Month lesson count")
    teacher_ids = fields.Many2many("users.teacher", string="Teachers")
    group_ids = fields.One2many("education.groups", inverse_name="subject_id")
    description = fields.Text(string="Note")
    #Compute fieldlar
    # student_count = fields.Integer(string="Student count", compute="_compute_student_count", store=True)
    # active_student_count = fields.Integer(string="Active student count", compute="_compute_active_student_count", store=True)
    # group_count = fields.Integer(string="Group_count", compute="_compute_group_count", store=True)
    # active_group_count = fields.Integer(string="Active group count", compute="_compute_active_group_count", store=True)
    # total_payment_summa = fields.Float(string="Total summa", compute="_compute_total_payment_summa")