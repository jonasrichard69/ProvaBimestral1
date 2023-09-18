import time

total_vendas = 0
fila_atendimento = []
proxima_pessoa = None

#funcoes fila
def adicionar_a_fila(nome):
    fila_atendimento.append(nome)
    print(f"{nome} foi adicionado(a) na fila.")

def atender_fila():
    global proxima_pessoa

    if proxima_pessoa is None:
        if fila_atendimento:
            proxima_pessoa = fila_atendimento.pop(0)
            print(f"{proxima_pessoa}, seu café está sendo preparado.")
            time.sleep(5)
            print(f"Seu café está pronto, {proxima_pessoa}. Aproveite!")
        else:
            print("A fila está vazia. Ninguém está na fila para ser atendido.")
    elif proxima_pessoa:
        print(f"{proxima_pessoa}, seu café está sendo preparado.")
        time.sleep(5)
        print(f"Seu café está pronto, {proxima_pessoa}. Aproveite!")
        proxima_pessoa = None


def mostrar_fila():
    if fila_atendimento:
        print("Fila de atendimento:")
        for i, nome in enumerate(fila_atendimento, start=1):
            print(f"{i}. {nome}")
    else:
        print("A fila está vazia.")

#funcoes venda
def registrar_venda(produto, quantidade, preco):
    global total_vendas
    valor_venda = quantidade * preco
    total_vendas += valor_venda
    print(f"Venda registrada... {quantidade} x {produto} - Total: R${valor_venda}")

def mostrar_total_vendas():
    global total_vendas
    print(f"Total de vendas registradas: R${total_vendas:.2f}")


def vender_cafe():
    cafepreco = {
        "Expresso Forte": 10.00,
        "Café com Leite": 10.00,
        "Cappuccino": 10.00,
        "Café Mocha": 10.00,
        "Macchiato Caramelo": 10.00,
        "Café Preto": 10.00,
        "Café Latte": 10.00,
        "Café Expresso Duplo": 10.00,
        "Café Gelado": 10.00,
        "Café Expresso Puro": 10.00,
        "Café Descafeinado": 10.00,
        "Café com Leite de Amêndoa": 10.00,
        "Café Padrão": 10.00,
    }
    return cafepreco

def mostrar_lista(cafepreco):
    print("Lista de cafés: ")
    for cafe, preco in cafepreco.items():
        print(f"{cafe}: R${preco}")

#funcoes cafe do signo
def obter_data_aniversario():
    dia = int(input("Digite o dia do seu aniversário: "))
    mes = int(input("Digite o mês do seu aniversário: "))
    return dia, mes

def calcular_signo(dia, mes):
    signos = {
        (3, 21): ("Áries", "♈"),
        (4, 21): ("Touro", "♉"),
        (5, 21): ("Gêmeos", "♊"),
        (6, 21): ("Câncer", "♋"),
        (7, 23): ("Leão", "♌"),
        (8, 23): ("Virgem", "♍"),
        (9, 23): ("Libra", "♎"),
        (10, 23): ("Escorpião", "♏"),
        (11, 23): ("Sagitário", "♐"),
        (12, 22): ("Capricórnio", "♑"),
        (1, 20): ("Aquário", "♒"),
        (2, 19): ("Peixes", "♓")
    }

    for intervalo, (signo, simbolo) in signos.items():
        mes_inicio, dia_inicio = intervalo[0], intervalo[1]
        if (mes == mes_inicio and dia >= dia_inicio) or (mes == mes_inicio + 1 and dia <= dia_inicio):
            return signo, simbolo

    return "Signo não encontrado", ""

def sugerir_cafe(signo):
    cafepor = {
        "Áries": "Expresso Forte",
        "Touro": "Café com Leite",
        "Gêmeos": "Cappuccino",
        "Cêncer": "Café Mocha",
        "Leão": "Macchiato Caramelo",
        "Virgem": "Café Preto",
        "Libra": "Café Latte",
        "Escorpião": "Café Expresso Duplo",
        "Sagitário": "Café Gelado",
        "Capricórnio": "Café Expresso Puro",
        "Aquário": "Café Descafeinado",
        "Peixes": "Café com Leite de Amendoa",
    }

    return cafepor.get(signo, "Café Padrão")

def vender_cafe_s(signo):
    cafeprecos = {
        "Aries": 10.00,
        "Touro": 10.00,
        "Gemeos": 10.00,
        "Cancer": 10.00,
        "Leao": 10.00,
        "Virgem": 10.00,
        "Libra": 10.00,
        "Escorpiao": 10.00,
        "Sagitario": 10.00,
        "Capricornio": 10.00,
        "Aquario": 10.00,
        "Peixes": 10.00,
    }
    return cafeprecos.get(signo, 10.00)

