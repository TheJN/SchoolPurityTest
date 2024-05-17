import streamlit as st


survey_categories = {
    "Performances_intellectuelles": [
        {
            "question": "As-tu déjà effectué des calculs frauduleux pour savoir si tu devais réviser pour un examen ?",
            "answers": ["Oui", "Non"],
            "scores": [-1, 1]
        },
       
        {
            "question": "As-tu déjà été à un DS sans réviser en te disant que réviser était douter de ses capacités ?",
            "answers": ["Oui", "Non"],
            "scores": [-1, 1]
        },
        {
            "question": "Participes-tu beaucoup à l’oral en cours ?",
            "answers": ["Oui", "Non"],
            "scores": [1, -1]
        },
        {
            "question": "Poses-tu des questions aux professeurs quand tu en ressens le besoin ?",
            "answers": ["Oui", "Non"],
            "scores": [1, -1]
        },
        {
            "question": "As-tu des facilitées en cours ?",
            "answers": ["Oui", "Non"],
            "scores": [1, -1]
        },
        {
            "question": "Es-tu une personne bien organisée ?",
            "answers": ["Oui", "Non"],
            "scores": [1, -1]
        },
        {
            "question": "Dans un travail de groupe, quel type de personne es-tu ?",
            "answers": ["Le meneur et bosseur du projet", "La personne qui ne travaille pas ", "Un « accompagnateur » du bosseur"],
            "scores": [1, 0, 0.5]
        },
        {
            "question": "Es-tu un élève intéressé par tes études ?",
            "answers": ["Oui", "Non"],
            "scores": [1, -1]
        }
    ],

    "Assiduité": [
        {
            "question": "As-tu déjà dormi en cours ?",
            "answers": ["Oui", "Non"],
            "scores": [-1, 1]
        },
        {
            "question": "Arrives-tu en retard en cours ?",
            "answers": ["Oui", "Non"],
            "scores": [-1, 1]
        },
        {
            "question": "As-tu déjà assisté à un cours de langue ?",
            "answers": ["Oui", "Non"],
            "scores": [1, -1]
        },
        {
            "question": "Que penses–tu du Voltaire à faire le week-end ?",
            "answers": ["C’est une bonne méthode pour progresser en français ", "Il y avait un voltaire à faire ? ", "Reverso devient ton meilleur ami "],
            "scores": [1, 0, 0.5]
        },
        {
            "question": "Que penses-tu des cours en distanciel :",
            "answers": ["Ça permet d’effectuer des cours lorsqu’on ne peut pas être en présentiel", "Séance dodo tous en restant connecté au cas où ", "Vancances !! "],
            "scores": [1, 0.5, -1]
        },
        {
            "question": "Pour toi les vacances scolaires sont :",
            "answers": ["Des journées sans cours ", "Le moment pour réviser et se remettre à jour ", "« Pendant les vacances je ne fais RIEN, je suis tranquille je ne fais RIEN » "],
            "scores": [1, 0.5, -1]
        },
        {
            "question": "As-tu une présence régulière en cours ?",
            "answers": ["Oui", "Non"],
            "scores": [1, -1]
        },
        {
            "question": "As-tu beaucoup d’absences injustifiées ?",
            "answers": ["Oui", "Non"],
            "scores": [-1, 1]
        },
        
    ],
    "Sécurité": [
        {
            "question": "As-tu déjà respecté le stop avant le parking de l’école ?",
            "answers": ["Oui", "Non"],
            "scores": [1, -1]
        },
        {
            "question": "As-tu déjà eu l’envie de shooter dans un bouffe de l’agora ?",
            "answers": ["Oui", "Non"],
            "scores": [-1, 1]
        },
        {
            "question": "T’ais-tu déjà garer sur des places visiteurs du parking ?",
            "answers": ["Oui", "Non"],
            "scores": [-1, 1]
        },
        {
            "question": "As-tu déjà eu l’envie de lancer quelque chose sur l’ISS ?",
            "answers": ["Oui", "Non"],
            "scores": [-1, 1]
        },
        {
            "question": "As-tu déjà pris le parking de l’école pour un circuit de F1 ?",
            "answers": ["Oui", "Non"],
            "scores": [-1, 1]
        },
        {
            "question": "Que penses- tu des prises de l’école ?",
            "answers": ["Moyen de se suspendre", "Optimise la place dans les salles de classes", "Moyen de destruction massif des plafonds de l’école", "Une séance bras sans abonnement "],
            "scores": [-1, 1, -1, 0.5]
        },
        {
            "question": "As-tu déjà manger dans une salle de cours alors que c’est strictement interdit ?",
            "answers": ["Oui", "Non"],
            "scores": [-1, 1]
        },
        {
            "question": "As-tu déjà fumé dans l’enceinte de l’école ?",
            "answers": ["Oui", "Non"],
            "scores": [-1, 1]
        },
        
    ],
    "Sérieux": [
        {
            "question": "Que penses-tu des stages à l’étranger :",
            "answers": ["Les entreprises partenaires ne connaissent toujours pas nôtre école ", "Très grande opportunité du point de vue culturel et découverte du monde du travail ", "Linkedin devient ton meilleur ami ", "Tu mets plus de temps à chercher un stage que la durée dans laquelle tu vas y être "],
            "scores": [-1, 1, 0.5, -1]
        }, 
        {
            "question": "Lorsque tu as un DS tu révises :",
            "answers": ["Une semaine à l’avance ", "La veille ", "Il y a DS aujourd’hui ? "],
            "scores": [1, 0.5, -1]
        },
        {
            "question": "As-tu déjà demandé à Madame Ramall de faire ton code ?",
            "answers": ["Oui", "Non"],
            "scores": [-1, 1]
        },
        {
            "question": "CHATGPT représente-t-il 50 % de ton diplôme ?",
            "answers": ["Oui", "Non"],
            "scores": [-1, 1]
        },
        {
            "question": "Vas-tu obtenir ton TOEIC ?",
            "answers": ["Oui", "Non"],
            "scores": [1, -1]
        },
        {
            "question": "As-tu déjà écouté ne serait-ce qu’un seul cours de PPL ?",
            "answers": ["Oui", "Non"],
            "scores": [1, -1]
        },
      
       
        {
            "question": "T’ais-tu déjà fais virer de cours ?",
            "answers": ["Oui", "Non"],
            "scores": [-1, 1]
        },
        
        {
            "question": "Es-tu déjà venu en cours bourré ?",
            "answers": ["Oui", "Non"],
            "scores": [-1, 1]
        },    
    ],
    "Sociabilité": [
        {
            "question": "Possèdes-tu des ami(e)s au sein de l’école ?",
            "answers": ["Oui", "Non"],
            "scores": [1, -1]
        },
        {
            "question": "Fais-tu des activités extra-scolaires avec tes ami(e)s de l’école ?",
            "answers": ["Oui", "Non"],
            "scores": [1, -1]
        },
        {
            "question": "Est-ce que tu te porterais volontaire si tu devais, à ton échelle, aider l’école ?",
            "answers": ["Oui", "Non"],
            "scores": [1, -1]
        },
        {
            "question": "Pourrais-tu participer à une journée porte ouverte pour promouvoir ton école ?",
            "answers": ["Oui", "Non"],
            "scores": [1, -1]
        },
        {
            "question": "Voudrais-tu faire partie du membre du BDE pour t’occuper de la vie étudiante au sein de l’école ?",
            "answers": ["Oui", "Non"],
            "scores": [1, -1]
        },
        {
            "question": "Voudrais-tu faire partie des ALUMNI après avoir été diplômé ?",
            "answers": ["Oui", "Non"],
            "scores": [1, -1]
        },
        {
            "question": "Pourrais-tu travailler au sein de l’école après ton diplôme ?",
            "answers": ["Oui", "Non"],
            "scores": [1, -1]
        }
    ],
    "Entre-aide": [
        {
            "question": "Aides-tu tes camarades de classe à réviser un examen quand ils en nécessitent le besoin ?",
            "answers": ["Oui", "Non"],
            "scores": [1, -1]
        },
        {
            "question": "As-tu déjà prêté tes cours ou tes corrections de TD à quelqu’un ?",
            "answers": ["Oui", "Non"],
            "scores": [1, -1]
        },
        {
            "question": "As-tu déjà aidé un élève de ta classe sur un projet ?",
            "answers": ["Oui", "Non"],
            "scores": [1, -1]
        },
        {
            "question": "As-tu déjà effectué du soutien scolaire pour les promotions en-dessous de la tienne ?",
            "answers": ["Oui", "Non"],
            "scores": [1, -1]
        },
        {
            "question": "Proposes-tu ton aide à quelconque élève en difficulté ?",
            "answers": ["Oui", "Non"],
            "scores": [1, -1]
        },
        {
            "question": "Aimes-tu aider tes camarades de classe quand tu en es capable ?",
            "answers": ["Oui", "Non"],
            "scores": [1, -1]
        }
    ]
}


