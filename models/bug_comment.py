from odoo import models, fields

class BugComment(models.Model):
    _name = "bug.comment"
    _description = "Bug Comment"

    bug_id = fields.Many2one("bug.tracker", string="Bug", ondelete="cascade")

    user_id = fields.Many2one(
        "res.users",
        string="Commented By",
        default=lambda self: self.env.user
    )

    comment = fields.Text(required=True)
