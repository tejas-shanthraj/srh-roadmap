import streamlit as st
from streamlit_option_menu import option_menu

# Set the page configuration
st.set_page_config(layout="wide", page_title="The Data Alchemists", page_icon=":crystal_ball:")

# Define the logo and navigation bar at the top of the page
def top_navbar():
    logo, navbar = st.columns([2, 8])

    with logo:
        st.image("assets/SRH_Bildung.svg", width=100)  # Replace with your logo URL
        st.write("### The Data Alchemists")

    with navbar:
        selected = option_menu(
            menu_title="",  # No title for the menu
            options=["Home", "Roadmaps", "Resources", "Projects", "Datasets", "About Us"],  # Tabs
            icons=["house", "map", "book", "briefcase", "database", "info-circle"],  # Icons for the tabs
            menu_icon="cast",  # Menu icon
            default_index=0,  # Default selected tab
            orientation="horizontal",  # Horizontal orientation
            styles={
                "nav-link-selected": {"background-color": "#FF5733", "font-weight": "bold"},  # Customize the selected tab color
                "nav-link": {"font-size": "16px"},
            }
        )
    return selected

def home_page():
    st.title("Together, We Make Data Speak!")
    st.write("""
        At The Data Alchemists, we believe in the power of data to change the world. 
        Our mission is to help aspiring data professionals unlock their potential through guided learning paths, curated resources, and community-driven support.
        Whether you're just starting out or looking to advance your skills, we're here to guide you on your journey into the realms of data science and AI.
    """)
    st.write("### Explore Our Features:")
    st.write("""
        - **Tailored Roadmaps:** Follow personalized learning paths that take you from novice to expert in data science and AI.
        - **Curated Resources:** Access a handpicked selection of tutorials, datasets, and tools to fuel your learning.
        - **Collaborative Community:** Join a vibrant community of data enthusiasts who are as passionate about insights as you are.
    """)
    st.image("https://www.example.com/data_alchemists_image.png", use_column_width=True)  # Replace with an appropriate image URL

# Roadmaps page with improved visuals
def roadmaps_page():
    st.title("Data & AI Career Roadmaps")
    st.write("Explore comprehensive roadmaps to guide your journey in data science and AI.")
    
    # Create columns for layout
    col1, col2 = st.columns([1, 2])

    with col1:
        # Input for aspiring data role
        role = st.selectbox(
            "Data Role",
            options=["Please select a role", "Data Analyst", "Data Engineer", "Data Scientist"],
            index=0,
            help="Select the role you're interested in pursuing."
        )
        
        # Dropdown for level of knowledge
        knowledge_levels = {
            "Please select a level": "",
            "Beginner": "You have no prior knowledge or experience in data science or AI.",
            "Theoretical knowledge": "You understand the basics but haven't applied them in real-world scenarios.",
            "Intermediate": "You have some experience and are looking to deepen your skills through projects.",
            "Advanced": "You have significant experience and are aiming to master a particular aspect of data science or AI."
        }
        
        knowledge_level = st.selectbox(
            "Current Knowledge Level",
            options=list(knowledge_levels.keys()),
            index=0,
            help="Hover over each option to see more details."
        )
        
        if knowledge_level != "Please select a level":
            st.markdown(f"*{knowledge_levels[knowledge_level]}*")
        
        # Multiselect for skills
        skills = st.multiselect(
            "Proficient Skills",
            options=[
                "Python", "R", "SQL", "Data Visualization", "Machine Learning", "Deep Learning", 
                "NLP", "Big Data Technologies", "Data Wrangling", "Statistics", "Cloud Computing", 
                "Data Engineering", "MLOps", "Data Warehousing", "ETL Processes", "Data Governance",
                "Data Ethics", "NoSQL Databases", "API Development", "Distributed Systems", "Feature Engineering",
                "Time Series Analysis", "Reinforcement Learning", "Bayesian Methods", "Business Intelligence",
                "Predictive Analytics", "Data Storytelling", "Dashboarding", "Data Cleaning", "Web Scraping", "DevOps",
                "Docker", "Kubernetes", "TensorFlow", "PyTorch", "Natural Language Processing", "Computer Vision"
            ],
            help="Select the skills you are proficient in."
        )

    with col2:
        st.write("### Suggested Roadmap:")
        
        # Add a gap for visual spacing
        st.write("")
        
        # Display roadmap if role and knowledge level are selected
        if role != "Please select a role" and knowledge_level != "Please select a level":
            display_roadmap(role, knowledge_level, skills)
        else:
            st.write("Please select a role and knowledge level to view a roadmap.")

