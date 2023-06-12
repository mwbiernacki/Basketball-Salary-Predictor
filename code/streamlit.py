import streamlit as st
import pandas as pd
from unidecode import unidecode

df_predictions = pd.read_csv('../data/predicted_2023.csv')
df_predictions['Player']= df_predictions['Player'].apply(unidecode)
st.title("Predicted Salary in 2023")
player_name = st.text_input("Enter player's name:")
if player_name:
    player_data = df_predictions[df_predictions['Player'] == player_name]
    if not player_data.empty:
        st.subheader(f"Salary for {player_name} in 2023")
        true_earnings = "${:,.2f}".format(player_data['True Salary'].values[0])
        predicted_earnings = "${:,.2f}".format(player_data['Predicted Salary'].values[0])
        disparity = "${:,.2f}".format(player_data['Disparity'].values[0])
        st.write("True Earnings: ", true_earnings)
        st.write("Predicted Earnings: ", predicted_earnings)
        st.write("Disparity: ", disparity)
    else:
        st.write(f"No data available for player {player_name}")
else:
    st.write("Please enter a player's name.")