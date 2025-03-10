# Netflix Data Visualization Project

## Project Overview
This project originated from a common question: **"Is the quality of movies and TV shows declining?"**  
A deeper question follows: **"If this is true, why do film companies and streaming platforms allow it to happen?"**  
Does this suggest that **content quality does not significantly impact a company's business performance?**

To explore this issue with data, I incorporated three key datasets from Netflix:

- **Netflix Movie & TV Show Data** (content production & metadata)
- **IMDb Ratings Data** (quality assessment)
- **Netflix Stock Price Data** (business performance)

As the most prominent streaming platform, Netflix's content strategy shifts may provide insights into broader industry trends.

---

## Research Framework
This analysis revolves around three core questions:

### 1. Has the quality of Netflix content declined?

✅ **Is the average IMDb rating of Netflix content decreasing?**  

- **Netflix IMDb Score Trend Over Time:** Shows the trend of IMDb scores over time.
- **High-Quality Content Proportion Over Time:** Tracks the percentage of high-rated content (IMDb ≥ 7.5).  

**Conclusion:** Both analyses indicate a noticeable decline in IMDb scores, suggesting a decline in content quality.

✅ **Is Netflix producing more content?**  

- **Movie vs. TV Show Production Trend:** Examines changes in Netflix's content production volume.  

**Conclusion:**  
The number of releases has significantly increased, while quality has declined. This raises further questions:  

- Is Netflix prioritizing quantity over quality?  
- Is this part of a deliberate expansion strategy where producing more content naturally lowers the proportion of high-quality releases?  

✅ **How do movies and TV shows compare in terms of ratings?**  

- **Movie vs. TV Show IMDb Score Trend:** Compares IMDb scores between movies and TV shows.  

**Findings:**  
- TV shows consistently have higher IMDb ratings than movies.  
- TV shows generally have higher production value.  
- IMDb users being more selective in rating TV shows than movies.  

---

### 2. Does content quality impact Netflix’s stock price?

✅ **Does content quantity affect Netflix’s stock price?**  

- **Netflix Content Releases & Stock Price Over Time:** Examines the relationship between the number of releases and stock price fluctuations.

✅ **Does content quality impact stock price?**  

- **Netflix High-Quality Content & Stock Price Over Time:** Investigates whether high-quality content influences stock performance.  

**Conclusion:**  
- Content quantity shows some correlation with stock price.  
- Content quality (IMDb ratings) has little to no impact on stock price.  

✅ **Did content quality have a stronger impact on stock price in Netflix’s early years compared to recent years?**  

- **Does Content Quality Affect Stock Volatility? (Early vs. Recent)**  

**Findings:**  
- In the early years (2005–2010), content quality had a stronger correlation with stock price fluctuations.  
- In recent years (2015–2022), stock price has been influenced by multiple factors, including subscriber growth, financial reports, and market expectations, making content quality a less significant factor.  

✅ **Do blockbuster releases impact stock price?**  

- **Impact of Hit Shows on Netflix Stock (Short-term):** Investigates whether high-profile releases influence stock price in the short term.  
- **Netflix Annual Hit Shows vs. Stock Price (Long-term):** Examines whether consistently producing hit shows affects long-term stock performance.  

**Conclusion:**  
- Individual hit shows do not significantly impact Netflix’s stock price.  
- Netflix’s ability to consistently produce successful content does not show a clear correlation with stock performance.  

**Key Takeaway:**  
The quality of Netflix content does not directly determine stock price.  
However, an indirect relationship may exist, where content quality influences subscriber growth, which in turn affects Netflix’s financial reports and stock price.

---

### 3. Why has Netflix shifted its content strategy?

✅ **Is Netflix prioritizing international expansion over content quality?**  

- **Netflix Content Genre Trends Over Time:** Analyzes changes in content type distribution.  
- **Trend of International Content Over Time:** Examines the growth of international content.  

**Findings:**  
- After 2015–2017, the proportion of international content in Netflix’s catalog increased significantly.  
- Netflix has expanded its investments in non-English content, potentially influencing IMDb ratings due to regional differences in rating behavior.  

✅ **How has Netflix's content production shifted geographically?**  

- **Netflix Content Production Growth by Country (2003–2021)**  

**Conclusion:**  
- Netflix has significantly diversified its content production across different countries.  
- This international expansion aligns with the observed decline in average IMDb ratings, potentially due to regional rating differences.  

## Final Takeaway

- **Netflix prioritizes subscriber growth and global market expansion over IMDb ratings (Quality).**  
- The decline in ratings is likely a byproduct of an expansion strategy, rather than an intentional drop in content quality.  
- Netflix operates more like a content platform than a traditional film studio, prioritizing content variety and user retention over high individual ratings.  
- While content quality does not directly impact Netflix’s stock price, it may have an indirect effect by influencing user subscriptions, retention rates, and overall platform engagement—factors that ultimately affect financial performance.  

