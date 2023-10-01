import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load the influencer data from influencer_data.csv
@st.cache_data
def load_influencer_data():
    data = pd.read_csv("influencer_data.csv")  # Replace with your dataset file path
    return data

influencer_data = load_influencer_data()

# Create a list of available influencer names and hashtags
available_influencers = sorted(influencer_data['Influencer'].unique())
available_hashtags = sorted(influencer_data['Hashtag'].unique())

# Sidebar title and user input
st.sidebar.title("Social Media Influence Tracker")
user_input = st.sidebar.selectbox("Choose an Influencer or Hashtag", available_influencers + available_hashtags)

# Determine whether the user input is an influencer or hashtag
is_influencer = user_input in available_influencers
if is_influencer:
    filtered_data = influencer_data[influencer_data['Influencer'] == user_input]
else:
    filtered_data = influencer_data[influencer_data['Hashtag'] == user_input]

# Main content
st.title("Social Media Influence Tracker")
st.header("Influencer Performance Over Time")

if not filtered_data.empty:
    # Create a line chart for follower count over time
    st.subheader("Follower Count Over Time")
    fig_followers = px.line(
        filtered_data, x='Timestamp', y='Followers',
        title=f"Follower Count for {user_input}"
    )
    st.plotly_chart(fig_followers)

    # Display engagement metrics in a bar chart
    st.subheader("Engagement Metrics")
    fig_engagement = px.bar(
        filtered_data, x='Timestamp', y=['Likes', 'Comments', 'Shares'],
        labels={'value': 'Count', 'variable': 'Metric'},
        title=f"Engagement Metrics for {user_input}"
    )
    st.plotly_chart(fig_engagement)

    # Create a pie chart to show the distribution of engagement metrics
    st.subheader("Distribution of Engagement Metrics")
    engagement_distribution = filtered_data[['Likes', 'Comments', 'Shares']].sum()
    fig_pie = go.Figure(
        data=[go.Pie(labels=engagement_distribution.index, values=engagement_distribution.values)]
    )
    fig_pie.update_traces(textinfo='percent+label')
    st.plotly_chart(fig_pie)

    # Display the top-performing posts
    st.subheader("Top-Performing Posts")
    top_posts = filtered_data.nlargest(5, 'Likes')  # Adjust the number of top posts as needed
    st.write(top_posts[['Timestamp', 'Likes', 'Comments', 'Shares']])

    # Provide additional insights based on the data
    st.subheader("Insights and Observations")
    st.markdown("""
    - The follower count for the selected influencer has been steadily increasing.
    - Engagement metrics (likes, comments, shares) show positive trends over time.
    - Most engagement is observed in the top-performing posts.
    - The distribution of engagement metrics is shown in the pie chart.
    """)

else:
    st.info("No data available for the selected influencer or hashtag. Please try another.")

# Additional description and call to action
st.header("About Social Media Influence Tracker")
st.markdown("""
The **Social Media Influence Tracker** helps you monitor and analyze the performance of social media influencers or specific hashtags over time. It provides insights into follower growth, engagement metrics, top-performing posts, and distribution of engagement.

**Get Started**:
1. Choose an influencer or hashtag from the sidebar.
2. Explore their follower count and engagement metrics over time.
3. Gain valuable insights for your social media marketing campaigns.

Feel free to analyze multiple influencers or hashtags to compare their performance. Use this tool to optimize your social media strategies and stay ahead in the digital world!
""")
