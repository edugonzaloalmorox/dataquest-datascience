# Removing features 

dc_listings.head()

# remove various variables with MA 
drop_columns = ['host_response_rate', 'host_acceptance_rate', 'room_type',
                'host_listings_count', 'city', 
                'state', 'longitude', 'latitude', 'zipcode']

dc_listings = dc_listings.drop(drop_columns, axis =1)

print(dc_listings)

# Handling missing values


dc_listings = dc_listings.drop(['cleaning_fee', 'security_deposit'], axis = 1)

dc_listings = dc_listings.dropna(axis = 0)

# check proportions of NAs in the dataframe
dc_listings.isna().mean().round(4) * 100


# Normalize columns 

normalized_listings = (dc_listings - dc_listings.mean()) / (dc_listings.std())

normalized_listings['price'] = dc_listings['price']

print(normalized_listings.head(3))

# Euclidean distance for multivariate 

from scipy.spatial import distance

first_listing = normalized_listings.iloc[0][['accommodates', 'bathrooms']]

fifth_listing = normalized_listings.iloc[4][['accommodates', 'bathrooms']]

first_fifth_distance = distance.euclidean(first_listing, fifth_listing)

print(first_fifth_distance)

# Fitting a model and making predictions

from sklearn.neighbors import KNeighborsRegressor


train_df = normalized_listings.iloc[0:2792]
test_df = normalized_listings.iloc[2792:]
train_columns = ['accommodates', 'bathrooms']

knn = KNeighborsRegressor(n_neighbors = 5, algorithm ='brute')

knn.fit(train_df[train_columns], train_df['price'])

predictions = knn.predict(test_df[train_columns])

# Using more features

features = ['accommodates', 'bedrooms', 'bathrooms', 'number_of_reviews']
from sklearn.neighbors import KNeighborsRegressor
knn = KNeighborsRegressor©(n_neighbors=5, algorithm='brute')

knn.fit(train_df[features], train_df['price'])

four_predictions = knn.predict(test_df[features])

# Evaluate the predictions of the model
four_mse = mean_squared_error(test_df['price'], four_predictions)

four_rmse = (four_mse)**(1/2)

# Using all the features of the Dataset 

train_df = normalized_listings.iloc[0:2792]

test_df = normalized_listings.iloc[2792:]

# Select features (all but price)
features = train_df.columns.tolist()
features.remove('price')


from sklearn.neighbors import KNeighborsRegressor
knn = KNeighborsRegressor(n_neighbors=5, algorithm='brute')

# Fit
knn.fit(train_df[features], train_df['price'])

all_features_predictions = knn.predict(test_df[features])

all_features_mse = mean_squared_error(test_df['price'], all_features_predictions)

all_features_rmse= (all_features_mse)**(1/2)

print(all_features_mse, all_features_rmse)


