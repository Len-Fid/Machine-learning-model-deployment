def predict: 
    # Import the libraries
    import pandas as pd 
    import numpy as np
    import matplotlib.pyplot as plt
    import pickle
    
    # Load the dataset
    dataset = pd.read_csv("Filtered_data.csv")
    dataset.head()
    
    # Features
    X = dataset[["Number of bedrooms","Number of facades","Living area","Surface area land","Open fireplace","Terrace","Garden","Pool","Condition"]]
    
    y = dataset["Price"]
    
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LinearRegression
    import numpy as np

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.2)

    regressor = LinearRegression()
    regressor.fit(X_train, y_train)
    print(regressor.score(X_test, y_test))
    print(regressor.score(X_train, y_train))
    
    from sklearn.linear_model import LinearRegression
    regressor = LinearRegression()

    regressor.fit(X.values, y.values)

    pickle.dump(regressor, open('model2.pkl','wb'))

    model = pickle.load(open('model2.pkl','rb'))
    print(model.predict([[3,2,100,300,1,0,1,1,0]]))