def find_question_index(category,question):
    if category not in survey_categories:
        return -1  # Category not found
    
    category_questions = survey_categories[category]
    
    for index, item in enumerate(category_questions):
        if item["question"] == question:
            return index+1
    return -1  # Answers not found in any question
    
def get_category_index(category_name):

    category_index = 0
    for category in survey_categories.keys():
        if category == category_name:
            return category_index
        category_index += 1
    return None  # Return None if the category name is not found

def display_questions(question,category):
        st.write(question["question"])
        answers = question['answers']
        scores = question['scores']
        question_index = find_question_index(category,question["question"])
        cat_index = get_category_index(category)
        radios = st.radio('',question["answers"],on_change=StoreAnswer(question_index,cat_index,answers,scores),key=f'selected_option_{cat_index}_{question_index}',horizontal=True)

def display_category(category):
    st.header(f"{category}")
    questions = survey_categories[category]
    for question_data in questions:
        display_questions(question_data,category)

def StoreAnswer(question_index,cat_index,answers,scores):

    selected_option = st.session_state[f'selected_option_{cat_index}_{question_index}'] # get the selected answer
    if selected_option is not None:
        answer_index = answers.index(selected_option)
        score = scores[answer_index]
    
        st.session_state[f"score_{cat_index}_{question_index}"] = score # Store the score into a session variable

