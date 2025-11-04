from odoo import fields, models, api


class Certifications(models.Model):
    _name = "users.certifications"
    _description = "Certifications"

    name = fields.Char(string="Name", required=True)
    degree = fields.Char(string="Degree")
    given_date = fields.Date(string="given date")
    validity_period = fields.Float(string="validity period", default=0, required=True) #Agar 0 bo'lsa amal qilish muddati cheksiz bo'ladi
    #Compute
    # end_date = fields.Date(string="end date", compute="_compute_end_date")


class Teacher(models.Model):
    _name = "users.teacher"
    _inherits = {"res.users": "user_id"}
    
    user_id = fields.Many2one("res.users", string="User", required=True, ondelete="cascade")
    branch_ids = fields.Many2many("res.company", string="Branch")
    certification_id = fields.Many2many(comodel_name="users.certifications", string="Certification")
    department_id = fields.Many2one(comodel_name="users.department", string="Department")
    postion = fields.Selection([('head_teacher', "Head Teacher"), ("teacher", "Teacher"), ("support_teacher", "Support teacher")])
    salary = fields.Float(string="Salary")
    work_schedule = fields.Selection([('full_time', "Full time"), ("part_time", "Part time"), ("hourly", "Hourly")])

    @api.model_create_multi
    def create(self, vals_list):
            records = super().create(vals_list)
            for record in records:
                if record.user_id:
                    record.user_id.user_type = "teacher"
            return records

        
  



   



