
import streamlit as st
import plotly.express as px
import database
if "profile" not in st.session_state:
    st.session_state.profile = database.load_student()

st.set_page_config(
    page_title="PATHFINITY AI",
    page_icon="🚀",
    layout="wide"
)

if "profile" not in st.session_state:
    st.session_state.profile = None


st.markdown("""
<style>

/* MAIN BACKGROUND */
.stApp {
    background:
        radial-gradient(ellipse at 10% 10%, #31106b 0%, transparent 35%),
        radial-gradient(ellipse at 90% 20%, #092e65 0%, transparent 35%),
        radial-gradient(ellipse at 50% 100%, #240b46 0%, transparent 45%),
        #070713;
    color: #ffffff;
}

/* MAIN CONTENT */
.block-container {
    padding-top: 2.5rem;
    padding-bottom: 3rem;
    max-width: 1450px;
}

/* HEADINGS */
h1 {
    color: #ffffff !important;
    font-size: 3rem !important;
    font-weight: 900 !important;
    letter-spacing: -1.5px;
}

h2, h3 {
    color: #e5d9ff !important;
    font-weight: 800 !important;
}

p, label, span {
    color: #e4e1f5;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #110d27, #080817);
    border-right: 1px solid rgba(155, 92, 255, 0.35);
}

section[data-testid="stSidebar"] h1 {
    color: #b58cff !important;
    font-size: 1.8rem !important;
}

/* NAVIGATION */
section[data-testid="stSidebar"] [data-testid="stRadio"] label {
    color: #e5ddff !important;
}

/* METRIC CARDS */
[data-testid="stMetric"] {
    background: linear-gradient(
        135deg,
        rgba(113, 65, 220, 0.25),
        rgba(18, 160, 220, 0.10)
    );
    border: 1px solid rgba(174, 121, 255, 0.45);
    padding: 22px;
    border-radius: 18px;
    box-shadow: 0 0 22px rgba(116, 60, 255, 0.12);
}

/* BUTTONS */
.stButton > button,
.stFormSubmitButton > button {
    background: linear-gradient(100deg, #7b35ff, #168bff);
    color: white !important;
    border: 1px solid rgba(255,255,255,0.2);
    border-radius: 12px;
    padding: 0.65rem 1.3rem;
    font-weight: 800;
    transition: 0.25s ease;
    box-shadow: 0 0 15px rgba(116, 60, 255, 0.35);
}

.stButton > button:hover,
.stFormSubmitButton > button:hover {
    transform: translateY(-3px);
    box-shadow: 0 0 25px rgba(32, 159, 255, 0.65);
    border-color: #b88aff;
}

/* INPUT FIELDS */
.stTextInput input,
.stSelectbox div[data-baseweb="select"],
.stMultiSelect div[data-baseweb="select"] {
    background-color: #17152c;
    border-radius: 10px;
}

/* EXPANDERS */
.streamlit-expanderHeader {
    background: rgba(100, 60, 180, 0.18);
    border: 1px solid rgba(160, 110, 255, 0.3);
    border-radius: 12px;
    color: white !important;
}

/* PROGRESS BAR */
.stProgress > div > div > div {
    background: linear-gradient(90deg, #9d4dff, #00d9ff);
}

/* DIVIDERS */
hr {
    border-color: rgba(157, 100, 255, 0.3);
}

/* ALERTS */
div[data-testid="stAlert"] {
    background: rgba(93, 63, 160, 0.17);
    border: 1px solid rgba(166, 120, 255, 0.4);
    border-radius: 14px;
}

/* CHART CONTAINERS */
div[data-testid="stPlotlyChart"] {
    background: rgba(19, 17, 43, 0.72);
    border: 1px solid rgba(145, 100, 255, 0.3);
    border-radius: 18px;
    padding: 12px;
}

/* HIDE STREAMLIT BRANDING */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)
# Career skill requirements (prototype data)
career_skills = {
    "Software Developer": [
        "Python", "Problem Solving", "C / C++",
        "Java", "Git and GitHub", "SQL",
        "Data Structures and Algorithms"
    ],
    "Data Analyst": [
        "Python", "Excel", "SQL",
        "Data Analysis", "Statistics",
        "Data Visualization"
    ],
    "AI / ML Engineer": [
        "Python", "Mathematics", "Statistics",
        "Machine Learning", "Data Analysis",
        "Problem Solving"
    ],
    "Business Analyst": [
        "Excel", "Communication", "Problem Solving",
        "Data Analysis", "Presentation",
        "Business Knowledge"
    ],
    "Financial Analyst": [
        "Excel", "Financial Analysis", "Accounting",
        "Data Analysis", "Communication"
    ],
    "UI / UX Designer": [
        "Graphic Design", "Creativity",
        "Communication", "User Research",
        "Prototyping"
    ],
    "Digital Marketer": [
        "Communication", "Creativity",
        "Writing", "Digital Marketing",
        "Data Analysis"
    ],
    "Content Strategist": [
        "Writing", "Creativity", "Research",
        "Communication", "Content Planning"
    ],
    "Entrepreneur": [
        "Leadership", "Communication",
        "Problem Solving", "Business Knowledge",
        "Creativity"
    ],
    "Researcher": [
        "Research", "Problem Solving",
        "Communication", "Statistics",
        "Writing"
    ]
}

st.sidebar.title("🚀 PATHFINITY AI")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "My Career DNA",
        "AI Skill Gap Analyzer",
        "Smart Career Roadmap",
        "Mission Tracker"
    ]
)

# DASHBOARD
if page == "Dashboard":

    st.title("🚀 PATHFINITY AI")
    st.subheader("Your Potential. Your Path. Your Future.")

    st.write("Your personalized career intelligence platform.")
    st.divider()

    st.header("Your Career Dashboard")

    if st.session_state.profile:
        profile = st.session_state.profile

        st.success(f"Welcome back, {profile['name']}!")

        col1, col2, col3 = st.columns(3)

        col1.metric("Profile Status", "Created")
        col2.metric("Career Goal", profile["goal"])
        col3.metric("Skills Added", len(profile["skills"]))

        st.write("Academic stream:", profile["stream"])

    else:
        st.info("Start by creating your Career DNA profile.")

# CAREER DNA
elif page == "My Career DNA":

    st.title("🧬 My Career DNA")

    st.write("Tell us about yourself to personalize your career journey.")

    with st.form("career_profile"):

        st.subheader("01 — Personal Information")

        name = st.text_input("Your full name")

        year = st.selectbox(
            "Current academic year",
            ["1st Year", "2nd Year", "3rd Year", "4th Year", "Other"]
        )

        stream = st.selectbox(
            "Your academic stream",
            [
                "Computer Science",
                "Engineering - Other",
                "Commerce",
                "Science",
                "Arts and Humanities",
                "Management",
                "Medicine and Healthcare",
                "Law",
                "Other"
            ]
        )

        st.subheader("02 — Your Interests")

        interests = st.multiselect(
            "Select your interests",
            [
                "Technology", "Business", "Finance",
                "Design", "Creativity", "Research",
                "Communication", "Science",
                "Entrepreneurship", "Social Impact"
            ]
        )

        st.subheader("03 — Your Current Skills")

        skills = st.multiselect(
            "Select your existing skills",
            [
                "Python", "C / C++", "Java", "Excel",
                "Communication", "Leadership",
                "Problem Solving", "Graphic Design",
                "Writing", "Data Analysis", "Research"
            ]
        )

        st.subheader("04 — Your Dream Career")

        goal = st.selectbox(
            "Choose your career interest",
            list(career_skills.keys()) + ["Not Sure Yet"]
        )

        submitted = st.form_submit_button("Create My Career DNA 🚀")

        
        if submitted:

            if not name.strip():
                st.error("Please enter your name.")

            elif not interests:
                st.error("Please select at least one interest.")

            elif not skills:
                st.error("Please select at least one skill.")

            else:
                st.session_state.profile = {
                    "name": name,
                    "year": year,
                    "stream": stream,
                    "interests": interests,
                    "skills": skills,
                    "goal": goal
                }

                database.save_student(
                    name,
                    year,
                    stream,
                    interests,
                    skills,
                    goal
                )

                st.success("Your Career DNA has been saved successfully!")


    if st.session_state.profile:

        profile = st.session_state.profile

        st.divider()
        st.header("Your Career DNA Summary")

        st.write("**Name:**", profile["name"])
        st.write("**Academic Year:**", profile["year"])
        st.write("**Academic Stream:**", profile["stream"])
        st.write("**Career Goal:**", profile["goal"])
        st.write("**Interests:**", ", ".join(profile["interests"]))
        st.write("**Current Skills:**", ", ".join(profile["skills"]))

# SKILL GAP ANALYZER
elif page == "AI Skill Gap Analyzer":

    st.title("🧠 AI Skill Gap Analyzer")

    st.write(
        "Discover which skills you already have and "
        "which skills you need to develop for your dream career."
    )

    st.divider()

    if not st.session_state.profile:

        st.warning("Please create your Career DNA profile first.")

    else:

        profile = st.session_state.profile
        goal = profile["goal"]

        if goal == "Not Sure Yet":

            st.info(
                "Choose a career in My Career DNA before "
                "using the Skill Gap Analyzer."
            )

        else:

            required = career_skills[goal]
            existing = profile["skills"]

            matched = [
                skill for skill in required
                if skill in existing
            ]

            missing = [
                skill for skill in required
                if skill not in existing
            ]

            score = round(
                (len(matched) / len(required)) * 100
            )

            st.subheader(f"Career Target: {goal}")

            st.metric(
                "Skill Coverage",
                f"{score}%",
                help="Percentage of listed role skills already selected in your profile."
            )

            st.progress(score / 100)

            col1, col2 = st.columns(2)

            with col1:
                st.success("Skills You Already Have")

                if matched:
                    for skill in matched:
                        st.write("✅ " + skill)
                else:
                    st.write("No matching skills yet.")

            with col2:
                st.warning("Skills You Need to Develop")

                if missing:
                    for skill in missing:
                        st.write("📌 " + skill)
                else:
                    st.write("You have selected all listed skills!")

            st.divider()

            st.subheader("Your Skill Gap Overview")

            chart_data = {
                "Category": ["Skills You Have", "Skills To Develop"],
                "Number of Skills": [
                    len(matched),
                    len(missing)
                ]
            }

            fig = px.pie(
                chart_data,
                names="Category",
                values="Number of Skills",
                hole=0.55,
                title="Your Career Skill Coverage"
            )

            fig.update_layout(
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                font_color="white"
            )

            st.plotly_chart(fig, use_container_width=True)

            st.divider()

            st.subheader("Recommended Next Steps")

            for index, skill in enumerate(missing[:3], start=1):
                st.write(f"{index}. Start learning **{skill}**")

            st.caption(
                "Prototype estimate based on predefined skill lists "
                "and the skills selected by the student. "
                "It is not a validated measure of job readiness."
            )
    # SMART CAREER ROADMAP
elif page == "Smart Career Roadmap":

    st.title("🗺️ Your Smart Career Roadmap")

    st.write(
        "A personalized action plan to help you move "
        "towards your dream career."
    )

    st.divider()

    if not st.session_state.profile:

        st.warning("Please create your Career DNA profile first.")

    else:

        profile = st.session_state.profile
        goal = profile["goal"]

        if goal == "Not Sure Yet":

            st.info("Please select a career goal in My Career DNA.")

        else:

            required = career_skills[goal]
            existing = profile["skills"]

            missing = [
                skill for skill in required
                if skill not in existing
            ]

            if not missing:
                missing = [
                    "Build a practical portfolio project",
                    "Practice career-related interview questions",
                    "Create a professional resume"
                ]

            weekly_tasks = [
                missing[i:i + 2]
                for i in range(0, len(missing), 2)
            ]

            while len(weekly_tasks) < 4:
                weekly_tasks.append([
                    "Complete a practical mini project",
                    "Review your progress and update your resume"
                ])

            weekly_tasks = weekly_tasks[:4]

            st.subheader(f"🎯 Your Target: {goal}")

            st.info(
                "Complete these weekly missions to work "
                "towards your selected career."
            )

            st.divider()

            st.subheader("📅 Your 4-Week Learning Journey")

            for week_number, tasks in enumerate(
                weekly_tasks, start=1
            ):

                with st.expander(
                    f"Week {week_number} — Learning Mission",
                    expanded=(week_number == 1)
                ):

                    st.write("Complete these activities:")

                    for task_number, task in enumerate(
                        tasks, start=1
                    ):

                        task_key = (
                            f"roadmap_{goal}_{week_number}_{task_number}"
                        )

                        st.checkbox(
                            f"Learn / complete: {task}",
                            key=task_key
                        )

            st.divider()

            st.subheader("🎯 Your Final Challenge")

            st.write(
                f"Create one practical project related to "
                f"{goal} and add it to your portfolio."
            )

            st.success(
                "Small consistent steps can turn your career "
                "goal into a practical learning journey!"
            )

            st.caption(
                "This is a suggested four-week learning plan, "
                "not a guarantee of career readiness."
            )

    # MISSION TRACKER
elif page == "Mission Tracker":

    st.title("🎯 Mission Tracker")

    st.write("See what you have completed and what is still pending.")

    st.divider()

    if not st.session_state.profile:

        st.warning("Please create your Career DNA profile first.")

    else:

        goal = st.session_state.profile["goal"]

        if goal == "Not Sure Yet":

            st.info("Choose a career goal to track your missions.")

        else:

            required = career_skills[goal]
            existing = st.session_state.profile["skills"]

            missing = [
                skill for skill in required
                if skill not in existing
            ]

            if not missing:
                missing = [
                    "Build a practical portfolio project",
                    "Practice career-related interview questions",
                    "Create a professional resume"
                ]

            weekly_tasks = [
                missing[i:i + 2]
                for i in range(0, len(missing), 2)
            ]

            while len(weekly_tasks) < 4:
                weekly_tasks.append([
                    "Complete a practical mini project",
                    "Review your progress and update your resume"
                ])

            weekly_tasks = weekly_tasks[:4]

            completed_tasks = []
            pending_tasks = []

            for week_number, tasks in enumerate(
                weekly_tasks, start=1
            ):

                for task_number, task in enumerate(
                    tasks, start=1
                ):

                    task_key = (
                        f"roadmap_{goal}_{week_number}_{task_number}"
                    )

                    if st.session_state.get(task_key, False):
                        completed_tasks.append(task)
                    else:
                        pending_tasks.append(task)

            total = len(completed_tasks) + len(pending_tasks)
            completed = len(completed_tasks)
            remaining = len(pending_tasks)

            progress = completed / total if total else 0

            col1, col2, col3 = st.columns(3)

            col1.metric("Total Missions", total)
            col2.metric("Completed", completed)
            col3.metric("Remaining", remaining)

            st.subheader("🚀 Your Learning Progress")

            st.progress(progress)

            st.write(f"You have completed {progress * 100:.0f}% of your missions.")

            st.divider()

            st.subheader("✅ Completed Missions")

            if completed_tasks:
                for task in completed_tasks:
                    st.success(f"✓ {task}")
            else:
                st.info("No missions completed yet.")

            st.subheader("⏳ Pending Missions")

            if pending_tasks:
                for task in pending_tasks:
                    st.write(f"○ {task}")
            else:
                st.success("All missions completed! 🎉")


