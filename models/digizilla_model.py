from odoo import models, fields, api

class DigizillaTest(models.Model):
    _name="digizilla.test"
    
    name = fields.Char(string='Name')
    gender = fields.Selection([ ('male', 'male'),('female', 'female')], defualt= 'male')
    joining_date = fields.Date()
    comments = fields.Char(string='Comments')
    notes = fields.Text(string='Notes')
    tags = fields.Selection([ ('tag1', 'one'),('tag2', 'two')], defualt= 'one', string='Tags')
    
    country = fields.Many2one('res.country', string='Country')
    
    customers_ids = fields.Many2many('res.partner', string='Customers')
    company_id = fields.Many2one('res.company', string='Company')
    
    digizilla_logs = fields.One2many(comodel_name="digizilla.log", inverse_name="logs_id")
    
    
    _sql_constraints = [
        ( 'name' ,'UNIQUE(name)' ,'name has to be Unique') ,
    ]
    
    
    
    
    @api.onchange('name', 'gender', 'joining_date', 'comments', 
                  'notes', 'country', 'tags', 'customers_ids', 'company_id')
    def fields_changed(self):
        logs = {
                'massage': 'changes happened',
                'logs_id': self.id
            }

        self.env['digizilla.log'].create(logs)
            