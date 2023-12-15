instructions = {
    "Third Person POV": {
        "summary": "Adhere to third-person omniscient POV, balance pacing, avoid foreshadowing intrusion, use engaging hooks and cliffhangers, and maintain relatability and originality.",
        "details": """
        {
            "role": "Writing Editor",
            "narrative_instructions":{
                "POV":"Strictly adhere to the third-person omniscient point of view. Adjust details or events 
                outside the characters' direct experience, awareness, or perception. Avoid head-hopping. Ensure 
                no narrative or authorial intrusions that break the third-person perspective are present.",
                "pacing":"Ensure pacing is appropriate to the action-adventure or science fiction genre, maintaining 
                a balance between fast-paced sequences and character development moments.",
                "foreshadowing":"Avoid any foreshadowing that feels like narrative intrusion, head hopping, 
                or authorial intrusion.",
                "opening_hook":"Ensure the opening sentence or paragraph serves as a hook to capture the reader's 
                interest immediately.",
                "cliffhanger_ending":"End with a suspenseful moment or revelation, compelling the reader to want to 
                continue or know more.",
                "relatability":"Include elements and dialogue that are relatable to a young adult audience. Use casual, 
                natural language that reflects how young people actually speak.",
                "fluid_transitions":"Ensure transitions between scenes or beats are smooth and almost imperceptible, 
                creating a continuous narrative thread akin to a single train of thought.",
                "originality":"Generate unique and unpredictable scenery descriptions, avoiding common or cliché 
                phrases. Make sure the descriptions sound fresh and original, not typical of machine-generated text."
            },
            "editing_request":{
                "task":"Perform a line edit on the provided prose",
                "specific_instructions":{
                    "filter_words":{
                        "action":"remove or rephrase",
                        "purpose":"make prose more direct and engaging"
                    },
                    "passive_voice":{
                        "action":"replace",
                        "with":"active voice",
                        "purpose":"enhance clarity and immediacy"
                    },
                    "dangling_modifiers":{
                        "action":"rectify",
                        "purpose":"ensure clarity"
                    },
                    "split_infinitives":{
                        "action":"amend",
                        "purpose":"ensure grammatical precision"
                    },
                    "line_edit":{
                        "action":"conduct",
                        "scope":"line-by-line",
                        "purpose":"improve clarity, coherence, and overall flow"
                    },
                    "wordiness":{
                        "action":"trim",
                        "purpose":"enhance brevity and clarity"
                    },
                    "redundancies":{
                        "action":"eliminate",
                        "purpose":"prevent repetition and improve flow"
                    },
                    "consistency":{
                        "action":"check and correct",
                        "scope":"terminology, tenses, and character details",
                        "purpose":"maintain a uniform narrative"
                    },
                    "collective_triumph":{
                        "action":"replace",
                        "with":"individualistic expressions",
                        "purpose":"focus on personal achievements and struggles, while maintaining relatability 
                        for a young adult audience"
                    },
                    "together":{
                        "action":"rephrase",
                        "purpose":"create prose more concerned with the immediate and the individualistic, while 
                        keeping the tone suitable for YA readers"
                    },
                    "cliches":{
                        "action":"identify and replace",
                        "scope":"descriptions, dialogue, common phrases",
                        "purpose":"produce unique, fresh prose that appeals to a YA audience"
                    },
                    "cliched_introductions":{
                        "action":"identify and replace",
                        "scope":"introductory descriptions, scene-setting",
                        "purpose":"create unique and engaging beginnings"
                    },
                    "transitions":{
                        "action":"insert or enhance",
                        "scope":"between scenes or beats",
                        "purpose":"create a seamless narrative flow that merges divergent elements into a unified whole, 
                        maintaining a continuous train of thought"
                    },
                    "dialogue":{
                        "action":"revise",
                        "scope":"all spoken and thought dialogue",
                        "tone":"casual, natural, contemporary",
                        "vernacular":"specific to a contemporary young adult audience",
                        "purpose":"use language that would resonate authentically with a young adult audience"
                    },
                    "originality":{
                        "action":"ensure",
                        "scope":"all descriptive language",
                        "purpose":"produce unique, fresh prose that doesn't appear typical of machine-generated text"
                    },
                    "brevity_balance":{
                        "action":"adjust",
                        "scope":"whole text",
                        "purpose":"preserve essential elements of narrative and dialogue, preventing oversimplification"
                    }
                },
                "guideline":"Maintain the original intent, meaning, and essence of the prose during the editing process. 
                Ensure a consistent third-person perspective throughout, starting with a captivating hook and ending on 
                a suspenseful cliffhanger. Ensure the language and dialogue are age-appropriate and relatable to a 
                YA demographic. Keep descriptions original and fresh, avoiding clichés or repetitive phrases. Carefully 
                balance brevity with the need to preserve crucial elements of narrative, dialogue, and characterization."
            },
            "do_not_include": [
                "footnotes",
                "disclaimers",
                "end notes",
                "recommendations",
                "explanatory notes",
                "commentary"
            ]
        }
    """
    },
    "Sensory-rich Enhancement": {
        "summary": "Include relatable dialogue and generate unique, vivid scenery descriptions for a young adult audience.",
        "details": """
        {
            "role": "Writing Editor",
            "narrative_instructions":{
                "relatability":"Include elements and dialogue that are relatable to a young adult audience. Use casual, 
                natural language that reflects how young people actually speak.",
                "originality":"Generate unique and unpredictable scenery descriptions, avoiding common or cliché phrases. 
                Make sure the descriptions sound fresh and original, not typical of machine-generated text."
            },
            "editing_request":{
                "task":"Perform a line edit on the provided prose",
                "specific_instructions":{
                    "sensory_details":{
                        "subject":"Any",
                        "sensory_elements":[
                        {
                            "sense":"sight",
                            "action":"write",
                            "guidelines":"Describe a visual element that captures the essence of the subject."
                        },
                        {
                            "sense":"sound",
                            "action":"write",
                            "guidelines":"Describe an auditory element that is often associated with the subject."
                        },
                        {
                            "sense":"touch",
                            "action":"write",
                            "guidelines":"Describe a tactile element that someone might encounter in relation to the subject."
                        },
                        {
                            "sense":"smell",
                            "action":"write",
                            "guidelines":"Describe an olfactory element that defines or accompanies the subject."
                        },
                        {
                            "sense":"taste",
                            "action":"write",
                            "guidelines":"Describe a taste that could be indirectly or directly related to the subject."
                        }
                        ]
                    },
                    "target_audience":"Readers looking for vivid, evocative descriptions",
                    "tone":"Engaging, specific, and sensory",
                    "language":"Vivid, descriptive"
                }
            },
            "do_not_include": [
                "footnotes",
                "disclaimers",
                "end notes",
                "recommendations",
                "explanatory notes",
                "commentary"
            ]
        }
    """
    },
    'Remove Overused Phrases':{
        "summary": "Identify and replace clichés and overused expressions to refresh the prose with original, engaging language.",
        "details": """
        {
            "role": "Writing Editor",
            "narrative_instructions": {
                "originality": "Ensure the prose avoids clichés and overused expressions, promoting fresh and innovative descriptions and narrative elements."
            },
            "editing_request": {
                "task": "Identify and replace overused phrases or words in the provided prose",
                "specific_instructions": {
                    "overused_phrases": {
                        "action": "identify and replace",
                        "purpose": "Refresh the prose with more original and engaging expressions."
                    },
                    "cliched_expressions": {
                        "action": "identify and replace",
                        "purpose": "Ensure the prose remains unique and avoids common clichés."
                    },
                    "repetitive_wording": {
                        "action": "identify and reduce",
                        "purpose": "Enhance the variety and richness of language used in the prose."
                    },
                    "language": {
                        "action": "ensure",
                        "details": "Employ a language style that is vivid, engaging, and original."
                    },
                    "exclusions": {
                        "action": "omit",
                        "details": ["footnotes", "disclaimers", "end notes"]
                    }
                },
                "guideline": "Maintain the originality and readability of the prose. Focus on eliminating overused phrases and clichés, 
                replacing them with fresh, engaging language that appeals to the target audience."
            },
            "do_not_include": [
                "footnotes",
                "disclaimers",
                "end notes",
                "recommendations",
                "explanatory notes",
                "commentary"
            ]
        }
    """
    },
    'Remove Chaff': {
        "summary": "Streamline prose by identifying and replacing unnecessary elements with concise, impactful alternatives, preserving the essence.",
        "details": """
        {
            "role": "Writing Editor",
            "narrative_instructions": {
                "task": "Focus on removing unnecessary elements ('chaff') while retaining the essential meaning and detail."
            },
            "editing_request": {
                "task": "Provide direct replacements for identified areas of text that need refinement",
                "specific_instructions": {
                    "text_refinement": {
                        "action": "identify and replace",
                        "purpose": "Streamline the prose by removing superfluous elements and enhancing its clarity and impact"
                    }
                },
                "examples": {
                    "original_text": "'The sky was a brilliant blue, vast and endless.'",
                    "replacement_text": "'The sky stretched, a deep azure expanse.'"
                },
                "guideline": "Focus on identifying and replacing text with concise, impactful alternatives. Maintain the original essence of the prose while enhancing its readability and effectiveness."
            },
            "do_not_include": [
                "footnotes",
                "disclaimers",
                "end notes",
                "recommendations",
                "explanatory notes",
                "commentary"
            ]
        }
    """
    },
    'Targeting Specific Phrases': {
        "summary": "Focus on rephrasing overused or clichéd phrases to refresh the narrative with more original expressions.",
        "details": """
        {
            "role": "Writing Editor",
            "narrative_instructions": {
                "phrase_usage": "Focus on identifying and rephrasing overused or clichéd phrases."
            },
            "editing_request": {
                "task": "Identify and replace specific overused phrases",
                "specific_instructions": {
                    "phrases_identification": {
                        "action": "identify and suggest replacements",
                        "purpose": "Refresh the narrative with more original expressions"
                    }
                },
                "guideline": "Maintain the narrative's original intent while replacing overused phrases with more unique and engaging alternatives."
            },
            "do_not_include": [
                "footnotes",
                "disclaimers",
                "end notes",
                "recommendations",
                "explanatory notes",
                "commentary"
            ]
        }
    """
    },
    'Improving Chapter Endings': {
        "summary": "Revise the ending to be impactful and intriguing, yet open-ended, drawing from the established narrative.",
        "details": """
        {
            "role": "Writing Editor",
            "narrative_instructions": {
                "focus": "Examine and revise only the last few paragraphs of the chapter to ensure a strong, compelling ending."
            },
            "editing_request": {
                "task": "Revise the ending to be impactful and intriguing, yet open-ended, drawing from the established narrative.",
                "specific_instructions": {
                    "evaluate_ending": {
                        "action": "analyze and refine",
                        "purpose": "Concentrate on the final few paragraphs to craft an ending that is engaging and leads into the next chapter. 
                        The analysis should be confined to these paragraphs without revisiting the entire chapter."
                    },
                    "no_additional_notes": {
                        "action": "omit",
                        "purpose": "Provide the revised ending text only, without any explanatory notes or commentary."
                    }
                },
                "guideline": "Ensure the chapter's conclusion is enticing and seamless, offering a hint of what is to come without wrapping up all plot points. 
                The focus should remain strictly on the ending, without altering earlier content."
            },
            "output_format": {
                "format": "Provide the revised text of the ending only, adhering closely to the narrative style and genre conventions."
            },
            "do_not_include": [
                "footnotes",
                "disclaimers",
                "end notes",
                "recommendations",
                "explanatory notes",
                "commentary"
            ]
        }
    """
    }
    ,
    "Enhance Intra-Chapter Analysis": {
        "summary": "Analyze and refine chapter elements for repetition reduction and dialogue smoothness, enhancing narrative quality and coherence.", 
        "details": """
        {
            "role": "Writing Editor",
            "narrative_instructions": {
                "task": "Analyze and refine intra-chapter elements for improved narrative quality",
                "focus_areas": ["repetition reduction", "dialogue smoothness"]
            },
            "editing_request": {
                "Repetition Reduction": {
                    "action": "analyze and recommend",
                    "focus_areas": ["phrase repetition", "redundant descriptions", "overused words"],
                    "purpose": "Identify areas where the text repeats phrases, descriptions, or uses overused words, reducing narrative redundancy and improving readability."
                },
                "Dialogue Smoothness": {
                    "action": "assess and improve",
                    "focus_areas": ["naturalness", "character voice", "dialogue pacing"],
                    "purpose": "Ensure that each character's dialogue is consistent with their established voice, and that conversations flow naturally and maintain an appropriate pace."
                },
                "guideline": "Enhance the overall narrative quality within each chapter by reducing repetition and improving dialogue, contributing to a more engaging and coherent reading experience."
            },
            "do_not_include": [
                "footnotes",
                "disclaimers",
                "end notes",
                "recommendations",
                "explanatory notes",
                "commentary"
            ]
        }
    """
    }
}