#funcoes cafe do rock
def obter_estilo_musical():
    print("Escolha um estilo musical:")
    print("1. Rock")
    print("2. Sertanejo")
    print("3. Funk")
    print("4. Hip Hop")
    print("5. MPB")
    print("6. Samba")
    print("7. Eletrônica")
    print("8. Heavy Metal")
    print("9. Dance")
    print("10. Pop")
    print("11. Pagode")
    print("12. Blues")
    escolha = int(input("Digite o número correspondente ao estilo musical: "))
    
    estilos_m = {
        1: "Rock",
        2: "Sertanejo",
        3: "Funk",
        4: "Hip Hop",
        5: "MPB",
        6: "Samba",
        7: "Eletrônica",
        8: "Heavy Metal",
        9: "Dance",
        10: "Pop",
        11: "Pagode",
        12: "Blues"
    }
    
    return estilos_m.get(escolha, "Opção invalida")
   
def sugerir_cafem(estilo_musical):
    cafeporm = {
        "Rock": "Expresso Forte",
        "Sertanejo": "Café com Leite",
        "Funk": "Café Mocha",
        "Hip Hop": "Café Preto",
        "MPB": "Café Latte",
        "Samba": "Café Expresso Duplo",
        "Eletrônica": "Café Gelado",
        "Heavy Metal": "Café Expresso Puro",
        "Dance": "Café Descafeinado",
        "Pop": "Café com Leite de Amendoa",
        "Pagode": "Café de Baunilha",
        "Blues": "Café Irlandês"
    }

    return cafeporm.get(estilo_musical, "Café Padrão")
def vender_cafe_m(estilo_musical):
    
    precos_cafe = {
        "Expresso Forte": 10.00,
        "Café com Leite": 10.00,
        "Café Mocha": 10.00,
        "Café Preto": 10.00,
        "Café Latte": 10.00,
        "Café Expresso Duplo": 10.00,
        "Café Gelado": 10.00,
        "Café Expresso Puro": 10.00,
        "Café Descafeinado": 10.00,
        "Café com Leite de Amendoa": 10.00,
        "Café de Baunilha": 10.00,
        "Café Irlandês": 10.00,
        "Cafe": 10.00,
    }
    

    return precos_cafe.get(sugerir_cafem(estilo_musical), 10.00) 

#cafeporcurso
def obter_curso():
    print("Escolha um curso:")
    print("1. Administração")
    print("2. Arquitetura e Urbanismo")
    print("3. Biomedicina")
    print("4. Ciências Contábeis")
    print("5. Direito")
    print("6. Enfermagem")
    print("7. Engenharia Agronômica")
    print("8. Engenharia Civil")
    print("9. Engenharia de Software")
    print("10. Engenharia Elétrica")
    print("11. Engenharia Mecânica")
    print("12. Farmácia")
    print("13. Fisioterapia")
    print("14. Medicina")
    print("15. Medicina Veterinária")
    print("16. Nutrição")
    print("17. Odontologia")
    print("18. Psicologia")
    print("19. Publicidade e Propaganda")
    
    escolhac = int(input("Digite o número correspondente ao curso que você faz: "))
    
    cursosc = {
        1: "Administração",
        2: "Arquitetura e Urbanismo",
        3: "Biomedicina",
        4: "Ciências Contábeis",
        5: "Direito",
        6: "Enfermagem",
        7: "Engenharia Agronômica",
        8: "Engenharia Civil",
        9: "Engenharia de Software",
        10: "Engenharia Elétrica",
        11: "Engenharia Mecânica",
        12: "Farmácia",
        13: "Fisioterapia",
        14: "Medicina",
        15: "Medicina Veterinária",
        16: "Nutrição",
        17: "Odontologia",
        18: "Psicologia",
        19: "Publicidade e Propaganda",
    }
    
    return cursosc.get(escolhac, "Opção inválida")

def sugerir_cafec(cursos):
    cafeporc = {
        "Admistração":"Café Friamente Calculado",
        "Arquitetura e Urbanismo":"Café Estruturado",
        "Biomedicina":"Café Microgrãos",
        "Ciências Contábeis":"Café Barato",
        "Direito":"Nigrum Capulus",
        "Enfermagem":"Café Vacinado",
        "Engenharia Agronômica":"Café com Terra",
        "Engenharia Civil":"Café Caseiro",
        "Engenharia de Software":"O Melhor Café da Casa",
        "Engenharia Elétrica":"Café Queimado",
        "Engenharia Mecânica":"Café com Óleo",
        "Farmácia":"Café com Paracetamol",
        "Fisioterapia":"Café com Torta",
        "Medicina":"Café com Nutella",
        "Medicina Veterinária":"Café Vegano",
        "Nutrição":"Café Descafeinado com Adoçante e Leite de Amêndoas",
        "Odontologia":"Leite",
        "Psicologia":"Café com Florais de Bach",
        "Publicidade e Propaganda":"Café Starbucks",
        
        
    }

    return cafeporc.get(cursos, "Café Padrão")

