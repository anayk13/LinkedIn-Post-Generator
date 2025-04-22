# LinkedIn Post Generator 🚀

A Streamlit-based web application that generates engaging LinkedIn posts using AI, with a built-in feedback system to improve post quality over time.

## Prerequisites

Before you begin, you'll need:
- Python 3.7 or higher
- An OpenAI API key (get one from [OpenAI's website](https://platform.openai.com/api-keys))

## Features

- **AI-Powered Post Generation**: Generate 3 unique LinkedIn posts on any topic
- **Interactive UI**: Clean and intuitive Streamlit interface
- **Feedback System**: Provide feedback on generated posts to improve future generations
- **Persistent Feedback Storage**: Feedback is saved and used to enhance future post generations
- **Multiple Post Styles**: Each generation includes posts with different tones and perspectives

## Project Structure

```
LinkedIn-Post-Generator/
├── app.py              # Main Streamlit application
├── ai.py              # Core AI post generation logic
├── feedback_history.json  # Stores user feedback
└── README.md          # Project documentation
```

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd LinkedIn-Post-Generator
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Set up your OpenAI API key:
   - Open `app.py` in your text editor
   - Replace the placeholder API key with your own:
   ```python
   client = OpenAI(
       api_key="your-api-key-here"  # Replace with your actual OpenAI API key
   )
   ```
   - Save the file

## Usage

1. Start the Streamlit application:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the provided local URL (typically http://localhost:8501)

3. Using the application:
   - Enter your desired topic in the text input field
   - Click "Generate Posts" to create 3 unique LinkedIn posts
   - Review the posts in the tabs
   - Select your preferred post
   - Provide feedback on what you liked and what could be improved
   - Submit your feedback to help improve future generations

## How It Works

### Post Generation
- The application uses OpenAI's GPT model to generate three unique LinkedIn posts
- Each post is generated with a different style and perspective
- Posts include relevant hashtags and are formatted for LinkedIn

### Feedback System
- User feedback is stored in `feedback_history.json`
- The feedback is used to improve future post generations
- Feedback includes both positive aspects and areas for improvement

### UI Components
- **Topic Input**: Text field for entering the desired post topic
- **Generate Button**: Triggers the post generation process
- **Post Tabs**: Three tabs displaying different post variations
- **Selection Buttons**: Allow users to choose their preferred post
- **Feedback Form**: Text area for providing feedback on selected posts

## Dependencies

- streamlit
- openai
- json
- os

## Security Note

For production use, it's recommended to:
1. Store your OpenAI API key in environment variables
2. Add `feedback_history.json` to your `.gitignore` file
3. Never commit API keys or sensitive data to version control

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- OpenAI for providing the GPT model
- Streamlit for the web application framework 