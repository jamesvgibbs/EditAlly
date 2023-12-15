import difflib
import json
import os
import re
import logging
from dotenv import load_dotenv
from openai import OpenAI
import time
from _instructions import instructions

load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

READ_PASSAGE = f"""
        Read the passage provided, and then perform a comprehensive line edit, following all instructions of 
        the given plugin framework format, then write the corrected prose in NON-JSON format."""

FINAL_INSTRUCTIONS="""Perform a comprehensive line edit, following all instructions of the given plugin framework format, 
        then write the corrected prose in NON-JSON format. Dialogue shall allows contain double quotes. 
        Adhere to this {genre} and {style}."""

RESULTS_DIR = "analysis_results"


class EditAlly:
    def __init__(self, novel, style, genre, model="gpt-4-1106-preview"):
        self.model = model
        self.rate_limit = 0
        self.rate_limit_reset = 0
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        self.client = OpenAI()
        self.novel = novel
        self.style = style
        self.genre = genre
        self.logger.info("Initialized")

    @staticmethod
    def find_chapters(text):
        chapter_pattern = re.compile(r'\nChapter\s*\d+', re.IGNORECASE)
        chapters = chapter_pattern.split(text)
        return [chapter.strip() for chapter in chapters if chapter.strip()]
    
    @staticmethod
    def word_count(text):
        return len(text.split())
    
    def analyze_chapter(self, chapter):
        sentences = chapter.split('.')
        num_sentences = len(sentences)
        dialogues = [sentence for sentence in sentences if '"' in sentence]
        num_dialogues = len(dialogues)

        # Placeholder for more advanced analysis
        # This could be expanded with more sophisticated NLP techniques

        return {
            "num_sentences": num_sentences,
            "num_dialogues": num_dialogues
        }

    def wait_for_rate_limit(self):
        if self.rate_limit_reset > 0:
            time_to_wait = self.rate_limit_reset - time.time()
            if time_to_wait > 0:
                self.logger.info(f"Waiting for rate limit reset: {time_to_wait:.2f} seconds")
                time.sleep(time_to_wait)
    
    def save_rewrite(self, chapter_number, rewritten_text):
        output_dir = "rewritten_chapters"
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, f"chapter_{chapter_number}_rewrite.txt")

        with open(output_path, "w", encoding="utf-8") as file:
            file.write(rewritten_text)
        self.logger.info(f"Rewritten chapter {chapter_number} saved to {output_path}")

    def save_analysis_results(self, chapter_number, edited_text, analysis_data):
        try:
            self.logger.debug("Saving analysis results")
            os.makedirs(RESULTS_DIR, exist_ok=True)

            if isinstance(edited_text, list):
                edited_text = ' '.join(edited_text)

            with open(f"{RESULTS_DIR}/chapter_{chapter_number}_edit.txt", "w", encoding="utf-8") as file:
                file.write(edited_text)

            with open(f"{RESULTS_DIR}/chapter_{chapter_number}_analysis.json", "w", encoding="utf-8") as file:
                json.dump(analysis_data, file, indent=4)
        except Exception as e:
            self.logger.error(f"Error saving analysis results: {e}")
            self.logger.error(f"Edited text: {edited_text}")
            self.logger.error(f"Analysis data: {analysis_data}")

    def read_saved_analysis_results(self):
        results_dir = "analysis_results"
        aggregated_data = {}

        for filename in os.listdir(results_dir):
            if filename.endswith("_analysis.json"):
                with open(f"{results_dir}/{filename}", "r") as file:
                    chapter_data = json.load(file)
                    # Aggregate data as needed for novel analysis
                    # ...

        return aggregated_data

    def openai_chat_completion(self, messages):
            self.logger.debug("OpenAI Chat Completion")
            self.wait_for_rate_limit()
            
            responses = self.client.chat.completions.create(
                model=self.model, 
                messages=messages,
                # temperature=0,
            )
            results = [
                choice.message.content.strip()
                for choice in responses.choices
                if choice.message.role == "assistant"
            ]
            return results

    def get_openai_suggestions(self, chapter, selected_functions=None):
        try:
            system_message = (
                f"You are an assistant skilled in literary analysis and editing. "
                f"Analyze the following chapter for narrative structure, dialogue quality, and language use, "
                f"adhering to these genre and style guidelines: '{self.genre}' and '{self.style}'.\n\n"
            )

            if selected_functions:
                system_message += "Apply the following editing functions to the chapter and provide suggestions in the specified JSON format. "
                system_message += "Focus on the objectives of each function:\n\n"
                
                for function in selected_functions:
                    if function in instructions:  
                        # system_message += f"'{function}': {instructions[function]}\n\n"
                        system_message += f"'{function}': {instructions[function]['summary']}\n\n"

            system_message += "Avoid changing the core storyline or characters, and maintain a respectful tone.\n\n" \
                            "Provide your output in the following JSON format:\n" \
                            "{\n" \
                            "    'suggestions': [\n" \
                            "        {\n" \
                            "            'tool': '[Name of the editing tool]',\n" \
                            "            'location': '[Specific text passage that needs editing]'\n" \
                            "        },\n" \
                            "        // Additional suggestions here\n" \
                            "    ]\n" \
                            "}\n\n"
            
            prompt = f"Here is the chapter text:\n\n{chapter}\n\nBased on the instructions, provide specific editing suggestions in the above JSON format."

            messages = [{
                'role': 'system',
                'content': system_message
            }, {
                'role': 'user',
                'content': prompt
            }]
            
            responses = self.openai_chat_completion(messages)
            return responses
        except Exception as e:
            logging.error(f"OpenAI API error: {e}")
            return None

    def send_edit_request(self, chapter, prompt_type):
        if prompt_type in instructions:
            system_message = f"{READ_PASSAGE} {instructions[prompt_type]['details']}"
        else:
            system_message = ""  

        user_prompt = f"""
        Read this passage:

        {chapter}

        {FINAL_INSTRUCTIONS.format(genre=self.genre, style=self.style)}
        """

        messages = [{
                'role': 'system',
                'content': system_message
            }, {
                'role': 'user',
                'content': user_prompt
            }]
        return self.openai_chat_completion(messages)
    
    def analyze_character_consistency(self, chapter):
        prompt = f"Analyze this text for character consistency in dialogue, descriptions, and actions:\n\n{chapter}"
        messages = [{
            'role': 'system',
            'content': 'You are an assistant skilled in character analysis in literature.'
        }, {
            'role': 'user',
            'content': prompt
        }]
        return self.openai_chat_completion(messages)
    
    def check_plot_continuity(self, chapter):
        prompt = f"Check this text for plot continuity and logical progression:\n\n{chapter}"
        messages = [{
            'role': 'system',
            'content': 'You are an assistant skilled in analyzing plot continuity in literature.'
        }, {
            'role': 'user',
            'content': prompt
        }]
        return self.openai_chat_completion(messages)

    def analyze_style_and_tone(self, chapter):
        prompt = f"""Analyze this text for style and tone, ensuring alignment with the overall style of the novel: {self.style}\n\n{chapter}"""
        messages = [{
            'role': 'system',
            'content': 'You are an assistant skilled in literary style and tone analysis.'
        }, {
            'role': 'user',
            'content': prompt
        }]
        return self.openai_chat_completion(messages)
    
    def enhance_dialogue(self, chapter):
        prompt = f"Suggest enhancements for the dialogues in this text for naturalness, character voice, and impact:\n\n{chapter}"
        messages = [{
            'role': 'system',
            'content': 'You are an assistant skilled in dialogue writing and enhancement.'
        }, {
            'role': 'user',
            'content': prompt
        }]
        return self.openai_chat_completion(messages)

    def identify_theme_and_symbolism(self, chapter):
        prompt = f"Identify themes and symbolism in this text, and suggest ways to make them more prominent or coherent:\n\n{chapter}"
        messages = [{
            'role': 'system',
            'content': 'You are an assistant skilled in identifying themes and symbolism in literature.'
        }, {
            'role': 'user',
            'content': prompt
        }]
        return self.openai_chat_completion(messages)

    def apply_ai_suggestions(self, chapter_text, chapter_number, suggestions_response, progress_callback=None):
        try:
            if isinstance(suggestions_response, list) and len(suggestions_response) > 0:
                cleaned_response = suggestions_response[0].replace('```json\n', '').replace('\n```', '').strip()
            else:
                cleaned_response = suggestions_response.replace('```json\n', '').replace('\n```', '').strip()
            suggestions_json = json.loads(cleaned_response)
        except json.JSONDecodeError as e:
            self.logger.error(f"Error decoding JSON: {e}")
            return chapter_text
        
        suggestions = suggestions_json.get('suggestions', [])
        total_suggestions = len(suggestions)
        
        for index, suggestion in enumerate(suggestions):
            tool = suggestion.get('tool')
            location = suggestion.get('location')
            self.logger.info("--------------------------------")
            self.logger.info(f"Suggestion: {tool} - {location}")

            edited_text = self.send_edit_request(location, tool)

            self.logger.info(f"Edited Text: {edited_text[0]}")
            self.logger.info("--------------------------------")

            if edited_text:
                chapter_text = self.replace_text(chapter_text, edited_text[0], location)
            
            if progress_callback:
                progress = ((index + 1) / total_suggestions) * 100
                progress_callback(progress)

        self.save_analysis_results(chapter_number, chapter_text, cleaned_response)

        return chapter_text
    
    def replace_text(self, original_text, new_text, location):
        return original_text.replace(location, new_text)
    
    def create_diff_file(self, original, edited):
        original_lines = original.split('\n')
        edited_lines = edited.split('\n')
        diff_view = ""
        for orig, edit in zip(original_lines, edited_lines):
            diff_view += f"Original: {orig}\nEdited: {edit}\n\n"
        return diff_view
    
    def create_diff_view(self, original, edited):
        original_lines = original.split('\n') if '\n' in original else [original]
        edited_lines = edited.split('\n') if '\n' in edited else [edited]

        diff = difflib.unified_diff(
            original_lines, 
            edited_lines, 
            lineterm='', 
            fromfile='Original', 
            tofile='Edited'
        )
        return '\n'.join(diff)
    
    def process_chapter(self, chapter_number, chapter_text, selected_functions=None, file_out=False, progress_callback=None):
        initial_analysis = self.analyze_chapter(chapter_text)
        self.logger.debug(f"Initial Analysis Chapter {chapter_number}: {initial_analysis}")
        suggestions_response = self.get_openai_suggestions(chapter_text, selected_functions)
        edited_text = self.apply_ai_suggestions(chapter_text, chapter_number, suggestions_response, progress_callback)
        
        if file_out:
            final_analysis = self.analyze_chapter(edited_text)
            self.logger.debug(f"Final Analysis Chapter {chapter_number}: {final_analysis}")

            diff_view = self.create_diff_file(chapter_text, edited_text)
            self.save_rewrite(chapter_number, diff_view)
        
        return edited_text

