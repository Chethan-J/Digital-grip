import streamlit as st
import pandas as pd
import joblib
import textwrap

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
# HELPER FOR HTML
# ============================================================

def render_html(html):
    st.markdown(
        textwrap.dedent(html),
        unsafe_allow_html=True
    )

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
        radial-gradient(
            circle at 10% 10%,
            rgba(71, 91, 255, 0.14),
            transparent 28%
        ),
        radial-gradient(
            circle at 90% 20%,
            rgba(150, 45, 255, 0.13),
            transparent 30%
        ),
        linear-gradient(
            135deg,
            #030b18 0%,
            #071426 50%,
            #040b17 100%
        );

    color: #f4f7ff;
}

.block-container {
    max-width: 1250px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

/* =========================================================
   SIDEBAR
   ========================================================= */

section[data-testid="stSidebar"] {
    background:
        linear-gradient(
            180deg,
            #061224 0%,
            #030a16 100%
        );

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

/* =========================================================
   TEXT
   ========================================================= */

h1, h2, h3 {
    color: #f6f8ff !important;
}

p {
    color: #aebed8;
    line-height: 1.7;
}

/* =========================================================
   BUTTONS
   ========================================================= */

.stButton > button {
    background: linear-gradient(
        90deg,
        #24b9ff,
        #7c3cff
    );

    color: white;
    border: none;
    border-radius: 12px;
    padding: 0.65rem 1.4rem;
    font-weight: 700;

    box-shadow:
        0 8px 25px rgba(77, 92, 255, 0.22);

    transition: 0.25s;
}

.stButton > button:hover {
    transform: translateY(-2px);

    box-shadow:
        0 12px 30px rgba(77, 92, 255, 0.35);
}

/* =========================================================
   CARDS
   ========================================================= */

.dark-card {
    background: rgba(10, 25, 45, 0.78);
    border: 1px solid rgba(93, 151, 255, 0.20);
    border-radius: 18px;
    padding: 25px;
    margin: 12px 0;

    box-shadow:
        0 12px 35px rgba(0,0,0,0.18);
}

.glass-card {
    background: rgba(255,255,255,0.045);
    border: 1px solid rgba(150,180,255,0.18);
    border-radius: 18px;
    padding: 24px;

    backdrop-filter: blur(12px);
}

/* =========================================================
   HERO
   ========================================================= */

.hero {
    min-height: 430px;

    border-radius: 28px;

    padding: 55px;

    position: relative;
    overflow: hidden;

    background:
        radial-gradient(
            circle at 75% 45%,
            rgba(0, 191, 255, 0.17),
            transparent 28%
        ),
        radial-gradient(
            circle at 90% 20%,
            rgba(139, 55, 255, 0.20),
            transparent 28%
        ),
        linear-gradient(
            120deg,
            #061122,
            #081a31 55%,
            #071022
        );

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
    background:
        linear-gradient(
            90deg,
            #29c8ff,
            #8550ff
        );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero p {
    max-width: 610px;
    font-size: 17px;
}

/* =========================================================
   PHONE VISUAL
   ========================================================= */

.phone-container {
    height: 330px;

    border-radius: 25px;

    background:
        radial-gradient(
            circle at 50% 30%,
            rgba(42,205,255,0.18),
            transparent 30%
        ),
        linear-gradient(
            145deg,
            #111c48,
            #071e36
        );

    border: 1px solid rgba(90,170,255,0.28);

    display: flex;
    align-items: center;
    justify-content: center;

    box-shadow:
        0 0 50px rgba(0,180,255,0.10),
        0 0 80px rgba(110,50,255,0.10);
}

.phone-visual {
    width: 175px;
    height: 285px;

    border-radius: 27px;

    background:
        linear-gradient(
            160deg,
            #111936,
            #082e49
        );

    border: 2px solid rgba(95,190,255,0.35);

    box-shadow:
        0 0 35px rgba(50,190,255,0.16);

    text-align: center;

    padding-top: 45px;
}

/* =========================================================
   LEVEL CARDS
   ========================================================= */

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

    margin:
        auto
        auto
        12px
        auto;
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

/* =========================================================
   STEP CARDS
   ========================================================= */

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

/* =========================================================
   RESULT
   ========================================================= */

.result-card {
    background:
        radial-gradient(
            circle at 50% 0%,
            rgba(83, 88, 255, 0.20),
            transparent 55%
        ),
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

    background:
        linear-gradient(
            90deg,
            #26c8ff,
            #a348ff
        );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* =========================================================
   RISK SCALE
   ========================================================= */

.risk-scale {
    display: flex;

    justify-content: space-between;

    align-items: flex-start;

    gap: 10px;

    background:
        rgba(4, 15, 29, 0.75);

    border:
        1px solid rgba(104, 158, 255, 0.20);

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

    margin:
        auto
        auto
        8px
        auto;
}

.risk-active {
    font-weight: 800;
    color: #ffffff;
}

.risk-normal {
    color: #8196b6;
    font-size: 13px;
}

/* =========================================================
   FACTOR CARDS
   ========================================================= */

.factor-card {
    background:
        rgba(8, 25, 45, 0.82);

    border:
        1px solid rgba(91, 151, 255, 0.18);

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

/* =========================================================
   RECOMMENDATIONS
   ========================================================= */

.recommendation {
    background:
        linear-gradient(
            90deg,
            rgba(37, 190, 255, 0.08),
            rgba(130, 60, 255, 0.08)
        );

    border-left:
        4px solid #4bc9ff;

    border-radius: 12px;

    padding:
        15px 18px;

    margin:
        10px 0;
}

/* =========================================================
   METRICS
   ========================================================= */

[data-testid="stMetric"] {
    background:
        rgba(8, 25, 45, 0.75);

    border:
        1px solid rgba(90, 150, 255, 0.18);

    border-radius: 15px;

    padding: 18px;
}

[data-testid="stMetricLabel"] {
    color: #8fa8cb !important;
}

[data-testid="stMetricValue"] {
    color: #f4f7ff !important;
}

/* =========================================================
   SLIDERS
   ========================================================= */

.stSlider label {
    color: #e8effc !important;
}

/* =========================================================
   DIVIDER
   ========================================================= */

hr {
    border-color: rgba(100, 150, 255, 0.15);
}

/* =========================================================
   FOOTER
   ========================================================= */

.footer {
    text-align: center;

    color: #7186a5;

    font-size: 12px;

    padding:
        35px 0
        10px;
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    render_html("""
    <div class="sidebar-title">
        📱 Digital <span style="color:#8050ff;">Grip</span>
    </div>

    <div class="sidebar-subtitle">
        Smartphone Dependence Analysis
    </div>
    """)

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

    render_html("""
    <div style="color:#7890b3;font-size:12px;">
        Understand your habits.<br>
        Discover your digital dependence.<br>
        Build healthier habits.
    </div>
    """)

# ============================================================
# HOME PAGE
# ============================================================

if page == "🏠 Home":

    render_html("""
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

        <div style="margin-top:30px;">
            <span style="
                display:inline-block;
                background:linear-gradient(90deg,#24b9ff,#7c3cff);
                padding:13px 25px;
                border-radius:12px;
                font-weight:700;
                color:white;
            ">
                Explore Your Digital Habits →
            </span>
        </div>

    </div>
    """)

    st.markdown("<br>", unsafe_allow_html=True)

    # --------------------------------------------------------
    # INTRODUCTION
    # --------------------------------------------------------

    col1, col2 = st.columns([1.25, 0.75])

    with col1:

        render_html("""
        <div class="dark-card" style="min-height:330px;">

            <div style="
                color:#50d4ff;
                font-size:13px;
                font-weight:700;
                letter-spacing:1.5px;
                margin-bottom:15px;
            ">
                DIGITAL WELLBEING
            </div>

            <h2 style="font-size:30px;">
                📱 Understand Your Digital Habits
            </h2>

            <p style="font-size:16px;">
                Your smartphone is part of everyday life.
                But how much does it influence your behavior?
            </p>

            <p style="font-size:16px;">
                Digital Grip analyzes behavioral patterns related to
                phone checking, distraction, productivity, sleep,
                and difficulty reducing smartphone usage.
            </p>

            <div style="
                margin-top:25px;
                display:flex;
                gap:10px;
                flex-wrap:wrap;
            ">

                <span style="
                    background:rgba(36,201,255,0.10);
                    border:1px solid rgba(36,201,255,0.25);
                    padding:8px 14px;
                    border-radius:20px;
                    color:#65d7ff;
                    font-size:13px;
                ">
                    Behavioral Analysis
                </span>

                <span style="
                    background:rgba(124,60,255,0.10);
                    border:1px solid rgba(124,60,255,0.25);
                    padding:8px 14px;
                    border-radius:20px;
                    color:#b58cff;
                    font-size:13px;
                ">
                    Machine Learning
                </span>

                <span style="
                    background:rgba(36,201,255,0.10);
                    border:1px solid rgba(36,201,255,0.25);
                    padding:8px 14px;
                    border-radius:20px;
                    color:#65d7ff;
                    font-size:13px;
                ">
                    Digital Wellbeing
                </span>

            </div>

        </div>
        """)

    with col2:

        render_html("""
        <div class="phone-container">

            <div class="phone-visual">

                <div style="
                    color:#67d8ff;
                    font-size:10px;
                    font-weight:700;
                    letter-spacing:1.5px;
                ">
                    DIGITAL GRIP
                </div>

                <div style="
                    font-size:42px;
                    margin-top:35px;
                ">
                    📱
                </div>

                <div style="
                    color:white;
                    font-size:18px;
                    font-weight:800;
                    margin-top:20px;
                ">
                    Better Habits
                </div>

                <div style="
                    font-size:14px;
                    margin-top:5px;
                    background:linear-gradient(90deg,#29c8ff,#a348ff);
                    -webkit-background-clip:text;
                    -webkit-text-fill-color:transparent;
                    font-weight:700;
                ">
                    Brighter Future
                </div>

                <div style="
                    font-size:27px;
                    margin-top:18px;
                ">
                    🌱
                </div>

            </div>

        </div>
        """)

    # --------------------------------------------------------
    # FIVE DEPENDENCE LEVELS
    # --------------------------------------------------------

    st.markdown("<br>", unsafe_allow_html=True)

    render_html("""
    <div style="margin-bottom:10px;">

        <h2>
            🎯 Five Dependence Levels
        </h2>

        <p>
            Your prediction will fall into one of these five levels.
        </p>

    </div>
    """)

    levels = [
        (
            "Very Low",
            "#39d98a",
            "Healthy usage"
        ),
        (
            "Low",
            "#8ee65f",
            "Mild indicators"
        ),
        (
            "Moderate",
            "#ffbd45",
            "Noticeable patterns"
        ),
        (
            "High",
            "#ff685b",
            "Strong indicators"
        ),
        (
            "Very High",
            "#ed4d83",
            "Severe indicators"
        )
    ]

    cols = st.columns(5)

    for col, (name, color, description) in zip(
        cols,
        levels
    ):

        with col:

            render_html(f"""
            <div class="level-box">

                <div class="level-dot"
                     style="
                         background:{color};
                         box-shadow:0 0 12px {color};
                     ">
                </div>

                <div class="level-name">
                    {name}
                </div>

                <div class="level-desc">
                    {description}
                </div>

            </div>
            """)

    # --------------------------------------------------------
    # HOW IT WORKS
    # --------------------------------------------------------

    st.markdown("<br>", unsafe_allow_html=True)

    render_html("""
    <div>

        <h2>
            🔍 How Digital Grip Works
        </h2>

        <p>
            Three simple steps to understand your smartphone habits.
        </p>

    </div>
    """)

    col1, col2, col3 = st.columns(3)

    steps = [
        (
            "01",
            "📱",
            "Enter Your Habits",
            "Answer simple questions about your everyday smartphone behavior."
        ),
        (
            "02",
            "🧠",
            "ML Prediction",
            "The machine learning model analyzes your behavioral patterns."
        ),
        (
            "03",
            "💡",
            "Get Insights",
            "Receive your dependence level and personalized recommendations."
        )
    ]

    for col, (
        number,
        icon,
        title,
        description
    ) in zip(
        [col1, col2, col3],
        steps
    ):

        with col:

            render_html(f"""
            <div class="step-card">

                <div class="step-number">
                    {number}
                </div>

                <div class="step-icon">
                    {icon}
                </div>

                <h3>
                    {title}
                </h3>

                <p>
                    {description}
                </p>

            </div>
            """)

    # --------------------------------------------------------
    # BOTTOM MESSAGE
    # --------------------------------------------------------

    st.markdown("<br>", unsafe_allow_html=True)

    render_html("""
    <div class="glass-card" style="
        text-align:center;
        padding:35px;
        background:
        linear-gradient(
            90deg,
            rgba(36,190,255,0.07),
            rgba(124,60,255,0.10)
        );
    ">

        <div style="font-size:30px;">
            🌱
        </div>

        <h2>
            Take Control of Your Digital Habits
        </h2>

        <p>
            Awareness is the first step toward healthier
            smartphone usage.
        </p>

    </div>
    """)

# ============================================================
# PREDICT RISK
# ============================================================

elif page == "🔮 Predict Risk":

    render_html("""
    <div class="hero" style="min-height:260px;padding:40px;">

        <div class="hero-small">
            SMARTPHONE HABIT ANALYSIS
        </div>

        <h1 style="font-size:40px;">
            Understand Your
            <span class="gradient-text">
                Digital Dependence
            </span>
        </h1>

        <p>
            Rate each behavior from 1 to 5.
            Higher values generally represent stronger
            smartphone-related behavior.
        </p>

    </div>
    """)

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

    st.markdown("### ")

    if st.button(
        "🔮 Predict My Dependence",
        use_container_width=True
    ):

        user_data = pd.DataFrame(
            [input_values]
        )[features]

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

        # ----------------------------------------------------
        # RESULT
        # ----------------------------------------------------

        render_html(f"""
        <div class="result-card">

            <div style="
                color:#8ea6c9;
                font-size:14px;
            ">
                YOUR ESTIMATED SMARTPHONE DEPENDENCE LEVEL
            </div>

            <div class="result-level">
                {predicted_label}
            </div>

            <div style="color:#9fb2ce;">
                Model confidence:
                <b>{confidence:.2f}%</b>
            </div>

        </div>
        """)

        # ----------------------------------------------------
        # RISK SCALE
        # ----------------------------------------------------

        st.markdown("### 🎯 Your Dependence Scale")

        risk_colors = {
            "Very Low": "#39d98a",
            "Low": "#8ee65f",
            "Moderate": "#ffbd45",
            "High": "#ff685b",
            "Very High": "#ed4d83"
        }

        scale_html = """
        <div class="risk-scale">
        """

        for level in [
            "Very Low",
            "Low",
            "Moderate",
            "High",
            "Very High"
        ]:

            active = (
                level == predicted_label
            )

            your_result = ""

            if active:
                your_result = """
                <div style="
                    color:#55d5ff;
                    font-size:11px;
                    margin-top:5px;
                ">
                    YOUR RESULT
                </div>
                """

            scale_html += f"""
            <div class="risk-item">

                <div class="risk-dot"
                     style="
                         background:{risk_colors[level]};
                         box-shadow:
                         0 0 10px
                         {risk_colors[level]};
                     ">
                </div>

                <div class="
                    {'risk-active'
                     if active
                     else 'risk-normal'}
                ">
                    {level}
                </div>

                {your_result}

            </div>
            """

        scale_html += """
        </div>
        """

        render_html(scale_html)

        # ----------------------------------------------------
        # PROBABILITY
        # ----------------------------------------------------

        st.markdown("### 📈 Prediction Probability")

        probability_df = pd.DataFrame({
            "Dependence Level": [
                "Very Low",
                "Low",
                "Moderate",
                "High",
                "Very High"
            ],
            "Probability (%)":
                probabilities * 100
        })

        probability_df = probability_df.set_index(
            "Dependence Level"
        )

        st.bar_chart(
            probability_df
        )

        # ----------------------------------------------------
        # KEY FACTORS
        # ----------------------------------------------------

        st.markdown("### 🧠 Key Behavioral Factors")

        importance = model.feature_importances_

        factor_data = []

        for feature, value, imp in zip(
            features,
            [
                input_values[f]
                for f in features
            ],
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

        for i, factor in enumerate(
            factor_data[:6]
        ):

            with cols[i % 2]:

                display_name = (
                    factor["feature"]
                    .replace("_", " ")
                    .title()
                )

                render_html(f"""
                <div class="factor-card">

                    <div class="factor-title">
                        {display_name}
                    </div>

                    <div class="factor-value">
                        Your rating:
                        {factor["value"]} / 5
                    </div>

                </div>
                """)

        # ----------------------------------------------------
        # RECOMMENDATIONS
        # ----------------------------------------------------

        st.markdown(
            "### 💡 Digital Wellbeing Recommendations"
        )

        if predicted_label in [
            "Very High",
            "High"
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

            render_html(f"""
            <div class="recommendation">
                {recommendation}
            </div>
            """)

# ============================================================
# ANALYTICS
# ============================================================

elif page == "📊 Analytics":

    render_html("""
    <div class="hero" style="min-height:240px;padding:40px;">

        <div class="hero-small">
            MODEL ANALYTICS
        </div>

        <h1 style="font-size:40px;">
            Explore the
            <span class="gradient-text">
                Model
            </span>
        </h1>

        <p>
            Understand how the machine learning model performs
            and which behavioral indicators contribute most
            to predictions.
        </p>

    </div>
    """)

    st.markdown("## 📊 Model Performance")

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

    st.markdown("## 🧠 Feature Importance")

    importance_df = pd.DataFrame({
        "Feature": features,
        "Importance":
            model.feature_importances_
    }).sort_values(
        "Importance",
        ascending=False
    )

    st.bar_chart(
        importance_df.set_index(
            "Feature"
        )
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
            "Feature":
                "Behavioral Indicator",

            "Importance":
                "Importance (%)"
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

    render_html("""
    <div class="hero" style="min-height:250px;padding:40px;">

        <div class="hero-small">
            MACHINE LEARNING
        </div>

        <h1 style="font-size:40px;">
            How the
            <span class="gradient-text">
                Model Works
            </span>
        </h1>

        <p>
            Digital Grip uses a Random Forest classification model
            to estimate smartphone dependence from behavioral indicators.
        </p>

    </div>
    """)

    st.markdown("## 🤖 Random Forest")

    render_html("""
    <div class="dark-card">

        <p>
            Random Forest is an ensemble machine learning algorithm
            that combines multiple decision trees to make a final
            prediction.
        </p>

        <p>
            Each tree analyzes behavioral patterns from the input
            features, while the combined forest produces the final
            dependence level.
        </p>

    </div>
    """)

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
        feature
        .replace("_", " ")
        .title()
        for feature in features
    ]

    for i in range(
        0,
        len(feature_names),
        2
    ):

        cols = st.columns(2)

        with cols[0]:

            render_html(f"""
            <div class="factor-card">
                🔹 {feature_names[i]}
            </div>
            """)

        if i + 1 < len(feature_names):

            with cols[1]:

                render_html(f"""
                <div class="factor-card">
                    🔹 {feature_names[i + 1]}
                </div>
                """)

# ============================================================
# ABOUT
# ============================================================

elif page == "ℹ️ About":

    render_html("""
    <div class="hero" style="min-height:260px;padding:40px;">

        <div class="hero-small">
            ABOUT DIGITAL GRIP
        </div>

        <h1 style="font-size:40px;">
            Building a
            <span class="gradient-text">
                Healthier Digital Life
            </span>
        </h1>

        <p>
            Digital Grip is a machine learning project focused on
            understanding smartphone-related behavioral patterns
            and estimating digital dependence.
        </p>

    </div>
    """)

    st.markdown("## 🎯 Project Objective")

    render_html("""
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
    """)

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

    for i, (
        icon,
        topic
    ) in enumerate(topics):

        with cols[i % 2]:

            render_html(f"""
            <div class="factor-card">
                {icon}
                &nbsp;
                <b>{topic}</b>
            </div>
            """)

    st.markdown("## 🌱 Digital Wellbeing")

    render_html("""
    <div class="glass-card">

        <h3>
            Technology should support your life —
            not control it.
        </h3>

        <p>
            Digital Grip is designed to encourage awareness
            of smartphone habits and help users make more
            intentional decisions about their digital behavior.
        </p>

    </div>
    """)

# ============================================================
# FOOTER
# ============================================================

render_html("""
<div class="footer">

    Digital Grip • Smartphone Usage & Digital Dependence Analysis

    <br>

    Built using Machine Learning and Streamlit

</div>
""")
