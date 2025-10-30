from odoo import fields, models


class Category(models.Model):
    _name = "education.category"

    name = fields.Char(string="Category", required=True)
    subject_ids = fields.One2many("education.subjects", inverse_name="category_id")