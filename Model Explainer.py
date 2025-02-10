from sklearn.ensemble import RandomForestClassifier
from explainerdashboard import ClassifierExplainer, ExplainerDashboard 
from explainerdashboard.datasets import titanic_survive, feature_descriptions

# Load the Titanic dataset
X_train, y_train, X_test, y_test = titanic_survive()

# Train a random forest model
model = RandomForestClassifier().fit(X_train, y_train)

# Create an explainer for the model
explainer = ClassifierExplainer(
    model, X_test, y_test,
    cats=["Sex", "Deck", "Embarked"],
    descriptions=feature_descriptions,
    labels=['Not Survived', 'Survived']
)

# Run the dashboard
ExplainerDashboard(explainer).run()


