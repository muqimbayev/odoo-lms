from odoo import fields, models, api


class Operator(models.Model):
    _name = "users.operator"
    _inherits = {"res.users": "user_id"}

    user_id = fields.Many2one(comodel_name="res.users", string="User", required=True, ondelete="cascade")
    branch_id = fields.Many2many("res.company", required=True, string="Branch")
    
    @api.model_create_multi
    def create(self, vals_list):
            records = super().create(vals_list)
            for record in records:
                if record.user_id:
                    record.user_id.user_type = "operator"
            return records