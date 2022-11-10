## 3 . Metodologia

O seguinte representa a ordem seqüencial das etapas para este metodologia de teste:

1. Identifique o Caminho MTU. Descoberta de MTU de caminho de camada de empacotamento (PLPMTUD) [ RFC4821 ] DEVE ser realizado. É importante identifique o caminho MTU para que o TCP TTD seja configurado corretamente para evitar a fragmentação.
2. Tempo de ida e volta da linha de base e largura de banda. Esta etapa estabelece a tempo de ida e volta (RTT) inerente e não congestionado e o gargalo Largura de banda (BB) do caminho de rede de ponta a ponta. Essas medidas são usados ​​para fornecer estimativas de TCP RWND e Send Socket Tamanhos de buffer que DEVEM ser usados ​​durante as etapas de teste subsequentes.
3. Testes de taxa de transferência de conexão TCP. Com medições de linha de base de Tempo de ida e volta e largura de banda de gargalo, único e múltiplo Os testes de taxa de transferência de conexão TCP DEVEM ser conduzidos para a linha de base desempenho da rede.

### 3.2 . Tempo de ida e volta (RTT) e largura de banda de gargalo (BB)

Antes que o teste de TCP com estado possa começar, é importante determinar o RTT de linha de base (ou seja, atraso inerente não congestionado) e BB do rede de ponta a ponta a ser testada. Essas medidas são usadas para calcular o BDP e fornecer estimativas do TCP RWND e Send Tamanhos de buffer de soquete que DEVEM ser usados ​​nas etapas de teste subsequentes.

#### 3.2.1 . Medindo RTT

Conforme definido anteriormente na Seção 1.2 , RTT é o tempo decorrido entre o clock in do primeiro bit de um segmento TCP enviado e o recebimento do último bit da confirmação TCP correspondente.

O RTT DEVE ser referenciado fora do horário de pico para obter uma figura confiável da latência de rede inerente. Por outro lado, atraso adicional causado pelo buffer de rede pode ocorrer. Também, quando amostragem de valores de RTT em um determinado intervalo de teste, o mínimo medido valor DEVE ser usado como o RTT de linha de base. Isso será mais próximo estimar o RTT inerente real. Este valor também é usado para determinar a métrica de Porcentagem de Atraso de Buffer definida na Seção 4.3 .

A lista a seguir não pretende ser exaustiva, embora resume algumas das formas mais comuns de determinar o tempo de ida e volta. A precisão de medição desejada (ou seja, ms versus nós) pode ditar se a medição RTT pode ser obtida com pings ICMP ou por um instrumento de teste de comunicações dedicado com temporizadores de precisão. o objetivo desta seção é listar várias técnicas em ordem de precisão decrescente.

- Use equipamentos de teste em cada extremidade da rede, "fazendo um loop" testador final para que um fluxo de pacotes possa ser medido para frente e para trás de ponta a ponta. Esta medição RTT pode ser compatível com atraso protocolos de medição especificados em [ RFC5357 ].

- Realizar capturas de pacotes de sessões de teste TCP usando "iperf" ou FTP, ou outros aplicativos de teste TCP. Ao executar vários experimentos, as capturas de pacotes podem então ser analisadas para estimar o RTT. Isso é importante notar que os resultados baseados em SYN -> SYN-ACK no início de sessões TCP DEVE ser evitado, pois os Firewalls podem abrandar os apertos de mão de 3 vias. Além disso, do lado do remetente, O utilitário LINUX TCPTRACE de Ostermann com argumentos -l -r pode ser usado para extrair os resultados do RTT diretamente das capturas de pacotes.

- Obter estatísticas RTT disponíveis a partir de MIBs definidas em [ RFC4898 ].

- Os pings ICMP também podem ser adequados para fornecer tempo de ida e volta estimativas, desde que o tamanho do pacote seja levado em consideração estimativas (ou seja, pings com tamanhos de pacotes diferentes podem ser requeridos). Algumas limitações com ping ICMP podem incluir ms resolução e se os elementos da rede estão ou não respondendo aos pings. Além disso, o ICMP é frequentemente limitado ou segregado em diferentes filas de buffer. O ICMP pode não funcionar se o QoS (Quality of Service) a reclassificação é feita em qualquer salto. ICMP não é tão confiáveis ​​e precisos como medições em banda.

#### 3.2.2 . Medição BB

Antes que qualquer teste de taxa de transferência TCP possa ser realizado, a largura de banda testes de medição DEVEM ser executados com fluxos IP sem estado (ou seja, não Stateful TCP) para determinar o BB do NUT. Esses medições DEVEM ser realizadas em ambas as direções, especialmente em redes de acesso assimétricas (por exemplo, DSL de taxa de bits assimétrica (ADSL) Acesso). Estes testes DEVEM ser realizados em vários intervalos ao longo de um dia útil ou mesmo durante uma semana.

Testes em vários intervalos de tempo forneceriam uma melhor caracterização do TCP Throughput e melhor percepção de diagnóstico (por casos em que há problemas de desempenho TCP). Os testes de largura de banda DEVE produzir saídas registradas das larguras de banda alcançadas em todo o duração completa do teste.

Existem muitas técnicas bem estabelecidas disponíveis para fornecer medidas estimadas de largura de banda em uma rede. É um comum prática para provedores de rede conduzirem largura de banda de camada 2/3 testes de capacidade usando [ RFC2544 ], embora se entenda que [ RFC2544 ] nunca foi feito para ser usado fora de um ambiente de laboratório. Essas medições de largura de banda DEVEM usar técnicas de capacidade de rede conforme definido em [ RFC5136 ].
