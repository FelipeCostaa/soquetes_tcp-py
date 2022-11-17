## 4 . Métricas TCP

Esta metodologia se concentra em um TCP Throughput e fornece 3 métricas que podem ser utilizadas para melhor compreensão dos resultados. Isto é reconhecido que a complexidade e imprevisibilidade do TCP torna é muito difícil desenvolver um conjunto completo de métricas que leve em conta para uma infinidade de variáveis ​​(ou seja, variações de RTT, condições de perda, implementações TCP, etc.). No entanto, essas 3 métricas facilitam o TCP Comparações de taxa de transferência em diferentes condições de rede e host configurações de tamanho do buffer/RWND.

### 4.1 . Taxa de Tempo de Transferência

A primeira métrica é o TCP Transfer Time Ratio, que é simplesmente o relação entre o tempo de transferência TCP real versus o TCP ideal Tempo de transferência.

O Tempo de Transferência TCP Real é simplesmente o tempo que leva para transferir um bloco de dados através de conexões TCP.

O Tempo de Transferência TCP Ideal é o tempo previsto para o qual um bloco de dados DEVE transferir através de conexões TCP, considerando o BB da NU.

                                 Tempo real de transferência TCP
      Relação de tempo de transferência TCP = -------------------------
                                 Tempo ideal de transferência TCP

O Tempo de Transferência TCP Ideal é derivado do Máximo Alcançável TCP Throughput, que está relacionado ao BB e Layer 1/2/3/4 overheads associados ao caminho da rede. As seguintes seções fornecer derivações para a taxa de transferência TCP máxima alcançável e cálculos de exemplo para o TCP Transfer Time Ratio.

4.1.1 . Cálculo da taxa de transferência TCP máxima alcançável

Esta seção fornece fórmulas para calcular o Máximo Alcançável TCP Throughput, com exemplos para T3 (44,21 Mbps) e Ethernet.

Todos os cálculos são baseados no IP versão 4 com cabeçalhos TCP/IP de 20 Bytes cada (20 para TCP + 20 para IP) dentro de um MTU de 1500 Bytes.

Primeiro, a taxa de transferência máxima da Camada 2 alcançável de uma interface T3 é limitado pela quantidade máxima de quadros por segundo (FPS) permitida pela velocidade real da camada física (Camada 1).

A fórmula de cálculo é:

      FPS = Velocidade Física T3 / ((MTU + PPP + Flags + CRC16) X 8)

      FPS = (44,21 Mbps /
                 ((1500 Bytes + 4 Bytes + 2 Bytes + 2 Bytes) X 8 )))
      FPS = (44,21 Mbps / (1508 Bytes X 8))
      FPS = 44,21 Mbps / 12064 bits
      FPS = 3664

Então, para obter o Throughput TCP Máximo Atingível (Camada 4), nós basta usar:

      (MTU - 40) em Bytes X 8 bits X Max FPS

Para um T3, a taxa de transferência TCP máxima =

      1460 Bytes X 8 bits X 3664 FPS

      Taxa de transferência TCP máxima = 11680 bits X 3664 FPS
      Taxa de transferência TCP máxima = 42,8 Mbps

Na Ethernet, a taxa de transferência máxima da Camada 2 alcançável é limitada por o máximo de quadros por segundo permitido pelo padrão IEEE802.3.

O FPS máximo para Ethernet de 100 Mbps é 8127, e o cálculo fórmula é:

      FPS = (100 Mbps / (1538 Bytes X 8 bits))

O FPS máximo para GigE é 81274 e a fórmula de cálculo é:

      FPS = (1 Gbps / (1538 Bytes X 8 bits))

O FPS máximo para 10GigE é 812743 e a fórmula de cálculo é:

      FPS = (10 Gbps / (1538 Bytes X 8 bits))

Os 1538 Bytes equivalem a:

      MTU + Ethernet + CRC32 + IFG + Preâmbulo + SFD
           (IFG = Inter-Frame Gap e SFD = Início do Delimitador de Quadro)

onde MTU é 1500 Bytes, Ethernet é 14 Bytes, CRC32 é 4 Bytes, IFG é 12 Bytes, Preâmbulo é 7 Bytes e SFD é 1 Byte.

Então, para obter o Throughput TCP Máximo Atingível (Camada 4), nós basta usar:

      (MTU - 40) em Bytes X 8 bits X Max FPS

Para Ethernet de 100 Mbps, a taxa de transferência TCP máxima =

      1460 Bytes X 8 bits X 8127 FPS

      Taxa de transferência TCP máxima = 11680 bits X 8127 FPS
      Taxa de transferência TCP máxima = 94,9 Mbps

