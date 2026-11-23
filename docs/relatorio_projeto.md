# Projeto Final – Análise de Vendas do E-commerce Olist

**Curso:** Analista de Dados  
**Tema:** Uso de dados para compreender o desempenho de um comércio eletrônico

## 1. Problema e justificativa

O comércio eletrônico gera muitos dados durante o processo de compra, como informações sobre pedidos, produtos, clientes, pagamentos, frete e avaliações. Quando essas informações são analisadas separadamente, a empresa pode ter dificuldade para entender o desempenho das vendas e identificar pontos que precisam de melhoria.

O problema abordado neste projeto é a necessidade de transformar os dados de uma operação de e-commerce em informações úteis para apoiar decisões. A análise é relevante porque permite acompanhar a evolução dos pedidos, reconhecer onde estão os clientes, entender quais formas de pagamento são mais utilizadas e observar a satisfação dos consumidores.

A análise de dados pode ajudar a organizar essas informações, identificar padrões e orientar ações. Por exemplo, uma empresa pode reforçar o planejamento comercial nos períodos de maior movimento, acompanhar regiões com maior concentração de clientes e investigar os motivos de avaliações baixas.

## 2. Fontes de dados e coleta

Foi utilizada a base **Brazilian E-Commerce Public Dataset by Olist**, disponibilizada publicamente no Kaggle:

https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

A página da fonte descreve aproximadamente 100 mil pedidos realizados entre 2016 e 2018. Os dados são comerciais, mas foram anonimizados antes da publicação.

As informações estão organizadas em arquivos CSV, portanto são dados estruturados. Foram consideradas principalmente estas tabelas:

| Arquivo | Conteúdo |
|---|---|
| `olist_orders_dataset.csv` | Pedidos, status e datas |
| `olist_customers_dataset.csv` | Clientes e localização por estado |
| `olist_order_items_dataset.csv` | Produtos vendidos, preços e frete |
| `olist_order_payments_dataset.csv` | Formas e valores de pagamento |
| `olist_order_reviews_dataset.csv` | Notas e comentários dos clientes |
| `olist_products_dataset.csv` | Produtos e categorias |
| `product_category_name_translation.csv` | Tradução das categorias |

**Método de coleta:** download direto dos arquivos CSV pela página do Kaggle. Para acessar a base, é necessário possuir uma conta na plataforma. Não foi necessário utilizar scraping nem acessar dados privados.

**Licença:** a página do Kaggle informa licença CC BY-NC-SA 4.0. A fonte deve ser creditada e as condições de uso devem ser respeitadas.

## 3. Tratamento, modelagem e análise exploratória

A preparação foi realizada com apoio do Power BI e das planilhas utilizadas no projeto. O código Python disponibilizado neste repositório permite repetir verificações e gerar resumos a partir dos arquivos originais.

As principais etapas de preparação foram:
- conferência dos tipos de dados, principalmente datas e valores numéricos;
- verificação de campos vazios e registros duplicados;
- padronização de campos de texto;
- criação de informações de ano e mês da compra;
- cálculo do valor do item considerando preço e frete;
- relacionamento das tabelas por identificadores, como `order_id`, `customer_id` e `product_id`.

Na modelagem, é importante respeitar o nível de detalhe de cada tabela. A tabela de pedidos possui uma linha por pedido, enquanto a tabela de itens pode possuir várias linhas para o mesmo pedido. Por isso, somas de valores devem ser calculadas na tabela adequada, evitando duplicidade após relacionamentos.

## 4. Resultados e insights

A análise registrada no projeto apresentou os seguintes indicadores:

| Indicador | Resultado |
|---|---:|
| Total de pedidos | 99.441 |
| Clientes únicos | 96.096 |
| Valor total dos produtos | R$ 13.569.858,94 |
| Média das avaliações | 4,09 |

Também foram observados os seguintes pontos:

**Evolução dos pedidos:** o volume de pedidos cresceu ao longo do período analisado, com variações entre os meses. Esse acompanhamento ajuda a identificar períodos de maior demanda.

**Distribuição geográfica:** São Paulo concentra a maior quantidade de clientes, seguido por Rio de Janeiro e Minas Gerais. Essa informação pode apoiar decisões de logística, atendimento e planejamento comercial.

**Avaliações:** a nota 5 foi a mais frequente, seguida pela nota 4. A média geral registrada foi de 4,09, indicando avaliações predominantemente positivas. Mesmo assim, as notas baixas devem ser acompanhadas para identificar problemas de entrega ou atendimento.

**Formas de pagamento:** o cartão de crédito aparece como a forma predominante na visualização analisada, seguido pelo boleto. Conhecer essa distribuição ajuda a empresa a acompanhar as preferências dos consumidores.

**Categorias:** a visualização por categoria permite comparar a quantidade de produtos cadastrados em cada grupo e compreender a variedade do catálogo.

## 5. Visualização dos dados

Os resultados foram organizados em um dashboard no Looker Studio, com indicadores e gráficos para facilitar a leitura das informações. O painel contempla a evolução dos pedidos, a distribuição geográfica dos clientes, as avaliações, as formas de pagamento e as categorias de produtos.

**Link do dashboard:** https://datastudio.google.com/u/0/reporting/8c9f6875-a1de-4023-ba23-e15f9c526480/page/6L8DG?s=g7XIWj-BPZs

As visualizações ajudam a transformar tabelas extensas em informações mais simples, facilitando a identificação de tendências e pontos de atenção.

## 6. Recomendações

Com base nos resultados, recomenda-se:
1. acompanhar mensalmente a quantidade de pedidos para antecipar períodos de maior demanda;
2. considerar a concentração de clientes em São Paulo, Rio de Janeiro e Minas Gerais no planejamento comercial e logístico;
3. investigar avaliações baixas para identificar oportunidades de melhoria na entrega, no atendimento e nos produtos;
4. acompanhar a distribuição das formas de pagamento para manter opções adequadas ao perfil dos clientes;
5. atualizar os indicadores periodicamente para apoiar decisões com dados recentes.

## 7. Conclusão

O projeto mostrou como a análise de dados pode ajudar a compreender o funcionamento de um comércio eletrônico. A partir de uma base pública e anonimizada, foi possível organizar informações de pedidos, clientes, produtos, pagamentos e avaliações.

Os resultados destacam a importância de acompanhar o volume de vendas, a localização dos clientes e a satisfação dos consumidores. O dashboard facilita a comunicação desses resultados e pode apoiar decisões comerciais e operacionais.

Como limitação, a base representa um período histórico de 2016 a 2018 e não deve ser interpretada como retrato do mercado atual. Além disso, os resultados dependem dos filtros e das regras de cálculo utilizados. Por isso, a análise deve ser entendida como um estudo exploratório da base disponibilizada.

## 8. Referência

OLIST. *Brazilian E-Commerce Public Dataset by Olist*. Kaggle. Disponível em: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce. Acesso em: 23 nov. 2026.
