import pandas as pd
import matplotlib.pyplot as plt

attendance = pd.read_csv('data/attendance.csv')
marks = pd.read_csv('data/marks.csv')

# Merge data
merged = pd.merge(attendance, marks, on='StudentID')

# Plot attendance vs average marks
merged['AverageMarks'] = merged[['Maths', 'Science', 'English']].mean(axis=1)
plt.scatter(merged['Attendance'], merged['AverageMarks'])
plt.xlabel('Attendance (%)')
plt.ylabel('Average Marks')
plt.title('Attendance vs Performance')
plt.grid(True)
plt.show()
