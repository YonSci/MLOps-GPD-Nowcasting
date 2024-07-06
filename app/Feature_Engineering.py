import streamlit as st

def Feature_Engineering():
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
        <h1>Feature Engineering</h1>
    </div>
    """,
    unsafe_allow_html=True
)
    
    
    st.markdown("---")
    
if __name__ == "__main__":
    Feature_Engineering()