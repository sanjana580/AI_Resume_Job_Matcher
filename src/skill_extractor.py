import re


# -------------------------------------------------
# STANDARD SKILL NAMES
# -------------------------------------------------

SKILLS = [
    "python",
    "java",
    "c",
    "sql",
    "mysql",
    "pandas",
    "numpy",
    "matplotlib",
    "scikit-learn",
    "machine learning",
    "deep learning",
    "tensorflow",
    "pytorch",
    "natural language processing",
    "computer vision",
    "statistics",
    "data preprocessing",
    "data visualization",
    "html",
    "css",
    "javascript",
    "git",
    "github",
    "fastapi",
    "streamlit",
]


# -------------------------------------------------
# SKILL ALIASES
# -------------------------------------------------

SKILL_ALIASES = {

    "ml": "machine learning",

    "machine-learning": "machine learning",

    "ai": "artificial intelligence",

    "nlp": "natural language processing",

    "natural-language-processing":
        "natural language processing",

    "cv": "computer vision",

    "scikit learn": "scikit-learn",

    "sklearn": "scikit-learn",

    "scikit_learn": "scikit-learn",

    "tf": "tensorflow",

    "pytorch": "pytorch",

    "py torch": "pytorch",

}


# -------------------------------------------------
# NORMALIZE TEXT
# -------------------------------------------------

def normalize_text(text):
    """
    Convert text to lowercase and normalize
    common skill aliases.
    """

    text = text.lower()

    for alias, standard_skill in SKILL_ALIASES.items():

        pattern = r"\b" + re.escape(alias) + r"\b"

        text = re.sub(
            pattern,
            standard_skill,
            text
        )

    return text


# -------------------------------------------------
# EXTRACT SKILLS
# -------------------------------------------------

def extract_skills(text):
    """
    Extract recognized skills from text.
    """

    text = normalize_text(text)

    found_skills = []

    for skill in SKILLS:

        # Special handling for the C programming language
        if skill == "c":

            pattern = r"(?<![a-z])c(?![a-z])"

        else:

            pattern = (
                r"(?<![a-z0-9])"
                + re.escape(skill)
                + r"(?![a-z0-9])"
            )

        if re.search(pattern, text):

            found_skills.append(skill)

    return found_skills


# -------------------------------------------------
# TEST
# -------------------------------------------------

if __name__ == "__main__":

    sample_text = """
    I have experience in Python, SQL, Pandas and NumPy.

    I also have knowledge of ML, NLP, sklearn,
    TensorFlow and PyTorch.

    I have worked on AI and computer vision projects.
    """

    skills = extract_skills(
        sample_text
    )

    print("Detected Skills:")

    for skill in skills:

        print("-", skill)