while True:
    print("Bem-vindo ao La Coffee:")
    print("O que deseja fazer hoje?")
    print("Entrar na fila - Digite 6 // Ser atendido - Digite 7 // Sair - Digite 8 // ver total de vendas - Digite 9")
    

    opcao = int(input("Digite: "))

    if opcao == 6:
        nome = input("Digite o seu nome: ")
        adicionar_a_fila(nome)
        if proxima_pessoa is None:
            proxima_pessoa = nome
        print("Aguarde a sua vez para ser atendido.")

    elif opcao == 7:
        if proxima_pessoa is not None:
            nome_atendimento = input("Digite o seu nome: ")
            if nome_atendimento == proxima_pessoa:
                print("O que deseja fazer? ")
                print("Comprar café - 1// Comprar café por sugestão - 2")
                opcao = int(input("Digite: "))

                if opcao == 1:
                    lista_cafes = vender_cafe()
                    mostrar_lista(lista_cafes)
                    escolha_cafe = input("Qual café deseja comprar? ")
                    if escolha_cafe in lista_cafes:
                        preco_cafe = lista_cafes[escolha_cafe]
                        quantidade = int(input(f"Quantos {escolha_cafe} você deseja comprar? "))
                        if quantidade > 0:
                            preco_total = preco_cafe * quantidade
                            print(f"Você escolheu {quantidade} {escolha_cafe} - Preço: R${preco_cafe} - Preço total a pagar: R${preco_total}")
                            print("Deseja confirmar a compra?")
                            confirmar = input("Sim ou Não: s/n ")
                            if confirmar == "s":
                                atender_fila()
                                time.sleep(3)
                                registrar_venda(escolha_cafe, quantidade, preco_cafe)
                            elif confirmar == "Não":
                                print("Vai se fuder então.")
                        else:
                            print("Quantidade inválida.")
                    else:
                        print("Café não encontrado na lista.")

                elif opcao == 2:
                    print("Sugestão pelo que gostaria? ")
                    print("Signo - 1// Estilo musical - 2// Curso superior - 3")
                    opcao2 = int(input("Digite: "))
            #escolhas 2 ====================================
                    if opcao2 == 1:
                        dia, mes = obter_data_aniversario()
                        signo, simbolo = calcular_signo(dia, mes)
                        cafe_recomendado = sugerir_cafe(signo)
                        print(f"Para você que é de {simbolo} {signo}, recomendamos o {cafe_recomendado}")
                        print("Deseja confirmar a compra?")
                        confirmar = input("Sim ou Não: s/n ")
                        if confirmar == "s":
                            atender_fila()
                            preco_cafe_recomendado = vender_cafe_s(signo)
                            registrar_venda(cafe_recomendado, 1, preco_cafe_recomendado)
                            
                        else:
                            print("Vai se fuder então.")
                    elif opcao2 == 2:
                        estilo_musical = obter_estilo_musical()
                        cafe_recomendado = sugerir_cafem(estilo_musical)
                        print(f"Para voce que curte um {estilo_musical}, recomendamos o {cafe_recomendado}")
                        print("Deseja confirmar a compra?")
                        confirmar = input("Sim ou Não: s/n ")
                        if confirmar == "s":
                            atender_fila()
                            preco_cafe_rec = vender_cafe_m(estilo_musical)
                            registrar_venda(cafe_recomendado, 1, preco_cafe_rec)
                        
                        else:
                            print("Vai se fuder então")
                        
                    elif opcao2 == 3:
                        print("Bem-vindo à recomendação de café para estudantes!")
                        cursoc = obter_curso()
                        cafe_recomendadoc = sugerir_cafec(cursoc)

                        print(f"Para você que é do curso de {cursoc}, recomendamos o {cafe_recomendadoc}")
                        print("Deseja confirmar a compra?")
                        confirmar = input("Sim ou Não: s/n ").lower()
                        if confirmar == "s":
                            atender_fila()
                            preco_cafe_rec = 10.00  
                            registrar_venda(cafe_recomendadoc, 1, preco_cafe_rec)
                        else:
                            print("Vai se fuder então")

                        
                        

                
            else:
                posicao_na_fila = fila_atendimento.index(proxima_pessoa) + 1
                print(f"Você não é {proxima_pessoa}. {proxima_pessoa} está na frente da fila. Você está na posição {posicao_na_fila}. Aguarde sua vez.")
        else:
            print("A fila está vazia. Ninguém está na fila para ser atendido.")

    elif opcao == 8:
        print("Obrigado por visitar o La Coffee. Volte sempre!")
        break  

    elif opcao == 9:
        mostrar_total_vendas()

    else:
        print("Opção inválida")
