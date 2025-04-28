import pandas as pd

def checkidade(idade):
    if idade >= 18:
        print('Bem vindo ao site')
    else:
        print('Você não possui a idade mínima para utilizar o site')


def checkemail(email):
    return '@' in email and '.' in email


try:
    df = pd.read_csv('users.csv')
except FileNotFoundError:
    df = pd.DataFrame(columns=['Nome', 'Email', 'Idade'])

print(df)

def insert(nome, email, idade):
    return {'Nome': nome, 'Email': email, 'Idade': idade}

num = int(input('Quantos users serão cadastrados: '))

for i in range(num):
    nome = input('Nome: ')
    email = input('Email: ')
    idade = input('Idade: ')

    checkidade(idade)

    checkemail(email)

    user = insert(nome, email, idade)

    df = pd.concat([df, pd.DataFrame([user])], ignore_index=True)


df.to_csv('users.csv', index=False)
print(df)
