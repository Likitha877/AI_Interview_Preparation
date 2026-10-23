import random
import streamlit as st

st.set_page_config(page_title="AI Interview Preparation", page_icon="🤖", layout="wide")

if "xp" not in st.session_state:
    st.session_state.xp = 0
if "answered" not in st.session_state:
    st.session_state.answered = 0

TECHNICAL = {
    "Python": [
        ("What is a list in Python?", "A mutable ordered collection of items."),
        ("What is inheritance?", "Inheritance allows a class to reuse properties and methods of another class."),
        ("What is a dictionary?", "A collection of key-value pairs."),
    ],
    "OOP": [
        ("What is polymorphism?", "Polymorphism allows the same interface to work with different object types."),
        ("What is encapsulation?", "Encapsulation bundles data and methods and controls access to them."),
        ("What is abstraction?", "Abstraction hides implementation details and exposes essential features."),
    ],
    "DBMS": [
        ("What is a primary key?", "A field or combination of fields that uniquely identifies a record."),
        ("What is normalization?", "Organizing data to reduce redundancy and improve consistency."),
    ],
    "Operating Systems": [
        ("What is a process?", "A program in execution."),
        ("What is a thread?", "A lightweight unit of execution within a process."),
        ("What is deadlock?", "A situation where processes wait indefinitely for resources held by each other."),
    ],
}

HR = [
    "Tell me about yourself.",
    "What are your strengths?",
    "What is one skill you are improving?",
    "Why should we hire you?",
    "Where do you see yourself in five years?",
]

CODING = [
    "Write a Python program to check whether a number is prime.",
    "Write a Python program to reverse a string.",
    "Write a Python program to find the largest element in a list.",
    "Write a Python program to count vowels in a string.",
]

MOCK = [
    "Tell me about yourself.",
    "Explain one academic project you completed.",
    "What is OOP?",
    "What is the difference between a process and a thread?",
    "What are your career goals?",
]

st.sidebar.title("🤖 AI Interview Prep")
menu = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "👤 Profile",
        "💻 Technical Interview",
        "👔 HR Interview",
        "👨‍💻 Coding Interview",
        "🎤 Mock Interview",
        "📊 Performance",
        "📄 Resume Analyzer",
        "🎯 Career Roadmap"
    ]
)

st.sidebar.metric("⭐ XP", st.session_state.xp)
st.sidebar.metric("📝 Answered", st.session_state.answered)

if menu == "🏠 Dashboard":
    st.title("🤖 AI Interview Preparation")
    st.subheader("Prepare. Practice. Improve.")
    st.write("Practice technical, HR, coding and mock interviews in one application.")
    a, b, c = st.columns(3)
    a.metric("Answered", st.session_state.answered)
    b.metric("XP", st.session_state.xp)
    c.metric("Modules", 9)
    st.divider()
    st.info("Use the menu on the left to start practicing.")

elif menu == "👤 Profile":
    st.title("👤 Student Profile")
    name = st.text_input("Name")
    branch = st.selectbox("Branch", ["CSE", "IT", "ECE", "EEE", "AI/ML", "Other"])
    level = st.selectbox("Level", ["Beginner", "Intermediate", "Advanced"])
    if st.button("💾 Save Profile"):
        st.success(f"Profile saved for {name or 'Student'} — {branch}, {level}.")

elif menu == "💻 Technical Interview":
    st.title("💻 Technical Interview")
    topic = st.selectbox("Choose a topic", list(TECHNICAL.keys()))
    question, answer = random.choice(TECHNICAL[topic])
    st.subheader("Question")
    st.info(question)
    st.text_area("Write your answer")
    if st.button("💡 Show Expected Answer"):
        st.success(answer)
    if st.button("⭐ Mark as Practiced"):
        st.session_state.answered += 1
        st.session_state.xp += 10
        st.success("Practice recorded! +10 XP")

elif menu == "👔 HR Interview":
    st.title("👔 HR Interview")
    question = random.choice(HR)
    st.info(question)
    response = st.text_area("Your answer", height=150)
    if st.button("💡 Answer Tips"):
        st.write("Be specific, keep the answer structured, and give a short real example.")
    if st.button("⭐ Complete Practice"):
        if response.strip():
            st.session_state.answered += 1
            st.session_state.xp += 10
            st.success("HR practice completed! +10 XP")
        else:
            st.warning("Please enter an answer first.")

elif menu == "👨‍💻 Coding Interview":
    st.title("👨‍💻 Coding Interview")
    question = random.choice(CODING)
    st.info(question)
    code = st.text_area("Write your Python solution", height=220)
    if st.button("✅ Submit Solution"):
        if code.strip():
            st.session_state.answered += 1
            st.session_state.xp += 15
            st.success("Solution submitted for practice! +15 XP")
        else:
            st.warning("Write some code first.")

elif menu == "🎤 Mock Interview":
    st.title("🎤 Mock Interview")
    if "mock_index" not in st.session_state:
        st.session_state.mock_index = 0
    i = st.session_state.mock_index
    if i < len(MOCK):
        st.progress(i / len(MOCK))
        st.subheader(f"Question {i + 1} of {len(MOCK)}")
        st.info(MOCK[i])
        response = st.text_area("Your response", key=f"mock_{i}", height=150)
        if st.button("➡️ Next Question"):
            if response.strip():
                st.session_state.mock_index += 1
                st.session_state.xp += 10
                st.session_state.answered += 1
                st.rerun()
            else:
                st.warning("Please answer before continuing.")
    else:
        st.success("🎉 Mock interview completed!")
        if st.button("🔄 Start Again"):
            st.session_state.mock_index = 0
            st.rerun()

elif menu == "📊 Performance":
    st.title("📊 Performance")
    st.metric("Questions Answered", st.session_state.answered)
    st.metric("XP", st.session_state.xp)
    st.subheader("⭐ XP Progress")
    st.progress(min(st.session_state.xp / 500, 1.0))
    st.write(f"{st.session_state.xp} / 500 XP")

elif menu == "📄 Resume Analyzer":
    st.title("📄 Resume Analyzer")
    file = st.file_uploader("Upload your resume", type=["pdf", "txt", "docx"])
    if file:
        st.success(f"Uploaded: {file.name}")
        st.write("✅ Highlight technical skills.")
        st.write("✅ Mention academic and personal projects.")
        st.write("✅ Keep the resume concise.")
        st.write("✅ Add measurable achievements.")
        if st.button("🎤 Start Interview"):
            st.info("Go to Mock Interview to begin practice.")

elif menu == "🎯 Career Roadmap":
    st.title("🎯 Career Roadmap")
    role = st.selectbox(
        "Choose your target career",
        ["Software Developer", "Python Developer", "Data Analyst", "AI/ML Engineer", "Full Stack Developer"],
    )
    st.subheader(f"🚀 Roadmap for {role}")
    steps = [
        "1️⃣ Learn programming fundamentals",
        "2️⃣ Practice data structures and algorithms",
        "3️⃣ Learn database management",
        "4️⃣ Build projects",
        "5️⃣ Prepare your resume",
        "6️⃣ Practice technical interviews",
        "7️⃣ Practice HR interviews",
        "8️⃣ Attend mock interviews",
        "9️⃣ Improve weak areas",
        "🔟 Start job preparation",
    ]
    for step in steps:
        st.write(step)
    st.success("Follow each step and practice regularly.")

