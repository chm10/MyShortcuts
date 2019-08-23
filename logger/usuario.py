#!/usr/bin/env python3

import uuid

class Usuario:
    def __init__(self, dinheiro, logger):
        self.id = uuid.uuid4()
        self.dinheiro = dinheiro
        self.logger = logger
        self.extrato = 0.0
        self.logger.info('Criou um usuario vazio: {}'.format(self.id))

    def depositar(self, dinheiro):
        try:
            assert isinstance(dinheiro, float), "Dinheiro deve ser decimal"
            assert dinheiro > 0.0,"Dinheiro deve ser nao negativo"
            self.extrato += dinheiro
        except AssertionError as e:
            self.logger.error("Usuario {}: {}".format(self.id,e))
    
    def sacar(self, dinheiro):
        try:
            assert isinstance(dinheiro,float),"Dinheiro deve ser decimal"
            assert dinheiro > 0.0,"Dinheiro deve ser nao negativo"
            self.extrato -= dinheiro
        except AssertionError as e:
            self.logger.error("Usuario {}: {}".format(
                self.id,e))
