# Interview questions based on missing skills

INTERVIEW_QUESTIONS = {

    "python": [
        "What are the main features of Python?",
        "What is the difference between a list and a tuple in Python?",
        "What are Python dictionaries and how are they used?"
    ],

    "sql": [
        "What is a SQL JOIN?",
        "What is the difference between INNER JOIN and LEFT JOIN?",
        "What is a subquery in SQL?"
    ],

    "machine learning": [
        "What is supervised learning?",
        "What is the difference between classification and regression?",
        "What is overfitting and how can it be reduced?"
    ],

    "deep learning": [
        "What is a neural network?",
        "What is backpropagation?",
        "What is the difference between CNN and RNN?"
    ],

    "natural language processing": [
        "What is Natural Language Processing?",
        "What is tokenization?",
        "What are word embeddings?"
    ],

    "pytorch": [
        "What is PyTorch?",
        "What is a tensor in PyTorch?",
        "How do you build a neural network using PyTorch?"
    ],

    "tensorflow": [
        "What is TensorFlow?",
        "What is Keras?",
        "How do you train a neural network using TensorFlow?"
    ],

    "scikit-learn": [
        "What is Scikit-learn?",
        "How do you split data into training and testing sets?",
        "What is the purpose of model evaluation?"
    ],

    "statistics": [
        "What is mean, median and mode?",
        "What is standard deviation?",
        "What is the difference between correlation and causation?"
    ],

    "data visualization": [
        "Why is data visualization important?",
        "What is the difference between a bar chart and a histogram?",
        "When would you use a scatter plot?"
    ]
}


def generate_interview_questions(missing_skills):
    """
    Generate interview questions based on missing skills.
    """

    questions = {}

    for skill in missing_skills:

        if skill in INTERVIEW_QUESTIONS:
            questions[skill] = INTERVIEW_QUESTIONS[skill]

        else:
            questions[skill] = [
                f"What is {skill}?",
                f"Why is {skill} important?",
                f"How is {skill} used in real-world applications?"
            ]

    return questions


if __name__ == "__main__":

    missing_skills = [
        "deep learning",
        "tensorflow",
        "pytorch"
    ]

    questions = generate_interview_questions(
        missing_skills
    )

    print("Interview Questions:")

    for skill, skill_questions in questions.items():

        print(f"\n{skill.title()}:")

        for question in skill_questions:
            print("-", question)