# Enhanced roadmap display with expander and container
def display_roadmap(role, knowledge_level, skills):
    # Mapping the knowledge levels to roadmap stages
    level_map = {
        "Beginner": "Beginner",
        "Theoretical knowledge": "Beginner",
        "Intermediate": "Intermediate",
        "Advanced": "Advanced"
    }

    mapped_level = level_map.get(knowledge_level, "Beginner")

    roadmap_links = {
            "Data Analyst": {
                "Beginner": [
                    ("Month 1", "Learn SQL basics and data manipulation with Python or R."),
                    ("Month 2", "Introduction to data visualization (Tableau/Power BI) and Excel."),
                    ("Month 3", "Statistics fundamentals and basic exploratory data analysis."),
                    ("Month 4", "Hands-on with datasets: Analyze simple datasets to practice visualization."),
                    ("Month 5", "Build a basic dashboard and learn about business metrics."),
                    ("Month 6", "Create your first full project: Analyze sales data and present findings.")
                ],
                "Intermediate": [
                    ("Month 1", "Deep dive into SQL queries and complex joins."),
                    ("Month 2", "Advanced Excel and building visual reports."),
                    ("Month 3", "Introduction to machine learning models (Supervised Learning)."),
                    ("Month 4", "Data wrangling techniques and cleaning large datasets."),
                    ("Month 5", "Dashboard creation and reporting (Tableau/Power BI)."),
                    ("Month 6", "Advanced statistical analysis and data storytelling techniques.")
                ],
                "Advanced": [
                    ("Month 1", "Master advanced SQL, NoSQL, and database optimization techniques."),
                    ("Month 2", "Advanced machine learning models (Unsupervised Learning)."),
                    ("Month 3", "Learn predictive analytics and business forecasting."),
                    ("Month 4", "Specialization in specific industry domains (Finance, Healthcare, etc.)."),
                    ("Month 5", "Create and deploy complex dashboards for business insights."),
                    ("Month 6", "Build a portfolio of projects targeting industry-specific problems.")
                ]
            },
            "Data Engineer": {
                "Beginner": [
                    ("Month 1", "Learn basic Python and SQL for database operations."),
                    ("Month 2", "Understand ETL processes and start working with Pandas."),
                    ("Month 3", "Learn about cloud services (AWS, GCP, Azure) and their data tools."),
                    ("Month 4", "Hands-on with small data pipeline projects using Python."),
                    ("Month 5", "Introduction to data warehousing concepts."),
                    ("Month 6", "Build a complete ETL pipeline from scratch using cloud tools.")
                ],
                "Intermediate": [
                    ("Month 1", "Learn advanced Python and cloud-based data tools (S3, BigQuery)."),
                    ("Month 2", "Work on distributed computing frameworks (Hadoop, Spark)."),
                    ("Month 3", "Master workflow automation with Airflow."),
                    ("Month 4", "Build data lakes and practice with data ingestion pipelines."),
                    ("Month 5", "Deploy data pipelines and CI/CD practices."),
                    ("Month 6", "Develop a cloud-based data engineering solution end-to-end.")
                ],
                "Advanced": [
                    ("Month 1", "Deep dive into distributed systems and big data technologies."),
                    ("Month 2", "Learn real-time data processing with Kafka and Spark Streaming."),
                    ("Month 3", "Advanced data security and compliance techniques."),
                    ("Month 4", "Create complex data pipelines and apply CI/CD for data workflows."),
                    ("Month 5", "Specialize in cloud-based data engineering (AWS, GCP)."),
                    ("Month 6", "Design a scalable, secure, real-time data architecture solution.")
                ]
            },
            "Data Scientist": {
                "Beginner": [
                    ("Month 1", "Learn Python programming and basic statistics."),
                    ("Month 2", "Introduction to machine learning and linear regression."),
                    ("Month 3", "Work with popular libraries like Pandas, NumPy, and Scikit-learn."),
                    ("Month 4", "Hands-on project: Build a simple classification model."),
                    ("Month 5", "Learn about model evaluation techniques and metrics."),
                    ("Month 6", "Complete a data science project: Predicting house prices or customer churn.")
                ],
                "Intermediate": [
                    ("Month 1", "Deepen your knowledge of supervised learning techniques."),
                    ("Month 2", "Work with real-world datasets (Kaggle, UCI) for exploratory analysis."),
                    ("Month 3", "Learn about neural networks and deep learning basics."),
                    ("Month 4", "Develop a simple image classification model using TensorFlow."),
                    ("Month 5", "Experiment with Natural Language Processing (NLP) models."),
                    ("Month 6", "Build a portfolio with multiple real-world data science projects.")
                ],
                "Advanced": [
                    ("Month 1", "Master advanced machine learning algorithms (XGBoost, CatBoost)."),
                    ("Month 2", "Deep dive into unsupervised learning techniques and clustering."),
                    ("Month 3", "Specialize in a domain like NLP, computer vision, or reinforcement learning."),
                    ("Month 4", "Work on cutting-edge projects (e.g., Generative AI models)."),
                    ("Month 5", "Learn about MLOps and model deployment in production."),
                    ("Month 6", "Create a comprehensive end-to-end data science solution.")
                ]
            }
        }
    if role in roadmap_links:
        st.markdown(f"**{mapped_level} Roadmap for {role}**")
        
        for topic, details in roadmap_links[role][mapped_level]:
            with st.expander(topic):
                st.markdown(f"<div style='background-color: #f0f0f5; padding: 10px; border-radius: 5px;'>{details}</div>", unsafe_allow_html=True)
    else:
        st.write("Please select a valid role to view the roadmap.")

