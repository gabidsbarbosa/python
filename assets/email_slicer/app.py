# coletar email do usuário
# dividir o email usando @, salvando a primeira parte como nome
# do usuário e a segunda parte salva como domínio
# separar o domínio usando '.'

def main():
    print("seja bem-vindo ao separador de e-mail")
    print("")

    email_input = input("insira seu endereço de e-mail: ")

    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")

    print("Usuário: ", username)
    print("Domínio: ", domain)
    print("Extensão: ", extension)

main()