from odoo import fields, models, api

class Material(models.Model):
    _name = "invetory.material"
    _description = "Educational Material"

    name = fields.Char(string="Title", required=True)
    type = fields.Selection([
        ('file', "File"),
        ('book', "Book"),
        ('other', "Book"),

    ], default="file")

    description = fields.Text()
    subject_id = fields.Many2one("education.subject", string="Subject")
    uploaded_by = fields.Many2one("res.users", string="Uploaded By")
    upload_date = fields.Datetime(default=fields.Datetime.now)
