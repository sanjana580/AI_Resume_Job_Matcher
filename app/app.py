import streamlit as st
import tempfile
import os
import sys


# -------------------------------------------------
# ADD PROJECT ROOT TO PYTHON PATH
# -------------------------------------------------

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)


# -------------------------------------------------
# IMPORT PROJECT MODULES
# -------------------------------------------------

from src.resume_parser import extract_resume_text

from src.skill_extractor import extract_skills

from src.job_parser import (
    extract_required_and_preferred_skills
)

from src.matcher import (
    calculate_match,
    find_missing_skills,
    calculate_weighted_score
)

from src.semantic_matcher import (
    calculate_semantic_similarity
)

from src.recommendations import (
    generate_recommendations,
    generate_strengths,
    generate_improvement_suggestions
)

from src.interview_questions import (
    generate_interview_questions
)

from src.pdf_report import (
    generate_pdf_report
)


# -------------------------------------------------
# PROFESSIONAL SKILL NAME FORMATTING
# -------------------------------------------------

def format_skill_name(skill):

    skill_names = {

        "python": "Python",
        "java": "Java",
        "c": "C",
        "sql": "SQL",
        "mysql": "MySQL",

        "pandas": "Pandas",
        "numpy": "NumPy",
        "matplotlib": "Matplotlib",

        "scikit-learn": "Scikit-learn",

        "machine learning": "Machine Learning",
        "deep learning": "Deep Learning",

        "tensorflow": "TensorFlow",
        "pytorch": "PyTorch",

        "natural language processing":
            "Natural Language Processing",

        "computer vision":
            "Computer Vision",

        "statistics":
            "Statistics",

        "data preprocessing":
            "Data Preprocessing",

        "data visualization":
            "Data Visualization",

        "html": "HTML",
        "css": "CSS",
        "javascript": "JavaScript",

        "git": "Git",
        "github": "GitHub",

        "fastapi": "FastAPI",
        "streamlit": "Streamlit"
    }

    return skill_names.get(
        skill.lower(),
        skill.title()
    )


# -------------------------------------------------
# GENERATE TXT ANALYSIS REPORT
# -------------------------------------------------

