import os
import requests
from dotenv import load_dotenv
import pandas as pd
import json

# Load environment variables
load_dotenv()

def analyze_data(task_type, complexity, dataset_info):
    """
    Interact with the Grouqcloud API to analyze data.
    """
    api_key = os.getenv('GROQ_API_KEY')
    if not api_key:
        raise ValueError("API key not found in environment variables")
    
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    
    # Convert sample data to a more readable format
    sample_df = pd.DataFrame(dataset_info['sample'])
    
    # Construct task-specific prompts
    if task_type == "Data Overview":
        prompt = f"""As a data analysis expert, provide a comprehensive overview of this dataset:
        
        Dataset Information:
        - Columns: {dataset_info['columns']}
        - Shape: {dataset_info['shape']}
        - Sample Data: {sample_df.to_string()}
        
        Please provide:
        1. Detailed description of each column and its potential purpose
        2. Basic statistics about the dataset size and structure
        3. Initial observations about data types and potential uses
        4. Any immediate concerns or notable characteristics
        
        Format the response in a clear, structured way with sections and bullet points.
        """
    
    elif task_type == "Data Cleaning":
        prompt = f"""As a data analysis expert, provide detailed data cleaning recommendations:
        
        Dataset Information:
        - Columns: {dataset_info['columns']}
        - Shape: {dataset_info['shape']}
        - Sample Data: {sample_df.to_string()}
        
        Please provide:
        1. Specific data quality issues identified in each column
        2. Step-by-step cleaning procedures needed
        3. Recommendations for handling missing values
        4. Data type conversions needed
        5. Outlier detection and handling suggestions
        
        Format the response as a detailed action plan with clear steps.
        """
    
    elif task_type == "Exploratory Data Analysis (EDA)":
        prompt = f"""As a data analysis expert, perform a detailed exploratory data analysis:
        
        Dataset Information:
        - Columns: {dataset_info['columns']}
        - Shape: {dataset_info['shape']}
        - Sample Data: {sample_df.to_string()}
        
        Please provide:
        1. Detailed statistical analysis of numerical columns
        2. Distribution patterns and trends
        3. Key relationships between variables
        4. Specific visualization recommendations with:
           - Exact columns to use
           - Type of chart (focus on line and bar charts)
           - Axis labels and titles
           - Purpose of each visualization
        5. Notable patterns or insights
        
        For visualizations, focus on creating meaningful line charts and bar charts that show real insights.
        Specify exact column names and relationships to visualize.
        """
    
    payload = {
        'model': 'mixtral-8x7b-32768',
        'messages': [
            {'role': 'system', 'content': 'You are an expert data analyst assistant. Provide detailed, technical analysis with specific references to the data.'},
            {'role': 'user', 'content': prompt}
        ],
        'temperature': 0.7,
        'max_tokens': 4096
    }
    
    try:
        response = requests.post(
            'https://api.groq.com/openai/v1/chat/completions',
            headers=headers,
            json=payload
        )
        response.raise_for_status()
        
        result = response.json()
        content = result['choices'][0]['message']['content']
        
        # Only extract visualization suggestions for EDA
        visualizations = []
        if task_type == "Exploratory Data Analysis (EDA)":
            visualizations = extract_visualization_suggestions(content, dataset_info['columns'])
        
        return {
            'explanation': content,
            'visualizations': visualizations
        }
        
    except requests.exceptions.RequestException as e:
        raise Exception(f"API request failed: {str(e)}")

def extract_visualization_suggestions(content, columns):
    """Extract specific visualization suggestions from the API response content"""
    visualizations = []
    
    # Look for specific visualization recommendations in the content
    lines = content.lower().split('\n')
    current_viz = {}
    
    for line in lines:
        # Look for lines that mention specific columns and chart types
        if ('line chart' in line or 'bar chart' in line) and any(col.lower() in line.lower() for col in columns):
            # Extract column names mentioned in the line
            mentioned_columns = [col for col in columns if col.lower() in line.lower()]
            
            if 'line chart' in line:
                if len(mentioned_columns) >= 2:
                    visualizations.append({
                        'type': 'line',
                        'params': {
                            'x': mentioned_columns[0],
                            'y': mentioned_columns[1],
                            'title': f'Trend of {mentioned_columns[1]} over {mentioned_columns[0]}',
                            'xlabel': mentioned_columns[0],
                            'ylabel': mentioned_columns[1]
                        }
                    })
            
            if 'bar chart' in line:
                if len(mentioned_columns) >= 2:
                    visualizations.append({
                        'type': 'bar',
                        'params': {
                            'x': mentioned_columns[0],
                            'y': mentioned_columns[1],
                            'title': f'{mentioned_columns[1]} by {mentioned_columns[0]}',
                            'xlabel': mentioned_columns[0],
                            'ylabel': mentioned_columns[1]
                        }
                    })
    
    return visualizations 