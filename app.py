import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
import plotly.graph_objects as go

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Smart Property Advisor", layout="wide")

# ---------------- LOAD DATA ----------------
@st.cache_data
def load_data():
    return pd.read_csv("smart_property_data.csv")

df = load_data()
df.columns = df.columns.str.strip()
df = df.dropna()

# ---------------- ENCODING ----------------
le_type = LabelEncoder()
le_loc = LabelEncoder()

df['property_type'] = le_type.fit_transform(df['property_type'])
df['location_tier'] = le_loc.fit_transform(df['location_tier'])

# ---------------- MODEL ----------------
X = df.drop("price", axis=1)
y = df["price"]

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# ---------------- SIDEBAR ----------------
st.sidebar.title("🏠 Smart Property Advisor")
page = st.sidebar.radio("Navigation", ["Price Prediction", "About"])
st.sidebar.success("Model Ready ✅")

# ---------------- PRICE PREDICTION PAGE ----------------
if page == "Price Prediction":

    st.title("📋 Property Details")

    col1, col2 = st.columns([2, 1])

    # -------- INPUT PANEL --------
    with col1:
        c1, c2 = st.columns(2)
        sqft = c1.number_input("Square Feet", 500, 5000, 1500)
        age = c2.number_input("Age (Years)", 0, 30, 5)

        c3, c4 = st.columns(2)
        bedrooms = c3.selectbox("Bedrooms", [1,2,3,4,5])
        floor = c4.number_input("Floor", 0, 50, 2)

        bathrooms = st.selectbox("Bathrooms", [1,2,3,4])

        st.subheader("Property Type & Location")
        c5, c6 = st.columns(2)

        property_type = c5.selectbox("Property Type", le_type.classes_)
        location_tier = c6.selectbox("Location Tier", le_loc.classes_)

        distance = st.slider("Distance to City Center (km)", 0.0, 30.0, 5.0)

        st.subheader("Amenities")
        garden = st.checkbox("🌳 Garden")
        pool = st.checkbox("🏊 Pool")
        garage = st.checkbox("🚗 Garage")
        furnished = st.checkbox("🛋 Furnished")

        st.subheader("Neighborhood")
        crime = st.slider("Crime Rate Index", 0, 100, 30)
        school = st.slider("School Rating", 0.0, 10.0, 7.0)
        hospital = st.slider("Hospital Distance (km)", 0.5, 10.0, 3.0)
        shopping = st.slider("Shopping Distance (km)", 0.5, 10.0, 2.0)

        predict = st.button("🔮 Predict Price")

    # -------- OUTPUT PANEL --------
    with col2:

        if predict:

            # Encode inputs
            property_type_enc = le_type.transform([property_type])[0]
            location_tier_enc = le_loc.transform([location_tier])[0]

            input_data = np.array([[sqft, age, bedrooms, bathrooms, floor,
                                    property_type_enc, location_tier_enc,
                                    distance, int(garden), int(pool),
                                    int(garage), int(furnished),
                                    crime, school, hospital, shopping]])

            # Prediction
            price = model.predict(input_data)[0]
            price_per_sqft = price / sqft

            # -------- PRICE CARD --------
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #667eea, #764ba2);
                        padding:20px;
                        border-radius:15px;
                        color:white;
                        text-align:center;">
                <h3>💰 Predicted Price</h3>
                <h2>₹ {price:,.0f}</h2>
                <p>₹ {price_per_sqft:,.0f} per sq ft</p>
            </div>
            """, unsafe_allow_html=True)

            # -------- INVESTMENT SCORE --------
            score = int(100 - crime + school*5 - distance)
            score = max(0, min(score, 100))

            gauge = go.Figure(go.Indicator(
                mode="gauge+number",
                value=score,
                title={'text': "Investment Score"},
                gauge={'axis': {'range': [0,100]}}
            ))

            st.plotly_chart(gauge, use_container_width=True)

            # -------- RECOMMENDATIONS --------
            st.subheader("💡 Recommendations")

            recommendations = []

            # Location
            if location_tier == "Tier 1":
                recommendations.append(("🌟 Location", "High growth potential area"))
            elif location_tier == "Tier 2":
                recommendations.append(("📍 Location", "Moderate growth area"))
            else:
                recommendations.append(("⚠ Location", "Lower appreciation potential"))

            # Amenities
            if not garden:
                recommendations.append(("🌳 Amenities", "Adding a garden can increase value"))
            if not pool:
                recommendations.append(("🏊 Amenities", "Pool can boost luxury appeal"))
            if not furnished:
                recommendations.append(("🛋 Amenities", "Furnished homes attract higher value"))

            # Risk
            if crime > 50:
                recommendations.append(("⚠ Risk", "High crime rate — risky investment"))

            if hospital > 5:
                recommendations.append(("🏥 Accessibility", "Far from hospitals"))

            if shopping > 5:
                recommendations.append(("🛒 Accessibility", "Far from shopping centers"))

            for title, msg in recommendations:
                st.info(f"**{title}**: {msg}")

        else:
            st.info("👈 Fill details and click Predict")

# ---------------- ABOUT PAGE ----------------
else:

    st.title("ℹ About Smart Property Advisor")

    st.markdown("""
    ### 🏠 Smart Property Advisor

    Smart Property Advisor is an intelligent system designed to assist users in evaluating real estate properties using data-driven insights.

    This platform goes beyond simple price prediction by combining property features, location analysis, and neighborhood conditions to provide a complete investment perspective.

    ---

    ### 🔍 Key Capabilities

    - 💰 Accurate property price estimation  
    - 📊 Investment scoring for decision making  
    - 💡 Personalized recommendations  

    ---

    ### 📈 Factors Considered

    - Property size, type, and age  
    - Location tier and accessibility  
    - Amenities and furnishing  
    - Neighborhood conditions like crime, schools, hospitals  

    ---

    ### 🎯 Objective

    The goal of this system is to help users:
    
    - Make smarter real estate decisions  
    - Identify high-return investment opportunities  
    - Minimize risk through better insights  

    ---
    
    ### 🚀 Application Areas

    - Property buyers  
    - Real estate investors  
    - Market analysis and comparison  

    """)