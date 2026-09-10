import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report,confusion_matrix

df=pd.read_csv('data/cleaned_spacex_falcon9.csv')
features=['FlightNumber','PayloadMass','Flights','GridFins','Reused','Legs','Block','ReusedCount','Orbit','LaunchSite']
X=pd.get_dummies(df[features],columns=['Orbit','LaunchSite'])
y=df['Class']
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=.2,random_state=42,stratify=y)

models={
'Logistic Regression':Pipeline([('scale',StandardScaler()),('clf',LogisticRegression(max_iter=3000))]),
'SVM':Pipeline([('scale',StandardScaler()),('clf',SVC())]),
'Decision Tree':DecisionTreeClassifier(random_state=42),
'KNN':Pipeline([('scale',StandardScaler()),('clf',KNeighborsClassifier(n_neighbors=5))])
}
for name,m in models.items():
    m.fit(X_train,y_train); print(name, m.score(X_test,y_test))
grid=GridSearchCV(DecisionTreeClassifier(random_state=42),
                  {'max_depth':[1,2,3,4,5,None],'min_samples_leaf':[1,2,3],
                   'criterion':['gini','entropy']},cv=5,scoring='accuracy')
grid.fit(X,y)
print('Best DT:',grid.best_score_,grid.best_params_)
