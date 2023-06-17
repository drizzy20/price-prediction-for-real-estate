import json
import pickle
import numpy as np

__locations = None
__model = None
__data_columns = None


def get_pedicted_prices(location, sqrft, BHK, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1
    x = np.zeros(len(__data_columns))
    x[0] = sqrft
    x[1] = bath
    x[2] = BHK
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)


def load_artifacts():
    print("loading artifacts")
    global __locations
    global __data_columns
    try:
        with open("./artifacts/columns.json", 'r') as f:
            __data_columns = json.load(f)['data_columns']
            __locations = __data_columns[3:]
            # print("Printing data columns and locations")
            # print("Data Columns:", __data_columns)
            # print("Locations:", __locations)
    except Exception as e:
        print("Error while loading json columns file:", e)

    try:
        global __model
        with open("./artifacts/Zim_Home_Prices_Prediction_model.pickle", 'rb') as f:
            __model = pickle.load(f)
            print("Loading artifacts done")
    except EOFError:
        print("Pickle file is empty")
    except Exception as e:
        print("Error loading pickle file:", e)


def get_locations():
    # print("These are the locations:", __locations)
    return __locations


if __name__ == "__main__":
    load_artifacts()
    # print("Locations:", get_locations())
