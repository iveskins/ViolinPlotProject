import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def generate_data(num_samples=100):
    np.random.seed(10)
    customer_index = np.arange(num_samples)
    customer_days_since_join = np.random.randint(1, 1000, size=num_samples)
    customer_total_lifetime_value = np.random.normal(loc=500, scale=150, size=num_samples)
    df = pd.DataFrame({
        'customer_index': customer_index,
        'customer_days_since_join': customer_days_since_join,
        'customer_total_lifetime_value': customer_total_lifetime_value
    })
    df['days_since_join_bins'] = pd.cut(df['customer_days_since_join'], bins=[0, 200, 400, 600, 800, 1000], labels=['<200', '200-400', '400-600', '600-800', '>800'])
    df['index_group'] = np.where(df['customer_index'] < np.percentile(df['customer_index'], 50), 'Bottom 50%', 'Top 50%')
    return df

def plot_violin(df):
    palette_days = {
        '<200': "#FF6F61",      # Light lips
        '200-400': "#F4A582",   # Light skin
        '400-600': "#8B0000",   # Dark lips
        '600-800': "#D2691E",   # Dark skin
        '>800': "#A52A2A"       # Medium dark
    }
    palette_index = {
        'Bottom 50%': "#F4A582",  # Cornflower blue
        'Top 50%': "#FF6F61"      # Tomato
    }
    palette_combined = {**palette_days, **palette_index}
    plt.figure(figsize=(12, 8))
    sns.violinplot(x='days_since_join_bins', y='customer_total_lifetime_value', hue='index_group', data=df, dodge=False, palette=palette_combined)
    plt.xlabel('Days Since Join (Binned)')
    plt.ylabel('Total Lifetime Value')
    plt.title('Customer Lifetime Value by Days Since Join')
    plt.legend(title='Index Group')
    plt.show()

if __name__ == "__main__":
    df = generate_data()
    plot_violin(df)
