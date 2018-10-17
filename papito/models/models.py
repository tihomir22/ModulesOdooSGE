# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.fields import One2many, Many2many


class city(models.Model):
    _name = 'papito.city'
    name = fields.Char()
    description = fields.Text()
    ubication = fields.Char(String="Ubication")
    country = fields.Many2one("res.country", "Pais")
    hotellist = fields.Many2many("papito.hotel")

    class hotel(models.Model):
        _name = 'papito.hotel'
        name = fields.Char()
        galeriaFotos = Many2many("papito.fotos")
        description=fields.Text()
        roomlist=fields.Many2many("papito.habitacion")
        valoraciones=fields.Integer()
        listaServicios=fields.Many2many("papito.reserva")

    class habitacion(models.Model):
        _name = 'papito.habitacion'
        hotel = fields.Many2many("papito.hotel", "Hotel")
        name = fields.Char()
        camas = fields.Integer()
        fotos=Many2many("papito.fotos")
        precios=fields.Integer()
        descripcion=fields.Text()

    class reserva(models.Model):
        _name = 'papito.reserva'
        fechaInicio=fields.Date()
        fechaFinal = fields.Date()
        habitaciones=fields.Many2one("papito.habitacion", "Habitacion a reservar")

    class fotos(models.Model):
        _name = 'papito.fotos'
        name=fields.Char("Nombre de la foto")
        foto=fields.Binary("Seleccione una foto para agregar")



