from odoo import fields, models, api


class Students(models.Model):
    _name = "users.students"

    _inherits = {"res.users": "user_id"}

    user_id = fields.Many2one(comodel_name="res.users", string="User", required=True, ondelete="cascade")
    branch_ids = fields.Many2many(comodel_name="res.company", compute="_compute_branch_ids")
    balance = fields.Float(string="Balance", default=0)

    @api.model_create_multi
    def create(self, vals_list):
            records = super().create(vals_list)
            for record in records:
                if record.user_id:
                    record.user_id.user_type = "student"
            return records
        






