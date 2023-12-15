# EditAlly

## Introduction

EditAlly is a Python-based novel editing assistant utilizing advanced natural language processing techniques. It provides comprehensive editing capabilities, including chapter analysis, style and tone adjustments, dialogue enhancements, and more, tailored to the specific needs of novelists and editors.

## Features

- **Chapter Analysis**: Breaks down novels into chapters and provides detailed analysis of each.
- **Style and Tone Analysis**: Analyzes and adjusts the style and tone of the text.
- **Dialogue Enhancement**: Offers suggestions for making dialogues more natural and impactful.
- **AI-driven Suggestions**: Utilizes OpenAI's GPT-4 model for generating editing suggestions.
- **Customizable Editing**: Supports various editing functions as per user requirements.

## Application Overview

1. Input Handling:

- ✅ Accepts plain text files (.txt).
- ❗ No explicit restriction on novel size or chapter length.

2. Chapter Identification:

- ✅ Detects chapters using a regex pattern.

3. Intra-Chapter Analysis:

- 🔄 Analyzes chapters for sentence count and dialogue presence.
- ✅ Specific focus on reducing repetition and enhancing dialogue smoothness needs further implementation.

4. Overused Phrases Detection:

- ✅ Identifying and replacing overused phrases are present.
- ✅ Targeting specific phrases and chapter endings needs explicit implementation.

5. Chapter-by-Chapter Rewrite:

- 🔄 Framework for chapter-by-chapter analysis and rewriting.
- ❗ Depends on AI suggestions for maintaining essence and improving dialogue/descriptions.

6. User Interface:

- ✅ Streamlit-based user interface available beyond a basic command-line interface.

7. Memory and Continuity:

- ❗ No explicit mechanism for maintaining "memory" of changes for consistency.

### Additional Features Identified:

- ✅ Rate Limit Handling: Manages rate limits with the OpenAI API.
- ✅ Save Functionality: Saves analysis results and rewritten chapters.
- ✅ Diverse Editing Functions: Customizable editing based on functions in \_instructions.py.
- ✅ OpenAI API Integration: Uses OpenAI's GPT-4 model for editing suggestions.

### Recommendations for Improvement:

- ❗ Implement restrictions on novel size and chapter length.
- ❗ Establish a continuity and memory mechanism for changes.

#### Emoji Key:

- ✅ Completed
- 🔄 Partially Implemented/In Progress
- ❗ Needs Implementation/Improvement

## Installation

### Prerequisites

- Python 3.x
- An active OpenAI API key

### Steps

1. Clone the repository:

   ```bash
   git clone [repository-url]
   ```

2. Navigate to the project directory:

   ```bash
   cd EditAlly
   ```

3. Install dependencies:

   ```bash
   make dev-env
   ```

4. Set up your .env file with the required API keys.

### Usage

To use EditAlly, follow these steps:

1. Running the Main Application:

   Execute the main script to process your novel text.

   ```bash
   make run-local
   ```

2. Using the Streamlit Interface:

   For a more interactive experience, run the Streamlit app.

   ```bash
   make run-streamlit
   ```

### Development

Contributions to EditAlly are welcome. To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

### License

This project is licensed under the [LICENSE NAME] - see the LICENSE file for details.
