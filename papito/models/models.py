# -*- coding: utf-8 -*-

from odoo import models, fields, api


class city(models.Model):
    _name = 'papito.city'
    name = fields.Char()
    description = fields.Text()
    ubication = fields.Char(String="Ubication")
    country = fields.Many2one("res.country", "Pais")
    hotelList = fields.One2many("papito.hotel","Hotel")

    class hotel(models.Model):
        _name = 'papito.hotel'
        name = fields.Char()
        galeriaFotos = fields.Binary()
        description=fields.Text()
        listaHabitaciones=fields.Many2one("papito.habitacion","Lista Habitaciones")
        valoraciones=fields.Integer()
        listaServicios=fields.Many2one("papito.reserva","Lista Reservas")

    class habitacion(models.Model):
        _name = 'papito.habitacion'
        hotel = fields.Many2one("papito.hotel", "Hotel")
        name = fields.Char()
        camas = fields.Text()
        fotos=fields.Text()
        precios=fields.Integer()
        descripcion=fields.Text()

    class reserva(models.Model):
        _name = 'papito.reserva'
        fe  cha=fields.Date()
        habitaciones=fields.Many2one("papito.habitacion", "Habitacion a reservar")


