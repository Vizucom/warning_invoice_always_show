# -*- coding: utf-8 -*-
from openerp import models, fields, api, _


class AccountInvoice(models.Model):

    _inherit = 'account.invoice'

    @api.one
    def _get_partner_invoice_warn_msg(self):
        if self.partner_id.invoice_warn in ['warning', 'block']:
            self.partner_invoice_warn_msg = self.partner_id.invoice_warn_msg
        else:
            self.partner_invoice_warn_msg = False

    partner_invoice_warn_msg = fields.Text(compute='_get_partner_invoice_warn_msg', readonly=True, string='Invoice Warning')
