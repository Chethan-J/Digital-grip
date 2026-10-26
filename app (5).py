
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
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.main {
    background-color: #f8f9fc;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
}

.hero {
    padding: 2rem;
    border-radius: 20px;
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
    margin-bottom: 2rem;
}

.hero h1 {
    font-size: 42px;
    margin-bottom: 8px;
}

.hero p {
    font-size: 18px;
    opacity: 0.95;
}

.card {
    padding: 1.5rem;
    border-radius: 18px;
    background-color: white;
    border: 1px solid #e8e8ef;
    box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    margin-bottom: 1rem;
}

.result-card {
    padding: 2rem;
    border-radius: 20px;
    background: linear-gradient(135deg, #eef2ff, #f5f3ff);
    border: 1px solid #dcd8ff;
    text-align: center;
}

.result-level {
    font-size: 34px;
    font-weight: 700;
    margin: 10px 0;
}

.small-text {
    color: #666;
    font-size: 14px;
}

.factor {
    padding: 12px;
    margin: 8px 0;
    border-radius: 12px;
    background-color: #f6f7fb;
}

.recommendation {
    padding: 15px;
    margin: 10px 0;
    border-radius: 14px;
    background-color: #f8f9ff;
    border-left: 5px solid #667eea;
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("📱 Digital Grip")
st.sidebar.caption("Smartphone Usage & Digital Wellbeing")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "🔮 Predict Risk",
        "📊 Analytics",
        "🤖 Model Information",
        "ℹ️ About"
    ]
)

# ============================================================
# DASHBOARD
# ============================================================

