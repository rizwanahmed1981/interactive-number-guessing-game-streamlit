import streamlit as st
import random as rd

st.title("🎯 Number Guessing Game")
st.subheader("Think of a number, and let the computer guess it!")

# Initialize session state variables
if "low" not in st.session_state:
    st.session_state.low = 1
if "high" not in st.session_state:
    st.session_state.high = 100
if "min_range" not in st.session_state:
    st.session_state.min_range = 1
if "max_range" not in st.session_state:
    st.session_state.max_range = 100
if "guess" not in st.session_state:
    st.session_state.guess = rd.randint(st.session_state.low, st.session_state.high)
if "game_active" not in st.session_state:
    st.session_state.game_active = False
if "feedback" not in st.session_state:
    st.session_state.feedback = "Select an option"
if "attempts" not in st.session_state:
    st.session_state.attempts = 0

# Display game instructions and range selection
if not st.session_state.game_active:
    st.info("👋 Welcome! Set your number range and click 'Start Game'")
    
    col1, col2 = st.columns(2)
    with col1:
        min_range = st.number_input("Minimum number", value=st.session_state.min_range, step=1)
    with col2:
        max_range = st.number_input("Maximum number", value=st.session_state.max_range, step=1)
    
    if min_range >= max_range:
        st.error("Minimum number must be less than maximum number!")
    else:
        st.session_state.min_range = min_range
        st.session_state.max_range = max_range

# Start game button
if st.button("Start Game") and not st.session_state.game_active and st.session_state.min_range < st.session_state.max_range:
    st.session_state.game_active = True
    st.session_state.low = st.session_state.min_range
    st.session_state.high = st.session_state.max_range
    st.session_state.guess = rd.randint(st.session_state.low, st.session_state.high)
    st.session_state.feedback = "Select an option"
    st.session_state.attempts = 0

# Run game only if it's active
if st.session_state.game_active:
    st.write(f"🎮 Range: {st.session_state.min_range} to {st.session_state.max_range}")
    st.write(f"🤖 Computer's Guess: **{st.session_state.guess}**")
    st.write(f"Attempts: {st.session_state.attempts}")

    # Take user feedback
    feedback = st.radio(
        "Is the guess:",
        ["Select an option", "Too High (H)", "Too Low (L)", "Correct (C)"],
        index=0,
        key="feedback_radio"
    )

    # Button to submit feedback
    if st.button("Submit Feedback"):
        if feedback == "Select an option":
            st.warning("⚠️ Please select whether the guess is too high, too low, or correct!")
        else:
            st.session_state.attempts += 1
            
            if feedback == "Too High (H)":
                st.session_state.high = st.session_state.guess - 1
            elif feedback == "Too Low (L)":
                st.session_state.low = st.session_state.guess + 1
            elif feedback == "Correct (C)":
                st.balloons()
                
                st.success(f"🎉 The computer guessed your number **{st.session_state.guess}** correctly in {st.session_state.attempts} attempts! 👌")
                st.session_state.game_active = False
                if st.button("Play Again"):
                    st.session_state.game_active = False
                st.stop()
            
            # Ensure low is not greater than high before making a new guess
            if st.session_state.low <= st.session_state.high:
                st.session_state.guess = rd.randint(st.session_state.low, st.session_state.high)
                st.rerun()
            else:
                st.error("🚨 There seems to be an inconsistency in your responses. The number you're thinking of might have changed. Please restart the game.")
                st.session_state.game_active = False
