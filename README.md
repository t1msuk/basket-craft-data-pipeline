As part of SQL Quiz 03, I built a complete end-to-end data pipeline that extracts website session data from the basket_craft MySQL database and transforms it for analysis and visualization. 
Using a Python script, I extracted sessions from December 2023 and loaded them into a raw.website_sessions table in PostgreSQL. 
I then automated this pipeline using GitHub Actions, with secure credentials managed via GitHub Secrets. 
In dbt, I created a staging model (stg_website_sessions) to clean and timestamp the data, and a warehouse model (fct_website_sessions_utm_source_daily) that calculates daily sessions and repeat session metrics by UTM source. 
Finally, I built an interactive Looker Studio dashboard featuring five key visualizations — including tables, a heatmap, a scorecard, and a bar chart — with cross-filtering enabled to support dynamic data exploration.

Dashboard: https://lookerstudio.google.com/reporting/fb6fe441-91c4-44d6-b298-211d56db621c

[png2pdf.pdf](https://github.com/user-attachments/files/20052828/png2pdf.pdf)
