import sys
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
import pickle

OUTPUT_MODELS_PATH = "./trained-models"

def save_trained_desicion_tree(X_train, y_train):
    dt_clf = DecisionTreeClassifier()
    dt_clf.fit(X_train, y_train)
    pickle.dump(dt_clf, open(f"{OUTPUT_MODELS_PATH}/dt.sav", 'wb'))

def save_trained_random_forest(X_train, y_train):
    rf_clf = RandomForestClassifier()
    rf_clf.fit(X_train, y_train)
    pickle.dump(rf_clf, open(f"{OUTPUT_MODELS_PATH}/rf.sav", 'wb'))

def save_trained_xgboost(X_train, y_train):
    xgb_clf = XGBClassifier()
    xgb_clf.fit(X_train, y_train)
    pickle.dump(xgb_clf, open(f"{OUTPUT_MODELS_PATH}/xgb.sav", 'wb'))

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('NO se entreno ningun modelo.')
    else:
        X_train = np.loadtxt("../../data/output/X_train.txt")
        y_train = np.loadtxt("../../data/output/y_train.txt")
        model_to_train = sys.argv[1]
        if model_to_train == 'dt':
            save_trained_desicion_tree(X_train, y_train)
            print('Se entreno un Desicion Tree.')
        elif model_to_train == 'rf':
            save_trained_random_forest(X_train, y_train)
            print('Se entrno un Random Forest.')
        elif model_to_train == 'xgb':
            save_trained_xgboost(X_train, y_train)
            print('Se entrno un XGBoost.')
        elif model_to_train == 'all':
            save_trained_desicion_tree(X_train, y_train)
            save_trained_random_forest(X_train, y_train)
            save_trained_xgboost(X_train, y_train)
            print('Se entrnaron TODOS los modelos.')
        else:
            print('NO se entrno ningun modelo. Las opciones de modelos a entranr son: dt, rf, xbg, all')
