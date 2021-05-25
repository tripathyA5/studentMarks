import pandas as pd
import csv
import plotly.express as px
import statistics
df = pd.read_csv('marks.csv')
studentPerf = df.groupby(["student_id","level"],as_index=False)["attempt"].mean()
fig = px.scatter(studentPerf, x="student_id",y="level",size="attempt",color ="attempt")

fig.show()
print(studentPerf)