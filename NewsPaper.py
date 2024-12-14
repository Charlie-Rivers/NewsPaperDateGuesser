import streamlit as st

#show the popup
def showPopup():
    st.markdown(
        """
        <style>
        .popup {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background-color: white;
            padding: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            z-index: 1000;
            text-align: center;
            border-radius: 8px;
        }
        .popup button {
            padding: 10px 15px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .popup button:hover {
            background-color: #0056b3;
        }
        </style>
        <div class="popup">
            <h3 style="color:black;">Welcome to the Historical Newspaper Explorer!</h3>
            <p style="color:black;">Guess the year of historical newspaper snippets and learn about history!</p>
            <button onclick="window.location.reload()">Close</button>
        </div>
        """,
        unsafe_allow_html=True,
    )

showPopup()

#main content
st.title("Newspaper Date Guesser")
st.write("Take a look at the front page of each News Paper. Then, take you best guess as to what year the News Paper was published!")
