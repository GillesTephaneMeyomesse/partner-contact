# Copyright 2021 ForgeFlow, S.L.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    @api.model
    def create(self, vals):
        res = super().create(vals)
        if res:
            partners = res.partner_id | res.partner_id.commercial_partner_id
            partners._increase_rank("supplier_rank")
        return res
