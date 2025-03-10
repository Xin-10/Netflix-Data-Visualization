import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from sklearn.linear_model import LinearRegression
import numpy as np
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "../data/netflix_final_merged.csv")

df = pd.read_csv(DATA_PATH)
df["release_date"] = pd.to_datetime(df["release_date"])
df["year"] = df["release_date"].dt.year

### 1. Netflix IMDb Score Trend Over Time**
def plot_imdb_score_trend():
    fig = px.line(df.groupby('year')['imdb_score'].mean().reset_index(),
                  x='year', y='imdb_score',
                  title="Netflix IMDb Score Trend Over Time",
                  labels={"imdb_score": "Average IMDb Score", "year": "Year"},
                  line_shape="spline",
                  color_discrete_sequence=["red"])

    fig.update_layout(
        template="plotly_dark",
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, zeroline=False),
        annotations=[
            dict(x=2015, y=6.5, xref="x", yref="y",
                 text="2015: Netflix began rapid expansion",
                 showarrow=True, arrowhead=2, font=dict(color="white"))
        ]
    )
    return fig

### 2. High-Quality Content Proportion Over Time**
df['high_quality'] = df['imdb_score'] >= 7.5
def plot_high_quality_proportion():
    df_quality = df.groupby('year')['high_quality'].mean().reset_index()

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=df_quality['year'], 
        y=df_quality['high_quality'], 
        name='High-Quality Content',
        marker=dict(color="rgba(229, 9, 20, 0.7)", line=dict(color="#E50914", width=1))
    ))

    annotations = [
        dict(
            x=2017, y=0.1, xref="x", yref="y",
            text="2017: Netflix surpasses 100M <br> subscribers, reinforcing leadership",
            showarrow=True, arrowhead=7, font=dict(color="white"),
            ax=0, ay=-40
        )
    ]

    fig.update_layout(
        title="High-Quality Content Proportion Over Time",
        title_font=dict(size=20, color="white"),
        xaxis=dict(title="Year", color="white"),
        yaxis=dict(title="Proportion of High-Rated Content", color="white"),
        template="plotly_dark",
        font=dict(color="white"),
        annotations=annotations,
        bargap=0.2,
        legend=dict(
            x=0.85, y=1, bgcolor="rgba(0,0,0,0)", bordercolor="white"
        )
    )

    return fig

### 3. Movie vs. TV Show Production Trend**
def plot_movie_vs_tv_production():
    df_type = df.groupby(['year', 'type']).size().reset_index(name='count')

    fig = px.line(df_type, x='year', y='count', color='type',
                  title="Movie vs. TV Show Production Trend",
                  labels={"year": "Year", "count": "Number of Productions"},
                  color_discrete_map={"MOVIE": "#E50914", "SHOW": "#B3B3B3"})

    fig.update_traces(mode="lines+markers", line=dict(width=3))

    annotations = [
        dict(x=2013, y=50, xref="x", yref="y",
             text="2013: House of Cards Released", showarrow=True, arrowhead=2, 
             font=dict(color="white"))
    ]

    fig.update_layout(
        template="plotly_dark",
        xaxis=dict(tickangle=-45),
        yaxis=dict(gridcolor="rgba(255,255,255,0.2)"),
        font=dict(size=14),
        annotations=annotations
    )

    return fig

### 4. Movie vs. TV Show IMDb Score Trend**
def plot_movie_vs_tv_imdb():
    df_score = df.groupby(['year', 'type'])['imdb_score'].mean().reset_index()

    fig = px.line(df_score, x='year', y='imdb_score', color='type',
                  title="Movie vs. TV Show IMDb Score Trend",
                  labels={"year": "Year", "imdb_score": "Average IMDb Score"},
                  color_discrete_map={"MOVIE": "#E50914", "SHOW": "#B3B3B3"})

    fig.update_traces(mode="lines+markers", line=dict(width=3))

    fig.update_layout(
        template="plotly_dark",
        xaxis=dict(tickangle=-45),
        yaxis=dict(gridcolor="rgba(255,255,255,0.2)"),
        font=dict(size=14),
    )

    return fig

### 5. Netflix Content Releases & Stock Price Over Time**
df_stock = df.groupby('year').agg({'close': 'mean', 'title': 'count'}).reset_index()
df_stock['high_quality_ratio'] = df.groupby('year')['high_quality'].sum().reset_index(drop=True) / df_stock['title']

