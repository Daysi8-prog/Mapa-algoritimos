"""Untitled1.pynb"""

import time
senha_mestre="2403"
while True:
  tentativa = input("confirme a senha")
  if tentativa == senha_mestre:
    print("acesso aprovado! bom treino")
  else:
    print("acesso negado! tente novamente")
    time.sleep(5)
    print("tente novamente agora")
