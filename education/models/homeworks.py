from odoo import fields, models


class Homework(models.Model):
    _name = "education.homework"
    _description = "Education"

    group_id = fields.Many2one(comodel_name="education.groups", required=True, string="Group")
    teacher_id = fields.Many2one("users.teacher", string="Teacher", required=True)
    start_date = fields.Datetime(string="Start date")
    dedline = fields.Selection([('12_hour', "12 hour"), ("24_hour", "24 hour"), ("36_hour", "36 hour"), ("48_hour", "48 hour")])
    homework_text = fields.Text(string="Homework text", required=True)
    homework_file = fields.Binary(string="Attachment")
    file_name = fields.Char(string="File Name")
    #Compute
    # end_date = fields.Datetime(string="End date", compute="_compute_end_date")


class HomeworkSubmission(models.Model):
    _name = "education.homework.submission"
    _description = "Homework Submission"
    _order = "submit_date desc"

    homework_id = fields.Many2one("education.homework", string="Homework", required=True, ondelete="cascade")
    student_id = fields.Many2one("lms.student", string="Student", required=True)
    submit_date = fields.Datetime( string="Submitted Date", default=lambda self: fields.Datetime.now())
    answer_text = fields.   Text(string="Answer Text")
    answer_file = fields.Binary(string="Attachment")
    state = fields.Selection(
        [
            ("submitted", "Submitted"),
            ("reviewed", "Reviewed"),
            ("graded", "Graded"),
        ],
        string="Status",
        default="submitted"
    )
    grade = fields.Float(string="Grade")
    teacher_feedback = fields.Text(string="Teacher Feedback")

