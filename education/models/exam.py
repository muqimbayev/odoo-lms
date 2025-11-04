from odoo import fields, models, api


class Exam(models.Model):
    _name = "education.exam"
    _description = "Exam"

    name = fields.Char(string="Exam Name", required=True)
    group_id = fields.Many2one("education.groups", string="Group", required=True)
    teacher_id = fields.Many2one("users.teacher", string="Examiner", required=True)
    exam_date = fields.Datetime(required=True)
    duration_minutes = fields.Integer(string="Duration (minutes)", default=60)
    question_ids = fields.One2many("education.exam.question", "exam_id")
    pass_score = fields.Float(string="Pass Score", default=60)
    state = fields.Selection([
        ('draft', "Draft"),
        ('in_progress', "In Progress"),
        ('done', "Finished"),
    ], default='draft')
    #Compute
    # max_score = fields.Float(string="Max Score", compute="_compute_max_score", store=True)


class ExamQuestion(models.Model):
    _name = "education.exam.question"
    _description = "Exam Question"

    exam_id = fields.Many2one("education.exam", required=True)
    question_text = fields.Text(required=True)
    score = fields.Float(default=0) 


class ExamResult(models.Model):
    _name = "education.exam.result"
    _description = "Exam Result"

    exam_id = fields.Many2one("education.exam", required=True)
    student_id = fields.Many2one("users.students", required=True)
    score = fields.Float(string="Score", default=0)
    #Compute
    # passed = fields.Boolean(compute="_compute_passed", store=True)
