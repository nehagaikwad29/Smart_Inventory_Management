import streamlit as st
import pandas as pd
import joblib
from datetime import date

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Smart Inventory Management",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# LOAD MODEL
# =========================================================

@st.cache_resource
def load_model():
    return joblib.load("inventory_demand_model.pkl")


model = load_model()

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>

    .stApp {
        background-color: #f4fbff;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    .hero {
        background: linear-gradient(135deg, #dff5ff, #eefaff);
        padding: 35px;
        border-radius: 22px;
        border: 1px solid #c8eafa;
        margin-bottom: 25px;
    }

    .hero h1 {
        color: #155d78;
        font-size: 40px;
        margin-bottom: 8px;
    }

    .hero p {
        color: #4d7180;
        font-size: 18px;
    }

    .card {
        background-color: white;
        padding: 25px;
        border-radius: 18px;
        border: 1px solid #d7edf7;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
        margin-bottom: 20px;
    }

    .result-card {
        background-color: #e9f8ff;
        padding: 30px;
        border-radius: 20px;
        border: 1px solid #bfe6f5;
        text-align: center;
        margin-top: 20px;
    }

    .result-number {
        font-size: 42px;
        font-weight: bold;
        color: #176b87;
    }

    .info-card {
        background-color: #eef9ff;
        padding: 25px;
        border-radius: 18px;
        border: 1px solid #cceaf7;
        margin-bottom: 20px;
    }

    .success-card {
        background-color: #ecfff4;
        padding: 25px;
        border-radius: 18px;
        border: 1px solid #bce8ce;
        margin-bottom: 20px;
    }

    .warning-card {
        background-color: #fff9e8;
        padding: 25px;
        border-radius: 18px;
        border: 1px solid #f0df9c;
        margin-bottom: 20px;
    }

    .danger-card {
        background-color: #fff0f0;
        padding: 25px;
        border-radius: 18px;
        border: 1px solid #efc2c2;
        margin-bottom: 20px;
    }

    .footer {
        text-align: center;
        padding: 30px;
        color: #607d8b;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# =========================================================
# SIDEBAR NAVIGATION
# =========================================================

st.sidebar.markdown("## 🤖 Smart Inventory")

st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "📈 Demand Prediction",
        "📦 Inventory Status",
        "ℹ️ About Project"
    ]
)

st.sidebar.markdown("---")

st.sidebar.info(
    "AI-powered demand prediction and smart inventory management."
)

# =========================================================
# DASHBOARD
# =========================================================

