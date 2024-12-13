import streamlit as st

# Check if the popup has already been displayed
if "popup_shown" not in st.session_state:
    st.session_state.popup_shown = False

# Function to show the popup
def show_popup():
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

# Show the popup on page load
if not st.session_state.popup_shown:
    show_popup()
    st.session_state.popup_shown = True

# Add main content
st.title("Historical Newspaper Explorer")
st.write("Start exploring historical snippets and guess their publication year!")
