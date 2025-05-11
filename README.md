# Netflix Data Visualization Project

This interactive dashboard explores trends in Netflix content production, quality (via IMDb ratings), and their potential business impact (via stock price). The analysis uses data from Kaggle and is implemented with Dash and Plotly.

### Live Demo

Check out the deployed dashboard here: [Netflix Dashboard on Render](https://netflix-dashboard-792p.onrender.com)

# Installation & Execution
This project runs on Python 3.12+ and requires several dependencies listed in requirements.txt.

## 1. Clone the repository
```bash
git clone https://github.com/Xin-10/Netflix-Data-Visualization.git
cd Netflix-Data-Visualization
```

## 2. Create a virtual environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate      # Windows
```

## 3. Install dependencies
```bash
pip install -r requirements.txt
```

## 4. Run the Dash Web Application
To launch the interactive visualization dashboard, run:
```bash
python app/app.py
```

## Repository Structure & File Descriptions  

This repository is structured as follows:

```bash
Netflix-Data-Visualization/
│
├── app/                        # Dash Web App
│   ├── app.py                 # Main app layout
│   └── visualization.py       # Plot functions
│
├── data/                       # Cleaned datasets
│   ├── cleaned_Netflix_IMDB.csv
│   ├── cleaned_Netflix_Shows.csv
│   ├── cleaned_Netflix_stocks.csv
│   └── netflix_final_merged.csv
│
├── notebooks/                  # EDA & prep notebooks
│   ├── Netflix_IMDB.ipynb
│   ├── Netflix_Stock.ipynb
│   ├── Netflix_Movie_TVShows.ipynb
│   └── final_visualization.ipynb
│
├── requirements.txt
├── README.md
└── Netflix_Report.pdf          # Full analysis

```
---
