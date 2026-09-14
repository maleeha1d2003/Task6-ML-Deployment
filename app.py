import streamlit as st
import pandas as pd
import joblib
from datetime import datetime


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="House Price Category Predictor",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    .main-title {
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 18px;
        color: #666666;
        margin-bottom: 20px;
    }

    .result-box {
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        margin: 10px 0;
    }

    .small-text {
        font-size: 14px;
        color: #666666;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SESSION STATE INITIALIZATION
# ============================================================

if "prediction_history" not in st.session_state:
    st.session_state.prediction_history = []

if "prediction_made" not in st.session_state:
    st.session_state.prediction_made = False

if "last_prediction" not in st.session_state:
    st.session_state.last_prediction = None

if "last_confidence" not in st.session_state:
    st.session_state.last_confidence = None

if "last_probabilities" not in st.session_state:
    st.session_state.last_probabilities = None


# ============================================================
# LOAD TRAINED MODEL
# ============================================================

@st.cache_resource
def load_model():
    try:
        return joblib.load("final_random_forest_model_task5.joblib")
    except Exception as e:
        st.error(f"Unable to load the trained model: {e}")
        st.stop()


model = load_model()


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.header("📌 About the Project")

    st.write(
        """
        This application demonstrates the deployment of a
        machine learning model developed for the house price
        classification task.

        The final **Random Forest Classifier** predicts whether
        a house belongs to the **Lower Price** or
        **Higher Price** category.
        """
    )

    st.divider()

    st.subheader("📋 How to Use")

    st.write(
        """
        **Step 1:** Enter the house information.

        **Step 2:** Select the categorical characteristics.

        **Step 3:** Click **Predict Price Category**.

        **Step 4:** Review the prediction and confidence score.

        **Step 5:** View or download your prediction history.
        """
    )

    st.divider()

    st.subheader("🤖 Model Information")

    st.write(
        """
        **Algorithm:** Random Forest Classifier

        **Model Source:** Task 5

        **Classification:** Binary

        **Output:**
        - Lower Price
        - Higher Price
        """
    )

    st.divider()

    st.caption("Machine Learning Deployment – Task 6")


# ============================================================
# RESET FUNCTION
# ============================================================

def reset_application():

    st.session_state.prediction_made = False
    st.session_state.last_prediction = None
    st.session_state.last_confidence = None
    st.session_state.last_probabilities = None

    # Reset input values
    st.session_state.area = 1500.0
    st.session_state.bedrooms = 3
    st.session_state.bathrooms = 2
    st.session_state.floors = 1
    st.session_state.year_built = 2010
    st.session_state.location = "Urban"
    st.session_state.condition = "Good"
    st.session_state.garage = "No"
    st.session_state.total_rooms = 5

    st.rerun()


# ============================================================
# RESET BUTTON
# ============================================================

reset_col1, reset_col2 = st.columns([5, 1])

with reset_col2:

    if st.button(
        "🔄 Reset",
        use_container_width=True
    ):
        reset_application()


# ============================================================
# MAIN TITLE
# ============================================================

st.markdown(
    '<div class="main-title">🏠 House Price Category Predictor</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="subtitle">
    Enter the characteristics of a house to predict whether
    it belongs to the Lower Price or Higher Price category.
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()


# ============================================================
# INPUT SECTION
# ============================================================

st.subheader("🏡 House Information")

col1, col2, col3 = st.columns(3)


# ------------------------------------------------------------
# Column 1
# ------------------------------------------------------------

with col1:

    area = st.number_input(
        "Area (sq ft)",
        min_value=100.0,
        max_value=10000.0,
        value=1500.0,
        step=50.0,
        key="area"
    )

    bedrooms = st.number_input(
        "Bedrooms",
        min_value=1,
        max_value=10,
        value=3,
        step=1,
        key="bedrooms"
    )

    bathrooms = st.number_input(
        "Bathrooms",
        min_value=1,
        max_value=10,
        value=2,
        step=1,
        key="bathrooms"
    )

    floors = st.number_input(
        "Floors",
        min_value=1,
        max_value=5,
        value=1,
        step=1,
        key="floors"
    )


# ------------------------------------------------------------
# Column 2
# ------------------------------------------------------------

with col2:

    current_year = datetime.now().year

    year_built = st.number_input(
        "Year Built",
        min_value=1900,
        max_value=current_year,
        value=2010,
        step=1,
        key="year_built"
    )

    location = st.selectbox(
        "Location",
        ["Urban", "Suburban", "Rural"],
        key="location"
    )

    condition = st.selectbox(
        "Condition",
        ["Good", "Fair", "Poor"],
        key="condition"
    )

    garage = st.selectbox(
        "Garage",
        ["Yes", "No"],
        key="garage"
    )


# ------------------------------------------------------------
# Column 3
# ------------------------------------------------------------

with col3:

    total_rooms = st.number_input(
        "Total Rooms",
        min_value=1,
        max_value=20,
        value=5,
        step=1,
        key="total_rooms"
    )

    st.info(
        """
        **Total Rooms**

        Enter the overall number of rooms in the house,
        including bedrooms and other rooms.
        """
    )

    st.caption(
        "The application automatically converts categorical "
        "inputs into the numerical format expected by the model."
    )


st.divider()


# ============================================================
# PREDICTION BUTTON
# ============================================================

predict_button = st.button(
    "🔮 Predict Price Category",
    type="primary",
    use_container_width=True
)


# ============================================================
# PREDICTION LOGIC
# ============================================================

if predict_button:

    # --------------------------------------------------------
    # INPUT VALIDATION
    # --------------------------------------------------------

    validation_error = None

    if area <= 0:
        validation_error = "Area must be greater than zero."

    elif bedrooms <= 0:
        validation_error = "Bedrooms must be greater than zero."

    elif bathrooms <= 0:
        validation_error = "Bathrooms must be greater than zero."

    elif floors <= 0:
        validation_error = "Floors must be greater than zero."

    elif year_built > current_year:
        validation_error = (
            f"Year Built cannot be greater than {current_year}."
        )

    elif total_rooms < bedrooms:
        validation_error = (
            "Total Rooms should be greater than or equal to "
            "the number of bedrooms."
        )

    # --------------------------------------------------------
    # DISPLAY VALIDATION ERROR
    # --------------------------------------------------------

    if validation_error:

        st.error(f"❌ {validation_error}")

    else:

        try:

            # ------------------------------------------------
            # ONE-HOT ENCODING
            # ------------------------------------------------

            location_rural = 1 if location == "Rural" else 0
            location_suburban = 1 if location == "Suburban" else 0
            location_urban = 1 if location == "Urban" else 0

            condition_fair = 1 if condition == "Fair" else 0
            condition_good = 1 if condition == "Good" else 0
            condition_poor = 1 if condition == "Poor" else 0

            garage_yes = 1 if garage == "Yes" else 0


            # ------------------------------------------------
            # CREATE MODEL INPUT
            # ------------------------------------------------

            input_data = pd.DataFrame({
                "Area": [area],
                "Bedrooms": [bedrooms],
                "Bathrooms": [bathrooms],
                "Floors": [floors],
                "YearBuilt": [year_built],
                "Location_Rural": [location_rural],
                "Location_Suburban": [location_suburban],
                "Location_Urban": [location_urban],
                "Condition_Fair": [condition_fair],
                "Condition_Good": [condition_good],
                "Condition_Poor": [condition_poor],
                "Garage_Yes": [garage_yes],
                "TotalRooms": [total_rooms]
            })


            # ------------------------------------------------
            # MODEL PREDICTION
            # ------------------------------------------------

            prediction = model.predict(input_data)[0]

            probabilities = model.predict_proba(input_data)[0]

            confidence = max(probabilities) * 100


            # ------------------------------------------------
            # DETERMINE CLASS PROBABILITIES
            # ------------------------------------------------

            class_probabilities = {}

            for class_label, probability in zip(
                model.classes_,
                probabilities
            ):

                if class_label == 0:
                    class_name = "Lower Price"
                else:
                    class_name = "Higher Price"

                class_probabilities[class_name] = probability * 100


            # ------------------------------------------------
            # SAVE RESULT IN SESSION STATE
            # ------------------------------------------------

            st.session_state.prediction_made = True

            if prediction == 1:
                prediction_label = "Higher Price"
            else:
                prediction_label = "Lower Price"

            st.session_state.last_prediction = prediction_label
            st.session_state.last_confidence = confidence
            st.session_state.last_probabilities = class_probabilities


            # ------------------------------------------------
            # SAVE TO PREDICTION HISTORY
            # ------------------------------------------------

            history_record = {
                "Timestamp": datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),
                "Area": area,
                "Bedrooms": bedrooms,
                "Bathrooms": bathrooms,
                "Floors": floors,
                "Year Built": year_built,
                "Location": location,
                "Condition": condition,
                "Garage": garage,
                "Total Rooms": total_rooms,
                "Prediction": prediction_label,
                "Confidence (%)": round(confidence, 2)
            }

            st.session_state.prediction_history.append(
                history_record
            )


        except Exception as e:

            st.error(
                f"❌ An error occurred while making the prediction: {e}"
            )


# ============================================================
# DISPLAY PREDICTION RESULT
# ============================================================

if st.session_state.prediction_made:

    st.divider()

    st.subheader("📊 Prediction Result")

    prediction_label = st.session_state.last_prediction
    confidence = st.session_state.last_confidence
    class_probabilities = st.session_state.last_probabilities


    # --------------------------------------------------------
    # Result
    # --------------------------------------------------------

    if prediction_label == "Higher Price":

        st.success(
            f"🏠 **Predicted Price Category: {prediction_label}**"
        )

    else:

        st.info(
            f"🏠 **Predicted Price Category: {prediction_label}**"
        )


    # --------------------------------------------------------
    # Confidence
    # --------------------------------------------------------

    metric_col1, metric_col2 = st.columns(2)

    with metric_col1:

        st.metric(
            "🎯 Confidence Score",
            f"{confidence:.2f}%"
        )

    with metric_col2:

        st.metric(
            "📌 Predicted Class",
            prediction_label
        )


    # --------------------------------------------------------
    # Probability Chart
    # --------------------------------------------------------

    st.subheader("📈 Prediction Probabilities")

    probability_df = pd.DataFrame(
        {
            "Price Category": list(
                class_probabilities.keys()
            ),
            "Probability (%)": list(
                class_probabilities.values()
            )
        }
    )

    st.bar_chart(
        probability_df.set_index("Price Category")
    )


    # --------------------------------------------------------
    # Submitted Information
    # --------------------------------------------------------

    st.subheader("🔍 Submitted Information")

    display_data = pd.DataFrame(
        {
            "Input": [
                "Area",
                "Bedrooms",
                "Bathrooms",
                "Floors",
                "Year Built",
                "Location",
                "Condition",
                "Garage",
                "Total Rooms"
            ],
            "Value": [
                f"{area:.0f} sq ft",
                bedrooms,
                bathrooms,
                floors,
                year_built,
                location,
                condition,
                garage,
                total_rooms
            ]
        }
    )

    st.dataframe(
        display_data,
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# PREDICTION HISTORY
# ============================================================

if st.session_state.prediction_history:

    st.divider()

    st.subheader("📜 Prediction History")

    history_df = pd.DataFrame(
        st.session_state.prediction_history
    )

    st.dataframe(
        history_df,
        use_container_width=True,
        hide_index=True
    )


    # --------------------------------------------------------
    # DOWNLOAD HISTORY
    # --------------------------------------------------------

    csv_data = history_df.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        label="📥 Download Prediction History as CSV",
        data=csv_data,
        file_name="prediction_history.csv",
        mime="text/csv",
        use_container_width=True
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Developed as part of Machine Learning Internship – Task 6"
)