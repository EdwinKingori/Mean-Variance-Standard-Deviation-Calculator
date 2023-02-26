import numpy as np
def calculator(list):
    
    if len(list) == 9:
        #Initializing the dictionary
        calculations = { 'mean': '', 'variance': '','standard deviation' : '', 'max' : '', 
        'min' : '', 'sum' : ''} 

        #storing values for the fattened matrix
        store = np.array ([list[0:3], list[3:6], list[6:9]])
        store_min = store.min()
        store_max = store.max()
        store_sum = store.sum()
        store_mean = store.mean()
        store_var = store.var()
        store_std = store.std()

        #store value across the rows
        store_min_row = store.min(0)
        store_max_row = store.max(0)
        store_sum_row = store.sum(0)
        store_mean_row = store.mean(0)
        store_var_row = store.var(0)
        store_std_row = store.std(0)

        #store value across the columns
        store_min_col = store.min(0)
        store_max_col = store.max(0)
        store_sum_col = store.sum(0)
        store_mean_col = store.mean(0)
        store_var_col = store.var(0)
        store_std_col = store.std(0)

        # using the .tolist() to convert numpy array to a python list
        calculations.update({'min': [store_min_row.tolist(), store_min_col.tolist(), store_min]})
        calculations.update({'min': [store_max_row.tolist(), store_max_col.tolist(), store_max]})
        calculations.update({'min': [store_sum_row.tolist(), store_sum_col.tolist(), store_sum]})
        calculations.update({'min': [store_mean_row.tolist(), store_mean_col.tolist(), store_mean]})
        calculations.update({'min': [store_var_row.tolist(), store_var_col.tolist(), store_var]})
        calculations.update({'min': [store_std_row.tolist(), store_std_col.tolist(), store_std]})

    else:
        raise ValueError('List must contain nine values! Please Again.')
    return calculations 
