#!/usr/bin/env

import logging
import usuario

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

user = usuario.Usuario('EUR',logger)
user.depositar(100.0)
user.depositar('20.0')
user.sacar(4000.0)
user.sacar(30.0)
logger.warning('Total de dinheiro eh: {}'.format(user.extrato))

