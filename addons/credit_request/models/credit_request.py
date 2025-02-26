from odoo import models, fields

class CreditRequest(models.Model):
    _name = 'credit.request'
    _description = 'Credit Request'

    partner_id = fields.Many2one(
        'res.partner',  # Modelo relacionado
        string='Contact',
        required=True
    )
    amount = fields.Float(string='Credit Amount', required=True)
    request_date = fields.Date(string='Request Date', default=fields.Date.today, required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ], string='Status', default='draft', required=True)