import streamlit as st
import pandas as pd
from api_utils import analyze_data
from visualization_utils import create_visualization
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def main():
    # Set page config and title
    st.set_page_config(
        page_title="Helper Analyst",
        page_icon="📊",
        layout="wide"
    )
    
    # Main title with custom styling
    st.markdown("""
        <h1 style='text-align: center;'>Helper Analyst</h1>
        <h3 style='text-align: center; color: #666;'>An AI helper designed for data analyst by Manish Paneru</h3>
        <hr>
        """, unsafe_allow_html=True)
    
    # File upload section
    uploaded_file = st.file_uploader("Upload your CSV file", type=['csv'])
    
    if uploaded_file is not None:
        # Read the dataset
        try:
            df = pd.read_csv(uploaded_file)
            st.success("File uploaded successfully!")
            
            # Task selection
            task_type = st.selectbox(
                "Select Analysis Task",
                ["Data Overview", "Data Cleaning", "Exploratory Data Analysis (EDA)"]
            )
            
            # Complexity level
            complexity = st.radio(
                "Select Analysis Complexity",
                ["Basic", "Intermediate", "Advanced"]
            )
            
            if st.button("Analyze"):
                with st.spinner("Analyzing your data..."):
                    # Get analysis from API
                    analysis_result = analyze_data(
                        task_type=task_type,
                        complexity=complexity,
                        dataset_info={
                            'columns': df.columns.tolist(),
                            'shape': df.shape,
                            'sample': df.head().to_dict()
                        }
                    )
                    
                    # Display results
                    st.subheader("Analysis Results")
                    st.write(analysis_result['explanation'])
                    
                    # Create and display visualizations if available
                    if 'visualizations' in analysis_result:
                        for viz in analysis_result['visualizations']:
                            fig = create_visualization(df, viz)
                            st.pyplot(fig)
                    
        except Exception as e:
            st.error(f"Error processing file: {str(e)}")
    
    # Add footer
    st.markdown("""
        <div style='text-align: center; color: #666; padding: 20px;'>
        Made with ❤️ by Manish Paneru
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main() 