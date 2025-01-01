from odoo import fields, models


class Ticket(models.Model):
    _name = "todo.ticket"
    _description = "Ticket"

    name = fields.Char()
    number = fields.Integer()
    tag = fields.Char()
    # state = fields.Selection([
    #     ('new', 'New'),
    #     ('doing', 'Doing'),
    #     ('done', 'Done'),
    # ])
    state = fields.Selection([
        ('new', 'New'),
        ('doing_edt', 'Doing_Edt'),
        ('done', 'Done')],
    )

    file = fields.Char()
    description = fields.Text()

    def action_new(self):
        for rec in self:
            rec.state = 'new'

    def action_doing_edt(self):
        for rec in self:
            rec.state = 'doing_edt'

    def action_done(self):
        for rec in self:
            rec.state = 'done'
