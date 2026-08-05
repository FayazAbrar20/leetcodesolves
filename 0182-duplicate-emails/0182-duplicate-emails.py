import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    value = person["email"][person["email"].duplicated()].drop_duplicates()

    
    return pd.DataFrame({"Email":value})