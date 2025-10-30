from odoo import fields, models, api


class CEO(models.Model):
    _name = "users.ceo"
    _description = "CEO"
    _inherits = {"res.users": "user_id"}

    user_id = fields.Many2one("res.users", string="User", required=True, ondelete="cascade")

    @api.model_create_multi
    def create(self, vals_list):
            records = super().create(vals_list)
            for record in records:
                if record.user_id:
                    record.user_id.user_type = "teacher"
            return records
