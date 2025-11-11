from odoo import fields, models, api

class EducationLesson(models.Model):
    _name = "education.lesson"
    _description = "Lesson"

    name = fields.Char(string="Name", required=True) #Bu dars nomi boladi, masalan 'modellar bilan ishlash'
    group_id = fields.Many2one('education.groups', string="Group")
    schedule_id = fields.Many2one('education.schedule', compute="_compute_schedule") #Qaysi dars bo'lgani belgilanadi
    homework_id = fields.Many2one('education.homework')

    def _compute_schedule(self):
        self.schedule_id = None

    def button_homework_wizard(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Vazifa yaratish',
            'res_model': 'education.homework',
            'view_mode': 'form',
            'target': 'new',  
            'context': {
                'default_lesson_id': self.id,
                'default_group_id': self.group_id.id,
            },
        }

