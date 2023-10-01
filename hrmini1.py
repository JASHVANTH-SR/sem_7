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
sample_comments = [
    "Great work-life balance, love the flexibility.",
    "The management needs to improve communication.",
    "I appreciate the recognition I received for my performance.",
    "The team collaboration is excellent.",
    "More opportunities for career growth would be appreciated.",
    "I feel valued and supported by my colleagues.",
]

# Display sample comments as a word cloud
# You may need to install the 'wordcloud' library: pip install wordcloud
from wordcloud import WordCloud
import matplotlib.pyplot as plt

comment_text = ' '.join(sample_comments)
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(comment_text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("Word Cloud of Employee Comments")
st.pyplot(plt)

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
st.write("Employee retention is crucial for the success of telecom companies. High employee turnover can lead to increased costs and disruptions. Here are some strategies to enhance employee satisfaction and retention:")

# Strategy 1: Recognition Programs
st.subheader("1. Recognition Programs")
st.write("Recognizing and rewarding employees for their contributions can boost morale and job satisfaction.")
st.write("Key Points:")
st.write("- Implement employee recognition programs to acknowledge outstanding performance.")
st.write("- Offer incentives, awards, or bonuses for achieving milestones.")
st.write("- Create a culture of appreciation and peer recognition.")

# Strategy 2: Career Growth Opportunities
st.subheader("2. Career Growth Opportunities")
st.write("Providing avenues for career advancement and skill development can motivate employees to stay.")
st.write("Key Points:")
st.write("- Offer training and development programs to enhance employees' skills.")
st.write("- Create clear career paths with opportunities for promotions.")
st.write("- Encourage continuous learning and skill-building.")

# Strategy 3: Work-Life Balance
st.subheader("3. Work-Life Balance")
st.write("Balancing work and personal life is essential for employee well-being and job satisfaction.")
st.write("Key Points:")
st.write("- Implement flexible work arrangements, such as remote work or flexible hours.")
st.write("- Promote the importance of taking breaks and vacations.")
st.write("- Provide resources for managing stress and maintaining a healthy work-life balance.")

# Strategy 4: Communication and Feedback
st.subheader("4. Communication and Feedback")
st.write("Open and transparent communication channels help address employee concerns and improve job satisfaction.")
st.write("Key Points:")
st.write("- Establish regular feedback mechanisms, such as surveys and one-on-one meetings.")
st.write("- Act on employee feedback and address concerns promptly.")
st.write("- Foster a culture of open communication and transparency.")

# Strategy 5: Employee Well-being Programs
st.subheader("5. Employee Well-being Programs")
st.write("Supporting employee well-being can lead to increased job satisfaction and productivity.")
st.write("Key Points:")
st.write("- Offer health and wellness programs, including mental health support.")
st.write("- Provide access to resources for stress management and relaxation.")
st.write("- Encourage a healthy lifestyle through fitness programs and initiatives.")

# Strategy 6: Inclusivity and Diversity
st.subheader("6. Inclusivity and Diversity")
st.write("Creating an inclusive and diverse workplace fosters a sense of belonging and satisfaction among employees.")
st.write("Key Points:")
st.write("- Promote diversity in hiring and leadership positions.")
st.write("- Implement diversity and inclusion training programs.")
st.write("- Celebrate cultural and individual differences.")

# Strategy 7: Employee Recognition and Feedback
st.subheader("7. Employee Recognition and Feedback")
st.write("Recognize and celebrate employee achievements and milestones.")
st.write("Key Points:")
st.write("- Hold regular appreciation events or ceremonies.")
st.write("- Encourage peer-to-peer recognition.")
st.write("- Share success stories and recognize long-term employees.")

# Strategy 8: Continuous Improvement
st.subheader("8. Continuous Improvement")
st.write("Regularly review and refine employee satisfaction initiatives.")
st.write("Key Points:")
st.write("- Analyze employee feedback and satisfaction survey results.")
st.write("- Adjust strategies based on changing employee needs and preferences.")
st.write("- Stay up-to-date with industry best practices.")

# Conclusion
st.markdown("Implementing these strategies can contribute to higher employee satisfaction and retention rates in the telecom sector. Remember that each organization is unique, and tailoring these strategies to your company's specific culture and needs is essential for success.")

# Encourage Action
st.write("Take the first step in enhancing employee satisfaction and retention in your telecom company. Evaluate your current practices and start implementing these strategies today!")


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