def plot_stock_vs_releases():
    df_stock['price_change'] = df_stock['close'].pct_change() * 100
    df_stock['price_change'] = df_stock['price_change'].rolling(window=5, min_periods=2).mean()
    df_stock['price_change'] = df_stock['price_change'].fillna(0)

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df_stock['year'], y=df_stock['close'],
        mode='lines',
        name='Stock Price',
        line=dict(color='#E50914', width=2),
        hovertemplate='Year: %{x}<br>Stock Price: %{y:.2f} USD'
    ))

    fig.add_trace(go.Scatter(
        x=df_stock['year'], y=df_stock['title'],
        mode='lines',
        name='Content Releases',
        line=dict(color='white', dash='dash'),
        yaxis='y2',
        hovertemplate='Year: %{x}<br>Content Releases: %{y}'
    ))

    fig.add_trace(go.Scatter(
        x=df_stock['year'], y=df_stock['price_change'],
        mode='lines+markers',
        name='Stock Price Change (%)',
        line=dict(color='orange', width=2),
        yaxis='y2',
        hovertemplate='Year: %{x}<br>Stock Change: %{y:.2f}%'
    ))

    fig.update_layout(
        title="Netflix Content Releases & Stock Price Over Time",
        title_font=dict(size=18, color="white"),
        xaxis_title="Year",
        yaxis=dict(title="Stock Price (USD)", side="left", tickfont=dict(color="white")),
        yaxis2=dict(title="Content Releases & Stock Price Change (%)", overlaying='y', side="right", tickfont=dict(color="white")),

        legend=dict(
            x=0.5,
            y=-0.2,
            xanchor="center",
            yanchor="top",
            orientation="h",
            bgcolor="rgba(0,0,0,0.4)",
            bordercolor="white",
            borderwidth=1
        ),
        template="plotly_dark",
        margin=dict(l=50, r=50, t=50, b=50),
        font=dict(family="Arial", color="white")
    )

    return fig

### 6. High-Quality Content & Stock Price Over Time**
df['high_quality'] = df['imdb_score'] >= 7.5

df_stock = df.groupby('year').agg(
    {'close': 'mean', 'title': 'count', 'high_quality': 'sum'}
).reset_index()

df_stock['high_quality_ratio'] = df_stock['high_quality'] / df_stock['title'] * 100
df_stock['price_change'] = df_stock['close'].pct_change().fillna(0) * 100
df_stock['price_change'] = df_stock['price_change'].rolling(window=5, min_periods=2).mean()

df_stock['high_quality_ratio'] = df_stock['high_quality_ratio'].fillna(0)
df_stock['price_change'] = df_stock['price_change'].fillna(0)

def plot_stock_vs_quality():
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df_stock['year'], y=df_stock['close'],
        mode='lines',
        name='Stock Price',
        line=dict(color='#E50914', width=2),
        hovertemplate='Year: %{x}<br>Stock Price: %{y:.2f} USD'
    ))

    fig.add_trace(go.Scatter(
        x=df_stock['year'], y=df_stock['high_quality_ratio'],
        mode='lines',
        name='High-Quality Content Ratio (%)',
        line=dict(color='lightblue', dash='dash'),
        yaxis='y2',
        hovertemplate='Year: %{x}<br>High-Quality Content: %{y:.2f}%'
    ))

    fig.add_trace(go.Scatter(
        x=df_stock['year'], y=df_stock['price_change'],
        mode='lines+markers',
        name='Stock Price Change (%)',
        line=dict(color='orange', width=2),
        yaxis='y2',
        hovertemplate='Year: %{x}<br>Stock Change: %{y:.2f}%'
    ))

    y2_min = df_stock[['high_quality_ratio', 'price_change']].min().min() * 0.8
    y2_max = df_stock[['high_quality_ratio', 'price_change']].max().max() * 1.2

    fig.update_layout(
        title="Netflix High-Quality Content & Stock Price Over Time",
        title_font=dict(size=18, color="white"),
        xaxis_title="Year",
        yaxis=dict(title="Stock Price (USD)", side="left", tickfont=dict(color="white")),
        yaxis2=dict(title="High-Quality Content Ratio (%) & Stock Price Change (%)",
                    overlaying='y', side="right", tickfont=dict(color="white"),
                    range=[y2_min, y2_max]),  
        legend=dict(
            x=0.5,
            y=-0.2,
            xanchor="center",
            yanchor="top",
            orientation="h",
            bgcolor="rgba(0,0,0,0.4)",
            bordercolor="white",
            borderwidth=1
        ),
        template="plotly_dark",
        margin=dict(l=50, r=50, t=50, b=50),
        font=dict(family="Arial", color="white")
    )

    return fig

### 7. Impact of IMDb Score on Stock Volatility**
df["release_date"] = pd.to_datetime(df["release_date"])

