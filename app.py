import streamlit as st
import pandas as pd
import joblib

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Digital Grip",
    page_icon="📱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# LOAD MODEL
# ============================================================

model = joblib.load("digital_grip_model.pkl")
features = joblib.load("digital_grip_features.pkl")

label_mapping = {
    0: "Very Low",
    1: "Low",
    2: "Moderate",
    3: "High",
    4: "Very High"
}

# ============================================================
# CUSTOM STYLE
# ============================================================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(
            circle at 10% 10%,
            rgba(70, 90, 255, 0.12),
            transparent 30%
        ),
        radial-gradient(
            circle at 90% 20%,
            rgba(150, 50, 255, 0.12),
            transparent 30%
        ),
        linear-gradient(
            135deg,
            #030b18,
            #071426,
            #050b17
        );
}

h1, h2, h3 {
    color: #f4f7ff !important;
}

p {
    color: #b8c6dc;
}

section[data-testid="stSidebar"] {
    background:
        linear-gradient(
            180deg,
            #061224,
            #030a16
        );
}

section[data-testid="stSidebar"] * {
    color: #eaf1ff;
}

.stButton > button {
    background:
        linear-gradient(
            90deg,
            #24b9ff,
            #7c3cff
        );
    color: white;
    border: none;
    border-radius: 12px;
    font-weight: 700;
    padding: 10px 20px;
}

[data-testid="stMetric"] {
    background: rgba(8, 25, 45, 0.75);
    border: 1px solid rgba(100, 150, 255, 0.20);
    border-radius: 15px;
    padding: 15px;
}

.stSlider label {
    color: #eaf1ff !important;
}

[data-testid="stDataFrame"] {
    border-radius: 12px;
}

hr {
    border-color: rgba(100, 150, 255, 0.18);
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# NAVIGATION SETUP
# ============================================================

pages = [
    "🏠 Home",
    "🔮 Predict Risk",
    "📊 Analytics",
    "🤖 Model Information",
    "ℹ️ About"
]

if "current_page" not in st.session_state:
    st.session_state.current_page = "🏠 Home"

# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        "# 📱 Digital **Grip**"
    )

    st.caption(
        "Smartphone Dependence Analysis"
    )

    st.markdown("---")

    selected_page = st.radio(
        "Navigation",
        pages,
        index=pages.index(
            st.session_state.current_page
        )
    )

    st.session_state.current_page = selected_page

    st.markdown("---")

    st.caption(
        "Understand your habits.\n\n"
        "Discover your digital dependence.\n\n"
        "Build healthier habits."
    )

page = st.session_state.current_page

# ============================================================
# HOME PAGE
# ============================================================