def resources_page():
    st.title("Learning Resources")
    st.write("Here is a curated list of resources to help you on your data journey.")

    st.write("### Data Science and AI Courses:")
    st.write("- [Coursera](https://www.coursera.org): Wide range of courses from top universities.")
    st.write("- [edX](https://www.edx.org): Professional courses from institutions like MIT, Harvard.")
    st.write("- [Udacity](https://www.udacity.com): Nanodegree programs focusing on industry-relevant skills.")
    st.write("- [Kaggle](https://www.kaggle.com/learn): Free courses and competitions to practice your skills.")
    st.write("- [DataCamp](https://www.datacamp.com): Interactive courses on data science and analytics.")
    st.write("- [Pluralsight](https://www.pluralsight.com): Tech courses with a focus on practical skills.")
    st.write("- [LinkedIn Learning](https://www.linkedin.com/learning/): Courses from industry experts on a wide range of topics.")
    
    st.write("### Books:")
    st.write("- **Python for Data Analysis** by Wes McKinney")
    st.write("- **Deep Learning** by Ian Goodfellow, Yoshua Bengio, and Aaron Courville")
    st.write("- **The Elements of Statistical Learning** by Trevor Hastie, Robert Tibshirani, and Jerome Friedman")
    st.write("- **Machine Learning Yearning** by Andrew Ng")
    st.write("- **Data Science for Business** by Foster Provost and Tom Fawcett")
    st.write("- **Storytelling with Data** by Cole Nussbaumer Knaflic")
    st.write("- **Artificial Intelligence: A Modern Approach** by Stuart Russell and Peter Norvig")

    st.write("### Blogs and Websites:")
    st.write("- [Towards Data Science](https://towardsdatascience.com)")
    st.write("- [KDnuggets](https://www.kdnuggets.com)")
    st.write("- [Analytics Vidhya](https://www.analyticsvidhya.com)")
    st.write("- [Data Science Central](https://www.datasciencecentral.com)")
    st.write("- [R Bloggers](https://www.r-bloggers.com/)")
    st.write("- [AI Trends](https://www.aitrends.com/)")

