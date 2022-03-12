# %% Interactive Python Cell
import psycopg2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

con = psycopg2.connect("dbname=irxrace user=postgres host=localhost port=5432")


def sql_to_df(sql_query: str):
    """Get result set of sql_query as a pandas DataFrame."""
    return pd.read_sql(sql_query, con)



title = "Races by ending_position"
query = """
        SELECT ending_position, COUNT(*)
        FROM race_info
        GROUP BY ending_position
        """

dataframe = sql_to_df(query)
_fig, axes = plt.subplots(figsize=(10, 5))
axes.set_title(title, fontsize=14)

# get evenly spaced x-axis positions
xpos = np.arange(len(dataframe))
# at each x, add bar (height based on count data)
axes.bar(xpos, dataframe["count"], width=0.50)
# at each x, add tick mark
axes.set_xticks(xpos)
# at each x, add label based on dept data
axes.set_xticklabels(dataframe["ending_position"])
# label y-axis
axes.set_ylabel("Count", fontsize=12)
# rotate x-axis labels to prevent overlap
plt.setp(axes.get_xticklabels(), rotation=30, horizontalalignment='right')

plt.show()
# %%
