import numpy as np
import pandas as pd

def mean_wt(df, var, wt):
    series = df[var]
    dropped = series.dropna()
    try:
        return np.average(dropped, weights = df.loc[dropped.index, wt])
    except ZeroDivisionError:
        return 0


def median_wt(df, var, wt):
    dropped = df.dropna(subset=[var])
    dropped_sorted = dropped.sort_values(var)

    if dropped_sorted.shape[0] == 0:
        return 0
    else:
        cumsum = dropped_sorted[wt].cumsum()
        cutoff = dropped_sorted[wt].sum() / 2.
        return dropped_sorted[cumsum >= cutoff][var].iloc[0]


def output_mean_table(df, var, ind_vars, wt):
    """Generalized function that takes in df, outcome variable, independent variable(s) and weight
    and returns a dataframe with disaggregated percentages
    
    - Requires import of mean_wt module -
    """

    # Create reduced dataframe
    temp = df

    ind_df = pd.DataFrame(temp[ind_vars])

    # Check if data is categorical or numeric
    if temp[var].dtypes == 'O':
        var_df = pd.get_dummies(temp[var], prefix=str(var)).replace({np.nan: 0})
    else:
        var_df = pd.DataFrame(temp[var])   

    var_col_names = var_df.columns.to_list()

    # Check if analysis is to be weighted
    if wt == None:
        wt_df = pd.DataFrame(np.ones((len(df),1)), columns=['wt'])
    else:
        wt_df = pd.DataFrame(temp[wt])
        wt_df.columns = ['wt']

    temp = ind_df[:].join(var_df).join(wt_df)

    # Run analysis
    # List comprehension for apply
    mean_list = [temp.groupby(ind_vars[i]).apply(mean_wt, var_col_names[j], 'wt') for i in range(len(ind_vars)) for j in range(len(var_col_names))]

    count_list = [temp.groupby(ind_vars[i])['wt'].apply(sum).round(1) for i in range(len(ind_vars))]

    # Concat lists
    var_len = len(var_col_names)
    mean_concat = [pd.concat(mean_list[(i*var_len):(i*var_len+var_len)], axis=1) for i in range(len(ind_vars))]

    count_concat = [pd.concat([count_list[i]], axis=0) for i in range(len(ind_vars))]

    # Concat (vertical stack)
    mean_df = pd.concat(mean_concat, axis=0)
    count_df = pd.DataFrame(pd.concat(count_concat, axis=0))

    # Rename cols
    old_names = [i for i in range(len(var_col_names))]
    col_dict = dict(zip(old_names, var_col_names))
    mean_df = mean_df.rename(columns = col_dict)

    # Join count to df
    output_df = mean_df.join(count_df)
    
    if wt == None:
        output_df = output_df.rename(columns={'wt': 'Count'})
    else:
        output_df = output_df.rename(columns={'wt': 'Weighted_Count'})

    return output_df