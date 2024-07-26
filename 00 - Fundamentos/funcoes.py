deposito = 0
extrato = ''

def funcao_deposito(deposito, extrato):
    deposito += 50
    extrato += "teste"
    return deposito,extrato

deposito,extrato = funcao_deposito(deposito,extrato)
#print(novo_deposito)
print(deposito)
print(extrato)
usuarios = [{'Nome': '1', 'Data de nascimento': '1', 'CPF': 1, 'Endereço': '1, 1, 1, 1/1'}, {'Nome': '2', 'Data de nascimento': '2', 'CPF': 2, 'Endereço': '2, 2, 2, 2/2'}, {'Nome': '3', 'Data de nascimento': '3', 'CPF': 3, 'Endereço': '3, 3, 3, 3/3'}]
def criar_usuario():
    novo_usuario = {}
    novo_usuario["Nome"] = input('Nome: ')
    novo_usuario["Data de nascimento"] = input('Data de nascimento (dd/mm/aaaa): ')
    novo_usuario["CPF"] = int(input("CPF: "))
    print("Endereço completo")
    novo_usuario["Endereço"] = input("Logradouro: ") + ', ' + input("Número: ") + ', ' + input("Bairro: ") + ', ' + input("Cidade: ") + "/" + input("UF: ")
    usuarios.append(novo_usuario)
    return usuarios

for usuario in usuarios:
    print(f'CPF: {usuario['CPF']}\nCliente: {usuario['Nome']}\n\n')

    