import dash
from dash import dcc, html  
import visualization  

app = dash.Dash(__name__, suppress_callback_exceptions=True)

chart_descriptions = {
    "plot_imdb_score_trend": ("Section 1: Content Quality Decline",
        "Does the overall IMDb rating trend show a decline in Netflix content quality? "
        "This graph illustrates the trend of average IMDb scores over time, revealing a significant drop after 2015."
    ),
    "plot_high_quality_proportion": ("",
        "Even if the overall scores decline, is the proportion of high-rated content (IMDb ≥ 7.5) stable? "
        "This graph demonstrates that high-rated content also shows a declining trend over time."
    ),
    "plot_movie_vs_tv_production": ("Section 2: Netflix Production Trends",
        "Is Netflix increasing content production? This graph shows trends in movie and TV show production over time, "
        "suggesting that Netflix has been focusing on quantity, possibly at the cost of quality."
    ),
    "plot_movie_vs_tv_imdb": ("",
        "Are Netflix movies and TV shows rated differently? This graph explores their IMDb score trends, revealing that "
        "TV shows generally receive higher ratings than movies."
    ),
    "plot_stock_vs_releases": ("Section 3: Stock Price vs. Content",
        "Does the quantity of content released influence Netflix’s stock price? "
        "This graph explores the relationship between content production and stock price growth."
    ),
    "plot_stock_vs_quality": ("",
        "Is there a direct link between high-quality content and Netflix stock prices? "
        "This graph suggests that Netflix’s success depends more on market expansion and subscription growth "
        "rather than pure content quality."
    ),
    "plot_quality_vs_stock_volatility": ("",
        "Over time, has content quality influenced Netflix's stock volatility? "
        "This graph compares early Netflix trends (pre-2010) vs. recent years (post-2015). "
        "We observe that in the early years, IMDb ratings had a stronger correlation with stock volatility."
    ),
    "plot_impact_of_hit_shows_on_stock": ("Section 4: Impact of Hit Shows",
        "Do blockbuster shows (IMDb ≥ 8.0, ≥ 100k votes) cause short-term stock price fluctuations? "
        "The data suggests that major hits do not immediately trigger significant stock price changes."
    ),
    "plot_hit_shows_vs_stock_long_term": ("",
        "How does the number of annual hit shows correlate with stock performance? "
        "The stock price follows a steady upward trend, seemingly independent of the number of hit shows."
    ),
    "plot_genre_trends": ("Section 5: Content & Global Expansion",
        "How has Netflix’s content strategy changed in terms of genre distribution? "
        "This graph reveals long-term shifts in genre popularity."
    ),
    "plot_international_trend": ("",
        "Is Netflix investing more in international content? This graph shows a sharp rise in global content after 2015, "
        "coinciding with Netflix’s expansion into over 190 countries in 2016."
    ),
    "plot_country_production_growth": ("",
        "Which countries contribute the most Netflix content? This world map highlights content production growth trends, "
        "showing a diversification beyond the U.S. to Europe and Asia."
    )
}

project_background = html.Div([
    html.H1("Netflix Data Analysis Dashboard", style={"textAlign": "center", "color": "white"}),

    html.P(
        "Many people claim that the quality of film and TV productions is declining. But is this true? "
        "And if so, why would entertainment companies allow this to happen? "
        "Does content quality have no impact on business performance?",
        style={"textAlign": "center", "color": "white", "fontSize": "18px", "padding": "0px 80px"}
    ),

    html.P("To explore these questions, we analyze three key Netflix datasets:", 
           style={"textAlign": "center", "color": "white", "fontSize": "18px"}),

    html.Ul([
        html.Li("Netflix content data (movies & TV shows)", style={"color": "white", "fontSize": "16px"}),
        html.Li("IMDb ratings (quality metric)", style={"color": "white", "fontSize": "16px"}),
        html.Li("Netflix stock prices (business impact)", style={"color": "white", "fontSize": "16px"}),
    ], style={"marginLeft": "38%", "marginRight": "38%"}),

    html.P(
        "By examining trends in content quality, production, and their relationship with stock performance, "
        "we aim to uncover meaningful insights.",
        style={"textAlign": "center", "color": "white", "fontSize": "18px", "padding": "0px 80px"}
    ),
], style={"padding": "20px", "backgroundColor": "black"})
\
layout_elements = [project_background]

previous_section = None

for plot_func_name in visualization.plot_functions_order:
    plot_func = getattr(visualization, plot_func_name, None)

    if callable(plot_func):
        section_title, description = chart_descriptions.get(plot_func_name, ("", ""))

        if section_title and section_title != previous_section:
            layout_elements.append(html.H2(section_title, style={"textAlign": "center", "color": "white", "marginTop": "60px"}))
            previous_section = section_title

        layout_elements.append(
            html.Div([
                html.H3(plot_func_name.replace("_", " ").title(), style={"textAlign": "center", "color": "white"}),
                html.P(description, style={"color": "white", "textAlign": "center", "marginBottom": "10px", "fontSize": "16px"}),
                dcc.Graph(figure=plot_func(), style={"textAlign": "center"}),  
            ],
            style={"width": "100%", "marginBottom": "50px"})
        )

layout_elements.append(
    html.Div([
        html.H2("Conclusion", style={"textAlign": "center", "color": "white", "marginTop": "60px"}),
        html.P(
            "Our findings reveal that while Netflix content quality has declined, stock price movements are more influenced by a combination of factors, "
            "including content volume, global expansion, the number of users, and various other elements, rather than direct quality metrics.",
            style={"textAlign": "center", "color": "white", "fontSize": "16px", "padding": "0px 60px"}
        ),
        html.P(
            "However, content quality may still play an indirect role by affecting subscriber engagement, brand loyalty, "
            "and user retention. As Netflix continues to scale, balancing quality with quantity may become crucial "
            "for long-term sustainability.",
            style={"textAlign": "center", "color": "white", "fontSize": "16px", "padding": "0px 60px"}
        )
    ])
)

app.layout = html.Div(
    layout_elements,
    style={"backgroundColor": "black", "padding": "20px"},
)

if __name__ == "__main__":
    app.run_server(debug=True)