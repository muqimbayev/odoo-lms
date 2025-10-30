from odoo import models, fields


class WorkPlaces(models.Model):
    _name = "users.work_places"
    _description = "Work Places"

    name = fields.Char(string="Name", required=True)


class LmsLanguage(models.Model):
    _name = "users.language"
    _description = "Language"

    name = fields.Char(string="Name", required=True)
    active = fields.Boolean(default=True)


class ResUsers(models.Model):
    _inherit = "res.users"

    experience_year = fields.Float(string="Experience Years", default=0.0)
    work_places = fields.Many2many("users.work_places")
    passport_id = fields.Char(string="Passport ID")
    languages = fields.Many2many(comodel_name="users.language", string="Languages")
    marital_status = fields.Selection(
        [
            ('married', "Married"),
            ('not_married', "Single"),
            ('divorced', "Divorced")
        ],
        string="Marital Status",
        default="not_married"
    )
    children_count = fields.Integer(string="Children Count", default=0)
    telegram_id = fields.Char(string="Telegram ID")
    user_type = fields.Selection([
        ("teacher", "Teacher"),
        ("student", "Student"),
        ("hr", "HR"),
        ("ceo", "CEO"),
        ("Manager", "Manager"),
        ("operator", "Operator"),
        ("accountant", "Accountant")
    ])
