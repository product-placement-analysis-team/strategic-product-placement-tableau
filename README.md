# Strategic Product Placement Analysis: Unveiling Sales Impact with Tableau Visualization

## Project Overview

Product placement plays a crucial role in influencing customer purchasing behavior in retail environments. Strategic positioning of products can significantly affect sales volume, customer engagement, and overall business performance.

This project analyzes the impact of product positioning, pricing strategies, competitor pricing, promotions, and consumer demographics on sales performance using data visualization techniques.

The project leverages Tableau for interactive visual analytics and integrates the dashboard into a Flask web application for presentation and accessibility.

---

## Project Objective

The objective of this project is to analyze how product placement and related factors affect sales performance and to present actionable insights using interactive data visualization.

Key goals include:

* Understanding how product positioning impacts sales.
* Comparing product prices with competitor prices.
* Analyzing the relationship between foot traffic and sales volume.
* Evaluating the impact of promotions on product sales.
* Visualizing consumer demographics against product categories.

---

## Dataset

The dataset used in this project was obtained from Kaggle.

Dataset Name:
Impact of Product Positioning on Sales

The dataset contains variables such as:

* Product Category
* Product Price
* Competitor Price
* Sales Volume
* Promotion Status
* Consumer Demographics
* Foot Traffic
* Product Position

The dataset was cleaned and prepared before being used for visualization.

---

## Tools and Technologies Used

Python – Backend application
Flask – Web framework for dashboard integration
Tableau – Data visualization and dashboard creation
GitHub – Version control and team collaboration
Kaggle – Dataset source

---

## Project Workflow

### 1. Data Collection

The dataset was collected from Kaggle and verified for completeness and relevance to the project objectives.

### 2. Data Preparation

Initial preprocessing steps included:

* Checking for missing values
* Verifying data types
* Renaming fields for clarity
* Ensuring proper formatting for Tableau analysis

### 3. Data Visualization

Using Tableau, multiple visualizations were created to analyze relationships between different variables.

### 4. Dashboard Design

Interactive dashboards were created to allow users to explore insights through filters and visual comparisons.

### 5. Story Creation

A Tableau story was developed to present the analysis in a structured narrative format.

### 6. Web Integration

The Tableau dashboard was embedded into a Flask web application using an iframe to make the visualization accessible through a web interface.

---

## Visualizations Created

The following visualizations were implemented in the Tableau dashboard:

* Average Sales Volume by Product Category
* Average Sales Volume by Product Category on Sales
* Consumer Demographics vs Product Category
* Foot Traffic vs Sales Volume
* Competitor Price vs Product Price
* Promotion Impact on Price and Sales Volume
* Product Category vs Price
* Average Sales Volume by Product Category by Product Position

These visualizations help identify patterns, trends, and correlations within the dataset.

---

## Dashboard Features

* Interactive filters for better analysis
* Clear visual representation of data relationships
* Multiple charts comparing product placement strategies
* Storyboard explaining insights step-by-step

---

## Flask Application

The Tableau dashboard is embedded into a Flask web application.

The application structure includes:

flask_app/

* app.py
* templates/
* static/

The Flask app loads the Tableau dashboard using an embedded iframe.

---

## Key Insights

* Product positioning significantly impacts sales volume.
* Competitive pricing influences purchasing behavior.
* Promotions positively affect product sales.
* Higher foot traffic generally correlates with increased sales performance.
* Certain product categories perform better when placed in high visibility areas.

## Repository Structure

The project repository is organized as follows:

strategic-product-placement-tableau
│
├── data/
│   ├── cleaned/                # Cleaned dataset files
│   ├── cleaning/               # Data cleaning-related files/scripts
│   └── raw/                    # Original raw dataset
│
├── documentation/              # Project documentation
│
├── flask_app/                  # Flask web application files
│
├── performance_testing/        # Dashboard testing and performance reports
│   ├── .gitkeep
│   └── dashboard_performance_report.md.txt
│
├── presentation/               # Presentation materials
│
├── tableau/                    # Tableau packaged workbook
│   └── strategic_product_placement_dashboard1.twbx
│
├── .gitignore
├── README.md
└── test.txt

## Team Members and Roles

Anuj Gautam
Role: Documentation, Tableau Publishing, Flask Integration, Project Reporting

Aditya Chauhan
Role: Data Collection and Data Preparation

Ishaan Dubey
Role: Data Visualization and Calculated Fields in Tableau

Harshit
Role: Storyboard Creation and Data Insight Presentation

---

## Conclusion

This project demonstrates how data visualization tools can help organizations make better strategic decisions. By analyzing product placement and related factors, businesses can optimize their retail strategies and improve sales performance.

The integration of Tableau with Flask allows the dashboard to be presented in a web-based interface, making the insights accessible and interactive.

---

## Future Improvements

Possible improvements include:

* Adding more datasets for broader analysis
* Implementing predictive analytics models
* Enhancing the web interface with advanced frontend frameworks
* Deploying the application to a cloud platform

---

## Acknowledgement

We would like to thank our faculty and mentors for guiding us throughout the development of this project and helping us understand the importance of data visualization in business analytics.
