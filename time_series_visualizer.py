import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=True, index_col='date')

# Clean data
df = df[(df['value'] > df['value'].quantile(0.025)) & (df['value'] < df['value'].quantile(0.975))]

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(16, 5))
    plt.plot(df.value, c='#cc0000')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy(deep=True)
    df_bar['year'] = df.index.year
    df_bar['month_num'] = df.index.month
    df_bar['month'] = df.index.month_name()
    df_bar = df_bar.sort_values(['year', 'month_num'])
    df_bar = df_bar.groupby(['year', 'month_num', 'month']).value.mean().reset_index()

    # Draw bar plot
    labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    fig, ax = plt.subplots(figsize=(7.5, 6.7))
    g = sns.barplot(x='year', y='value', hue='month', data=df_bar, hue_order=labels, palette='tab10')
    g.set_xticklabels(g.get_xticklabels(),rotation=90, ha='center')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(loc='upper left', title="Months")

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(figsize=(40, 15))
    sns.set(font_scale=2)
    sns.set_style('white')
    labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    plt.subplot(1, 2, 1)
    sns.boxplot(x='year', y='value', data=df_box)
    plt.title('Year-wise Box Plot (Trend)')
    plt.xlabel('Year')
    plt.ylabel('Page Views')
    plt.yticks([0, 20000, 40000, 60000, 80000, 100000, 120000, 140000, 160000, 180000, 200000])
    
    plt.subplot(1, 2, 2)
    sns.boxplot(x='month', y='value', order=labels, data=df_box)
    plt.title('Month-wise Box Plot (Seasonality)')
    plt.xlabel('Month')
    plt.ylabel('Page Views')
    plt.yticks([0, 20000, 40000, 60000, 80000, 100000, 120000, 140000, 160000, 180000, 200000])
  
    plt.tight_layout(pad=3.00)

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
