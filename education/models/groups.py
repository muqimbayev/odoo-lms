from odoo import fields, models, api


class GroupStudent(models.Model):
    _name = "education.group_student"
    _description = "Group Student"

    student_id = fields.Many2many("users.student", string="Student")
    status = fields.Selection([('active', 'Active'), ('inactive', 'Inactive'), ('froozen', 'Froozen')])
    reason = fields.Text(string="Reason")
    date = fields.Date(string="Stoppend date")
    group_id = fields.Many2one("education.group")


class Group(models.Model):
    _name = "education.groups"
    _description = "Groups"

    name = fields.Char(string="Name", required=True)
    subject_id = fields.Many2one(comodel_name="education.subjects")
    teacher_ids = fields.Many2many("users.teacher")
    support_teacher_ids = fields.Many2one('users.teacher' ,compute="_compute_support_teacher")
    student_ids = fields.One2many("education.group_student", inverse_name="group_id")
    status = fields.Selection(
    [
        ('draft', "Yangi"),
        ('active', "Faol"),
        ('finished', "Yakunlangan"),
        ('cancel', "Bekor qilingan")
    ],
    default='draft'
    )
    schedule_ids = fields.One2many("education.schedule", "group_id", string="Schedule")
    room_id = fields.Many2one("building.room")
    branch_id = fields.Many2one("res.company", required=True, string="Branch")
    max_capacity = fields.Integer(default=20)
    # payment_ids = fields.One2many("payment.course_fee", "group_id")
    notes = fields.Text(string="Notes")
    #Compute
    # remaining_seats = fields.Integer(string="remaining seats", compute="_compute_remaining_seats")





    

