{{ config(materialized='view') }}

SELECT
  DATE(website_session_created_at) AS website_session_day,
  utm_source,
  COUNT(website_session_id) AS sessions,
  SUM(is_repeat_session)::INT AS repeat_sessions,
  (SUM(is_repeat_session)::NUMERIC / COUNT(website_session_id)) * 100 AS repeat_sessions_pct
FROM {{ ref('stg_website_sessions') }}
GROUP BY 1, 2
