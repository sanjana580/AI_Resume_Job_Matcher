from src.interview_questions import generate_interview_questions
from src.recommendations import generate_recommendations
from src.semantic_matcher import calculate_semantic_similarity
from src.resume_parser import extract_resume_text
from src.job_parser import read_job_description
from src.skill_extractor import extract_skills
from src.matcher import calculate_match, find_missing_skills


# -----------------------------
# File paths
# -----------------------------import streamlit as st
import tempfile
import os

from src.resume_parser import extract_resume_text
from src.job_parser import read_job_description
from src.skill_extractor import extract_skills
from src.matcher import calculate_match, find_missing_skills
from src.semantic_matcher import calculate_semantic_similarity
from src.recommendations import generate_recommendations
from src.interview_questions import generate_interview_questions


st.set_page_config(
    page_title="AI Resume Job Matcher",
    page_icon="🤖",
    layout="wide"
)


st.title("🤖 AI Resume Job Matcher")

st.write(
    "Upload your resume and enter a job description "
    "to analyze your job compatibility."
)


# -----------------------------
# Resume Upload
# -----------------------------

st.header("📄 Upload Resume")

uploaded_resume = st.file_uploader(
    "Upload your resume PDF",
    type=["pdf"]
)


# -----------------------------
# Job Description
# -----------------------------

st.header("💼 Job Description")

job_text = st.text_area(
    "Paste the job description here",
    height=250
)


# -----------------------------
# Analyze Button
# -----------------------------

if st.button("🔍 Analyze Resume"):

    if uploaded_resume is None:
        st.error("Please upload a resume PDF.")

    elif not job_text.strip():
        st.error("Please enter a job description.")

    else:

        # Save uploaded PDF temporarily
        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".pdf"
        ) as temp_file:

            temp_file.write(
                uploaded_resume.getbuffer()
            )

            temp_pdf_path = temp_file.name


        # Extract resume text
        resume_text = extract_resume_text(
            temp_pdf_path
        )


        # Extract skills
        resume_skills = extract_skills(
            resume_text
        )

        job_skills = extract_skills(
            job_text
        )


        # Keyword matching
        keyword_score = calculate_match(
            resume_skills,
            job_skills
        )


        # Semantic matching
        semantic_score = calculate_semantic_similarity(
            resume_text,
            job_text
        )


        # Final score
        final_score = round(
            (keyword_score + semantic_score) / 2,
            2
        )


        # Matched and missing skills
        matched_skills = sorted(
            set(resume_skills).intersection(
                set(job_skills)
            )
        )

        missing_skills = find_missing_skills(
            resume_skills,
            job_skills
        )


        # Recommendations
        recommendations = generate_recommendations(
            missing_skills
        )


        # Interview questions
        interview_questions = generate_interview_questions(
            missing_skills
        )


        # -----------------------------
        # Results
        # -----------------------------

        st.success("Resume analysis completed!")

        st.header("🎯 Match Results")


        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Keyword Match",
                f"{keyword_score}%"
            )

        with col2:
            st.metric(
                "Semantic Match",
                f"{semantic_score}%"
            )

        with col3:
            st.metric(
                "Final AI Score",
                f"{final_score}%"
            )


        # -----------------------------
        # Skills
        # -----------------------------

        st.header("✅ Matched Skills")

        if matched_skills:

            st.write(
                ", ".join(
                    skill.title()
                    for skill in matched_skills
                )
            )

        else:

            st.write("No matching skills found.")


        st.header("❌ Missing Skills")

        if missing_skills:

            for skill in missing_skills:
                st.write(f"- {skill.title()}")

        else:

            st.write(
                "No missing skills found!"
            )


        # -----------------------------
        # Recommendations
        # -----------------------------

        st.header("📚 Learning Recommendations")

        for skill, resources in recommendations.items():

            st.subheader(skill.title())

            for resource in resources:

                st.write(
                    f"- {resource}"
                )


        # -----------------------------
        # Interview Questions
        # -----------------------------

        st.header("🎤 Interview Questions")

        for skill, questions in interview_questions.items():

            st.subheader(skill.title())

            for question in questions:

                st.write(
                    f"- {question}"
                )


        # Remove temporary file
        os.remove(temp_pdf_path)

RESUME_PATH = "data/resumes/sanjana.pdf"
JOB_PATH = "data/job_descriptions/data_scientist.txt"


# -----------------------------
# Extract resume and job text
# -----------------------------

resume_text = extract_resume_text(RESUME_PATH)
job_text = read_job_description(JOB_PATH)


# -----------------------------
# Extract skills
# -----------------------------

resume_skills = extract_skills(resume_text)
job_skills = extract_skills(job_text)


# -----------------------------
# Calculate match
# -----------------------------

match_score = calculate_match(resume_skills, job_skills)

semantic_score = calculate_semantic_similarity(
    resume_text,
    job_text
)

final_score = round(
    (match_score + semantic_score) / 2,
    2
)

missing_skills = find_missing_skills(
    resume_skills,
    job_skills
)

recommendations = generate_recommendations(
    missing_skills
)

interview_questions = generate_interview_questions(
    missing_skills
)

matched_skills = sorted(
    set(resume_skills).intersection(set(job_skills))
)


# -----------------------------
# Display results
# -----------------------------

print("\n==============================")
print("     AI RESUME MATCHER")
print("==============================")

print("\nResume Skills:")
for skill in resume_skills:
    print("-", skill)

print("\nJob Required Skills:")
for skill in job_skills:
    print("-", skill)

print("\nMatched Skills:")
for skill in matched_skills:
    print("-", skill)

print("\nMissing Skills:")
for skill in missing_skills:
    print("-", skill)

print("\nLearning Recommendations:")

for skill, resources in recommendations.items():

    print(f"\n{skill.title()}:")

    for resource in resources:
        print("-", resource)  

print("\nInterview Questions:")

for skill, questions in interview_questions.items():

    print(f"\n{skill.title()}:")

    for question in questions:
        print("-", question)          



print("\nKeyword Match Score:", match_score, "%")
print("Semantic Match Score:", semantic_score, "%")
print("Final AI Match Score:", final_score, "%")

print("\n==============================")