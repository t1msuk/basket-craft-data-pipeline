WITH raw_orders AS (
  SELECT *
  FROM {{ source('basket_craft', 'orders') }}
),

stg_orders AS (
  SELECT
    order_id,

    -- aliased with order_ prefix for clarity
    created_at,
    website_session_id,
    user_id,
    primary_product_id,
    items_purchased,
    price_usd,
    cogs_usd,

    -- load timestamp
    CURRENT_TIMESTAMP     AS loaded_at
  FROM raw_orders
)

SELECT *
FROM stg_orders
