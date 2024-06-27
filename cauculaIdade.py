
while(True):
  try:
    mensagemNome = "Insira seu nome completo:\n"
    print(mensagemNome)
    nome = input()

    mensagemAnoNascimento = "Insira o ano do seu nascimento:\n"
    print(mensagemAnoNascimento)
    ano = int(input())

    if(ano < 1922) or (ano > 2021):
      raise Exception("Data informada inválida")      

    print(f"\nO usuário {nome} completará {-(ano - 2022)} anos em 2022")
    
    break;

  except:
    print("Existem dados inconsistentes, favor informe novamente")