if page == "🏠 Dashboard":

    st.markdown("""
    <div class="hero">
        <h1>📱 Digital Grip</h1>
        <p>
        Understand your smartphone habits and estimate your
        digital dependence level using Machine Learning.
        </p>
    </div>
    """, unsafe_allow_html=True)

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

    st.markdown("### 🎯 What does Digital Grip do?")

    st.write(
        "Digital Grip analyzes smartphone-related behavioral patterns "
        "and predicts a user's smartphone dependence level."
    )

    st.write(
        "The system uses ten behavioral indicators related to phone "
        "checking, distraction, productivity, sleep, and difficulty "
        "reducing smartphone usage."
    )

    st.markdown("### 🔍 How it works")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">
        <h3>1️⃣ Enter Habits</h3>
        <p>Answer questions about your everyday smartphone behavior.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
        <h3>2️⃣ ML Prediction</h3>
        <p>The Random Forest model analyzes your behavioral patterns.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
        <h3>3️⃣ Get Insights</h3>
        <p>Receive your dependence level and personalized recommendations.</p>
        </div>
        """, unsafe_allow_html=True)

# ============================================================
# PREDICTION PAGE
# ============================================================

elif page == "🔮 Predict Risk":

    st.markdown("""
    <div class="hero">
        <h1>🔮 Smartphone Dependence Prediction</h1>
        <p>Tell us about your smartphone habits.</p>
    </div>
    """, unsafe_allow_html=True)

    st.info(
        "Rate each behavior from 1 to 5. Higher values generally "
        "represent stronger smartphone-related behavior."
    )

    st.markdown("### 📊 Your Smartphone Habits")

    col1, col2 = st.columns(2)

    with col1:

        phone_checking = st.slider(
            "📱 How often do you check your phone without a notification?",
            1, 5, 3
        )

        usage_interference = st.slider(
            "📚 How often does smartphone use interfere with your daily responsibilities?",
            1, 5, 3
        )

        urge_to_check = st.slider(
            "🔄 How often do you feel the urge to check your phone without a reason?",
            1, 5, 3
        )

        productivity_impact = st.slider(
            "⚡ How often does smartphone use reduce your productivity?",
            1, 5, 3
        )

        distraction = st.slider(
            "🎯 How often does smartphone use distract you while studying or working?",
            1, 5, 3
        )

    with col2:

        comfort_without_phone = st.slider(
            "📵 How uncomfortable do you feel without your smartphone?",
            1, 5, 3
        )

        reduce_difficulty = st.slider(
            "🛑 How difficult is it for you to reduce smartphone usage?",
            1, 5, 3
        )

        check_within_15_min = st.slider(
            "🌅 How often do you check your phone within 15 minutes of waking up?",
            1, 5, 3
        )

        sleep_impact = st.slider(
            "😴 To what extent does smartphone usage affect your sleep?",
            1, 5, 3
        )

        night_checking = st.slider(
            "🌙 How often do you wake up during the night and check your phone?",
            1, 5, 3
        )

    st.markdown("---")

    predict_button = st.button(
        "🔍 Predict My Dependence Level",
        use_container_width=True
    )

    if predict_button:

        user_data = pd.DataFrame([{
            "Phone_Checking": phone_checking,
            "Usage_Interference": usage_interference,
            "Urge_To_Check": urge_to_check,
            "Productivity_Impact": productivity_impact,
            "Distraction": distraction,
            "Comfort_Without_Phone": comfort_without_phone,
            "Reduce_Difficulty": reduce_difficulty,
            "Check_Within_15_Min": check_within_15_min,
            "Sleep_Impact": sleep_impact,
            "Night_Checking": night_checking
        }])

        user_data = user_data[features]

        prediction = model.predict(user_data)[0]

        probabilities = model.predict_proba(user_data)[0]

        predicted_label = label_mapping[prediction]

        confidence = probabilities[prediction] * 100

        # ----------------------------------------------------
        # RESULT
        # ----------------------------------------------------

        st.markdown("---")

        st.markdown("### 🎯 Your Result")

        st.markdown(f"""
        <div class="result-card">
            <p>Your estimated smartphone dependence level is</p>
            <div class="result-level">{predicted_label}</div>
            <p>Model confidence: <b>{confidence:.2f}%</b></p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### 📈 Prediction Probability")

        probability_df = pd.DataFrame({
            "Dependence Level": list(label_mapping.values()),
            "Probability": probabilities * 100
        })

        st.bar_chart(
            probability_df.set_index("Dependence Level")
        )

        # ----------------------------------------------------
        # KEY FACTORS
        # ----------------------------------------------------

        st.markdown("### 🧠 Key Behavioral Factors")

        input_values = user_data.iloc[0]

        factor_scores = pd.DataFrame({
            "Feature": features,
            "Input": [input_values[f] for f in features],
            "Importance": model.feature_importances_
        })

        factor_scores["Impact"] = (
            factor_scores["Input"] *
            factor_scores["Importance"]
        )

        factor_scores = factor_scores.sort_values(
            "Impact",
            ascending=False
        )

        for _, row in factor_scores.head(5).iterrows():

            readable_name = row["Feature"].replace("_", " ")

            st.markdown(f"""
            <div class="factor">
                <b>{readable_name.title()}</b><br>
                Your rating: {int(row["Input"])} / 5
            </div>
            """, unsafe_allow_html=True)

        # ----------------------------------------------------
        # RECOMMENDATIONS
        # ----------------------------------------------------

        st.markdown("### 💡 Digital Wellbeing Recommendations")

        recommendations = []

        if phone_checking >= 4:
            recommendations.append(
                "Try keeping your phone out of immediate reach while studying or working."
            )

        if usage_interference >= 4:
            recommendations.append(
                "Create phone-free periods during important academic or work activities."
            )

        if urge_to_check >= 4:
            recommendations.append(
                "Turn off unnecessary notifications and avoid checking your phone automatically."
            )

        if productivity_impact >= 4:
            recommendations.append(
                "Use focused work sessions and keep distracting apps closed during them."
            )

        if distraction >= 4:
            recommendations.append(
                "Use a dedicated study/work mode to reduce smartphone distractions."
            )

        if comfort_without_phone >= 4:
            recommendations.append(
                "Start with short phone-free periods and gradually increase their duration."
            )

        if reduce_difficulty >= 4:
            recommendations.append(
                "Set small daily usage-reduction goals rather than making a sudden change."
            )

        if check_within_15_min >= 4:
            recommendations.append(
                "Try beginning your morning routine before checking your smartphone."
            )

        if sleep_impact >= 4:
            recommendations.append(
                "Avoid smartphone use close to bedtime and keep the device away from your bed."
            )

        if night_checking >= 4:
            recommendations.append(
                "Keep your smartphone away from your sleeping area to reduce nighttime checking."
            )

        if len(recommendations) == 0:

            recommendations.append(
                "Your current responses do not indicate strong concerns in these areas. "
                "Continue maintaining balanced smartphone habits."
            )

        for recommendation in recommendations:

            st.markdown(
                f"""
                <div class="recommendation">
                💡 {recommendation}
                </div>
                """,
                unsafe_allow_html=True
            )

