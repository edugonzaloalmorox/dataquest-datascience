# Notes

- To prevent any single column from having much of an impact on the distance we can normalise all of the columns (mean  = 0 and sd = 1) 

- `scikit-learn` most popular machine learning library in Python

    - 1. run the ML model
    - 2. fit the model to the training data
    - 3. use the model to make predictions
    - 4. evaluate the accuracy of predictions. 

- `KNeighborsRegressor` has three arguments.

    - `n_neighbors`: number of neighbors.
    - `algorithm` for computing nearest neighbors. 
    - `p` Euclidean distance. 

- `fit` used for fitting the model. It requires the _training data_ (matrix-like object) that has the features and the target values (list-like object). 

    - `matrix-like` object can be a 2D array of values accepted - _dataframe_ or _NumPy 2D_ 

- Data passed in `fit` must be non missing and and numerical. Error otherwise. Use `knn.fit`

- Predictions are run in the test data. The `predict` method requires online a  `matrix-like` with the  feature columns from the dataset we want to make predictions on. Use `knn.predict` (`knn.predict(test_df[['feature1', 'feature2']])`)

 - Important shortcut for selecting all features but one in the train dataset:

    - `features = train_df.columns.tolist()`
        `features.remove('price')`

- Rather than increasing the number of attributes to improve the accuracy it is necessary to increase the number of **relevant** characteristics. 
 



