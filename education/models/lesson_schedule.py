from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime


class LessonSchedule(models.Model):
    _name = "education.schedule"
    _description = "Lesson schedule"

    group_id = fields.Many2one("education.groups", string="Group", required=True)
    teacher_id = fields.Many2one("lms.teacher", string="Teacher", required=True)
    day_of_week = fields.Selection(
        [
            ("mon", "Monday"),
            ("tue", "Tuesday"),
            ("wed", "Wednesday"),
            ("thu", "Thursday"),
            ("fri", "Friday"),
            ("sat", "Saturday"),
            ("sun", "Sunday"),
        ],
        required=True,
        string="Day"
    )
    start_time = fields.Float(string="Start Time", required=True)
    end_time = fields.Float(string="End Time", required=True)
    active = fields.Boolean(default=True)
