from odoo import fields, models, api

class Accountant(models.Model):
    _name = "users.accountant"
    _description = "Accountant"
    _inherits  = {"res.users": "user_id"}

    user_id = fields.Many2one("res.users", string="User", required=True, ondelete="cascade")

    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)
        for record in records:
            if record.user_id:
                record.user_id.user_type = "accountant"
        return records