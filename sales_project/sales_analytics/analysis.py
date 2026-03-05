class SalesAnalysis:

    @staticmethod
    def total_revenue(df):

        total = df["revenue"].sum()

        print("Total Revenue:", total)

        return total

    @staticmethod
    def revenue_by_category(df):

        result = df.groupby("category")["revenue"].sum()

        print(result)

        return result