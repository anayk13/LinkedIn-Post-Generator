from openai import OpenAI
import json
import os
Key = st.secrets["OPENAI_API_KEY"]

# Initialize OpenAI client
client = OpenAI(
    api_key=Key
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
    print("Welcome to the LinkedIn Post Generator!")
    topic = input("What do you want your post to be about? ")
    print(f"\nGenerating 3 different posts about {topic}...\n")
    
    # Load feedback history if available
    feedback_history = None
    if os.path.exists("feedback_history.json"):
        with open("feedback_history.json", 'r') as f:
            feedback_data = json.load(f)
            if "posts" in feedback_data and feedback_data["posts"]:
                feedback_history = str(feedback_data["posts"])
    
    # Generate posts
    posts = generate_linkedin_posts(topic, feedback_history)
    print("Generated Posts:\n")
    print(posts)
    
    # Get user preference
    while True:
        try:
            preferred_post = int(input("\nWhich post do you prefer? (Enter 1, 2, or 3): "))
            if preferred_post in [1, 2, 3]:
                break
            print("Please enter 1, 2, or 3.")
        except ValueError:
            print("Please enter a valid number (1, 2, or 3).")
    
    # Get feedback
    feedback = input("\nWhat did you like about this post? What could be improved? ")
    if feedback.strip():
        save_feedback(preferred_post, feedback)
        print("\nThank you for your feedback! It will be used to improve future post generations.")

if __name__ == "__main__":
    main()
