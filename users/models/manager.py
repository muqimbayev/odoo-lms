from odoo import fields, models, api

class Manager(models.Model):
    _name = "users.manager"
    _description = "Manager"
    _inherits = {"res.users": "user_id"}

    user_id = fields.Many2one("res.users", string="User", required=True, ondelete="cascade")
    branch_id = fields.One2many("res.company", inverse_name="manager_id", string="Filial", required=True)

    @api.model_create_multi
    def create(self, vals_list):
            records = super().create(vals_list)
            for record in records:
                if record.user_id:
                    record.user_id.user_type = "manager"
            return records