import streamlit as st
st.set_page_config(layout="wide")
from streamlit_option_menu import option_menu

# Define the logo and navigation bar at the top of the page
def top_navbar():
    logo, navbar = st.columns([2, 8])

    with logo:
        st.image("assets\SRH_Bildung.svg", width=100)  # Replace with your logo URL
        st.write("### The Data Alchemists")

    with navbar:
        selected = option_menu(
            menu_title="",  # No title for the menu
            options=["Home", "Roadmaps", "Resources", "About Us"],  # Tabs
            icons=["house", "map", "book", "info-circle"],  # Icons for the tabs
            menu_icon="cast",  # Menu icon
            default_index=0,  # Default selected tab
            orientation="horizontal",  # Horizontal orientation
            styles={
                "nav-link-selected": {"background-color": "#FF5733"},  # Customize the selected tab color
            }
        )
    return selected

def home_page():
    st.title("Together, We Make Data Speak !")
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

# Define the enhanced roadmaps page
def roadmaps_page():
    st.title("Data & AI Career Roadmaps")
    st.write("Explore comprehensive roadmaps to guide your journey in data science and AI.")

    # Input for aspiring data role
    role = st.text_input("What data role are you aspiring to?", placeholder="e.g., Data Scientist, Data Engineer, etc.")
    
    # Dropdown for level of knowledge
    knowledge_levels = {
        "I'm a complete beginner (starting from scratch)": "You have no prior knowledge or experience in data science or AI.",
        "I have theoretical knowledge but no practical exposure": "You understand the basics but haven't applied them in real-world scenarios.",
        "Intermediate (Looking to get my hands dirty on data projects)": "You have some experience and are looking to deepen your skills through projects.",
        "Advanced (Seeking to specialize in a specific area)": "You have significant experience and are aiming to master a particular aspect of data science or AI."
    }
    
    knowledge_level = st.selectbox(
        "What is your current level of knowledge?",
        options=list(knowledge_levels.keys()),
        help="Hover over each option to see more details."
    )
    
    st.markdown(f"*{knowledge_levels[knowledge_level]}*")

    # Multiselect for skills
    skills = st.multiselect(
        "What skills are you good at?",
        options=["Python", "R", "SQL", "Data Visualization", "Machine Learning", "Deep Learning", "NLP", "Big Data Technologies", "Data Wrangling", "Statistics", "Cloud Computing", "Data Engineering"],
        help="Select the skills you are proficient in."
    )
    
    st.write("### Suggested Path:")
    st.write("Based on your inputs, we recommend the following roadmap:")
    
    # Here you could add logic to generate a suggested roadmap based on the user's inputs
    # For now, just a placeholder text
    if role and knowledge_level and skills:
        st.write(f"As an aspiring {role}, with your current level being '{knowledge_level}', and your skills in {', '.join(skills)}, consider starting with hands-on projects to gain practical experience.")
    else:
        st.write("Please fill out all fields to get a personalized roadmap suggestion.")

# Define other pages (resources, about us)
def resources_page():
    st.title("Learning Resources")
    st.write("Access curated study materials, datasets, and other resources to aid your learning.")
    st.write("""
        - [Python for Data Science](https://www.example.com/python-course)
        - [Machine Learning Datasets](https://www.example.com/ml-datasets)
        - [Data Visualization Tools](https://www.example.com/data-viz)
    """)

def about_us_page():
    st.title("About The Data Alchemists")
    st.write("Turning Raw Data into Gold")
    st.write("""
        The Data Alchemists is a collective of passionate individuals who are dedicated to unlocking the hidden potential within data. 
        Our team is driven by the belief that data is the new alchemy, and through careful analysis, we can turn raw data into valuable insights that make a difference.
        
        **Our Vision:**
        We envision a world where anyone with the drive to learn can harness the power of data to create impactful solutions. 
        Our platform is designed to empower individuals at all stages of their data journey, offering them the tools, knowledge, and support they need to succeed.

        **What We Offer:**
        - **Expert Guidance:** Benefit from the expertise of seasoned data professionals who are eager to share their knowledge.
        - **Community Engagement:** Connect with like-minded individuals who are on the same path as you, and collaborate to achieve your goals.
        - **Continuous Learning:** Stay ahead of the curve with access to the latest trends, technologies, and techniques in the world of data science and AI.
        
        Join us in our quest to transform data into actionable insights and become a part of The Data Alchemists.
    """)
    st.write("""
        **Contact Us:**
        - Email: thedataalchemists@srh.org
        - Office: LGS T220, The Data Lab
    """)


# Main function to control the flow of the application
def main():
    selected = top_navbar()

    if selected == "Home":
        home_page()
    elif selected == "Roadmaps":
        roadmaps_page()
    elif selected == "Resources":
        resources_page()
    elif selected == "About Us":
        about_us_page()

if __name__ == "__main__":
    main()
