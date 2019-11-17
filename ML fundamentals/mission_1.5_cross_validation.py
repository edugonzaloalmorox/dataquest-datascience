# Introduction ---------------------------------- 

import numpy as np
import pandas as pd

dc_listings = pd.read_csv("dc_airbnb.csv")
stripped_commas = dc_listings['price'].str.replace(',', '')
stripped_dollars = stripped_commas.str.replace('$', '')
dc_listings['price'] = stripped_dollars.astype('float')

# set .copy() 

# create an index with np.random.permutation
shuffled_index = np.random.permutation(dc_listings.index)
# use reindex in the dataframe df.reindex(_reindexed index_)
dc_listings = dc_listings.reindex(shuffled_index)


split_one = dc_listings.iloc[0:1862].copy()
split_two = dc_listings.iloc[1862:].copy()


# Holdout Validation -------------------------------

