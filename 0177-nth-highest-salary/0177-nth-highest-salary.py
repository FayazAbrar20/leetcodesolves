import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    value = employee["salary"].drop_duplicates().nlargest(N)

    if(len(value)<N)or (N<=0):
        return pd.DataFrame({f"getNthHighestSalary({N})":[None]})
    else:
        return pd.DataFrame({f"getNthHighestSalary({N})":[value.iloc[N-1]]})