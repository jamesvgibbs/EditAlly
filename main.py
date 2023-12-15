import logging

from editally import EditAlly
import json

def process_chapters(editally, novel_text):
    if novel_text:
        logging.info(f"Total word count: {editally.word_count(novel_text)}")
        chapters = editally.find_chapters(novel_text)
        logging.info(f"Found {len(chapters)} chapters.")

        for i, chapter in enumerate(chapters):
            editally.process_chapter(i + 1, chapter, selected_functions=['Rewrite: Remove Chaff'], file_out=True)
    else:
        logging.error("No novel text found.")

def process_suggestions(editally, novel_text):
    if novel_text:
        logging.info(f"Total word count: {editally.word_count(novel_text)}")
        chapters = editally.find_chapters(novel_text)
        logging.info(f"Found {len(chapters)} chapters.")

        for i, chapter in enumerate(chapters):         
            editally.apply_ai_suggestions(chapter, i + 1, read_json())
    else:
        logging.error("No novel text found.")

def read_json():
    json_path = "novel/analysis.json"
    try:
        with open(json_path, 'r', encoding='utf-8') as file:
            file_read = file.read()
            return json.loads(file_read)
    except FileNotFoundError:
        logging.error(f"JSON File not found: {json_path}")
        return None

def main():
    novel_path = "novel/test.txt"  
    genre_path = "novel/genre.txt"
    style_path = "novel/style.txt"
    def read_novel():
        try:
            with open(novel_path, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            logging.error(f"Novel File not found: {novel_path}")
            return None
        
    def read_style():
        try:
            with open(style_path, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            logging.error(f"Style File not found: {style_path}")
            return None
        
    def read_genre():
        try:
            with open(genre_path, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            logging.error(f"Genre File not found: {genre_path}")
            return None
        
    editally = EditAlly(
        model="gpt-4-1106-preview",
        novel=read_novel(),
        style=read_style(),
        genre=read_genre()
    )
    novel_text = editally.novel
    # process_chapters(editally, novel_text)
    process_suggestions(editally, novel_text)
    

if __name__ == "__main__":
    main()