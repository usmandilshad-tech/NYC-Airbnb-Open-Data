import matplotlib.pyplot as plt
import seaborn as sns
import os

def run_univariate_analysis(df):
    os.makedirs("../output/charts", exist_ok=True)

    # Borough bar chart
    ax = df['neighbourhood_group'].value_counts().plot(kind='bar', title='Listings by Borough')
    plt.tight_layout()
    plt.savefig('../output/charts/listings_by_borough.png')
    plt.clf()

    # Room type pie chart
    df['room_type'].value_counts().plot(kind='pie', autopct='%1.1f%%', title='Room Types')
    plt.tight_layout()
    plt.savefig('../output/charts/room_types_pie.png')
    plt.clf()

    # Price distribution
    sns.histplot(df[df['price'] < 500]['price'], bins=50)
    plt.title("Price Distribution (Under $500)")
    plt.tight_layout()
    plt.savefig('../output/charts/price_distribution.png')
    plt.clf()