df_early = df[df["release_date"] < "2010"].copy()
df_recent = df[df["release_date"] > "2015"].copy()

df_early = df_early.set_index("release_date").resample("QE")[["imdb_score", "volatility"]].mean().reset_index()
df_recent = df_recent.set_index("release_date").resample("QE")[["imdb_score", "volatility"]].mean().reset_index()

def fit_trendline(df, x_col, y_col):
    df = df.dropna(subset=[x_col, y_col]).copy()
    X = df[[x_col]]
    y = df[y_col]

    if len(X) > 1 and len(y) > 1:
        model = LinearRegression().fit(X, y)
        df.loc[:, "trendline"] = model.predict(X)
    else:
        df.loc[:, "trendline"] = np.nan

    return df

df_early = fit_trendline(df_early, "imdb_score", "volatility")
df_recent = fit_trendline(df_recent, "imdb_score", "volatility")

corr_early = df_early["imdb_score"].corr(df_early["volatility"])
corr_recent = df_recent["imdb_score"].corr(df_recent["volatility"])

def plot_quality_vs_stock_volatility():
    fig = make_subplots(rows=1, cols=2, subplot_titles=(
        f"Early Years (<2010): Corr={corr_early:.2f}", 
        f"Recent Years (>2015): Corr={corr_recent:.2f}"
    ))

    fig.add_trace(go.Scatter(
        x=df_early["imdb_score"], 
        y=df_early["volatility"], 
        mode='markers', name="Early Years",
        marker=dict(color="#FF4C4C", size=8, opacity=0.8)
    ), row=1, col=1)

    fig.add_trace(go.Scatter(
        x=df_early["imdb_score"], 
        y=df_early["trendline"], 
        mode='lines', name="Trend (Early)", 
        line=dict(color="#FFAA4C", width=2)
    ), row=1, col=1)

    fig.add_trace(go.Scatter(
        x=df_recent["imdb_score"], 
        y=df_recent["volatility"], 
        mode='markers', name="Recent Years",
        marker=dict(color="#E50914", size=8, opacity=0.8)
    ), row=1, col=2)

    fig.add_trace(go.Scatter(
        x=df_recent["imdb_score"], 
        y=df_recent["trendline"], 
        mode='lines', name="Trend (Recent)", 
        line=dict(color="#FFC14C", width=2)
    ), row=1, col=2)

    fig.update_layout(
        title="Does Content Quality Affect Stock Volatility? (Early vs. Recent)",
        title_x=0.5,  
        title_font=dict(size=20, color="white"),
        template="plotly_dark",
        font=dict(color="white"),
    )

    fig.update_xaxes(title_text="IMDb Score (Early Years)", row=1, col=1)
    fig.update_xaxes(title_text="IMDb Score (Recent Years)", row=1, col=2)

    return fig

### 8. Impact of Hit Shows on Netflix Stock**
hit_shows = df[(df['imdb_score'] >= 8.0) & (df['imdb_votes'] >= 100000)].copy()
hit_shows["year"] = hit_shows["release_date"].dt.year

def plot_impact_of_hit_shows_on_stock(df=df):
    hit_shows["release_date_jitter"] = hit_shows["release_date"].astype(np.int64) // 10**9
    hit_shows["release_date_jitter"] += np.random.uniform(-5, 5, size=len(hit_shows))
    hit_shows["release_date_jitter"] = pd.to_datetime(hit_shows["release_date_jitter"], unit="s")

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df["release_date"], y=df["close"],
        mode="lines",
        name="Netflix Stock Trend",
        line=dict(color="lightgrey", width=1.5, dash="solid"),
        opacity=0.8
    ))

    fig.add_trace(go.Scatter(
        x=hit_shows["release_date_jitter"], 
        y=hit_shows["close"],
        mode="markers",
        marker=dict(
            size=hit_shows["imdb_votes"] / 20000,
            color=hit_shows["imdb_score"],  
            colorscale="YlOrRd",
            opacity=1,
            symbol="circle-open",
            line=dict(width=1.2, color="white")
        ),
        name="Hit Shows",
        legendgroup="Hit Shows",
        hovertemplate="<b>%{text}</b><br>IMDb: %{marker.color}<br>Stock Price: %{y}",
        text=hit_shows["title"]
    ))

    fig.update_layout(
        title=dict(
            text="Impact of Hit Shows on Netflix Stock (Short-term)",
            font=dict(size=18)
        ),
        coloraxis=dict(
            colorscale="YlOrRd",
            colorbar=dict(
                title="IMDb Score",
                thickness=15,
                x=1.07,
                xanchor="center"
            )
        ),
        legend=dict(
            x=0.02,
            y=1.15,
            orientation="h",
            font=dict(size=12)
        ),
        xaxis_title="Release Date",
        yaxis_title="Stock Price",
        font=dict(color="white"),
        template="plotly_dark"
    )

    return fig