---

## Limitations & Future Improvements

### Limitations

#### **Potential Bias in IMDb Ratings**
- IMDb ratings are user-generated and tend to be skewed toward English-speaking audiences, leading to a potential bias in content evaluation.  
- As Netflix expands internationally, a growing portion of its content is produced in non-English languages, but non-English-speaking audiences may be less likely to rate content on IMDb.  
- This underrepresentation may cause certain international content to appear lower-rated than it actually is within its target markets, potentially distorting the perception of content quality.  

#### **Stock Price Influences Beyond Content Quality**
- Netflix’s stock price is affected by multiple external factors, including subscriber growth, revenue reports, competitive dynamics, and macroeconomic conditions.  
- This complexity makes it difficult to isolate the impact of content quality on stock performance.  
- While content quality may indirectly influence Netflix’s financial health through user engagement and retention, it is not the sole driver of stock price fluctuations.  

#### **Lack of Direct User Engagement Data**
- This analysis does not incorporate subscriber engagement metrics, such as watch time, churn rates, or subscription renewal trends.  
- Understanding how content quality affects user retention and engagement would require access to Netflix’s internal data, which is not publicly available.  
- Without this data, it is challenging to measure the true impact of content quality on business performance beyond stock trends.  

---

## Future Work

### **Analyze Netflix Subscriber Growth vs. IMDb Ratings (if possible)**
- Investigate whether declining IMDb scores correlate with subscriber retention rates, user dissatisfaction, or reduced engagement over time.  
- Identify whether lower-rated content leads to increased subscription cancellations or a shift in viewing habits.  

### **Explore Sentiment Analysis on Social Media Data**
- Extract discussions from Twitter, Reddit, and YouTube to analyze how public sentiment toward Netflix content evolves.  
- Determine whether negative/positive reception on social media aligns with IMDb ratings trends or subscriber behavior.  

### **Compare Netflix’s Strategy to Other Streaming Platforms**
- Expand the analysis to Disney+, Amazon Prime, and HBO Max to examine whether content quality decline is a Netflix-specific trend or an industry-wide phenomenon.  
- Investigate whether other streaming platforms prioritize different content strategies, such as investing more in high-quality productions.  

---

## Key Visualizations

| **Visualization** | **Description** |
|------------------|----------------|
| **Netflix IMDb Score Trend Over Time** | Is Netflix's content quality declining? |
| **High-Quality Content Proportion Over Time** | Is the proportion of high-rated content stable? |
| **Movie vs. TV Show Production Trend** | Is Netflix increasing content production? |
| **Movie vs. TV Show IMDb Score Trend** | Are Netflix movies and TV shows rated differently? |
| **Netflix Content Releases & Stock Price Over Time** | Does the number of releases influence stock price? |
| **Netflix High-Quality Content & Stock Price Over Time** | Is high-quality content correlated with stock price? |
| **Does Content Quality Affect Stock Volatility? (Early vs. Recent)** | Has content quality influenced Netflix's stock volatility over time? |
| **Impact of Hit Shows on Netflix Stock (Short-term)** | Do blockbuster shows (IMDb ≥ 8.0, ≥ 100k votes) cause short-term stock fluctuations? |
| **Netflix Annual Hit Shows vs. Stock Price (Long-term)** | Does the number of annual hit shows correlate with stock performance? |
| **Netflix Content Genre Trends Over Time** | How has Netflix’s content strategy changed in terms of genre distribution? |
| **Trend of International Content Over Time** | Is Netflix investing more in international content? |
| **Netflix Content Production Growth by Country (2003–2021)** | Which countries contribute the most Netflix content? |

---

## Repository Structure & File Descriptions  

This repository is structured as follows:

```bash
Netflix-Data-Visualization/
│── app/               # Dash Web Application
│   ├── app.py         # Main application script
│   ├── visualization.py # Visualization functions for generating charts
│── data/              # Cleaned datasets used for analysis
│   ├── cleaned_Netflix_IMDB.csv     # Processed IMDb ratings data
│   ├── cleaned_Netflix_Shows.csv    # Processed Netflix shows metadata
│   ├── cleaned_Netflix_stocks.csv   # Processed stock price data
│   ├── netflix_final_merged.csv     # Merged dataset combining all sources
│── notebooks/         # Jupyter Notebooks for data processing & visualization
│   ├── final_visualization.ipynb       # Main notebook for final charts
│   ├── Netflix_Movie_TVShows.ipynb     # Analysis of Netflix content production trends
│   ├── Netflix_IMDB.ipynb              # IMDb ratings analysis
│   ├── Netflix_Overall_DataProcessing.ipynb # Data cleaning and transformation steps
│   ├── Netflix_Stock.ipynb             # Stock price trends analysis
│── README.md          # Project documentation
│── requirements.txt   # List of dependencies for running the project
│── .gitignore         # Specifies files & folders to be ignored by Git
```
---

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