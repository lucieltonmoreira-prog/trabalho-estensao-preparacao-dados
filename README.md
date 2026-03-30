# trabalho-estensao-preparacao-dados
Análise Sobre as Percepções do Ensino Superior na Comunidade (Disciplina: Preparação de Dados)

Percepção sobre a Importância do Ensino Superior em Diferentes Gerações
Este projeto de extensão acadêmica investiga as barreiras educacionais e a evolução da percepção sobre o ensino superior em uma comunidade de baixa renda. Através da análise de 45 respostas, o trabalho destaca o contraste entre jovens (18-29 anos), adultos (30-49 anos) e idosos (50+ anos).

Tecnologias e Fluxo de Trabalho
O projeto foi estruturado em três etapas principais, utilizando ferramentas que permitiram transformar dados brutos em insights sociais:

1. Coleta e Estruturação (Microsoft Excel)
A coleta foi realizada via Google Forms e exportada para o Excel. Nesta etapa, o software serviu como a base de armazenamento inicial. O desafio era lidar com nomes de colunas extensos (perguntas completas do formulário) e dados brutos que precisavam de padronização antes da análise técnica.

2. Tratamento e Engenharia de Dados (Python & Pandas)
Utilizando o PyCharm Community Edition, o Python foi a peça central para a "limpeza" dos dados. Através da biblioteca Pandas, realizei as seguintes operações:

Renomeação Estratégica: Redução dos nomes das colunas para termos técnicos curtos, facilitando a manipulação e a legibilidade.
Criação de Grupos Geracionais: Desenvolvimento de uma lógica de segmentação para agrupar os respondentes em três faixas etárias distintas.
Filtragem de Atributos: Seleção exclusiva das variáveis de maior impacto para o estudo (Escolaridade, Intenção na Juventude, Barreiras de Acesso e Percepção Histórica).
Normalização: Garantia de que os dados estivessem prontos para uma integração perfeita com ferramentas de visualização.

3. Visualização e Análise Interativa (Power BI)
Com os dados tratados pelo Python, o Power BI Desktop foi utilizado para criar um dashboard interativo. O foco da visualização foi o contraste geracional:

Gráficos de Colunas Agrupadas: Para comparar os níveis de escolaridade entre gerações.
Gráficos 100% Empilhados: Para analisar a intenção de cursar faculdade em diferentes épocas.
Segmentadores Dinâmicos: Filtros que permitem ao usuário navegar pela realidade de cada faixa etária individualmente.
