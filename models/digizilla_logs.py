from odoo import models, fields

class DigizillaLog(models.Model):
    _name = "digizilla.log"

    massage = fields.Text()

    logs_id = fields.Many2one("digizilla.test")
    