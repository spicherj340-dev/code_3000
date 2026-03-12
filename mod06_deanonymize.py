import pandas as pd

def load_data(anonymized_path, auxiliary_path):
    """
    Load anonymized and auxiliary datasets.
    """
    anon = pd.read_csv(anonymized_path)
    aux = pd.read_csv(auxiliary_path)
    return anon, aux


def link_records(anon_df, aux_df):
    """
    Attempt to link anonymized records to auxiliary records
    using exact matching on quasi-identifiers.

    Returns a DataFrame with columns:
      anon_id, matched_name
    containing ONLY uniquely matched records.
    """
    df = pd.merge(anon_df, aux_df, on=["age","zip3", "gender"])
    uni = df.groupby("anon_id").filter(lambda x: len(x) == 1)
    return uni[["anon_id", "matched_name"]]


def deanonymization_rate(matches_df, anon_df):
    """
    Compute the fraction of anonymized records
    that were uniquely re-identified.
    """
    rows1 = len(matches_df)
    rows2 = len(anon_df)
    frac = rows1/rows2
    return frac
    raise NotImplementedError