def generate_report(
    resume_name,
    required_match,
    semantic_score,
    preferred_match,
    final_score,
    matched_required_skills,
    missing_required_skills,
    matched_preferred_skills,
    missing_preferred_skills,
    strengths,
    improvement_suggestions,
    recommendations,
    interview_questions
):

    report = []

    report.append(
        "AI RESUME JOB MATCHER"
    )

    report.append(
        "=" * 60
    )

    report.append(
        f"Resume: {resume_name}"
    )

    report.append("")

    # -------------------------------------------------
    # MATCH RESULTS
    # -------------------------------------------------

    report.append(
        "MATCH RESULTS"
    )

    report.append(
        "-" * 60
    )

    report.append(
        f"Required Skills Match: "
        f"{required_match:.2f}%"
    )

    report.append(
        f"Semantic Match: "
        f"{semantic_score:.2f}%"
    )

    report.append(
        f"Preferred Skills Match: "
        f"{preferred_match:.2f}%"
    )

    report.append(
        f"Final AI Score: "
        f"{final_score:.2f}%"
    )

    report.append("")

    # -------------------------------------------------
    # AI ANALYSIS SUMMARY
    # -------------------------------------------------

    report.append(
        "AI ANALYSIS SUMMARY"
    )

    report.append(
        "-" * 60
    )

    report.append(
        f"Your resume matches "
        f"{required_match:.0f}% of the required "
        f"skills for this role."
    )

    if matched_required_skills:

        formatted_skills = ", ".join(
            format_skill_name(skill)
            for skill in matched_required_skills
        )

        report.append(
            f"Strongest technical matches: "
            f"{formatted_skills}."
        )

    if missing_required_skills:

        formatted_skills = ", ".join(
            format_skill_name(skill)
            for skill in missing_required_skills
        )

        report.append(
            f"Main required skill gaps: "
            f"{formatted_skills}."
        )

    if missing_preferred_skills:

        formatted_skills = ", ".join(
            format_skill_name(skill)
            for skill in missing_preferred_skills
        )

        report.append(
            f"Additional preferred skills: "
            f"{formatted_skills}."
        )

    report.append("")

    # -------------------------------------------------
    # RESUME STRENGTHS
    # -------------------------------------------------

    report.append(
        "RESUME STRENGTHS"
    )

    report.append(
        "-" * 60
    )

    if strengths:

        for strength in strengths:

            report.append(
                f"- {strength}"
            )

    else:

        report.append(
            "No specific strengths detected."
        )

    report.append("")

    # -------------------------------------------------
    # IMPROVEMENT SUGGESTIONS
    # -------------------------------------------------

    report.append(
        "IMPROVEMENT SUGGESTIONS"
    )

    report.append(
        "-" * 60
    )

    if improvement_suggestions:

        for suggestion in improvement_suggestions:

            report.append(
                f"- {suggestion}"
            )

    else:

        report.append(
            "No major improvement suggestions."
        )

    report.append("")

    # -------------------------------------------------
    # REQUIRED SKILLS
    # -------------------------------------------------

    report.append(
        "REQUIRED SKILLS"
    )

    report.append(
        "-" * 60
    )

    if matched_required_skills:

        report.append(
            "Matched:"
        )

        for skill in matched_required_skills:

            report.append(
                f"- {format_skill_name(skill)}"
            )

    if missing_required_skills:

        report.append(
            "Missing:"
        )

        for skill in missing_required_skills:

            report.append(
                f"- {format_skill_name(skill)}"
            )

    report.append("")

    # -------------------------------------------------
    # PREFERRED SKILLS
    # -------------------------------------------------

    report.append(
        "PREFERRED SKILLS"
    )

    report.append(
        "-" * 60
    )

    if matched_preferred_skills:

        report.append(
            "Matched:"
        )

        for skill in matched_preferred_skills:

            report.append(
                f"- {format_skill_name(skill)}"
            )

    if missing_preferred_skills:

        report.append(
            "Missing:"
        )

        for skill in missing_preferred_skills:

            report.append(
                f"- {format_skill_name(skill)}"
            )

    report.append("")

    # -------------------------------------------------
    # LEARNING RECOMMENDATIONS
    # -------------------------------------------------

    report.append(
        "LEARNING RECOMMENDATIONS"
    )

    report.append(
        "-" * 60
    )

    if recommendations:

        for skill, resources in recommendations.items():

            report.append(
                f"\n{format_skill_name(skill)}:"
            )

            for resource in resources:

                report.append(
                    f"- {resource}"
                )

    else:

        report.append(
            "No learning recommendations available."
        )

    report.append("")

    # -------------------------------------------------
    # INTERVIEW QUESTIONS
    # -------------------------------------------------

    report.append(
        "INTERVIEW QUESTIONS"
    )

    report.append(
        "-" * 60
    )

    if interview_questions:

        for skill, questions in interview_questions.items():

            report.append(
                f"\n{format_skill_name(skill)}:"
            )

            for question in questions:

                report.append(
                    f"- {question}"
                )

    else:

        report.append(
            "No interview questions generated."
        )

    report.append("")

    report.append(
        "=" * 60
    )

    report.append(
        "Generated by AI Resume Job Matcher"
    )

    return "\n".join(report)


# -------------------------------------------------
# PAGE CONFIGURATION
# -------------------------------------------------

st.set_page_config(
    page_title="AI Resume Job Matcher",
    page_icon="🤖",
    layout="wide"
)


# -------------------------------------------------
# TITLE
# -------------------------------------------------

st.title(
    "🤖 AI Resume Job Matcher"
)

st.write(
    "Upload your resume and enter a job description "
    "to analyze your job compatibility."
)


# -------------------------------------------------
# RESUME UPLOAD
# -------------------------------------------------

st.header(
    "📄 Upload Resume"
)

uploaded_resume = st.file_uploader(
    "Upload your resume PDF",
    type=["pdf"]
)


# -------------------------------------------------
# JOB DESCRIPTION
# -------------------------------------------------

st.header(
    "💼 Job Description"
)

job_description = st.text_area(
    "Paste the job description here",
    height=250,
    placeholder=(
        "Paste the complete job description here..."
    )
)


# -------------------------------------------------
# ANALYZE BUTTON
# -------------------------------------------------

analyze_button = st.button(
    "🔍 Analyze Resume",
    type="primary"
)


