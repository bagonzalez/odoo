from odoo import models, fields

class ResPartner(models.Model):
    _inherit = ['res.partner']

    credit_request_ids = fields.One2many(
        'credit.request',  # Modelo relacionado
        'partner_id',      # Campo Many2one en el modelo relacionado
        string='Credit Requests'
    )