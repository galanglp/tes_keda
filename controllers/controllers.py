# -*- coding: utf-8 -*-
from odoo import http


class Kedatech(http.Controller):
    @http.route('/kedatech/kedatech', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/kedatech/kedatech/objects', auth='public')
    def list(self, **kw):
        return http.request.render('kedatech.listing', {
            'root': '/kedatech/kedatech',
            'objects': http.request.env['kedatech.kedatech'].search([]),
        })

    @http.route('/kedatech/kedatech/objects/<model("kedatech.kedatech"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('kedatech.object', {
            'object': obj
        })
