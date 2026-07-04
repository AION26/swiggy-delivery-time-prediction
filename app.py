import pickle
import streamlit as st
import pandas as pd

with open('swiggy_model.pkl','rb') as f:
    model = pickle.load(f)


st.title("Swiggy Delivery Time Prediction")

input_df = pd.DataFrame([{
    'age': st.number_input("Age", min_value=18, max_value=70, value=25),

    'ratings': st.number_input(
        "Ratings",
        min_value=1.0,
        max_value=5.0,
        value=4.0,
        step=0.1
    ),

    'weather': st.selectbox(
        "Weather",
        ["sunny", "rainy", "windy", "sandstorm", "fog", "stormy"]
    ),

    'traffic': st.selectbox(
        "Traffic",
        ["low", "medium", "high", "jam"]
    ),

    'vehicle_condition': st.selectbox(
        "Vehicle Condition",
        [0, 1, 2, 3]
    ),

    'type_of_order': st.selectbox(
        "Type of Order",
        ["snack", "drinks", "meal", "buffet"]
    ),

    'type_of_vehicle': st.selectbox(
        "Type of Vehicle",
        ["motorcycle", "scooter", "electric_scooter", "bicycle"]
    ),

    'multiple_deliveries': st.selectbox(
        "Multiple Deliveries",
        [0, 1, 2, 3]
    ),

    'festival': st.selectbox(
        "Festival",
        ["yes", "no"]
    ),

    'city_type': st.selectbox(
        "City Type",
        ["urban", "semi-urban", "metropolitian"]
    ),

    'city_name': st.selectbox(
        "City Name",
        [
            'JAP', 'RANCHI', 'BANG', 'SUR', 'HYD', 'MUM', 'MYS',
            'COIMB', 'VAD', 'INDO', 'CHEN', 'PUNE', 'AGR',
            'LUDH', 'ALH', 'KNP', 'DEH', 'GOA', 'AURG',
            'KOC', 'KOL', 'BHP'
        ]
    ),

    'order_day': st.number_input(
        "Order Day",
        min_value=1,
        max_value=31,
        value=15
    ),

    'order_month': st.selectbox(
        "Order Month",
        [2, 3, 4]
    ),

    'order_day_of_week': st.selectbox(
        "Order Day of Week",
        [
            'monday',
            'tuesday',
            'wednesday',
            'thursday',
            'friday',
            'saturday',
            'sunday'
        ]
    ),

    'is_weekend': st.selectbox(
        "Is Weekend",
        [0, 1]
    ),

    'pickup_time_minutes': st.selectbox(
        "Pickup Time (Minutes)",
        [5, 10, 15]
    ),

    'order_time_hour': st.number_input(
        "Order Hour",
        min_value=0,
        max_value=23,
        value=12
    ),

    'order_time_of_day': st.selectbox(
        "Order Time of Day",
        ['after_midnight', 'afternoon', 'evening', 'morning', 'night']
    ),

    'distance': st.number_input(
        "Distance (km)",
        min_value=0.0,
        value=5.0
    )
}])

if st.button("Predict Delivery Time"):
    prediction = model.predict(input_df)
    st.success(f"Predicted Delivery Time: {prediction[0]:.2f} minutes")