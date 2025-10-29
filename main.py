import os

def limpa():
    """Função para limpar a tela do terminal"""
    # Para Windows
    if os.name == 'nt':
        os.system('cls')
    # Para Linux/Mac
    else:
        os.system('clear')

def exibir_apresentacao(): 
    """Função para apresentar a IA"""
    print("=" * 50)
    print("🌟  Olá! Eu sou a TôNaModa! 🌟")
    print("Sua assistente pessoal de moda e estilo!")
    print("Estou aqui para te ajudar com dicas de moda,")
    print("tendências e muito mais!")
    print("=" * 50)
    print()

def exibir_menu():
    """Função para exibir o menu de opções"""
    print("📋 O que você gostaria de saber sobre moda?")
    print()
    print("1. Quais são as tendências de moda para 2025?")
    print("2. Como combinar cores na roupa?")
    print("3. Qual o tipo de roupa ideal para cada ocasião?")
    print("4. Como montar um guarda-roupa básico?")
    print("5. Quais acessórios estão em alta?")
    print("6. Como adaptar meu estilo para o trabalho sem perder a personalidade?")
    print("7. Como usar um blazer de forma moderna?")
    print("8. Qual a diferença entre tons neutros e terrosos?")
    print("9. O que vestir em uma entrevista de emprego?")
    print("10. Como equilibrar maquiagem e roupa no mesmo visual?")
    print()

def resposta_tendencias():
    """Responde sobre tendências de moda 2025"""
    print("✨ TENDÊNCIAS DE MODA 2025:")
    print("• Cores vibrantes como verde limão e rosa choque")
    print("• Estilo oversized e confortável")
    print("• Sustentabilidade e moda consciente")
    print("• Mix de texturas: couro, seda e tricô")
    print("• Acessórios statement (brincos grandes, bolsas coloridas)")
    print()

def resposta_cores():
    """Responde sobre combinação de cores"""
    print("🎨 COMO COMBINAR CORES:")
    print("• Cores neutras (preto, branco, bege) combinam com tudo")
    print("• Use a regra do círculo cromático: cores complementares")
    print("• Máximo 3 cores por look")
    print("• Azul marinho + branco = clássico atemporal")
    print("• Para iniciantes: tons da mesma família de cores")
    print()

def resposta_ocasioes():
    """Responde sobre roupas para ocasiões"""
    print("👔 ROUPAS PARA CADA OCASIÃO:")
    print("• TRABALHO: Blazer, calça social, camisa/blusa")
    print("• CASUAL: Jeans, camiseta, tênis confortável")
    print("• FESTA: Vestido/terno, sapato social, acessórios")
    print("• ESPORTE: Roupas técnicas, tênis apropriado")
    print("• PRAIA: Roupas leves, proteção solar, chinelos")
    print()

def resposta_guarda_roupa():
    """Responde sobre guarda-roupa básico"""
    print("👗 GUARDA-ROUPA BÁSICO ESSENCIAL:")
    print("• 3 camisetas básicas (branca, preta, colorida)")
    print("• 2 calças jeans (uma escura, uma clara)")
    print("• 1 blazer neutro")
    print("• 1 vestido versátil")
    print("• 2 pares de sapatos (casual e social)")
    print("• Acessórios básicos: cinto, bolsa, relógio")
    print()

def resposta_acessorios():
    """Responde sobre acessórios em alta"""
    print("💎 ACESSÓRIOS EM ALTA:")
    print("• Brincos grandes e chamativos")
    print("• Bolsas pequenas e coloridas")
    print("• Óculos de sol com armação diferenciada")
    print("• Cintos statement")
    print("• Lenços e bandanas")
    print("• Relógios minimalistas")
    print()

def resposta_estilo_trabalho():
    """Responde sobre adaptar estilo para o trabalho"""
    print("👔 ESTILO NO TRABALHO COM PERSONALIDADE:")
    print("• Use acessórios sutis que reflitam seu gosto pessoal")
    print("• Escolha cores que você ama dentro da paleta profissional")
    print("• Adicione detalhes únicos: lenço, broche ou sapato colorido")
    print("• Misture peças clássicas com toques modernos")
    print("• Mantenha o corte das roupas adequado ao dress code")
    print("• Aposte em estampas discretas se gostar de padrões")
    print()

