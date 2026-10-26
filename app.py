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
# CUSTOM DARK THEME
# ============================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(71, 91, 255, 0.14), transparent 28%),
        radial-gradient(circle at 90% 20%, rgba(150, 45, 255, 0.13), transparent 30%),
        linear-gradient(135deg, #030b18 0%, #071426 50%, #040b17 100%);
    color: #f4f7ff;
}

/* Main container */
.block-container {
    max-width: 1250px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background:
        linear-gradient(180deg, #061224 0%, #030a16 100%);
    border-right: 1px solid rgba(111, 160, 255, 0.18);
}

section[data-testid="stSidebar"] * {
    color: #eaf1ff !important;
}

.sidebar-title {
    font-size: 25px;
    font-weight: 800;
    margin-bottom: 5px;
}

.sidebar-subtitle {
    color: #8ea5c8 !important;
    font-size: 13px;
    margin-bottom: 25px;
}

/* Text */
h1, h2, h3 {
    color: #f6f8ff !important;
}

p {
    color: #aebed8;
    line-height: 1.7;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(90deg, #24b9ff, #7c3cff);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 0.65rem 1.4rem;
    font-weight: 700;
    transition: 0.25s;
    box-shadow: 0 8px 25px rgba(77, 92, 255, 0.22);
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 12px 30px rgba(77, 92, 255, 0.35);
}

/* Cards */
.dark-card {
    background: rgba(10, 25, 45, 0.78);
    border: 1px solid rgba(93, 151, 255, 0.20);
    border-radius: 18px;
    padding: 25px;
    margin: 12px 0;
    box-shadow: 0 12px 35px rgba(0,0,0,0.18);
}

.glass-card {
    background: rgba(255,255,255,0.045);
    border: 1px solid rgba(150,180,255,0.18);
    border-radius: 18px;
    padding: 24px;
    backdrop-filter: blur(12px);
}

/* Hero */
.hero {
    min-height: 430px;
    border-radius: 28px;
    padding: 55px 55px 45px 55px;
    position: relative;
    overflow: hidden;
    background:
        radial-gradient(circle at 75% 45%, rgba(0, 191, 255, 0.17), transparent 28%),
        radial-gradient(circle at 90% 20%, rgba(139, 55, 255, 0.20), transparent 28%),
        linear-gradient(120deg, #061122, #081a31 55%, #071022);
    border: 1px solid rgba(100, 160, 255, 0.20);
}

.hero-small {
    color: #91a9ff;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
}

.hero h1 {
    font-size: 52px;
    line-height: 1.08;
    margin: 18px 0;
    max-width: 650px;
}

.gradient-text {
    background: linear-gradient(90deg, #29c8ff, #8550ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero p {
    max-width: 610px;
    font-size: 17px;
}

/* Phone visual */
.phone-visual {
    background: linear-gradient(160deg, #161d49, #082f4e);
    border: 2px solid rgba(111, 179, 255, 0.30);
    border-radius: 34px;
    width: 210px;
    height: 360px;
    margin: auto;
    padding: 30px 18px;
    box-shadow:
        0 0 50px rgba(0, 170, 255, 0.18),
        0 0 90px rgba(120, 50, 255, 0.14);
    text-align: center;
}

.phone-title {
    font-size: 20px;
    font-weight: 800;
    margin-top: 70px;
}

.phone-leaf {
    font-size: 45px;
    margin-top: 15px;
}

/* Level cards */
.level-box {
    background: rgba(7, 22, 40, 0.85);
    border: 1px solid rgba(100,150,255,0.18);
    border-radius: 18px;
    padding: 20px 10px;
    text-align: center;
    height: 100%;
}

.level-dot {
    width: 15px;
    height: 15px;
    border-radius: 50%;
    margin: auto auto 12px auto;
}

.level-name {
    font-weight: 700;
    color: #eef4ff;
}

.level-desc {
    color: #8298b8;
    font-size: 12px;
    margin-top: 7px;
}

/* Step cards */
.step-card {
    background: rgba(8, 24, 43, 0.82);
    border: 1px solid rgba(95, 153, 255, 0.18);
    border-radius: 18px;
    padding: 25px;
    min-height: 190px;
}

.step-number {
    color: #53d4ff;
    font-size: 13px;
    font-weight: 800;
}

.step-icon {
    font-size: 30px;
    margin: 10px 0;
}

/* Result */
.result-card {
    background:
        radial-gradient(circle at 50% 0%, rgba(83, 88, 255, 0.20), transparent 55%),
        rgba(8, 24, 43, 0.90);
    border: 1px solid rgba(108, 150, 255, 0.28);
    border-radius: 24px;
    padding: 35px;
    text-align: center;
    margin-top: 20px;
}

.result-level {
    font-size: 42px;
    font-weight: 800;
    background: linear-gradient(90deg, #26c8ff, #a348ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Risk scale */
.risk-scale {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 10px;
    background: rgba(4, 15, 29, 0.75);
    border: 1px solid rgba(104, 158, 255, 0.20);
    border-radius: 18px;
    padding: 22px 15px;
    margin: 20px 0;
}

.risk-item {
    text-align: center;
    flex: 1;
}

.risk-dot {
    width: 14px;
    height: 14px;
    border-radius: 50%;
    margin: auto auto 8px auto;
}

.risk-active {
    font-weight: 800;
    color: #ffffff;
}

.risk-normal {
    color: #8196b6;
    font-size: 13px;
}

/* Feature cards */
.factor-card {
    background: rgba(8, 25, 45, 0.82);
    border: 1px solid rgba(91, 151, 255, 0.18);
    border-radius: 15px;
    padding: 18px;
    margin-bottom: 12px;
}

.factor-title {
    font-weight: 700;
    color: #f2f6ff;
}

.factor-value {
    color: #42caff;
    font-size: 14px;
}

/* Recommendation */
.recommendation {
    background: linear-gradient(
        90deg,
        rgba(37, 190, 255, 0.08),
        rgba(130, 60, 255, 0.08)
    );
    border-left: 4px solid #4bc9ff;
    border-radius: 12px;
    padding: 15px 18px;
    margin: 10px 0;
}

/* Metrics */
[data-testid="stMetric"] {
    background: rgba(8, 25, 45, 0.75);
    border: 1px solid rgba(90, 150, 255, 0.18);
    border-radius: 15px;
    padding: 18px;
}

[data-testid="stMetricLabel"] {
    color: #8fa8cb !important;
}

[data-testid="stMetricValue"] {
    color: #f4f7ff !important;
}

/* Slider */
.stSlider label {
    color: #e8effc !important;
}

div[data-baseweb="slider"] div {
    color: white;
}

/* Divider */
hr {
    border-color: rgba(100, 150, 255, 0.15);
}

/* Footer */
.footer {
    text-align: center;
    color: #7186a5;
    font-size: 12px;
    padding: 35px 0 10px;
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("""
    <div class="sidebar-title">📱 Digital <span style="color:#8050ff;">Grip</span></div>
    <div class="sidebar-subtitle">
    Smartphone Dependence Analysis
    </div>
    """, unsafe_allow_html=True)

    page = st.radio(
        "Navigation",
        [
            "🏠 Home",
            "🔮 Predict Risk",
            "📊 Analytics",
            "🤖 Model Information",
            "ℹ️ About"
        ]
    )

    st.markdown("---")

    st.markdown("""
    <div style="color:#7890b3;font-size:12px;">
    Understand your habits.<br>
    Discover your digital dependence.<br>
    Build healthier habits.
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# HOME PAGE
# ============================================================

if page == "🏠 Home":

    st.markdown("""
    <div class="hero">

        <div class="hero-small">
        UNDERSTAND • ANALYZE • BUILD HEALTHIER HABITS
        </div>

        <h1>
        Is Your Smartphone<br>
        <span class="gradient-text">Controlling You?</span>
        </h1>

        <p>
        Digital Grip helps you understand your smartphone habits,
        estimate your dependence level using machine learning,
        and receive personalized insights for a healthier digital life.
        </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("### ")

    col1, col2 = st.columns([1.2, 1])

    with col1:

        st.markdown("""
        <div class="dark-card">

        <h2>📱 Understand Your Digital Habits</h2>

        <p>
        Answer a few simple questions about your everyday
        smartphone behavior. Digital Grip analyzes behavioral
        patterns related to phone checking, distraction,
        productivity, sleep, and difficulty reducing usage.
        </p>

        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div class="phone-visual">

            <div style="color:#65d7ff;font-size:12px;">
            DIGITAL WELL-BEING
            </div>

            <div class="phone-title">
            Better Habits<br>
            <span class="gradient-text">Brighter Future</span>
            </div>

            <div class="phone-leaf">
            🌱
            </div>

        </div>
        """, unsafe_allow_html=True)

    # Risk levels

    st.markdown("## 🎯 5 Dependence Levels")

    st.markdown("""
    <p>
    Your prediction will fall into one of these five levels.
    </p>
    """, unsafe_allow_html=True)

    levels = [
        ("Very Low", "#39d98a", "Healthy usage patterns"),
        ("Low", "#8ee65f", "Mild signs of dependence"),
        ("Moderate", "#ffbd45", "Noticeable patterns"),
        ("High", "#ff685b", "Strong dependence indicators"),
        ("Very High", "#ed4d83", "Severe dependence indicators")
    ]

    cols = st.columns(5)

    for col, (name, color, desc) in zip(cols, levels):

        with col:

            st.markdown(f"""
            <div class="level-box">

                <div class="level-dot"
                style="background:{color};"></div>

                <div class="level-name">
                {name}
                </div>

                <div class="level-desc">
                {desc}
                </div>

            </div>
            """, unsafe_allow_html=True)

    # How it works

    st.markdown("## 🔍 How It Works")

    st.markdown("""
    <p>
    Simple steps. Powerful insights.
    </p>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    steps = [
        ("01", "📱", "Enter Your Habits",
         "Answer a few simple questions about your smartphone usage and behavior."),
        ("02", "🧠", "ML Prediction",
         "Our machine learning model analyzes your behavioral patterns and predicts your dependence level."),
        ("03", "💡", "Get Insights",
         "Receive your dependence level and practical digital wellbeing recommendations.")
    ]

    for col, (num, icon, title, text) in zip(
        [col1, col2, col3], steps
    ):

        with col:

            st.markdown(f"""
            <div class="step-card">

                <div class="step-number">{num}</div>

                <div class="step-icon">{icon}</div>

                <h3>{title}</h3>

                <p>{text}</p>

            </div>
            """, unsafe_allow_html=True)

    st.markdown("### ")

    st.markdown("""
    <div class="glass-card" style="text-align:center;">

    <h3>Small changes can make a big difference. 🌱</h3>

    <p>
    Take control of your smartphone habits and build a healthier
    relationship with technology.
    </p>

    </div>
    """, unsafe_allow_html=True)

# ============================================================
# PREDICT RISK
# ============================================================

elif page == "🔮 Predict Risk":

    st.markdown("""
    <div class="hero" style="min-height:260px;padding:40px;">

    <div class="hero-small">SMARTPHONE HABIT ANALYSIS</div>

    <h1 style="font-size:40px;">
    Understand Your <span class="gradient-text">Digital Dependence</span>
    </h1>

    <p>
    Rate each behavior from 1 to 5.
    Higher values generally represent stronger smartphone-related behavior.
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("## 📊 Your Smartphone Habits")

    input_values = {}

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

    col1, col2 = st.columns(2)

    for index, feature in enumerate(features):

        if feature not in questions:
            continue

        with (col1 if index % 2 == 0 else col2):

            input_values[feature] = st.slider(
                questions[feature],
                min_value=1,
                max_value=5,
                value=3,
                key=feature
            )

    st.markdown("### ")

    if st.button("🔮 Predict My Dependence", use_container_width=True):

        user_data = pd.DataFrame([input_values])[features]

        prediction = model.predict(user_data)[0]

        probabilities = model.predict_proba(user_data)[0]

        predicted_label = label_mapping[prediction]

        confidence = probabilities[prediction] * 100

        # Result

        st.markdown(f"""
        <div class="result-card">

        <div style="color:#8ea6c9;font-size:14px;">
        YOUR ESTIMATED SMARTPHONE DEPENDENCE LEVEL
        </div>

        <div class="result-level">
        {predicted_label}
        </div>

        <div style="color:#9fb2ce;">
        Model confidence: <b>{confidence:.2f}%</b>
        </div>

        </div>
        """, unsafe_allow_html=True)

        # Risk scale

        st.markdown("### 🎯 Your Dependence Scale")

        risk_colors = {
            "Very Low": "#39d98a",
            "Low": "#8ee65f",
            "Moderate": "#ffbd45",
            "High": "#ff685b",
            "Very High": "#ed4d83"
        }

        scale_html = '<div class="risk-scale">'

        for level in [
            "Very Low",
            "Low",
            "Moderate",
            "High",
            "Very High"
        ]:

            active = level == predicted_label

            scale_html += f"""
            <div class="risk-item">

                <div class="risk-dot"
                style="background:{risk_colors[level]};"></div>

                <div class="{'risk-active' if active else 'risk-normal'}">
                {level}
                </div>

                {'<div style="color:#55d5ff;font-size:11px;margin-top:5px;">YOUR RESULT</div>' if active else ''}

            </div>
            """

        scale_html += "</div>"

        st.markdown(scale_html, unsafe_allow_html=True)

        # Probability chart

        st.markdown("### 📈 Prediction Probability")

        probability_df = pd.DataFrame({
            "Dependence Level": [
                "Very Low",
                "Low",
                "Moderate",
                "High",
                "Very High"
            ],
            "Probability": probabilities * 100
        })

        st.bar_chart(
            probability_df.set_index("Dependence Level")
        )

        # Key factors

        st.markdown("### 🧠 Key Behavioral Factors")

        importance = model.feature_importances_

        factor_data = []

        for feature, value, imp in zip(
            features,
            [input_values[f] for f in features],
            importance
        ):

            factor_data.append({
                "feature": feature,
                "value": value,
                "score": value * imp
            })

        factor_data = sorted(
            factor_data,
            key=lambda x: x["score"],
            reverse=True
        )

        cols = st.columns(2)

        for i, factor in enumerate(factor_data[:6]):

            with cols[i % 2]:

                display_name = factor["feature"].replace("_", " ")

                st.markdown(f"""
                <div class="factor-card">

                <div class="factor-title">
                {display_name.title()}
                </div>

                <div class="factor-value">
                Your rating: {factor["value"]} / 5
                </div>

                </div>
                """, unsafe_allow_html=True)

        # Recommendations

        st.markdown("### 💡 Digital Wellbeing Recommendations")

        if predicted_label in ["Very High", "High"]:

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

            st.markdown(
                f"""
                <div class="recommendation">
                {recommendation}
                </div>
                """,
                unsafe_allow_html=True
            )

# ============================================================
# ANALYTICS
# ============================================================

elif page == "📊 Analytics":

    st.markdown("""
    <div class="hero" style="min-height:240px;padding:40px;">

    <div class="hero-small">MODEL ANALYTICS</div>

    <h1 style="font-size:40px;">
    Explore the <span class="gradient-text">Model</span>
    </h1>

    <p>
    Understand how the machine learning model performs
    and which behavioral indicators contribute most to predictions.
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("## 📊 Model Performance")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("ML Model", "Random Forest")

    with col2:
        st.metric("Test Accuracy", "88.67%")

    with col3:
        st.metric("Risk Levels", "5")

    st.markdown("## 🧠 Feature Importance")

    importance_df = pd.DataFrame({
        "Feature": features,
        "Importance": model.feature_importances_
    }).sort_values(
        "Importance",
        ascending=False
    )

    st.bar_chart(
        importance_df.set_index("Feature")
    )

    st.markdown("## 📋 Behavioral Indicators")

    display_df = importance_df.copy()

    display_df["Feature"] = (
        display_df["Feature"]
        .str.replace("_", " ")
        .str.title()
    )

    display_df["Importance"] = (
        display_df["Importance"] * 100
    ).round(2)

    display_df = display_df.rename(
        columns={
            "Feature": "Behavioral Indicator",
            "Importance": "Importance (%)"
        }
    )

    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True
    )

# ============================================================
# MODEL INFORMATION
# ============================================================

elif page == "🤖 Model Information":

    st.markdown("""
    <div class="hero" style="min-height:250px;padding:40px;">

    <div class="hero-small">MACHINE LEARNING</div>

    <h1 style="font-size:40px;">
    How the <span class="gradient-text">Model Works</span>
    </h1>

    <p>
    Digital Grip uses a Random Forest classification model
    to estimate smartphone dependence from behavioral indicators.
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("## 🤖 Random Forest")

    st.markdown("""
    <div class="dark-card">

    <p>
    Random Forest is an ensemble machine learning algorithm that
    combines multiple decision trees to make a final prediction.
    Each tree analyzes behavioral patterns from the input features,
    while the combined forest produces the final dependence level.
    </p>

    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Algorithm", "Random Forest")

    with col2:
        st.metric("Input Features", "10")

    with col3:
        st.metric("Classes", "5")

    st.markdown("## 🎯 Prediction Classes")

    class_df = pd.DataFrame({
        "Class": [
            "Very Low",
            "Low",
            "Moderate",
            "High",
            "Very High"
        ],
        "Meaning": [
            "Healthy usage patterns",
            "Mild dependence indicators",
            "Noticeable dependence patterns",
            "Strong dependence indicators",
            "Severe dependence indicators"
        ]
    })

    st.dataframe(
        class_df,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("## 📌 Model Inputs")

    feature_names = [
        feature.replace("_", " ").title()
        for feature in features
    ]

    for i in range(0, len(feature_names), 2):

        cols = st.columns(2)

        with cols[0]:

            st.markdown(
                f"""
                <div class="factor-card">
                🔹 {feature_names[i]}
                </div>
                """,
                unsafe_allow_html=True
            )

        if i + 1 < len(feature_names):

            with cols[1]:

                st.markdown(
                    f"""
                    <div class="factor-card">
                    🔹 {feature_names[i+1]}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

# ============================================================
# ABOUT
# ============================================================

elif page == "ℹ️ About":

    st.markdown("""
    <div class="hero" style="min-height:260px;padding:40px;">

    <div class="hero-small">ABOUT DIGITAL GRIP</div>

    <h1 style="font-size:40px;">
    Building a <span class="gradient-text">Healthier Digital Life</span>
    </h1>

    <p>
    Digital Grip is a machine learning project focused on
    understanding smartphone-related behavioral patterns
    and estimating digital dependence.
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("## 🎯 Project Objective")

    st.markdown("""
    <div class="dark-card">

    <p>
    The goal of Digital Grip is to help users understand
    their smartphone-related behaviors and identify patterns
    associated with different levels of smartphone dependence.
    </p>

    <p>
    The system combines behavioral inputs with machine learning
    to provide an estimated dependence level and personalized
    digital wellbeing recommendations.
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("## ⚙️ What Digital Grip Analyzes")

    topics = [
        ("📱", "Phone Checking"),
        ("🎯", "Distraction"),
        ("⚡", "Productivity"),
        ("📚", "Daily Responsibilities"),
        ("🌅", "Morning Phone Checking"),
        ("😴", "Sleep Impact"),
        ("🌙", "Night Checking"),
        ("📵", "Comfort Without Phone"),
        ("🛑", "Difficulty Reducing Usage"),
        ("🔄", "Urge To Check")
    ]

    cols = st.columns(2)

    for i, (icon, topic) in enumerate(topics):

        with cols[i % 2]:

            st.markdown(
                f"""
                <div class="factor-card">
                {icon} &nbsp; <b>{topic}</b>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown("## 🌱 Digital Wellbeing")

    st.markdown("""
    <div class="glass-card">

    <h3>Technology should support your life — not control it.</h3>

    <p>
    Digital Grip is designed to encourage awareness of smartphone
    habits and help users make more intentional decisions about
    their digital behavior.
    </p>

    </div>
    """, unsafe_allow_html=True)

# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="footer">
Digital Grip • Smartphone Usage & Digital Dependence Analysis
<br>
Built using Machine Learning and Streamlit
</div>
""", unsafe_allow_html=True)