### 9. Netflix Annual Hit Shows vs. Stock Price**
df = pd.read_csv(DATA_PATH)

df["release_date"] = pd.to_datetime(df["release_date"])
df["year"] = df["release_date"].dt.year
df["close"] = pd.to_numeric(df["close"], errors="coerce")

df["high_quality"] = df["imdb_score"] >= 7.5

hit_shows = df[(df["imdb_score"] >= 8.0) & (df["imdb_votes"] >= 100000)].copy()
hit_shows["year"] = hit_shows["release_date"].dt.year

hit_shows_per_year = hit_shows.groupby("year").size().reset_index(name="hit_count")

hit_shows_per_year["hit_count_smoothed"] = (
    hit_shows_per_year["hit_count"].rolling(window=5, min_periods=1).mean()
)

df_sampled = df.resample("YE", on="release_date")["close"].median().reset_index()

df_sampled["year"] = df_sampled["release_date"].dt.year

def plot_hit_shows_vs_stock_long_term():
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df_sampled["year"],
        y=df_sampled["close"],
        mode="lines",
        name="Netflix Stock Trend",
        line=dict(color="white", width=2),
        opacity=0.8
    ))

    fig.add_trace(go.Scatter(
        x=hit_shows_per_year["year"],
        y=hit_shows_per_year["hit_count_smoothed"],
        mode="lines+markers",
        name="Hit Shows Per Year (Smoothed)",
        line=dict(color="red", width=2, dash="solid"),
        marker=dict(size=5, color="red"),
        opacity=0.8,
        yaxis="y2"
    ))

    fig.update_layout(
        title=dict(
            text="Netflix Annual Hit Shows vs. Stock Price (Long-term)",
            font=dict(size=18)
        ),
        xaxis=dict(
            title="Year",
            showgrid=True, gridcolor="gray"
        ),
        yaxis=dict(
            title="Stock Price",
            showgrid=True, gridcolor="gray"
        ),
        yaxis2=dict(
            title="Hit Shows Per Year (Smoothed)",
            overlaying="y",
            side="right",
            tickfont=dict(color="white"),
            showgrid=False
        ),
        coloraxis_colorbar=dict(
            title="IMDb Score",
            thickness=15,
            x=1.07,
            xanchor="center"
        ),
        legend=dict(
            x=0.02, y=1.15,
            orientation="h",
            font=dict(size=12)
        ),
        font=dict(color="white"),
        template="plotly_dark"
    )

    return fig

### 10. Netflix Content Genre Trends Over Time**
df["release_date"] = pd.to_datetime(df["release_date"], errors="coerce")
df["year"] = df["release_date"].dt.year

df["genres"] = df["genres"].astype(str).str.lower().str.replace("dramas", "drama").str.replace("comedies", "comedy")

df_exploded_genres = df.assign(genres=df["genres"].str.split(", ")).explode("genres")

df_exploded_genres = df_exploded_genres.dropna(subset=["release_date"])
df_exploded_genres["year"] = df_exploded_genres["release_date"].dt.year

genre_trend = df_exploded_genres.groupby(["year", "genres"])["title"].count().reset_index()

genre_trend["total_per_year"] = genre_trend.groupby("year")["title"].transform("sum")

genre_trend["percentage"] = genre_trend["title"] / genre_trend["total_per_year"]

top_genres = genre_trend.groupby("genres")["title"].sum().nlargest(10).index
genre_trend_filtered = genre_trend[genre_trend["genres"].isin(top_genres)]

def plot_genre_trends():
    fig = px.area(
        genre_trend_filtered, 
        x="year", 
        y="percentage", 
        color="genres",
        title="Netflix Content Genre Trends Over Time",
        labels={"year": "Year", "percentage": "Percentage of Content"},
        color_discrete_sequence=px.colors.qualitative.Dark24
    )

    fig.update_layout(
        template="plotly_dark",
        font=dict(color="white"),
        title_font=dict(size=20, color="white"),
        legend_title_font=dict(size=14, color="white"),
        legend_font=dict(size=12, color="white"),
        xaxis=dict(
            title="Year",
            tickfont=dict(color="white"),
            gridcolor='gray'
        ),
        yaxis=dict(
            title="Percentage of Content",
            tickfont=dict(color="white"),
            gridcolor='gray'
        )
    )

    return fig

### 11. Trend of International Content Over Time**
df["release_date"] = pd.to_datetime(df["release_date"], errors="coerce")
df["year"] = df["release_date"].dt.year

