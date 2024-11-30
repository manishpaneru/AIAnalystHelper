# AIAnalystHelper
This is an program that is designed to help Data analyst. Created by one data analyst for others. 




# AI-Powered Data Analysis Web App

This project is a dynamic, AI-driven web application that assists users in exploring, cleaning, and understanding datasets. Powered by Grouqcloud's `llama-8b-instant` API and built using Streamlit, the app is designed to cater to users of all expertise levels—novice, expert, or world-class professionals.

---

## **Features**
- **Dynamic Data Overview**:
  - Generate concise or detailed summaries of the uploaded dataset.
  - Adjust output complexity based on the user's chosen expertise level.

- **Data Cleaning Assistance**:
  - Provides 10–30 tailored cleaning steps for the uploaded dataset.
  - The depth and complexity of steps adapt to the user's needs.

- **Exploratory Data Analysis (EDA)**:
  - Recommends EDA steps and generates visualizations (2-3 charts per dataset).
  - Tailored to the dataset's depth and user's expertise level.

- **Interactive User Interface**:
  - Simple, intuitive web app built with Streamlit.
  - Upload CSV files, choose tasks, and set expertise level—all within the app.

---

## **How It Works**
1. **Upload a Dataset**: 
   - The app accepts CSV files for analysis.
2. **Select a Task**:
   - Options include:
     - Data Cleaning
     - EDA
     - Data Overview
3. **Choose Complexity**:
   - Levels include:
     - Novice
     - Expert Data Professional
     - World-Class Data Professional
4. **Get Results**:
   - Outputs are tailored based on user input, offering insights, steps, and visualizations.

---

## **Tech Stack**
- **Frontend**: Streamlit
- **Backend**: Python
- **API**: Grouqcloud `llama-8b-instant`
- **Libraries**:
  - `pandas`: Data processing.
  - `matplotlib`: Data visualization.
  - `python-dotenv`: Environment variable management.

---

## **Setup Instructions**

### **1. Prerequisites**
- Python 3.8 or higher
- Grouqcloud API key

### **2. Clone the Repository**
```bash
git clone https://github.com/yourusername/data-analysis-webapp.git
cd data-analysis-webapp
