# 🤖 AI Resume Job Matcher

An AI-powered Resume Screening and Job Matching System that analyzes a candidate's resume against a job description and provides skill matching, semantic similarity, skill-gap analysis, learning recommendations, interview questions, and downloadable reports.

---

## 📌 Project Overview

The **AI Resume Job Matcher** is a Python-based AI/ML application designed to help candidates understand how well their resume matches a particular job description.

The system accepts:

- 📄 Resume PDF
- 💼 Job Description

It performs:

- Resume text extraction
- Skill extraction
- Required skill matching
- Preferred skill matching
- Semantic similarity analysis
- Weighted AI compatibility scoring
- Missing skill identification
- Resume strength analysis
- Learning recommendations
- Interview question generation
- TXT report generation
- Professional PDF report generation

The application provides the results through an interactive **Streamlit dashboard**.

---

## 🎯 Objectives

- Automate basic resume screening.
- Compare resume skills with job requirements.
- Identify missing technical skills.
- Measure semantic similarity between a resume and job description.
- Generate an overall AI-based compatibility score.
- Provide learning recommendations.
- Generate interview preparation questions.
- Produce downloadable analysis reports.

---

## ✨ Features

### 📄 Resume PDF Parsing

Extracts text from uploaded resume PDFs using **PyMuPDF**.

### 🔍 Skill Extraction

Identifies technical skills from resumes and job descriptions using a predefined skill dictionary and text normalization.

Supported skills include:

- Python
- Java
- C
- SQL
- MySQL
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Machine Learning
- Deep Learning
- TensorFlow
- PyTorch
- Natural Language Processing
- Computer Vision
- Statistics
- Data Preprocessing
- Data Visualization
- HTML
- CSS
- JavaScript
- Git
- GitHub
- FastAPI
- Streamlit

### 🎯 Required Skill Matching

Calculates the percentage of required job skills found in the resume.

### ⭐ Preferred Skill Matching

Analyzes preferred skills separately from required skills.

### 🧠 Semantic Matching

Uses the **all-MiniLM-L6-v2** Sentence Transformer model to calculate semantic similarity between the resume and job description.

Cosine similarity is used to compare the generated embeddings.

### 🤖 Weighted AI Score

The final score combines:

| Component | Weight |
|---|---:|
| Required Skills Match | 60% |
| Semantic Similarity | 30% |
| Preferred Skills Match | 10% |

Formula:

```text
Final Score =
(Required Match × 0.60)
+
(Semantic Similarity × 0.30)
+
(Preferred Match × 0.10)