if page == "🏠 Dashboard":

    st.markdown(
        """
        <div class="hero">
            <h1>🤖 Smart Inventory Management</h1>
            <p>
                Predict demand • Monitor stock • Make smarter inventory decisions
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.subheader("✨ How It Works")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div class="card">
                <h3>1️⃣ Enter Data</h3>
                <p>
                    Enter the store, product and sales information.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class="card">
                <h3>2️⃣ AI Prediction</h3>
                <p>
                    The machine learning model estimates future demand.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """
            <div class="card">
                <h3>3️⃣ Smart Decision</h3>
                <p>
                    Compare demand with available stock and take action.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("### 🚀 Project Highlights")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("🤖 ML Model", "Random Forest")

    with col2:
        st.metric("📈 Demand", "Prediction")

    with col3:
        st.metric("📦 Inventory", "Monitoring")

    with col4:
        st.metric("🔄 Reorder", "Recommendation")

    st.markdown("---")

    st.markdown(
        """
        <div class="info-card">
            <h3>💡 Why Smart Inventory Management?</h3>
            <p>
                Poor inventory planning can cause stock shortages or
                unnecessary excess stock. This project uses machine
                learning to support smarter demand and inventory decisions.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

# =========================================================
# DEMAND PREDICTION
# =========================================================

elif page == "📈 Demand Prediction":

    st.title("📈 Demand Prediction")

    st.write(
        "Enter the required information and generate a demand prediction."
    )

    col1, col2 = st.columns(2)

    with col1:

        store_id = st.number_input(
            "🏪 Store ID",
            min_value=0,
            value=1,
            step=1
        )

        product_id = st.number_input(
            "📦 Product ID",
            min_value=0,
            value=1,
            step=1
        )

    with col2:

        prediction_date = st.date_input(
            "📅 Prediction Date",
            value=date.today()
        )

        previous_sales = st.number_input(
            "📊 Previous Sales",
            min_value=0.0,
            value=25.0,
            step=1.0
        )

    st.markdown("---")

    if st.button(
        "🔮 Predict Demand",
        use_container_width=True
    ):

        year = prediction_date.year
        month = prediction_date.month
        day = prediction_date.day
        day_of_week = prediction_date.weekday()

        # -------------------------------------------------
        # Create input using the model's expected features
        # -------------------------------------------------

        values = {
            "store": store_id,
            "store_id": store_id,
            "Store": store_id,
            "Store ID": store_id,

            "item": product_id,
            "item_id": product_id,
            "product": product_id,
            "product_id": product_id,
            "Product": product_id,
            "Product ID": product_id,

            "year": year,
            "Year": year,

            "month": month,
            "Month": month,

            "day": day,
            "Day": day,

            "day_of_week": day_of_week,
            "DayOfWeek": day_of_week,
            "weekday": day_of_week,

            "previous_sales": previous_sales,
            "Previous Sales": previous_sales,
            "previous sales": previous_sales
        }

        # Get feature names if the saved model provides them
        expected_features = getattr(
            model,
            "feature_names_in_",
            None
        )

        try:

            if expected_features is not None:

                input_data = pd.DataFrame(
                    [[values.get(feature, 0) for feature in expected_features]],
                    columns=expected_features
                )

            else:

                input_data = pd.DataFrame(
                    {
                        "store": [store_id],
                        "item": [product_id],
                        "year": [year],
                        "month": [month],
                        "day": [day],
                        "day_of_week": [day_of_week],
                        "previous_sales": [previous_sales]
                    }
                )

            prediction = model.predict(input_data)[0]

            prediction = max(0, float(prediction))

            st.success("✅ Prediction generated successfully!")

            st.markdown(
                """
                <div class="result-card">
                    <h2>🎯 Predicted Demand</h2>
                    <div class="result-number">
                        """
                + f"{prediction:.0f}"
                + """ units
                    </div>
                    <p>
                        Estimated demand for the selected product
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.markdown("### 📋 Prediction Details")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "🏪 Store",
                    store_id
                )

            with col2:
                st.metric(
                    "📦 Product",
                    product_id
                )

            with col3:
                st.metric(
                    "📊 Previous Sales",
                    f"{previous_sales:.0f}"
                )

            st.markdown("---")

            st.info(
                f"💡 The model estimates approximately "
                f"*{prediction:.0f} units* of demand."
            )

        except Exception as error:

            st.error("❌ Prediction could not be generated.")

            st.write(
                "Please check the model input features."
            )

            st.code(str(error))

# =========================================================
# INVENTORY STATUS
# =========================================================

elif page == "📦 Inventory Status":

    st.title("📦 Inventory Status")

    st.write(
        "Check whether your current stock is sufficient."
    )

    col1, col2 = st.columns(2)

    with col1:

        current_stock = st.number_input(
            "📦 Current Stock",
            min_value=0,
            value=25,
            step=1
        )

    with col2:

        predicted_demand = st.number_input(
            "📈 Predicted Demand",
            min_value=0.0,
            value=18.0,
            step=1.0
        )

    remaining_stock = current_stock - predicted_demand

    reorder_quantity = max(
        0,
        predicted_demand - current_stock
    )

    st.markdown("---")

    if current_stock < predicted_demand:

        st.markdown(
            """
            <div class="danger-card">
                <h2>🔴 Low Stock</h2>
                <p>
                    Current stock is below predicted demand.
                    Reordering is recommended.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    elif current_stock <= predicted_demand * 1.2:

        st.markdown(
            """
            <div class="warning-card">
                <h2>🟡 Moderate Stock</h2>
                <p>
                    Stock is available, but it should be monitored.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            """
            <div class="success-card">
                <h2>🟢 Healthy Stock</h2>
                <p>
                    Current stock is sufficient for predicted demand.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("### 📊 Inventory Overview")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Current Stock",
            f"{current_stock:.0f} units"
        )

    with col2:
        st.metric(
            "Predicted Demand",
            f"{predicted_demand:.0f} units"
        )

    with col3:
        st.metric(
            "Recommended Reorder",
            f"{reorder_quantity:.0f} units"
        )

    if reorder_quantity > 0:

        st.warning(
            f"🔄 Recommended action: reorder approximately "
            f"{reorder_quantity:.0f} units."
        )

    else:

        st.success(
            f"✅ Stock is sufficient. "
            f"Approximately {max(0, remaining_stock):.0f} units "
            f"may remain."
        )

# =========================================================
# ABOUT PROJECT
# =========================================================

elif page == "ℹ️ About Project":

    st.title("ℹ️ About Project")

    st.markdown(
        """
        <div class="card">

            <h2>🤖 Smart Inventory Management</h2>

            <p>
                Smart Inventory Management is a machine-learning project
                designed to predict product demand and support better
                inventory decisions.
            </p>

            <h3>🎯 Objective</h3>

            <p>
                The system estimates future product demand and helps
                identify whether available inventory is sufficient.
            </p>

            <h3>🧠 Machine Learning</h3>

            <p>
                The main machine learning algorithm used in the project
                is <b>Random Forest Regressor</b>.
            </p>

            <h3>📊 Model Evaluation</h3>

            <ul>
                <li>Mean Absolute Error (MAE)</li>
                <li>Root Mean Squared Error (RMSE)</li>
                <li>R² Score</li>
            </ul>

            <h3>✨ Main Features</h3>

            <ul>
                <li>Demand Prediction</li>
                <li>Inventory Status</li>
                <li>Smart Reorder Recommendation</li>
                <li>Machine Learning</li>
                <li>Interactive Dashboard</li>
            </ul>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="info-card">
            <h2>👩‍💻 Project Developed By</h2>
            <h3>Neha Gaikwad</h3>
            <p>
                Designed and developed as a Machine Learning project
                for smart and data-driven inventory management.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.markdown(
    """
    <div class="footer">
        <b>🤖 Smart Inventory Management</b><br>
        Machine Learning • Demand Prediction • Inventory Intelligence
        <br><br>
        Developed by <b>Neha Gaikwad</b>
    </div>
    """,
    unsafe_allow_html=True
)