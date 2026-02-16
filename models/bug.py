from odoo import models, fields
from odoo.exceptions import UserError

class BugTracker(models.Model):
    _name = "bug.tracker"
    _description = "Bug Tracker"
    _order = "create_date desc"

    name = fields.Char(string="Title", required=True)
    description = fields.Text()

    project_id = fields.Many2one("project.project", string="Project")
    developer_id = fields.Many2one("res.users", string="Assigned Developer")

    tag_ids = fields.Many2many("project.tags", string="Tags")

    comment_ids = fields.One2many("bug.comment", "bug_id", string="Comments")

    state = fields.Selection([
        ("new", "New"),
        ("assigned", "Assigned"),
        ("progress", "In Progress"),
        ("done", "Done"),
        ("closed", "Closed"),
    ], default="new")

    def action_assign(self):
        for rec in self:
            if not rec.developer_id:
                raise UserError("Assign a developer first.")
            rec.state = "assigned"

    def action_start(self):
        self.state = "progress"

    def action_done(self):
        self.state = "done"

    def action_close(self):
        for rec in self:
            if rec.state != "done":
                raise UserError("Bug must be Done before closing.")
            rec.state = "closed"
