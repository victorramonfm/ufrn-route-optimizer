import os
from PIL import Image
from graph import UFRNGraphWeighted

def exibir_imagem_mapa(caminho_imagem="./docs/mapa_ufrn.jpeg"):
    if os.path.exists(caminho_imagem):
        try:
            img = Image.open(caminho_imagem)
            img.show()
            print("🗺️ [Visualizador] A imagem do mapa foi aberta na sua tela para consulta.")
        except Exception as e:
            print(f"⚠️ Não foi possível abrir a imagem automaticamente: {e}")
    else:
        print(f"⚠️ Imagem '{caminho_imagem}' não encontrada na pasta do projeto.")

def inicializar_mapa_ponderado_ufrn():
    g = UFRNGraphWeighted()
    
    nos_oficiais = {
        0: "0_IMD",
        1: "1_Anel_Viario",
        2: "2_Artes",
        3: "3_Praca",
        4: "4_Capela",
        5: "5_NUPLAM",
        6: "6_Meio_Ambiente",
        7: "7_Horto",
        8: "8_Saude",
        9: "9_Esporte",
        10: "10_Sociais_Aplicadas",
        11: "11_Biblioteca",
        12: "12_Convivencia",
        13: "13_Reitoria",
        14: "14_Biociencias",
        15: "15_Exatas",
        16: "16_Agora",
        17: "17_Humanidades",
        18: "18_Educacao",
        19: "19_Observatorio",
        20: "20_Engenharias",
        21: "21_Tecnologia"
    }
    
    for nome in nos_oficiais.values():
        g.adicionar_vertice(nome)

    # Vetor de conexões exato parametrizado como verdade absoluta
    conexoes_com_pesos = [
        ("0_IMD", "18_Educacao", 1.29),
        ("0_IMD", "8_Saude", 0.69),
        
        ("1_Anel_Viario", "4_Capela", 1.91),
        ("1_Anel_Viario", "3_Praca", 2.09),
        ("1_Anel_Viario", "5_NUPLAM", 1.68),
        ("1_Anel_Viario", "6_Meio_Ambiente", 1.10),
        
        ("2_Artes", "3_Praca", 2.20),

        ("3_Praca", "1_Anel_Viario", 1.93),
        ("3_Praca", "4_Capela", 1.91),

        ("4_Capela", "1_Anel_Viario", 1.93),
        ("4_Capela", "3_Praca", 2.09),
        
        ("5_NUPLAM", "6_Meio_Ambiente", 1.10),
        ("5_NUPLAM", "14_Biociencias", 1.29),
        
        ("6_Meio_Ambiente", "1_Anel_Viario", 1.93),
        ("6_Meio_Ambiente", "7_Horto", 0.74),
        ("6_Meio_Ambiente", "5_NUPLAM", 1.68),
        ("6_Meio_Ambiente", "10_Sociais_Aplicadas", 1.09),

        ("7_Horto", "6_Meio_Ambiente", 1.10),
        ("7_Horto", "8_Saude", 0.69),

        ("8_Saude", "0_IMD", 0.00),
        ("8_Saude", "10_Sociais_Aplicadas", 1.09),
        ("8_Saude", "7_Horto", 0.74),
        ("8_Saude", "9_Esporte", 1.05),
        
        ("9_Esporte", "8_Saude", 0.69),
        ("9_Esporte", "18_Educacao", 1.09),

        ("10_Sociais_Aplicadas", "6_Meio_Ambiente", 1.10),
        ("10_Sociais_Aplicadas", "8_Saude", 1.29),
        ("10_Sociais_Aplicadas", "9_Esporte", 1.05),
        ("10_Sociais_Aplicadas", "11_Biblioteca", 1.20),
        ("10_Sociais_Aplicadas", "13_Reitoria", 1.30),

        ("11_Biblioteca", "10_Sociais_Aplicadas", 1.09),
        ("11_Biblioteca", "12_Convivencia", 1.34),
        ("11_Biblioteca", "17_Humanidades", 1.56),

        ("12_Convivencia", "11_Biblioteca", 1.32),
        ("12_Convivencia", "13_Reitoria", 1.14),
        ("12_Convivencia", "15_Exatas", 1.55),

        ("13_Reitoria", "10_Sociais_Aplicadas", 1.30),
        ("13_Reitoria", "12_Convivencia", 1.34),
        ("13_Reitoria", "14_Biociencias", 1.29),
        
        ("14_Biociencias", "5_NUPLAM", 1.68),
        ("14_Biociencias", "13_Reitoria", 1.14),
        ("14_Biociencias", "21_Tecnologia", 1.79),

        ("15_Exatas", "12_Convivencia", 1.34),
        ("15_Exatas", "16_Agora", 1.56),
        ("15_Exatas", "21_Tecnologia", 1.79),

        ("16_Agora", "15_Exatas", 1.55),
        ("16_Agora", "17_Humanidades", 1.56),
        ("16_Agora", "19_Observatorio", 1.75),
        
        ("17_Humanidades", "11_Biblioteca", 1.32),
        ("17_Humanidades", "16_Agora", 1.56),
        ("17_Humanidades", "18_Educacao", 1.29),

        ("18_Educacao", "0_IMD", 0.00),
        ("18_Educacao", "17_Humanidades", 1.56),

        ("19_Observatorio", "16_Agora", 1.56),
        ("19_Observatorio", "20_Engenharias", 1.86),

        ("20_Engenharias", "19_Observatorio", 1.75),
        ("20_Engenharias", "21_Tecnologia", 1.79),

        ("21_Tecnologia", "15_Exatas", 1.55),
        ("21_Tecnologia", "20_Engenharias", 1.86),
        ("21_Tecnologia", "14_Biociencias", 1.29)
    ]

    for origem, destino, peso in conexoes_com_pesos:
        g.adicionar_aresta(origem, destino, peso)

    return g, nos_oficiais

