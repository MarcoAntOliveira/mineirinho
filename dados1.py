from dados import postos_de_gasolina
import pandas as pd
from random import random

def calcular_dados_posteriores(postos_de_gasolina, meses_futuros):
  """
  Calcula os dados de venda de pão de queijo para os meses futuros com base nos dados dos meses anteriores.

  Args:
      postos_de_gasolina (dict): Dicionário com dados de venda de pão de queijo em postos de gasolina.
      meses_futuros (int): Número de meses futuros para os quais os dados serão calculados.

  Returns:
      dict: Dicionário com os dados de venda de pão de queijo para os meses futuros.
  """

  dados_posteriores = {}

  for posto in postos_de_gasolina:
    dados_posto = postos_de_gasolina[posto]
    lista_keys = list(dados_posto.keys())
    ultimo_mes = lista_keys[-1]
    ultimo_dados = dict(dados_posto[ultimo_mes].get("Pão de queijo"))
   
    
    for mes in range(1, meses_futuros + 1):
      mes_futuro = f"{ultimo_mes} {mes+1}" if mes == 1 else f"{ultimo_mes} +{mes}"
      dados_posteriores.setdefault(posto, {})[mes_futuro] = {
          "Unidades vendidas": int(ultimo_dados["Unidades vendidas"] * (1.05 + 0.01 *random())),
          "Preço médio": ultimo_dados["Preço médio"] * (1.02 + 0.01 * random()),
      }

  return dados_posteriores

dados_posteriores = calcular_dados_posteriores(postos_de_gasolina, 3)

# Exibir dados de Março para o Posto 1
try:
    print(dados_posteriores["Posto 1"]["Março"])
except KeyError :  
    print ("chave nao encontrada")




#posto1 = postos_de_gasolina["Posto 1"]

#for mes in posto1:
#   print(posto1[mes]['Pão de queijo']['Preço médio'])