from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
OUT = ROOT / "data" / "processed"
OUT.mkdir(parents=True, exist_ok=True)

def load_csv(name, dates=None):
    path = RAW / name
    if not path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {path}. Baixe os CSVs do Kaggle e coloque-os em data/raw/.")
    return pd.read_csv(path, parse_dates=dates or [], low_memory=False)

orders = load_csv("olist_orders_dataset.csv", [
    "order_purchase_timestamp", "order_approved_at",
    "order_delivered_carrier_date", "order_delivered_customer_date",
    "order_estimated_delivery_date"
])
customers = load_csv("olist_customers_dataset.csv")
items = load_csv("olist_order_items_dataset.csv")
payments = load_csv("olist_order_payments_dataset.csv")
reviews = load_csv("olist_order_reviews_dataset.csv")
products = load_csv("olist_products_dataset.csv")

# Limpeza básica
orders = orders.drop_duplicates(subset="order_id")
customers = customers.drop_duplicates(subset="customer_id")
products = products.drop_duplicates(subset="product_id")
orders["order_purchase_timestamp"] = pd.to_datetime(orders["order_purchase_timestamp"], errors="coerce")
orders["ano_compra"] = orders["order_purchase_timestamp"].dt.year
orders["mes_compra"] = orders["order_purchase_timestamp"].dt.to_period("M").astype("string")
customers["customer_state"] = customers["customer_state"].astype("string").str.strip().str.upper()
items["price"] = pd.to_numeric(items["price"], errors="coerce")
items["freight_value"] = pd.to_numeric(items["freight_value"], errors="coerce")
items["valor_total_item"] = items["price"].fillna(0) + items["freight_value"].fillna(0)

# Indicadores calculados em suas tabelas de origem para evitar duplicação por junções
kpis = pd.DataFrame([
    ["total_pedidos", orders["order_id"].nunique()],
    ["clientes_unicos", customers["customer_unique_id"].nunique()],
    ["valor_produtos", items["price"].sum()],
    ["valor_frete", items["freight_value"].sum()],
    ["media_avaliacoes", reviews["review_score"].mean()],
], columns=["indicador", "valor"])
kpis.to_csv(OUT / "indicadores.csv", index=False, encoding="utf-8-sig")

mensal = (orders.dropna(subset=["mes_compra"])
          .groupby("mes_compra", as_index=False)
          .agg(total_pedidos=("order_id", "nunique")))
mensal.to_csv(OUT / "pedidos_por_mes.csv", index=False, encoding="utf-8-sig")

por_estado = (customers.groupby("customer_state", as_index=False)
              .agg(clientes=("customer_unique_id", "nunique"))
              .sort_values("clientes", ascending=False))
por_estado.to_csv(OUT / "clientes_por_estado.csv", index=False, encoding="utf-8-sig")

por_pagamento = (payments.groupby("payment_type", as_index=False)
                 .agg(valor_pagamento=("payment_value", "sum"),
                      quantidade=("order_id", "count"))
                 .sort_values("valor_pagamento", ascending=False))
por_pagamento.to_csv(OUT / "pagamentos.csv", index=False, encoding="utf-8-sig")

por_nota = (reviews.groupby("review_score", as_index=False)
            .agg quantidade=("review_id", "count")
            .sort_values("review_score"))
por_nota.to_csv(OUT / "avaliacoes.csv", index=False, encoding="utf-8-sig")

print("EDA concluída. Arquivos salvos em:", OUT)
print(kpis.to_string(index=False))
