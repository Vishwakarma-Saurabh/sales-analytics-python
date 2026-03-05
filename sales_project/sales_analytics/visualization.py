import matplotlib.pyplot as plt
import seaborn as sns
import os

from sales_project.sales_analytics.config import FIGURES_DIR


class SalesVisualization:

    @staticmethod
    def revenue_by_category(df):

        plt.figure(figsize=(8,5))

        sns.barplot(x="category", y="revenue", data=df)

        plt.xticks(rotation=45)

        plt.title("Revenue by Category")

        path = os.path.join(FIGURES_DIR, "revenue_by_category.png")

        plt.tight_layout()

        plt.savefig(path)

        plt.close()

    @staticmethod
    def monthly_sales_trend(df):

        monthly = df.groupby("month")["revenue"].sum()

        plt.figure(figsize=(8,5))

        monthly.plot(kind="line", marker="o")

        plt.title("Monthly Sales Trend")

        path = os.path.join(FIGURES_DIR, "monthly_sales.png")

        plt.tight_layout()

        plt.savefig(path)

        plt.close()

    @staticmethod
    def correlation_heatmap(df):

        plt.figure(figsize=(6,5))

        sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")

        plt.title("Correlation Heatmap")

        path = os.path.join(FIGURES_DIR, "correlation.png")

        plt.tight_layout()

        plt.savefig(path)

        plt.close()