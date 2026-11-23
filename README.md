# Análise de Vendas – E-commerce Olist

Projeto de análise de dados desenvolvido como atividade do curso de Analista de Dados.

## Objetivo
Analisar dados públicos de pedidos do e-commerce brasileiro Olist para compreender o comportamento das vendas, a distribuição geográfica dos clientes, as formas de pagamento e a satisfação dos consumidores.

## Problema
Empresas de comércio eletrônico precisam acompanhar pedidos, faturamento, clientes e avaliações para identificar oportunidades de melhoria. Sem uma análise organizada, fica mais difícil reconhecer tendências, entender a experiência do cliente e apoiar decisões comerciais e operacionais.

## Fonte de dados
- **Dataset:** Brazilian E-Commerce Public Dataset by Olist.
- **Página oficial:** https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce
- **Período:** 2016 a 2018.
- **Formato:** arquivos CSV estruturados.
- **Acesso:** download direto pela página do Kaggle. É necessário ter uma conta na plataforma.
- **Privacidade:** a própria página informa que os dados comerciais foram anonimizados.
- **Licença:** CC BY-NC-SA 4.0. Consulte as condições na página original antes de redistribuir os dados.

## Tabelas utilizadas
- `olist_orders_dataset.csv`: pedidos, status e datas.
- `olist_customers_dataset.csv`: identificação e localização dos clientes.
- `olist_order_items_dataset.csv`: itens, preços e fretes.
- `olist_order_payments_dataset.csv`: formas e valores de pagamento.
- `olist_order_reviews_dataset.csv`: notas e comentários.
- `olist_products_dataset.csv`: produtos e categorias.
- `product_category_name_translation.csv`: tradução dos nomes das categorias.

## Como reproduzir
1. Baixe o conjunto de dados no Kaggle pelo link acima.
2. Extraia os arquivos CSV para `data/raw/`.
3. Instale as bibliotecas:
   ```bash
   pip install -r requirements.txt
   ```
4. Execute:
   ```bash
   python scripts/eda_olist.py
   ```
5. Para abrir o notebook, use Jupyter Notebook ou Google Colab e abra `notebooks/01_analise_exploratoria_olist.ipynb`.

O script gera tabelas resumidas em `data/processed/`.

## Preparação e modelagem
As tabelas são relacionadas principalmente pelo identificador do pedido (`order_id`), do cliente (`customer_id`) e do produto (`product_id`). A tabela de itens possui uma linha por item vendido; por isso, valores de pedidos não devem ser somados depois de juntar tabelas sem considerar a granularidade, para evitar duplicidade.

O tratamento inclui conversão de datas, conferência de valores ausentes, remoção de duplicidades quando aplicável e criação de campos de ano/mês e valor do item com frete.

## Principais resultados registrados no relatório
- 99.441 pedidos.
- 96.096 clientes únicos.
- R$ 13.591.643,70 em valor de produtos.
- Nota média de avaliação: 4,09.
- São Paulo aparece como o estado com maior concentração de clientes, seguido por Rio de Janeiro e Minas Gerais.
- O cartão de crédito é a forma de pagamento predominante na visualização analisada.

Os indicadores acima foram transcritos do relatório do projeto e devem ser conferidos com os filtros e as fontes efetivamente usados no dashboard. O notebook/script permite reproduzir a análise a partir dos CSVs originais.

## Dashboard

O dashboard interativo foi desenvolvido no Microsoft Power BI, com indicadores, gráficos e filtros para análise dos dados de vendas da Olist.

O arquivo do projeto (.pbix) será disponibilizado junto com a entrega da atividade.

E também foi desenvolvido no Looker Studio e pode ser acessado pelo link público:

https://datastudio.google.com/reporting/8c9f6875-a1de-4023-ba23-e15f9c526480


## Conclusões e recomendações
Os resultados mostram a importância de acompanhar vendas, localização dos clientes, pagamentos e avaliações em conjunto. Recomenda-se monitorar mensalmente o volume de pedidos, investigar avaliações baixas, acompanhar os estados com maior demanda e revisar a experiência de pagamento e entrega.

## Estrutura
- `docs/relatorio_projeto.md`: documentação completa.
- `notebooks/01_analise_exploratoria_olist.ipynb`: notebook de EDA.
- `scripts/eda_olist.py`: script reproduzível.
- `data/raw/`: local para colocar os CSVs originais (não incluídos).
- `data/processed/`: resultados gerados pelo script.

## Observação
Os arquivos originais do Kaggle não foram incluídos neste repositório por tamanho e pelas condições de licença. Faça o download diretamente da fonte oficial.
