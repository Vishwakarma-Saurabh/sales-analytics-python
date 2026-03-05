from sales_project.sales_analytics.repositories import SalesRepository
from sales_project.sales_analytics.analysis import SalesAnalysis
from sales_project.sales_analytics.visualization import SalesVisualization


def main():

    SalesRepository.create_table()

    SalesRepository.insert_sample_data()

    df = SalesRepository.fetch_all()

    SalesAnalysis.total_revenue(df)

    SalesAnalysis.revenue_by_category(df)

    SalesVisualization.revenue_by_category(df)

    SalesVisualization.monthly_sales_trend(df)

    SalesVisualization.correlation_heatmap(df)