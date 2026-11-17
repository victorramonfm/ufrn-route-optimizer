import heapq

class UFRNGraphWeighted:
    def __init__(self):
        self.grafo = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = []

    def adicionar_aresta(self, origem, destino, peso_km):
        if origem in self.grafo and destino in self.grafo:
            if not any(v[0] == destino for v in self.grafo[origem]):
                self.grafo[origem].append((destino, peso_km))
            if not any(v[0] == origem for v in self.grafo[destino]):
                self.grafo[destino].append((origem, peso_km))

    def menor_caminho_dijkstra(self, inicio, fim):
        if inicio not in self.grafo or fim not in self.grafo:
            return None, float('inf')

        fila_prioridade = [(0.0, inicio, [inicio])]
        visitados = set()

        while fila_prioridade:
            custo_atual, atual, caminho = heapq.heappop(fila_prioridade)

            if atual == fim:
                return caminho, custo_atual

            if atual in visitados:
                continue
            visitados.add(atual)

            for vizinho, peso in self.grafo[atual]:
                if vizinho not in visitados:
                    heapq.heappush(fila_prioridade, (custo_atual + peso, vizinho, caminho + [vizinho]))

        return None, float('inf')

    def top_5_melhores_caminhos(self, inicio, fim):
        if inicio not in self.grafo or fim not in self.grafo:
            return []

        caminhos_encontrados = []

        def dfs_caminhos_validos(atual, destino, caminho_atual, custo_atual, visitados_no_caminho):
            if atual == destino:
                caminhos_encontrados.append((list(caminho_atual), round(custo_atual, 2)))
                return

            if len(caminho_atual) > 12:
                return

            for vizinho, peso in self.grafo[atual]:
                if vizinho not in visitados_no_caminho:
                    visitados_no_caminho.add(vizinho)
                    caminho_atual.append(vizinho)
                    
                    dfs_caminhos_validos(vizinho, destino, caminho_atual, custo_atual + peso, visitados_no_caminho)
                    
                    caminho_atual.pop()
                    visitados_no_caminho.remove(vizinho)

        dfs_caminhos_validos(inicio, fim, [inicio], 0.0, {inicio})
        caminhos_encontrados.sort(key=lambda x: x[1])

        unicos = []
        vistos = set()
        for item in caminhos_encontrados:
            tup_caminho = tuple(item[0])
            if tup_caminho not in vistos:
                vistos.add(tup_caminho)
                unicos.append(item)

        return unicos[:5]