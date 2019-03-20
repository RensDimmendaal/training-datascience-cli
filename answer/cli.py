import fire

import numpy as np
import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.externals import joblib


# fixed filepaths
MODEL_FP = './output/model.pkl'
WORD_SENTIMENT_FP = './output/word_sentiment.csv'

def train(train_fp):
    train = pd.read_csv(train_fp)

    pipeline = Pipeline([
        ('vect', CountVectorizer()),
        ('clf', SGDClassifier(loss='log',max_iter=1000, tol=1e-3)),
        ])

    parameters = {
        'vect__min_df': (
            5,
            10,
            15,
        ),
        'vect__max_df': (
            0.5, 
            0.75,
            1.0,
        ),
        'clf__alpha': np.logspace(-5,3,3),
    }
   
    grid_search = GridSearchCV(pipeline, parameters, cv=5,
                               n_jobs=-1, verbose=1,return_train_score=True)

    grid_search.fit(train.Comment, train.Insult)

    # save the best model
    joblib.dump(grid_search.best_estimator_, MODEL_FP)


def predict_file(test_fp, out_fp):
    test = pd.read_csv(test_fp)
    model = joblib.load(MODEL_FP)
    preds = model.predict_proba(test.Comment)
    test['Insult_proba'] = preds[:,1] #insult prob is in second column
    test.to_csv(out_fp)


def save_word_sentiment():
    model = joblib.load(MODEL_FP)
    words = model.named_steps['vect'].get_feature_names()
    coefs = model.named_steps['clf'].coef_.reshape(-1)
    word_sentiment = pd.DataFrame({'sentiment':coefs*-1,},index=words)
    word_sentiment.to_csv(WORD_SENTIMENT_FP)


def predict_sentence(sentence):
    model = joblib.load(MODEL_FP)
    pred_insult = model.predict_proba([sentence])[0,1]
    print(f'Insult probability: {pred_insult:.2f}')

if __name__ == '__main__':
  fire.Fire()