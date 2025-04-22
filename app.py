import streamlit as st
import json
import os
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(
    api_key="YOUR-API-KEY"
)

def generate_linkedin_posts(topic, feedback_history=None):
    prompt = f"Generate 3 different LinkedIn posts about {topic}. Each post should be engaging, professional, and include relevant hashtags. Number each post clearly as 'Post 1:', 'Post 2:', and 'Post 3:'. Make each post unique in style and content."
    
    if feedback_history:
        prompt += f"\nConsider this feedback from previous generations: {feedback_history}"

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a professional LinkedIn content creator."},
            {"role": "user", "content": prompt}
        ]
    )

    return completion.choices[0].message.content

def save_feedback(post_number, feedback):
    feedback_file = "feedback_history.json"
    feedback_data = {}
    
    if os.path.exists(feedback_file):
        with open(feedback_file, 'r') as f:
            feedback_data = json.load(f)
    
    if "posts" not in feedback_data:
        feedback_data["posts"] = []
    
    feedback_entry = {
        "post_number": post_number,
        "feedback": feedback
    }
    
    feedback_data["posts"].append(feedback_entry)
    
    with open(feedback_file, 'w') as f:
        json.dump(feedback_data, f, indent=4)

def main():
    st.set_page_config(
        page_title="LinkedIn Post Generator",
        page_icon="📝",
        layout="centered"
    )
    
    st.title("LinkedIn Post Generator 🚀")
    st.markdown("Generate engaging LinkedIn posts with AI assistance!")
    
    # Topic input
    topic = st.text_input("What do you want your post to be about?", 
                         placeholder="e.g., AI, Leadership, Career Growth")
    
    if topic:
        # Load feedback history if available
        feedback_history = None
        if os.path.exists("feedback_history.json"):
            with open("feedback_history.json", 'r') as f:
                feedback_data = json.load(f)
                if "posts" in feedback_data and feedback_data["posts"]:
                    feedback_history = str(feedback_data["posts"])
        
        # Generate posts button
        if st.button("Generate Posts"):
            with st.spinner("Generating posts..."):
                posts = generate_linkedin_posts(topic, feedback_history)
                
                # Display posts in tabs
                tab1, tab2, tab3 = st.tabs(["Post 1", "Post 2", "Post 3"])
                
                # Split posts into individual posts
                post_list = posts.split("---")
                
                with tab1:
                    st.markdown(post_list[0])
                    if st.button("Select Post 1", key="btn1"):
                        st.session_state.selected_post = 1
                
                with tab2:
                    st.markdown(post_list[1])
                    if st.button("Select Post 2", key="btn2"):
                        st.session_state.selected_post = 2
                
                with tab3:
                    st.markdown(post_list[2])
                    if st.button("Select Post 3", key="btn3"):
                        st.session_state.selected_post = 3
                
                # Feedback section
                if 'selected_post' in st.session_state:
                    st.subheader("Feedback")
                    feedback = st.text_area("What did you like about this post? What could be improved?")
                    
                    if st.button("Submit Feedback"):
                        if feedback.strip():
                            save_feedback(st.session_state.selected_post, feedback)
                            st.success("Thank you for your feedback! It will be used to improve future post generations.")
                            del st.session_state.selected_post
                            st.experimental_rerun()

if __name__ == "__main__":
    main() 