if page == "🏠 Home":

    st.markdown(
        "# Is Your Smartphone **Controlling You?**"
    )

    st.markdown(
        "### UNDERSTAND • ANALYZE • BUILD HEALTHIER HABITS"
    )

    st.write(
        "Digital Grip helps you understand your smartphone "
        "habits, estimate your digital dependence level using "
        "machine learning, and discover personalized insights "
        "for a healthier digital life."
    )

    st.markdown("")

    # --------------------------------------------------------
    # EXPLORE BUTTON
    # --------------------------------------------------------

    if st.button(
        "🔮 Explore Your Digital Habits",
        use_container_width=False
    ):
        st.session_state.current_page = "🔮 Predict Risk"
        st.rerun()

    st.markdown("---")

    # --------------------------------------------------------
    # INTRODUCTION
    # --------------------------------------------------------

    st.header(
        "📱 Understand Your Digital Habits"
    )

    col1, col2 = st.columns([1.4, 1])

    with col1:

        st.write(
            "Your smartphone is an important part of everyday "
            "life. Digital Grip helps you understand how your "
            "smartphone behavior may relate to digital dependence."
        )

        st.write(
            "The system analyzes behavioral patterns related to:"
        )

        st.markdown("""
        - 📱 Phone checking
        - 🎯 Distraction
        - ⚡ Productivity
        - 📚 Daily responsibilities
        - 😴 Sleep impact
        - 🌙 Night-time checking
        - 🔄 Urge to check
        - 🛑 Difficulty reducing smartphone usage
        """)

    with col2:

        st.markdown(
            "## 📱 Better Habits"
        )

        st.markdown(
            "### Brighter Digital Life 🌱"
        )

        st.info(
            "Awareness is the first step toward healthier "
            "smartphone usage."
        )

    st.markdown("---")

    # --------------------------------------------------------
    # FIVE DEPENDENCE LEVELS
    # --------------------------------------------------------

    st.header(
        "🎯 Five Dependence Levels"
    )

    st.write(
        "Your prediction will fall into one of these five levels."
    )

    levels = [
        ("🟢", "Very Low", "Healthy usage"),
        ("🟢", "Low", "Mild indicators"),
        ("🟡", "Moderate", "Noticeable patterns"),
        ("🔴", "High", "Strong indicators"),
        ("🟣", "Very High", "Severe indicators")
    ]

    cols = st.columns(5)

    for col, (icon, level, description) in zip(
        cols,
        levels
    ):

        with col:

            st.markdown(
                f"### {icon} {level}"
            )

            st.caption(
                description
            )

    st.markdown("---")

    # --------------------------------------------------------
    # HOW IT WORKS
    # --------------------------------------------------------

    st.header(
        "🔍 How Digital Grip Works"
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.subheader(
            "1️⃣ Enter Your Habits"
        )

        st.write(
            "Answer simple questions about your everyday "
            "smartphone behavior."
        )

    with col2:

        st.subheader(
            "2️⃣ ML Prediction"
        )

        st.write(
            "The machine learning model analyzes your "
            "behavioral patterns."
        )

    with col3:

        st.subheader(
            "3️⃣ Get Insights"
        )

        st.write(
            "Receive your estimated dependence level and "
            "personalized digital wellbeing recommendations."
        )

    st.markdown("---")

    st.header(
        "🌱 Take Control of Your Digital Habits"
    )

    st.write(
        "Technology should support your life — not control it."
    )

# ============================================================
# PREDICT RISK PAGE
# ============================================================

elif page == "🔮 Predict Risk":

    st.title(
        "🔮 Smartphone Dependence Prediction"
    )

    st.write(
        "Tell us about your smartphone habits."
    )

    st.info(
        "Rate each behavior from 1 to 5. "
        "Higher values generally represent stronger "
        "smartphone-related behavior."
    )

    st.header(
        "📊 Your Smartphone Habits"
    )

    questions = {

        "Phone_Checking":
            "📱 How often do you check your phone without a notification?",

        "Usage_Interference":
            "📚 How often does smartphone use interfere with your daily responsibilities?",

        "Urge_To_Check":
            "🔄 How often do you feel the urge to check your phone without a reason?",

        "Productivity_Impact":
            "⚡ How often does smartphone use reduce your productivity?",

        "Distraction":
            "🎯 How often does smartphone use distract you while studying or working?",

        "Comfort_Without_Phone":
            "📵 How uncomfortable do you feel without your smartphone?",

        "Reduce_Difficulty":
            "🛑 How difficult is it for you to reduce smartphone usage?",

        "Check_Within_15_Min":
            "🌅 How often do you check your phone within 15 minutes of waking up?",

        "Sleep_Impact":
            "😴 To what extent does smartphone usage affect your sleep?",

        "Night_Checking":
            "🌙 How often do you wake up during the night and check your phone?"
    }

    input_values = {}

    col1, col2 = st.columns(2)

    for index, feature in enumerate(features):

        if feature not in questions:
            continue

        with (
            col1
            if index % 2 == 0
            else col2
        ):

            input_values[feature] = st.slider(
                questions[feature],
                min_value=1,
                max_value=5,
                value=3,
                key=feature
            )

    st.markdown("")

    if st.button(
        "🔮 Predict My Dependence",
        use_container_width=True
    ):

        user_data = pd.DataFrame(
            [input_values]
        )

        user_data = user_data[features]

        prediction = model.predict(
            user_data
        )[0]

        probabilities = model.predict_proba(
            user_data
        )[0]

        predicted_label = label_mapping[
            prediction
        ]

        confidence = (
            probabilities[prediction] * 100
        )

        st.markdown("---")

        # ----------------------------------------------------
        # RESULT
        # ----------------------------------------------------

        st.header(
            "🎯 Your Result"
        )

        st.success(
            f"Your estimated smartphone dependence level is: "
            f"**{predicted_label}**"
        )

        st.metric(
            "Model Confidence",
            f"{confidence:.2f}%"
        )

        # ----------------------------------------------------
        # OVERALL LEVEL
        # ----------------------------------------------------

        st.subheader(
            "📊 Overall Dependence Level"
        )

        risk_levels = [
            "Very Low",
            "Low",
            "Moderate",
            "High",
            "Very High"
        ]

        for level in risk_levels:

            if level == predicted_label:

                st.success(
                    f"🎯 **YOUR RESULT → {level}**"
                )

            else:

                st.write(
                    f"○ {level}"
                )

        # ----------------------------------------------------
        # PROBABILITY
        # ----------------------------------------------------

        st.subheader(
            "📈 Prediction Probability"
        )

        probability_df = pd.DataFrame(
            {
                "Probability (%)":
                    probabilities * 100
            },
            index=[
                "Very Low",
                "Low",
                "Moderate",
                "High",
                "Very High"
            ]
        )

        st.bar_chart(
            probability_df
        )

        # ----------------------------------------------------
        # KEY FACTORS
        # ----------------------------------------------------

        st.subheader(
            "🧠 Key Behavioral Factors"
        )

        importance = model.feature_importances_

        factor_data = []

        for feature, importance_value in zip(
            features,
            importance
        ):

            factor_data.append(
                (
                    feature,
                    input_values[feature],
                    importance_value
                )
            )

        factor_data.sort(
            key=lambda x: x[1] * x[2],
            reverse=True
        )

        factor_col1, factor_col2 = st.columns(2)

        for index, (
            feature,
            value,
            importance_value
        ) in enumerate(
            factor_data[:6]
        ):

            display_name = (
                feature
                .replace("_", " ")
                .title()
            )

            with (
                factor_col1
                if index % 2 == 0
                else factor_col2
            ):

                st.info(
                    f"**{display_name}**\n\n"
                    f"Your rating: **{value}/5**"
                )

        # ----------------------------------------------------
        # RECOMMENDATIONS
        # ----------------------------------------------------

        st.subheader(
            "💡 Digital Wellbeing Recommendations"
        )

        if predicted_label in [
            "High",
            "Very High"
        ]:

            recommendations = [

                "📵 Set specific phone-free periods during study or work.",

                "🔕 Reduce unnecessary notifications and alerts.",

                "🌙 Avoid smartphone use close to bedtime.",

                "⏱️ Set daily limits for high-distraction apps.",

                "🧘 Try short periods of intentional phone-free time."
            ]

        elif predicted_label == "Moderate":

            recommendations = [

                "⏱️ Monitor your daily smartphone usage.",

                "📵 Try short phone-free periods during focused work.",

                "🌙 Reduce smartphone use before sleeping.",

                "🔕 Turn off non-essential notifications."
            ]

        else:

            recommendations = [

                "🌱 Your current responses do not indicate strong concerns.",

                "📱 Continue maintaining balanced smartphone habits.",

                "⏱️ Keep monitoring your usage over time.",

                "🌙 Maintain healthy sleep and phone-use boundaries."
            ]

        for recommendation in recommendations:

            st.write(
                f"💡 {recommendation}"
            )

# ============================================================
# ANALYTICS PAGE
# ============================================================

elif page == "📊 Analytics":

    st.title(
        "📊 Analytics"
    )

    st.write(
        "Explore the machine learning model and the behavioral "
        "features used for prediction."
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "ML Model",
            "Random Forest"
        )

    with col2:

        st.metric(
            "Test Accuracy",
            "88.67%"
        )

    with col3:

        st.metric(
            "Risk Levels",
            "5"
        )

    st.markdown("---")

    st.header(
        "🧠 Feature Importance"
    )

    importance_df = pd.DataFrame(
        {
            "Feature": features,
            "Importance":
                model.feature_importances_
        }
    )

    importance_df = (
        importance_df
        .sort_values(
            "Importance",
            ascending=False
        )
    )

    chart_df = importance_df.copy()

    chart_df["Feature"] = (
        chart_df["Feature"]
        .str.replace(
            "_",
            " ",
            regex=False
        )
        .str.title()
    )

    chart_df = chart_df.set_index(
        "Feature"
    )

    st.bar_chart(
        chart_df
    )

    st.header(
        "📋 Behavioral Indicators"
    )

    table_df = importance_df.copy()

    table_df["Feature"] = (
        table_df["Feature"]
        .str.replace(
            "_",
            " ",
            regex=False
        )
        .str.title()
    )

    table_df["Importance (%)"] = (
        table_df["Importance"] * 100
    ).round(2)

    table_df = table_df[
        [
            "Feature",
            "Importance (%)"
        ]
    ]

    table_df = table_df.rename(
        columns={
            "Feature":
                "Behavioral Indicator"
        }
    )

    st.dataframe(
        table_df,
        use_container_width=True,
        hide_index=True
    )

# ============================================================
# MODEL INFORMATION PAGE
# ============================================================

elif page == "🤖 Model Information":

    st.title(
        "🤖 Model Information"
    )

    st.write(
        "Digital Grip uses a Random Forest classification "
        "model to estimate smartphone dependence."
    )

    st.header(
        "🌳 Random Forest"
    )

    st.write(
        "Random Forest is an ensemble machine learning algorithm "
        "that combines multiple decision trees to make a final "
        "classification."
    )

    st.write(
        "The model analyzes the behavioral indicators provided "
        "by the user and predicts one of five dependence levels."
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Algorithm",
            "Random Forest"
        )

    with col2:

        st.metric(
            "Input Features",
            "10"
        )

    with col3:

        st.metric(
            "Classes",
            "5"
        )

    st.markdown("---")

    st.header(
        "🎯 Prediction Classes"
    )

    class_df = pd.DataFrame(
        {
            "Dependence Level": [
                "Very Low",
                "Low",
                "Moderate",
                "High",
                "Very High"
            ],

            "Description": [
                "Healthy usage patterns",
                "Mild dependence indicators",
                "Noticeable dependence patterns",
                "Strong dependence indicators",
                "Severe dependence indicators"
            ]
        }
    )

    st.dataframe(
        class_df,
        use_container_width=True,
        hide_index=True
    )

    st.header(
        "📌 Model Inputs"
    )

    feature_names = [
        feature
        .replace("_", " ")
        .title()
        for feature in features
    ]

    for index in range(
        0,
        len(feature_names),
        2
    ):

        col1, col2 = st.columns(2)

        with col1:

            st.info(
                f"🔹 {feature_names[index]}"
            )

        if index + 1 < len(feature_names):

            with col2:

                st.info(
                    f"🔹 {feature_names[index + 1]}"
                )

# ============================================================
# ABOUT PAGE
# ============================================================

elif page == "ℹ️ About":

    st.title(
        "ℹ️ About Digital Grip"
    )

    st.write(
        "Digital Grip is a machine learning project focused on "
        "understanding smartphone-related behavioral patterns "
        "and estimating digital dependence."
    )

    st.header(
        "🎯 Project Objective"
    )

    st.write(
        "The goal of Digital Grip is to help users understand "
        "their smartphone-related behaviors and identify patterns "
        "associated with different levels of smartphone dependence."
    )

    st.write(
        "The system combines behavioral inputs with machine "
        "learning to provide an estimated dependence level and "
        "digital wellbeing recommendations."
    )

    st.markdown("---")

    st.header(
        "⚙️ What Digital Grip Analyzes"
    )

    topics = [

        "📱 Phone Checking",
        "🎯 Distraction",
        "⚡ Productivity",
        "📚 Daily Responsibilities",
        "🌅 Morning Phone Checking",
        "😴 Sleep Impact",
        "🌙 Night Checking",
        "📵 Comfort Without Phone",
        "🛑 Difficulty Reducing Usage",
        "🔄 Urge To Check"
    ]

    col1, col2 = st.columns(2)

    for index, topic in enumerate(topics):

        with (
            col1
            if index % 2 == 0
            else col2
        ):

            st.info(topic)

    st.markdown("---")

    st.header(
        "🌱 Digital Wellbeing"
    )

    st.write(
        "Technology should support your life — not control it."
    )

    st.write(
        "Digital Grip is designed to encourage awareness of "
        "smartphone habits and help users make more intentional "
        "decisions about their digital behavior."
    )

# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "Digital Grip • Smartphone Usage & Digital Dependence Analysis"
)

st.caption(
    "Built using Machine Learning and Streamlit"
)