if __name__ == "__main__":
    print("=== OTIMIZADOR DE ROTAS UFRN (EED II) ===")
    
    exibir_imagem_mapa("./docs/mapa_ufrn.jpeg")
    
    mapa, dicionario_nos = inicializar_mapa_ponderado_ufrn()
    
    print("\n--- NÓS DISPONÍVEIS NO MAPA DA UFRN ---")
    for num, nome in sorted(dicionario_nos.items()):
        print(f"[{num}] {nome}")
    print("-" * 38)

    try:
        num_origem = int(input("\nDigite o número do nó de ORIGEM (conforme o mapa): "))
        num_destino = int(input("Digite o número do nó de DESTINO (conforme o mapa): "))

        origem = dicionario_nos[num_origem]
        destino = dicionario_nos[num_destino]

        print(f"\nCalculando rotas eficientes de '{origem}' para '{destino}'...")

        caminho_otimo, distancia_otima = mapa.menor_caminho_dijkstra(origem, destino)
        
        if not caminho_otimo:
            print("\n❌ Não há caminho possível entre os pontos selecionados.")
        else:
            print(f"\n🏆 MELHOR CAMINHO (Ótimo):")
            print(f"Distância Total: {distancia_otima:.2f} km")
            print(" Caminho: " + " -> ".join(caminho_otimo))

            top_caminhos = mapa.top_5_melhores_caminhos(origem, destino)
            print(f"\n📊 TOP {len(top_caminhos)} CAMINHOS MAIS EFICIENTES:")
            for rank, (caminho, distancia) in enumerate(top_caminhos, 1):
                print(f"  {rank}º Lugar | Distância: {distancia:.2f} km")
                print(f"     Caminho: {' -> '.join(caminho)}")

    except (ValueError, KeyError):
        print("\n⚠️ Entrada inválida! Certifique-se de digitar um número correspondente à tabela acima.")