df["is_international"] = df["genres"].astype(str).str.contains("international", case=False, na=False)

international_trend = df.groupby("year")["is_international"].mean().reset_index()

international_trend["smoothed"] = international_trend["is_international"].rolling(window=3, min_periods=1).mean()

def plot_international_trend():
    fig = px.line(
        international_trend,
        x="year", 
        y="smoothed", 
        title="Trend of International Content Over Time",
        labels={"year": "Year", "smoothed": "Percentage of International Content"},
        markers=True
    )

    fig.update_traces(
        line=dict(color="#E50914", width=3),
        marker=dict(size=8, color="white", line=dict(width=2, color="#E50914"))
    )

    fig.update_layout(
        template="plotly_dark",
        font=dict(color="white"),
        title_font=dict(size=22, color="white"),
        xaxis=dict(
            title="Year",
            tickfont=dict(color="white", size=14),
            gridcolor="rgba(255,255,255,0.3)",
            showgrid=True,
            mirror=True
        ),
        yaxis=dict(
            title="Percentage of International Content",
            tickfont=dict(color="white", size=14),
            gridcolor="rgba(255,255,255,0.3)",
            showgrid=True,
            mirror=True
        ),
        margin=dict(l=60, r=60, t=60, b=60)
    )

    fig.add_vline(x=2010, line_width=2, line_dash="dash", line_color="gray")
    fig.add_vline(x=2016, line_width=2, line_dash="dash", line_color="gray")

    fig.add_annotation(x=2010, y=0.05, text="Netflix expands to Canada", showarrow=True, arrowhead=2, font=dict(color="white"))
    fig.add_annotation(x=2016, y=0.3, text="Global Expansion", showarrow=True, arrowhead=2, font=dict(color="white"))
    fig.add_annotation(x=2015, y=0.05, text="Growth starts", showarrow=True, arrowhead=2, font=dict(color="white"))

    return fig

### 12. Netflix Content Production Growth by Country**
df_cleaned = df[df["country"] != "Unknown"].copy()

df_cleaned = df_cleaned.assign(country=df_cleaned["country"].str.split(", ")).explode("country")

df_country_trend = df_cleaned.groupby(["year", "country"])["title"].count().reset_index()
df_country_trend.rename(columns={"title": "content_count"}, inplace=True)

df_total_per_year = df_country_trend.groupby("year")["content_count"].sum().reset_index()
df_total_per_year.rename(columns={"content_count": "total_content"}, inplace=True)

df_country_trend = df_country_trend.merge(df_total_per_year, on="year")
df_country_trend["percentage"] = df_country_trend["content_count"] / df_country_trend["total_content"]

all_years = df_country_trend["year"].unique()
all_countries = df_cleaned["country"].unique()
full_index = pd.MultiIndex.from_product([all_years, all_countries], names=["year", "country"])
df_country_trend = df_country_trend.set_index(["year", "country"]).reindex(full_index, fill_value=0).reset_index()

df_country_trend = df_country_trend[df_country_trend["percentage"] > 0]

def plot_country_production_growth():
    fig = px.choropleth(
        df_country_trend,
        locations="country",
        locationmode="country names",
        color="percentage",
        animation_frame="year",
        title="Netflix Content Production Growth by Country (2003-2021)",
        color_continuous_scale="YlOrRd",
        range_color=(0, 1),
        labels={"percentage": "Percentage of Netflix Titles"},
    )

    fig.update_layout(
        template="plotly_dark",
        geo=dict(
        showcoastlines=True,
        coastlinecolor="gray",
        showland=True,
        landcolor="grey",
        showframe=False,
        showcountries=True,
        countrycolor="white",
        ),
        margin=dict(l=0, r=0, t=90, b=50),
        font=dict(color="white"),
        title_text="Netflix Content Production Growth by Country (2003-2021)",
        title_x=0.18,
        title_font=dict(size=20, color="white"),
        coloraxis_colorbar=dict(
        title="Percentage of Netflix Titles",
        thicknessmode="pixels", thickness=25,
        yanchor="middle", y=0.4,
        )
    )

    return fig

plot_functions_order = [
    "plot_imdb_score_trend",
    "plot_high_quality_proportion",
    "plot_movie_vs_tv_production",
    "plot_movie_vs_tv_imdb",
    "plot_stock_vs_releases",
    "plot_stock_vs_quality",
    "plot_quality_vs_stock_volatility",
    "plot_impact_of_hit_shows_on_stock",
    "plot_hit_shows_vs_stock_long_term",
    "plot_genre_trends",
    "plot_international_trend",
    "plot_country_production_growth"
]
