import logging
from odoo import models, fields, api

# Setup logger
_logger = logging.getLogger(__name__)

class SaleOrderInherited(models.Model):
    _inherit = 'sale.order'

    business_model = fields.Selection([
        ('retail', 'Retail'),
        ('corporate', 'Corporate'),
        ('subscription', 'Subscription')
    ], string='Business Model', required=True)

    display_name = fields.Char(string='Display Name', compute='_compute_display_name', store=True)

    @api.depends('name', 'business_model')
    def _compute_display_name(self):
        for order in self:
            business_model_short = {
                'retail': 'RT',
                'corporate': 'CORP',
                'subscription': 'SUB'
            }.get(order.business_model, '')
            if business_model_short:
                order.display_name = f"[{business_model_short}] - {order.name}"
            else:
                order.display_name = order.name

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    business_model = fields.Selection(related='order_id.business_model', store=True, readonly=True)
    
    # tax_id = fields.Many2many('account.tax', string='Taxes', compute='_compute_tax_ids', store=True)

    # @api.depends('order_id.business_model', 'tax_id')
    # def _compute_tax_ids(self):
    #     for line in self:
    #         if line.order_id.business_model:
    #             # Ambil semua pajak dan filter berdasarkan business_model
    #             all_taxes = self.env['account.tax'].sudo().search([])
    #             filtered_taxes = all_taxes.filtered(lambda tax: tax.business_model == line.order_id.business_model)
    #             line.tax_id = filtered_taxes
    #         else:
    #             line.tax_id = self.env['account.tax']