The following represents the sequential order of steps for this testing methodology:

1.  Identify the Path MTU. Packetization Layer Path MTU Discovery (PLPMTUD) [RFC4821] SHOULD be conducted. It is important to identify the path MTU so that the TCP TTD is configured properly to avoid fragmentation.
2.  Baseline Round-Trip Time and Bandwidth. This step establishes the inherent, non-congested Round-Trip Time (RTT) and the Bottleneck Bandwidth (BB) of the end-to-end network path. These measurements are used to provide estimates of the TCP RWND and Send Socket Buffer sizes that SHOULD be used during subsequent test steps.
3.  TCP Connection Throughput Tests. With baseline measurements of Round-Trip Time and Bottleneck Bandwidth, single- and multiple- TCP-connection throughput tests SHOULD be conducted to baseline network performance.

O seguinte representa a ordem seqüencial das etapas para este Metodologia de teste:

1. Identifique o caminho MTU. A descoberta do caminho da camada de pacotização (PLPMTUD) [RFC4821] deve ser realizada. É importante identificar o caminho MTU para que o TCP TTD seja configurado corretamente para evitar fragmentação.
2. Tempo de ida e volta da linha de base e largura de banda. Esta etapa estabelece o tempo de viagem de ida e volta inerente e não congelante (RTT) e a largura de banda de gargalo (BB) do caminho da rede de ponta a ponta. Essas medidas são usadas para fornecer estimativas do TCP RWND e enviam tamanhos de buffer de soquete que devem ser usados durante as etapas de teste subsequentes.
3. Testes de taxa de transferência de conexão TCP. Com as medidas da linha de base do tempo de ida e volta e a largura de banda de gargalo, os testes de rendimento de conexão única e múltipla de TCP devem ser realizados no desempenho da rede basal.
