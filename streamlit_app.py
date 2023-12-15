import difflib
import os
from editally import EditAlly
import streamlit as st
from _instructions import instructions

if 'testing_mode' not in st.session_state:
    st.session_state['testing_mode'] = False
    
st.set_page_config(
    page_title="EditAlly - Novel Editing Assistant",
    layout="wide"
)

st.sidebar.title('EditAlly Settings')

if 'progress' not in st.session_state:
    st.session_state['progress'] = 0

def process_chapters(text):
    chapters = EditAlly.find_chapters(text)
    st.session_state['chapters'] = chapters
    st.session_state['chapter_data'] = {i: {'original': chap, 'edited': None} for i, chap in enumerate(chapters, start=1)}

def save_edited_text(chapter_number, edited_text):
    edited_dir = "edited_chapters"
    os.makedirs(edited_dir, exist_ok=True)

    with open(f"{edited_dir}/chapter_{chapter_number}_edit.txt", "w") as file:
        file.write(edited_text)
    st.success(f"Chapter {chapter_number} edited text saved successfully.")

def create_side_by_side_diff_view(original, edited):
    diff = difflib.ndiff(original.splitlines(keepends=True), edited.splitlines(keepends=True))

    left_column, right_column = [], []

    for line in diff:
        if line.startswith('-'):
            left_column.append(f"<span style='background-color: rgba(239, 67, 67, 0.4);'>{line[2:]}</span>")
        elif line.startswith('+'):
            right_column.append(f"<span style='background-color: rgba(0, 179, 119, 0.4);'>{line[2:]}</span>")
        elif line.startswith(' '):
            common_text = line[2:]
            left_column.append(common_text)
            right_column.append(common_text)

    left_html = "<br>".join(left_column)
    right_html = "<br>".join(right_column)

    return left_html, right_html

def update_progress_bar(progress):
    st.session_state['progress'] = progress / 100
    progress_bar.progress(st.session_state['progress'])

def mock_process_chapter(chapter_number, chapter_text, selected_functions, progress_callback):
    # Simulate some processing
    edited_text = chapter_text + "\n\n[This is a mocked edit for testing. Chapter: {}]".format(chapter_number)
    # Update progress bar
    progress_callback(100)
    return edited_text


with st.sidebar:
    st.session_state['testing_mode'] = st.checkbox('Enable Testing Mode')
    st.subheader('Upload Novel')
    uploaded_file = st.file_uploader("Upload Novel", type=['txt'])
    if uploaded_file is not None:
        novel_text = uploaded_file.getvalue().decode("utf-8")
        st.session_state['novel_text'] = novel_text  
        process_chapters(novel_text)
        st.write(f"Found {len(st.session_state['chapters'])} chapters.")
        st.success("Novel uploaded successfully!")

    analysis_functions = list(instructions.keys())

    if 'selected_functions' not in st.session_state:
        st.session_state['selected_functions'] = []

    st.subheader('Select Analysis Functions')
    for func_name in analysis_functions:
        if st.checkbox(func_name, key=func_name):
            if func_name not in st.session_state['selected_functions']:
                st.session_state['selected_functions'].append(func_name)
        else:
            if func_name in st.session_state['selected_functions']:
                st.session_state['selected_functions'].remove(func_name)


    st.subheader('Set Genre and Style')
    default_genre = "Young Adult Science Fiction and Action-Adventure with themes of Friendship, Identity, Romance, Humor"
    default_style = "Tense urgency in third-person limited present tense. Fast-paced, direct dialogue; selective, "
    default_style += "vivid descriptions supporting action. Varied sentences enhance rhythm, short for impact. Avoid "
    default_style += "adverbs for tight prose. Use foreshadowing, symbolism subtly; chapter hooks for momentum. "
    default_style += "Balance action and introspection."

    if 'genre' not in st.session_state or not st.session_state['genre']:
        st.session_state['genre'] = default_genre

    if 'style' not in st.session_state or not st.session_state['style']:
        st.session_state['style'] = default_style

    genre = st.text_area('Genre', value=st.session_state['genre'], height=100)
    style = st.text_area('Writing Style', value=st.session_state['style'], height=200)
    st.session_state['genre'] = genre
    st.session_state['style'] = style

    st.markdown(
    "[![smile please](https://forthebadge.com/images/badges/makes-people-smile.svg)](https://www.linkedin.com/in/jimgibbs/)")


st.title('EditAlly - Novel Editing Assistant')

if 'novel_text' in st.session_state:
    novel_text = st.session_state['novel_text']
    st.success("Novel loaded from previous session.")
    if 'chapters' not in st.session_state:
        process_chapters(novel_text)
else:
    novel_text = None

progress_bar = st.empty()
progress_bar = st.progress(st.session_state['progress'])

if 'chapters' in st.session_state:
    chapter_options = [f"Chapter {i}" for i in range(1, len(st.session_state['chapters']) - 1)]
    selected_option = st.selectbox('Select a chapter to edit', chapter_options)
    chapter_number = int(selected_option.split()[1]) 

    selected_chapter = st.session_state['chapter_data'][chapter_number]['original']

    with st.expander(f"See Chapter {chapter_number} Text"):
        st.text_area("Chapter Text", value=selected_chapter, height=350, disabled=True)

    editally_instance = EditAlly(novel=selected_chapter, style=st.session_state['style'], genre=st.session_state['genre'])

    if st.session_state['selected_functions']:
        if st.button('Evaluate Chapter'):
            if st.session_state['testing_mode']:
                # Use mock function in testing mode
                edited_text = mock_process_chapter(chapter_number, selected_chapter, 
                                                st.session_state['selected_functions'], 
                                                update_progress_bar)
                st.session_state['edited_text'] = edited_text
            else:
                editally_instance = EditAlly(novel=selected_chapter, style=style, genre=genre)
                update_progress_bar(2)
                edited_text = editally_instance.process_chapter(chapter_number, selected_chapter, 
                                                                selected_functions=st.session_state['selected_functions'], 
                                                                progress_callback=update_progress_bar)
                st.session_state['edited_text'] = edited_text

            if not st.session_state.get('show_diff', False):
                with st.expander(f"See Edited {chapter_number} Text"):
                    st.text_area("Edited Text Session Load", value=st.session_state['edited_text'], height=300)
                st.download_button(
                    label="Download Edited Text",
                    data=st.session_state['edited_text'],
                    file_name=f"chapter_{chapter_number}_edit.txt",
                    mime="text/plain"
                )
            left_html, right_html = create_side_by_side_diff_view(selected_chapter, edited=st.session_state['edited_text'])
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(left_html, unsafe_allow_html=True)

            with col2:
                st.markdown(right_html, unsafe_allow_html=True)
    else:
        st.button('Evaluate Chapter', disabled=True)

