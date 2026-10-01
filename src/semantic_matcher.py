import streamlit as st
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# -------------------------------------------------
# LOAD AI MODEL
# -------------------------------------------------

@st.cache_resource
def load_model():

    return SentenceTransformer(
        "all-MiniLM-L6-v2"
    )


# -------------------------------------------------
# SEMANTIC MATCHING
# -------------------------------------------------

def calculate_semantic_similarity(
    resume_text,
    job_text
):
    """
    Calculate semantic similarity between
    resume and job description.
    """

    model = load_model()

    resume_embedding = model.encode(
        [resume_text]
    )

    job_embedding = model.encode(
        [job_text]
    )

    similarity = cosine_similarity(
        resume_embedding,
        job_embedding
    )[0][0]

    score = round(
        float(similarity) * 100,
        2
    )

    return score


# -------------------------------------------------
# TEST
# -------------------------------------------------

if __name__ == "__main__":

    resume = """
    I am a computer science student with experience
    in Python, machine learning, data preprocessing,
    Pandas, NumPy and SQL.
    """

    job = """
    We are looking for a data scientist who can build
    machine learning models, analyze data and work
    with Python, SQL and data preprocessing.
    """

    score = calculate_semantic_similarity(
        resume,
        job
    )

    print(
        "Semantic Match Score:",
        score,
        "%"
    )