import matplotlib.pyplot as plt
import seaborn as sns
import os

def run_bivariate_analysis(df):
    os.makedirs("../output/charts", exist_ok=True)

    # Avg price by borough
    avg_price = df.groupby('neighbourhood_group')['price'].mean().sort_values()
    avg_price.plot(kind='bar', title='Average Price by Borough')
    plt.tight_layout()
    plt.savefig('../output/charts/avg_price_by_borough.png')
    plt.clf()

    # Boxplot: price vs room type
    sns.boxplot(x='room_type', y='price', data=df[df['price'] < 500])
    plt.title("Room Type vs Price (Under $500)")
    plt.tight_layout()
    plt.savefig('../output/charts/boxplot_roomtype_price.png')
    plt.clf()

    # Correlation heatmap
    num_cols = ['price', 'minimum_nights', 'number_of_reviews', 'reviews_per_month']
    corr = df[num_cols].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.savefig('../output/charts/correlation_heatmap.png')
    plt.clf()
