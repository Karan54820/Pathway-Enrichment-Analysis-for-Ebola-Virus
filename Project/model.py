import pandas as pd
from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv("pathway_enrichment_data.csv")  
X = data[['p_value', 'term_size', 'query_size', 'intersection_size', 'effective_domain_size', 'precision', 'recall']]
y = data['significant'].apply(lambda x: 1 if x == 'TRUE' else 0)  


clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X, y)


data['probability'] = clf.predict_proba(X)[:, 0]  
potential_biomarkers = data[data['probability'] >= 0.5]  

print("Potential Biomarkers:")
print(potential_biomarkers[['source', 'name', 'description', 'probability']])