É importante notar que melhores resultados podem ser obtidos com quadros jumbo em interfaces Gigabit e 10 Gigabit Ethernet.

#### 4.1.2 . Tempo de Transferência TCP e Cálculo da Razão de Tempo de Transferência

A tabela a seguir ilustra o Tempo de Transferência TCP Ideal de um uma única conexão TCP quando seus tamanhos TCP RWND e Send Socket Buffer igual ou superior ao BDP.

![img4](Screenshot_4.png)

Para um arquivo de 100 MB (100 X 8 = 800 Mbits), o Tempo de Transferência TCP Ideal
é derivado da seguinte forma:

                                          800 Mbits
      Tempo ideal de transferência TCP = -----------------------------------
                                 Taxa de transferência TCP máxima alcançável

Para ilustrar o TCP Transfer Time Ratio, um exemplo seria o transferência em massa de 100 MB em 5 conexões TCP simultâneas (cada conexão transferindo 100 MB). Neste exemplo, a Ethernet O serviço fornece uma Taxa de Acesso Comprometido (CAR) de 500 Mbps. Cada conexão pode atingir diferentes taxas de transferência durante um teste, e o a taxa de transferência geral nem sempre é fácil de determinar (especialmente conforme o número de conexões aumenta).

O Tempo de Transferência TCP Ideal seria ~8 segundos, mas neste exemplo, o Tempo de Transferência TCP Real foi de 12 segundos. O tempo de transferência TCP
A razão seria então 12/8 = 1,5, o que indica que a transferência em todas as conexões levou 1,5 vezes mais do que o ideal.

### 4.2 . Eficiência TCP

A segunda métrica representa a porcentagem de Bytes que não foram retransmitido.

                          Bytes Transmitidos - Bytes Retransmitidos
      Eficiência TCP % = --------------------------------------- X 100
                                   Bytes transmitidos

Bytes transmitidos são o número total de Bytes TCP a serem
transmitidos, incluindo os Bytes originais e retransmitidos.

#### 4.2.1 . Cálculo da Porcentagem de Eficiência TCP

Por exemplo, se 100.000 Bytes foram enviados e 2.000 tiveram que ser
retransmitida, a Porcentagem de Eficiência TCP seria calculada como:

                           102.000 - 2.000
      Eficiência TCP % = ----------------- X 100 = 98,03%
                             102.000

Observe que os Bytes Retransmitidos podem ter ocorrido mais de uma vez;
em caso afirmativo, essas múltiplas retransmissões são adicionadas ao
Bytes Retransmitidos e para as contagens de Bytes Transmitidos.

4.3 . Atraso do buffer

A terceira métrica é a Porcentagem de Atraso do Buffer, que representa a
aumento no RTT durante um teste TCP Throughput versus o inerente ou
RTT de linha de base. O RTT de linha de base é o tempo de ida e volta inerente ao
o caminho de rede sob condições não congestionadas, conforme definido em
Seção 3.2.1 . O RTT médio é derivado do total de todos os
RTTs medidos durante o teste real a cada segundo dividido pelo
duração do teste em segundos.

                                      Total de RTTs durante a transferência
      RTT médio durante a transferência = -----------------------------
                                     Duração da transferência em segundos


                       RTT médio durante a transferência - RTT de linha de base
      % de atraso do buffer = ------------------------------------------ X 100
                                   RTT de linha de base

Constantino, et ai. Informativo [Página 20]

RFC 6349 Framework para teste de throughput TCP agosto de 2011

4.3.1 . Cálculo da porcentagem de atraso do buffer

Como exemplo, considere um caminho de rede com um RTT de linha de base de 25 ms.
Durante o curso de uma transferência TCP, o RTT médio no
toda a transferência aumenta para 32 ms. Então, o atraso do buffer
A porcentagem seria calculada como:

                       32 - 25
      % de atraso do buffer = ------- X 100 = 28%
                         25

Observe que o TCP Transfer Time Ratio, o TCP Efficiency Percentage e o TCP
a Porcentagem de Atraso do Buffer DEVE ser medida durante cada
teste de rendimento. Uma relação de tempo de transferência TCP ruim (ou seja, TCP real
Tempo de Transferência maior que o Tempo de Transferência TCP Ideal) pode ser
diagnosticado pela correlação com a Porcentagem de Eficiência TCP abaixo do ideal
e/ou métricas de Porcentagem de Atraso de Buffer.
