import pandas as pd
from sklearn.linear_model import LinearRegression

attendance = pd.read_csv('data/attendance.csv')
marks = pd.read_csv('data/marks.csv')

merged = pd.merge(attendance, marks, on='StudentID')
merged['AverageMarks'] = merged[['Maths', 'Science', 'English']].mean(axis=1)

X = merged[['Attendance']]
y = merged['AverageMarks']

model = LinearRegression()
model.fit(X, y)

predicted = model.predict(X)
print('Predicted Scores:', predicted)
