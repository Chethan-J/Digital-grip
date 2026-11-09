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

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "Test Accuracy",
            "88.67%"
        )

    with col2:

        st.metric(
            "Weighted Precision",
            "89%"
        )

    with col3:

        st.metric(
            "Weighted Recall",
            "89%"
        )

    with col4:

        st.metric(
            "Weighted F1-Score",
            "89%"
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
