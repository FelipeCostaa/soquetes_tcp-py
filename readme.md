# Trabalho Prático de Redes

---

## IFMG Campus Formiga

---

**==== INICIO ====**

TEMA: **Teste de Vazão TCP**

REFERÊNCIAS:

- Inspiração: RFC 6349 Framework for TCP Throughput Testing ( https://tools.ietf.org/html/rfc6349 )
- Dica: compare seus resultados com os obtidos via iperf (https://iperf.fr), software similar de aferição de desempenho;

**Seção 2)** Objetivos [pag. 8 do RFC 6349]

- Deverá ser utilizada programação de sockets TCP para a realização do trabalho.

_DICA:_ recomendo o uso de no mínimo DUAS conexões: uma somente para o "canal de controle" (seu protocolo) e outra para o "canal de dados" (bytes dos testes).

**Seção 3)** Metodologia [pag. 9]

- 3.2) estabelecer estimativas iniciais [pag. 11-12]

  - 3.2.1) LATÊNCIA (RTT: Round-trip Time, echo req/resp)
  - 3.2.2) Capacidade máxima de LARGURA DE BANDA (BB: bidirecional bandwidth)

_DICA:_ configurar minimum rWND e socket BUFFER sizes (Rx/Tx)

- 3.3) testar a VAZÃO da conexão TCP [pag. 12-16]
  - 5.1) Testes com uma única conexão vs múltiplas conexões TCP (single / multiple)

**Seção 4)** Métricas [pag. 16-21]

- 4.1.1) razão do Tempo de Transferência ( atual / ideal )
- 4.1.2) vazão máxima TCP (max tput)
- 4.3) atraso no buffer ( avg_RTT — init_RTT ) / init_RTT

**Seção 5)** Resultados [pag. 22-25]

**==== FIM ====**