# -------------------------------------------------
# ANALYSIS
# -------------------------------------------------

if analyze_button:

    # -------------------------------------------------
    # VALIDATION
    # -------------------------------------------------

    if uploaded_resume is None:

        st.warning(
            "Please upload a resume PDF."
        )

        st.stop()


    if not job_description.strip():

        st.warning(
            "Please enter a job description."
        )

        st.stop()


    # -------------------------------------------------
    # SAVE TEMPORARY RESUME
    # -------------------------------------------------

    temp_file = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    )

    temp_file.write(
        uploaded_resume.getbuffer()
    )

    temp_file.close()

    resume_path = temp_file.name


    try:

        # =================================================
        # EXTRACT RESUME TEXT
        # =================================================

        resume_text = extract_resume_text(
            resume_path
        )


        # =================================================
        # EXTRACT RESUME SKILLS
        # =================================================

        resume_skills = extract_skills(
            resume_text
        )


        # =================================================
        # EXTRACT JOB SKILLS
        # =================================================

        (
            required_job_skills,
            preferred_job_skills
        ) = extract_required_and_preferred_skills(
            job_description
        )


        # =================================================
        # REQUIRED SKILL MATCH
        # =================================================

        required_match = calculate_match(
            resume_skills,
            required_job_skills
        )


        # =================================================
        # PREFERRED SKILL MATCH
        # =================================================

        preferred_match = calculate_match(
            resume_skills,
            preferred_job_skills
        )


        # =================================================
        # SKILL SETS
        # =================================================

        resume_skill_set = set(
            resume_skills
        )

        required_skill_set = set(
            required_job_skills
        )

        preferred_skill_set = set(
            preferred_job_skills
        )


        # =================================================
        # MATCHED REQUIRED SKILLS
        # =================================================

        matched_required_skills = sorted(
            resume_skill_set.intersection(
                required_skill_set
            )
        )


        # =================================================
        # MISSING REQUIRED SKILLS
        # =================================================

        missing_required_skills = find_missing_skills(
            resume_skills,
            required_job_skills
        )


        # =================================================
        # MATCHED PREFERRED SKILLS
        # =================================================

        matched_preferred_skills = sorted(
            resume_skill_set.intersection(
                preferred_skill_set
            )
        )


        # =================================================
        # MISSING PREFERRED SKILLS
        # =================================================

        missing_preferred_skills = sorted(
            preferred_skill_set - resume_skill_set
        )


        # =================================================
        # SEMANTIC MATCHING
        # =================================================

        semantic_score = calculate_semantic_similarity(
            resume_text,
            job_description
        )


        # =================================================
        # FINAL AI SCORE
        # =================================================

        final_score = calculate_weighted_score(
            required_match,
            semantic_score,
            preferred_match
        )


        # =================================================
        # ALL MISSING SKILLS
        # =================================================

        all_missing_skills = (
            missing_required_skills
            + missing_preferred_skills
        )


        # =================================================
        # LEARNING RECOMMENDATIONS
        # =================================================

        recommendations = generate_recommendations(
            all_missing_skills
        )


        # =================================================
        # RESUME STRENGTHS
        # =================================================

        strengths = generate_strengths(
            matched_required_skills,
            matched_preferred_skills
        )


        # =================================================
        # IMPROVEMENT SUGGESTIONS
        # =================================================

        improvement_suggestions = (
            generate_improvement_suggestions(
                missing_required_skills,
                missing_preferred_skills
            )
        )


        # =================================================
        # INTERVIEW QUESTIONS
        # =================================================

        interview_questions = (
            generate_interview_questions(
                all_missing_skills
            )
        )


        # =================================================
        # SUCCESS MESSAGE
        # =================================================

        st.success(
            "Resume analysis completed!"
        )


        # =================================================
        # MATCH RESULTS
        # =================================================

        st.header(
            "🎯 Match Results"
        )


        col1, col2, col3 = st.columns(3)


        with col1:

            st.metric(
                "🔑 Required Skills Match",
                f"{required_match:.2f}%"
            )


        with col2:

            st.metric(
                "🧠 Semantic Match",
                f"{semantic_score:.2f}%"
            )


        with col3:

            st.metric(
                "🤖 Final AI Score",
                f"{final_score:.2f}%"
            )


        # =================================================
        # SCORE BREAKDOWN
        # =================================================

        st.subheader(
            "⚖️ AI Score Breakdown"
        )


        (
            breakdown_col1,
            breakdown_col2,
            breakdown_col3
        ) = st.columns(3)


        with breakdown_col1:

            st.write(
                "**Required Skills**"
            )

            st.write(
                f"{required_match:.2f}%"
            )

            st.caption(
                "Weight: 60%"
            )


        with breakdown_col2:

            st.write(
                "**Semantic Similarity**"
            )

            st.write(
                f"{semantic_score:.2f}%"
            )

            st.caption(
                "Weight: 30%"
            )


        with breakdown_col3:

            st.write(
                "**Preferred Skills**"
            )

            st.write(
                f"{preferred_match:.2f}%"
            )

            st.caption(
                "Weight: 10%"
            )


        # =================================================
        # AI ANALYSIS SUMMARY
        # =================================================

        st.subheader(
            "🧠 AI Analysis Summary"
        )


        summary_parts = []


        summary_parts.append(
            f"Your resume matches "
            f"{required_match:.0f}% of the required "
            f"skills for this role."
        )


        if matched_required_skills:

            strengths_text = ", ".join(
                format_skill_name(skill)
                for skill in matched_required_skills
            )

            summary_parts.append(
                "Your strongest technical matches "
                f"include {strengths_text}."
            )


        if missing_required_skills:

            gaps_text = ", ".join(
                format_skill_name(skill)
                for skill in missing_required_skills
            )

            summary_parts.append(
                "The main required skill gaps are "
                f"{gaps_text}."
            )


        if missing_preferred_skills:

            preferred_text = ", ".join(
                format_skill_name(skill)
                for skill in missing_preferred_skills
            )

            summary_parts.append(
                "Additional preferred skills that "
                "could strengthen the profile include "
                f"{preferred_text}."
            )


        for sentence in summary_parts:

            st.write(
                sentence
            )


        # =================================================
        # RESUME STRENGTHS
        # =================================================

        st.subheader(
            "💪 Resume Strengths"
        )


        if strengths:

            for strength in strengths:

                st.success(
                    strength
                )

        else:

            st.info(
                "No specific strengths detected."
            )


        # =================================================
        # IMPROVEMENT SUGGESTIONS
        # =================================================

        st.subheader(
            "🛠️ Improvement Suggestions"
        )


        if improvement_suggestions:

            for suggestion in improvement_suggestions:

                st.warning(
                    suggestion
                )

        else:

            st.success(
                "No major improvement suggestions."
            )


        # =================================================
        # SKILLS DASHBOARD
        # =================================================

        st.header(
            "📊 Skills Dashboard"
        )


        (
            dashboard_col1,
            dashboard_col2,
            dashboard_col3,
            dashboard_col4
        ) = st.columns(4)


        with dashboard_col1:

            st.metric(
                "📋 Required Skills",
                len(required_job_skills)
            )


        with dashboard_col2:

            st.metric(
                "✅ Required Matched",
                len(matched_required_skills)
            )


        with dashboard_col3:

            st.metric(
                "❌ Required Missing",
                len(missing_required_skills)
            )


        with dashboard_col4:

            st.metric(
                "📈 Skill Coverage",
                f"{required_match:.2f}%"
            )


        # =================================================
        # REQUIRED VS PREFERRED
        # =================================================

        st.subheader(
            "📌 Required vs Preferred Skills"
        )


        required_col, preferred_col = st.columns(2)


        with required_col:

            st.markdown(
                "### 🔴 Required Skills"
            )

            st.write(
                f"Total: {len(required_job_skills)}"
            )

            st.write(
                f"Matched: {len(matched_required_skills)}"
            )

            st.write(
                f"Missing: {len(missing_required_skills)}"
            )


        with preferred_col:

            st.markdown(
                "### 🟡 Preferred Skills"
            )

            st.write(
                f"Total: {len(preferred_job_skills)}"
            )

            st.write(
                f"Matched: {len(matched_preferred_skills)}"
            )

            st.write(
                f"Missing: {len(missing_preferred_skills)}"
            )


        # =================================================
        # BAR CHART
        # =================================================

        st.subheader(
            "📊 Required Skill Match"
        )


        chart_data = {

            "Matched": len(
                matched_required_skills
            ),

            "Missing": len(
                missing_required_skills
            )
        }


        st.bar_chart(
            chart_data
        )


        # =================================================
        # SKILL-BY-SKILL ANALYSIS
        # =================================================

        st.subheader(
            "📋 Skill-by-Skill Analysis"
        )


        st.markdown(
            "### ✅ Matched Skills"
        )


        if matched_required_skills:

            for skill in matched_required_skills:

                st.write(
                    f"**{format_skill_name(skill)}** — "
                    "Required & Matched"
                )


        if matched_preferred_skills:

            for skill in matched_preferred_skills:

                st.write(
                    f"**{format_skill_name(skill)}** — "
                    "Preferred & Matched"
                )


        st.markdown(
            "### ❌ Missing Skills"
        )


        if missing_required_skills:

            for skill in missing_required_skills:

                st.write(
                    f"**{format_skill_name(skill)}** — "
                    "Required & Missing"
                )


        if missing_preferred_skills:

            for skill in missing_preferred_skills:

                st.write(
                    f"**{format_skill_name(skill)}** — "
                    "Preferred & Missing"
                )


        # =================================================
        # LEARNING RECOMMENDATIONS
        # =================================================

        st.subheader(
            "📚 Learning Recommendations"
        )


        if recommendations:

            for skill, resources in recommendations.items():

                st.markdown(
                    f"### 📘 {format_skill_name(skill)}"
                )

                for resource in resources:

                    st.write(
                        f"- {resource}"
                    )

        else:

            st.info(
                "No learning recommendations available."
            )


        # =================================================
        # INTERVIEW QUESTIONS
        # =================================================

        st.subheader(
            "🎤 Interview Questions"
        )


        if interview_questions:

            for skill, questions in interview_questions.items():

                st.markdown(
                    f"### 💡 {format_skill_name(skill)}"
                )

                for question in questions:

                    st.write(
                        f"- {question}"
                    )

        else:

            st.info(
                "No interview questions generated."
            )


        # =================================================
        # DOWNLOAD TXT REPORT
        # =================================================

        st.subheader(
            "📄 Resume Analysis Report"
        )


        report_text = generate_report(

            uploaded_resume.name,

            required_match,

            semantic_score,

            preferred_match,

            final_score,

            matched_required_skills,

            missing_required_skills,

            matched_preferred_skills,

            missing_preferred_skills,

            strengths,

            improvement_suggestions,

            recommendations,

            interview_questions
        )


        st.download_button(

            label="⬇️ Download AI Analysis Report",

            data=report_text,

            file_name=(
                "AI_Resume_Analysis_Report.txt"
            ),

            mime="text/plain"
        )


        # =================================================
        # GENERATE PDF REPORT
        # =================================================

        st.subheader(
            "📑 Professional PDF Report"
        )


        pdf_file = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".pdf"
        )

        pdf_file.close()

        pdf_path = pdf_file.name


        # -------------------------------------------------
        # CREATE PDF
        # -------------------------------------------------

        generate_pdf_report(

            pdf_path,

            uploaded_resume.name,

            required_match,

            semantic_score,

            preferred_match,

            final_score,

            matched_required_skills,

            missing_required_skills,

            matched_preferred_skills,

            missing_preferred_skills,

            strengths,

            improvement_suggestions,

            recommendations,

            interview_questions
        )


        # -------------------------------------------------
        # READ PDF
        # -------------------------------------------------

        with open(
            pdf_path,
            "rb"
        ) as file:

            pdf_data = file.read()


        # -------------------------------------------------
        # PDF DOWNLOAD BUTTON
        # -------------------------------------------------

        st.download_button(

            label="📄 Download Professional PDF Report",

            data=pdf_data,

            file_name=(
                "AI_Resume_Analysis_Report.pdf"
            ),

            mime="application/pdf"
        )


        # -------------------------------------------------
        # DELETE TEMPORARY PDF
        # -------------------------------------------------

        if os.path.exists(pdf_path):

            os.remove(
                pdf_path
            )


    finally:

        # -------------------------------------------------
        # DELETE TEMPORARY RESUME
        # -------------------------------------------------

        if os.path.exists(resume_path):

            os.remove(
                resume_path
            )