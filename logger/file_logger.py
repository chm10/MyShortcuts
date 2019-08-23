import usuario
import logging
import os

# Construindo Logger 
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

#Criando um adaptador
logfile = os.path.join(os.path.dirname(os.path.realpath(__file__)),"usuario.log")
handler = logging.FileHandler(logfile)
handler.setLevel(logging.INFO)

# Formatar o log
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Anexar o log ao adaptador
logger.addHandler(handler)

user = usuario.Usuario('EUR',logger)
user.depositar(100.0)
user.depositar('20.0')
user.sacar(4000.0)
user.sacar(30.0)
logger.warning('Total de dinheiro eh: {}'.format(user.extrato))