# ============================================================
# ANALYTICS
# ============================================================

elif page == "📊 Analytics":

    st.markdown("""
    <div class="hero">
        <h1>📊 Model Analytics</h1>
        <p>Performance and feature importance of the Digital Grip ML model.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🏆 Model Performance")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Random Forest Accuracy", "88.67%")

    with col2:
        st.metric("Classification Levels", "5")

    with col3:
        st.metric("Input Features", "10")

    st.markdown("### 🧠 Feature Importance")

    importance_df = pd.DataFrame({
        "Feature": features,
        "Importance": model.feature_importances_
    })

    importance_df = importance_df.sort_values(
        "Importance",
        ascending=False
    )

    importance_df["Feature"] = importance_df["Feature"].str.replace(
        "_", " "
    ).str.title()

    st.bar_chart(
        importance_df.set_index("Feature")
    )

    st.markdown("### 📋 Features Used by the Model")

    feature_display = pd.DataFrame({
        "Feature": [
            feature.replace("_", " ").title()
            for feature in features
        ]
    })

    st.dataframe(
        feature_display,
        use_container_width=True,
        hide_index=True
    )

# ============================================================
# MODEL INFORMATION
# ============================================================

elif page == "🤖 Model Information":

    st.markdown("""
    <div class="hero">
        <h1>🤖 Machine Learning Model</h1>
        <p>Technical information about the Digital Grip prediction system.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🌲 Algorithm")

    st.write(
        "Digital Grip uses a Random Forest Classifier to predict "
        "five levels of smartphone dependence."
    )

    st.markdown("### 📊 Performance")

    st.write(
        "The final reproducible Random Forest model achieved "
        "**88.67% test accuracy**."
    )

    st.markdown("### 🎯 Prediction Classes")

    classes_df = pd.DataFrame({
        "Class": [
            "Very Low",
            "Low",
            "Moderate",
            "High",
            "Very High"
        ],
        "Encoded Value": [0, 1, 2, 3, 4]
    })

    st.dataframe(
        classes_df,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("### 🔢 Input Features")

    for feature in features:
        st.write(
            "• " + feature.replace("_", " ").title()
        )

    st.markdown("### 💾 Saved Model")

    st.code("digital_grip_model.pkl")

    st.markdown("### 📦 Feature File")

    st.code("digital_grip_features.pkl")

# ============================================================
# ABOUT
# ============================================================

elif page == "ℹ️ About":

    st.markdown("""
    <div class="hero">
        <h1>ℹ️ About Digital Grip</h1>
        <p>Smartphone usage and digital wellbeing analysis.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🎯 Project Objective")

    st.write(
        "Digital Grip is a machine learning project designed to "
        "analyze smartphone-related behavioral patterns and estimate "
        "a user's level of smartphone dependence."
    )

    st.markdown("### 👥 Target Users")

    st.write(
        "The project focuses on Gen Z users, particularly students "
        "and young adults."
    )

    st.markdown("### 🧠 Machine Learning")

    st.write(
        "The system uses behavioral indicators such as phone checking, "
        "distraction, productivity impact, sleep impact, and difficulty "
        "reducing smartphone usage."
    )

    st.markdown("### ⚠️ Important Note")

    st.info(
        "This prediction is an ML-based estimate intended for digital "
        "wellbeing awareness. It is not a medical or psychological diagnosis."
    )

    st.markdown("### 📱 Digital Wellbeing")

    st.write(
        "The goal is not simply to label smartphone usage as good or bad. "
        "Instead, Digital Grip aims to help users understand their habits "
        "and identify areas where healthier digital habits may be useful."
    )