def resposta_blazer_moderno():
    """Responde sobre como usar blazer de forma moderna"""
    print("✨ BLAZER MODERNO:")
    print("• Use oversized para um visual mais atual")
    print("• Combine com jeans para um look casual chique")
    print("• Arregace as mangas para um toque despojado")
    print("• Use aberto sobre camiseta básica ou top")
    print("• Experimente cores diferentes do tradicional preto/azul")
    print("• Combine com tênis para modernizar o visual")
    print()

def resposta_tons_neutros():
    """Responde sobre tons neutros vs terrosos"""
    print("🎨 NEUTROS VS TERROSOS:")
    print("• NEUTROS: preto, branco, cinza, bege, nude")
    print("• TERROSOS: marrom, caramelo, terracota, mostarda, verde oliva")
    print("• Neutros são mais versáteis e atemporais")
    print("• Terrosos trazem aconchego e conexão com a natureza")
    print("• Ambos são fáceis de combinar entre si")
    print("• Use terrosos no outono/inverno e neutros o ano todo")
    print()

def resposta_entrevista():
    """Responde sobre o que vestir em entrevista"""
    print("💼 LOOK PARA ENTREVISTA:")
    print("• Sempre opte pelo mais formal que o dress code da empresa")
    print("• CLÁSSICO: terno ou blazer + calça social + camisa")
    print("• Cores seguras: azul marinho, preto, cinza ou bege")
    print("• Evite decotes, transparências ou roupas muito justas")
    print("• Sapatos fechados e bem cuidados são essenciais")
    print("• Acessórios discretos: relógio simples, brincos pequenos")
    print()

def resposta_maquiagem_roupa():
    """Responde sobre equilibrar maquiagem e roupa"""
    print("💄 EQUILIBRANDO MAKE E ROUPA:")
    print("• REGRA GERAL: destaque uma coisa por vez")
    print("• Roupa neutra = pode ousar mais na maquiagem")
    print("• Look colorido/estampado = maquiagem mais natural")
    print("• Para o dia: base leve + um ponto focal (olho OU boca)")
    print("• Para a noite: pode intensificar ambos com moderação")
    print("• Considere a ocasião: trabalho pede discrição")
    print()

def main():
    """Função principal da TôNaModa"""
    exibir_apresentacao()
    
    # Estrutura de repetição - A IA continua funcionando até o usuário pedir para sair
    while True:
        exibir_menu()
        opcao = input("Digite sua escolha (1-10): ").strip()
        
        # Estrutura condicional para processar a resposta
        if opcao == "1":
            limpa()
            resposta_tendencias()
            
        elif opcao == "2":
            limpa()
            resposta_cores()
            
        elif opcao == "3":
            limpa()
            resposta_ocasioes()
            
        elif opcao == "4":
            limpa()
            resposta_guarda_roupa()
            
        elif opcao == "5":
            limpa()
            resposta_acessorios()
            
        elif opcao == "6":
            limpa()
            resposta_estilo_trabalho()
            
        elif opcao == "7":
            limpa()
            resposta_blazer_moderno()
            
        elif opcao == "8":
            limpa()
            resposta_tons_neutros()
            
        elif opcao == "9":
            limpa()
            resposta_entrevista()
            
        elif opcao == "10":
            limpa()
            resposta_maquiagem_roupa()
            
        else:
            print("❌ Opção inválida! Por favor, escolha uma opção de 1 a 10.")
            input("Pressione Enter para continuar...")
            limpa()
            continue
        
        # Se chegou aqui, foi uma opção válida (1-10)
        # Pergunta se quer continuar
        print()
        resposta = input("💝 Deseja fazer outra pergunta? (s/n): ").strip().lower()

        if resposta not in ['s', 'sim', 'yes', 'y', 'S', 'Sim', 'Yes', 'SIM']:
            print()
            print("👋 Obrigada por usar a TôNaModa!")
            print("Volte sempre que precisar de dicas de moda!")
            print("Até a próxima! ✨")
            break
        else:
            limpa()

# Execução do programa
if __name__ == "__main__":
    main()