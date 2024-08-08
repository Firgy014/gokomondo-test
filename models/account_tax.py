from odoo import models, fields, api

class AccountTaxInherited(models.Model):
    _inherit = 'account.tax'

    business_model = fields.Selection([
        ('retail', 'Retail'),
        ('corporate', 'Corporate'),
        ('subscription', 'Subscription')
    ], string='Business Model', required=True)