def projects_page():
    st.title("Suggested Projects")
    st.write("Based on your selected role and proficiency level, here are some project ideas:")

    st.write("### Data Analyst:")
    st.write("- **Beginner:** Create a dashboard using public datasets (e.g., COVID-19 data) to visualize trends.")
    st.write("- **Beginner:** Analyze the Titanic dataset to find correlations between passengers' demographics and their survival rates.")
    st.write("- **Intermediate:** Perform A/B testing analysis using a dataset from an e-commerce site.")
    st.write("- **Intermediate:** Analyze customer churn data and identify key factors contributing to customer retention.")
    st.write("- **Advanced:** Develop a predictive model to forecast sales using time-series data.")
    st.write("- **Advanced:** Create a data-driven report on social media sentiment analysis for a specific industry.")
    
    st.write("### Data Engineer:")
    st.write("- **Beginner:** Build an ETL pipeline to ingest, transform, and load data into a database using Python.")
    st.write("- **Beginner:** Set up a data warehouse for a small business using Google BigQuery or Amazon Redshift.")
    st.write("- **Intermediate:** Design a data lake architecture and implement it using AWS S3 and Apache Hadoop.")
    st.write("- **Intermediate:** Create a data pipeline with Apache Kafka to handle real-time streaming data.")
    st.write("- **Advanced:** Develop a CI/CD pipeline for data processing workflows using Jenkins and Docker.")
    st.write("- **Advanced:** Implement a distributed data processing system using Apache Spark for big data analysis.")
    
    st.write("### Data Scientist:")
    st.write("- **Beginner:** Train a simple classification model on the Iris dataset and evaluate its performance.")
    st.write("- **Beginner:** Develop a regression model to predict house prices using the Boston housing dataset.")
    st.write("- **Intermediate:** Build a machine learning model to predict customer churn for a telecom company.")
    st.write("- **Intermediate:** Create a sentiment analysis model using NLP techniques on Twitter data.")
    st.write("- **Advanced:** Develop a deep learning model for image classification using the CIFAR-10 dataset.")
    st.write("- **Advanced:** Implement a reinforcement learning agent to solve a simple game (e.g., CartPole).")

def datasets_page():
    st.title("Datasets")
    st.write("Here are some datasets you can use for your projects:")

    datasets = {
        "Data Analyst": [
            ("COVID-19 Dataset", "https://github.com/CSSEGISandData/COVID-19"),
            ("Titanic Dataset", "https://www.kaggle.com/c/titanic"),
            ("E-commerce A/B Testing Dataset", "https://www.kaggle.com/olistbr/brazilian-ecommerce"),
            ("Customer Churn Dataset", "https://www.kaggle.com/blastchar/telco-customer-churn"),
            ("Retail Sales Time Series Data", "https://fred.stlouisfed.org/series/RSXFS"),
            ("Social Media Sentiment Analysis Dataset", "https://www.kaggle.com/datasets/yash612/social-media-sentiment-dataset")
        ],
        "Data Engineer": [
            ("Sample ETL Dataset", "https://datahub.io/core/airport-codes"),
            ("Google BigQuery Public Datasets", "https://cloud.google.com/bigquery/public-data"),
            ("AWS S3 Sample Datasets", "https://registry.opendata.aws/"),
            ("Apache Kafka Sample Data", "https://github.com/confluentinc/kafka-streams-examples"),
            ("Apache Hadoop Sample Data", "https://github.com/hortonworks/hadoop-samples"),
            ("Apache Spark Datasets", "https://github.com/databricks/Spark-The-Definitive-Guide")
        ],
        "Data Scientist": [
            ("Iris Dataset", "https://archive.ics.uci.edu/ml/datasets/iris"),
            ("Boston Housing Dataset", "https://www.kaggle.com/c/boston-housing"),
            ("Telecom Customer Churn Dataset", "https://www.kaggle.com/blastchar/telco-customer-churn"),
            ("Twitter Sentiment Analysis Dataset", "https://www.kaggle.com/kazanova/sentiment140"),
            ("CIFAR-10 Dataset", "https://www.cs.toronto.edu/~kriz/cifar.html"),
            ("CartPole Reinforcement Learning Dataset", "https://gym.openai.com/envs/CartPole-v1/")
        ]
    }

    role = st.selectbox("Select your role to find relevant datasets:", options=["Data Analyst", "Data Engineer", "Data Scientist"])

    if role:
        st.write(f"### Datasets for {role}:")
        for dataset_name, dataset_link in datasets[role]:
            st.markdown(f"- [{dataset_name}]({dataset_link})")

def about_us_page():
    st.title("About Us")
    st.write("""
        The Data Alchemists is a community-driven platform designed to guide aspiring data professionals on their journey. 
        Our mission is to make data education accessible, engaging, and effective by providing tailored learning paths, curated resources, and collaborative project opportunities.
    """)

# Map the selected tab to the corresponding page
page_function_mapping = {
    "Home": home_page,
    "Roadmaps": roadmaps_page,
    "Resources": resources_page,
    "Projects": projects_page,
    "Datasets": datasets_page,
    "About Us": about_us_page
}

selected_page = top_navbar()
page_function_mapping[selected_page]()
