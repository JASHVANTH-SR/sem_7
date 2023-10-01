import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load the dataset
@st.cache_data
def load_data():
    data = pd.read_csv("Employee Satisfaction Index.csv")  # Replace with your dataset file path
    return data

data = load_data()

st.title("Understanding Employee Job Satisfaction in the Telecom Sector")
st.markdown("Exploring Factors, Trends, and Strategies for Enhancing Satisfaction")

# Sidebar filters
st.sidebar.header("Filter Data")
selected_dept = st.sidebar.selectbox("Select Department", data['Dept'].unique())
selected_education = st.sidebar.selectbox("Select Education", data['education'].unique())
selected_job_level = st.sidebar.selectbox("Select Job Level", data['job_level'].unique())

filtered_data = data[(data['Dept'] == selected_dept) & (data['education'] == selected_education) & (data['job_level'] == selected_job_level)]

# Section 1: Employee Satisfaction Overview
st.header("Section 1: Employee Satisfaction Overview")
st.write("Distribution of Job Satisfaction Ratings")

fig = px.histogram(filtered_data, x='satisfied', color='satisfied', title='Satisfaction Distribution')
st.plotly_chart(fig)

st.write("Average Salary by Job Satisfaction")
fig = px.box(filtered_data, x='satisfied', y='salary', title='Salary Distribution by Satisfaction')
st.plotly_chart(fig)

st.write("Employee Ratings vs. Awards")
fig = px.scatter(filtered_data, x='rating', y='awards', color='satisfied', title='Employee Ratings vs. Awards')
st.plotly_chart(fig)

# Section 2: Factors Influencing Satisfaction
st.header("Section 2: Factors Influencing Satisfaction")
st.write("Word Cloud of Factors Mentioned in Comments")

# You can add code to generate a word cloud here if you have comments data

# Section 3: Detailed Data Analysis
st.header("Section 3: Detailed Data Analysis")

# Interactive Data Table
st.subheader("Filtered Data")
st.dataframe(filtered_data)

# Detailed Insights and Observations
st.subheader("Insights and Observations")
st.markdown("""
- Employees with higher ratings tend to receive more awards, indicating a positive correlation between performance and recognition.
- The majority of employees are satisfied with their jobs, but there's a small percentage that isn't. Further analysis is needed to understand the factors influencing job satisfaction for dissatisfied employees.
""")

# Section 4: Employee Demographics
st.header("Section 4: Employee Demographics")

# Interactive Charts for Demographics
st.write("Age Distribution")
fig = px.histogram(filtered_data, x='age', title='Age Distribution')
st.plotly_chart(fig)

st.write("Education Levels")
edu_counts = filtered_data['education'].value_counts()
fig = px.bar(x=edu_counts.index, y=edu_counts.values, title='Education Levels')
st.plotly_chart(fig)

st.write("Location Distribution")
loc_counts = filtered_data['location'].value_counts()
fig = px.bar(x=loc_counts.index, y=loc_counts.values, title='Location Distribution')
st.plotly_chart(fig)

# Section 5: Employee Retention Strategies
st.header("Section 5: Employee Retention Strategies")
st.write("Strategies for Enhancing Employee Satisfaction")

# Provide detailed information and strategies here

# Section 6: Conclusion and Call to Action
st.header("Section 6: Conclusion and Call to Action")
st.markdown("""
In this comprehensive analysis, we explored various aspects of employee job satisfaction in the telecom sector. Key takeaways include:
- A majority of employees are satisfied with their jobs.
- Performance and recognition (awards) are positively correlated.
- Further investigation is needed to identify specific factors affecting job satisfaction for dissatisfied employees.

Enhancing employee satisfaction is essential for telecom companies to retain and motivate their workforce. Strategies such as recognition programs, addressing employee concerns, and offering opportunities for career growth can make a significant difference.

Please feel free to explore the data further using the filters and visualizations. If you have any questions or feedback, don't hesitate to reach out.

**Your Feedback Matters**: We value your thoughts and suggestions. If you have any ideas or feedback for improving employee satisfaction in the telecom sector, please share them with us.
""")

# Section 7: User Feedback and Comments
st.header("Section 7: User Feedback and Comments")
st.write("We'd love to hear from you! Share your thoughts, comments, or suggestions below:")

user_feedback = st.text_area("Your Feedback")

# You can add code to handle user feedback and comments here

