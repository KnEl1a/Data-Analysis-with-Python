import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# Lee el archivo CSV y configura el índice como la columna 'date'
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)

# Filtra los datos usando los cuantiles, específicamente percentiles el de 2.5 y el de 97.5
df = df.loc[(df['value'] >= df['value'].quantile(0.025))
            & (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
  fig, ax = plt.subplots(figsize=(14, 7))

  ax.plot(df.index, df['value'], color='r')
  ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
  ax.set_xlabel("Date")
  ax.set_ylabel("Page Views")

  fig.savefig('line_plot.png')
  return fig


def draw_bar_plot():
  df_bar = df.copy()
  df_bar['year'] = df_bar.index.year
  df_bar['month'] = df_bar.index.month_name()

  df_bar = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

  # Ordenar los meses
  month_order = [
      "January", "February", "March", "April", "May", "June", "July", "August",
      "September", "October", "November", "December"
  ]
  df_bar = df_bar.reindex(columns=month_order)

  fig = df_bar.plot(kind='bar', figsize=(14, 7)).figure

  plt.xlabel('Years', fontsize=15)
  plt.ylabel('Average Page Views', fontsize=15)
  plt.legend(loc='upper left', title='Months', fontsize=8)

  fig.savefig('bar_plot.png')
  return fig


def draw_box_plot():
  df_box = df.copy()
  df_box.reset_index(inplace=True)
  df_box['year'] = [d.year for d in df_box.date]
  df_box['month'] = [d.strftime('%b') for d in df_box.date]

  fig, axes = plt.subplots(1, 2, figsize=(14, 7))

  sns.boxplot(data=df_box, x='year', y='value', ax=axes[0])
  axes[0].set_title('Year-wise Box Plot (Trend)')
  axes[0].set_xlabel("Year")
  axes[0].set_ylabel("Page Views")

  month_order = [
      "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct",
      "Nov", "Dec"
  ]

  df_box['month'] = pd.Categorical(df_box['month'],
                                   categories=month_order,
                                   ordered=True)

  sns.boxplot(data=df_box, x='month', y='value', ax=axes[1], order=month_order)
  axes[1].set_title("Month-wise Box Plot (Seasonality)")
  axes[1].set_xlabel("Month")
  axes[1].set_ylabel("Page Views")

  fig.savefig('box_plot.png')
  return fig