def check_category_scores(category_index, scores):
    category_scores = [scores.get(f"score_{category_index-1}_{i}", 0) for i in range(1, 4)]
    result = {i: score != 0 for i, score in enumerate(category_scores, start=1)}
    return result
def extract_scores(data):
    scores = {key: value for key, value in data.items() if "score_" in key}
    return scores



def calculate_category_scores(scores_dict):
    category_scores = {}

    for key, value in scores_dict.items():
        if key.startswith("score_"):
            # Extract category index from the key
            parts = key.split('_')
            if len(parts) == 3:
                category_index = int(parts[1])
            else:
                continue  # Skip keys that don't match the expected format

            # Get score from the key
            score = value if value is not None else 0
            score = score if score > 0 else 0
            category_scores[category_index] = category_scores.get(category_index, 0) + score

    return category_scores

def extract_scores(data):
    scores = {key: value for key, value in data.items() if "score_" in key}
    return scores

def instantiate_session_state_variables():
    for category_index, category_questions in enumerate(survey_categories.values()):
        for question_index, question in enumerate(category_questions, start=1):
            st.session_state.setdefault(f"selected_option_{category_index}_{question_index}", None)

def calculate_max_scores(survey_categories):
    max_scores = {}
    for category_index,category in enumerate(survey_categories.values(),start=0):
        max_score = sum(max(question["scores"]) for question in category)
        max_scores[category_index] = max_score
    return max_scores


def calculate_percentage(x, y):
    percentages = {}
    for key in x:
        if key in y and y[key] != 0:
            percentage = (x[key] / y[key]) * 100
            percentages[key] = percentage
        else:
            percentages[key] = None  # Handle division by zero or missing keys
    return percentages


def combine_data(*args):
    combined = {}
    for data_dict in args:
        for key, value in data_dict.items():
            if key not in combined:
                combined[key] = []
            combined[key].append(value)
    return combined

def get_category_key(index):
    """
    Get the key (category) from the given index.
    
    Parameters:
        index (int): The index of the category.
        
    Returns:
        str: The key (category) corresponding to the index.
    """
    categories = list(survey_categories.keys())
    if index < 0 or index >= len(categories):
        raise ValueError("Index out of range")
    return categories[index]


def get_category_index(key):
    """
    Get the index from the given category key.
    
    Parameters:
        key (str): The key (category) of the survey category.
        
    Returns:
        int: The index corresponding to the category key.
    """
    categories = list(survey_categories.keys())
    if key not in categories:
        raise ValueError("Category key not found")
    return categories.index(key)

def convert_keys_to_categories(data):
    """
    Convert dictionary keys from index format to category keys.

    Parameters:
        data (dict): The dictionary with keys in index format.

    Returns:
        dict: A new dictionary with keys replaced by category keys.
    """
    converted_data = {}
    for index, values in data.items():
        category_key = get_category_key(int(index))
        converted_data[category_key] = values
    return converted_data

def calculate_average_percentage(category_dict):
    # Check if the dictionary is empty
    if not category_dict:
        return 0
    
    # Calculate the sum of all percentages
    total_percentage = sum(category_dict.values())
    
    # Calculate the number of categories
    number_of_categories = len(category_dict)
    
    # Calculate the average percentage
    average_percentage = total_percentage / number_of_categories
    
    return average_percentage