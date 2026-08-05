import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    value = employee["salary"].drop_duplicates().nlargest(2)
    
    if len(value)<2:
        return pd.DataFrame({"SecondHighestSalary":[None]})

    else:
        return pd.DataFrame({"SecondHighestSalary":[value.iloc[-1]]})
