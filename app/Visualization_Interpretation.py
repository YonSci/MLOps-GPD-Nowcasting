import streamlit as st

def Visualization_Interpretation():
    #  blue, green, orange, red, violet, gray/grey, rainbow.
    st.markdown(
    """
    <style>
    .title {
        background-color: lightblue;
        padding: 10px;
        border-radius: 8px;
    }
    </style>
    <div class="title">
        <h1>Visualization and Interpretation</h1>
    </div>
    """,
    unsafe_allow_html=True
)
    
    
    st.markdown("---")
    
if __name__ == "__main__":
    Visualization_Interpretation()