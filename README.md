<div id="top">

<!-- HEADER STYLE: CLASSIC -->
<div align="center">


# UBER_NYC

<em>Transforming Urban Mobility with Data-Driven Insights</em>

<!-- BADGES -->
<img src="https://img.shields.io/github/last-commit/mmatthieu1290/Uber_NYC?style=flat&logo=git&logoColor=white&color=0080ff" alt="last-commit">
<img src="https://img.shields.io/github/languages/top/mmatthieu1290/Uber_NYC?style=flat&color=0080ff" alt="repo-top-language">
<img src="https://img.shields.io/github/languages/count/mmatthieu1290/Uber_NYC?style=flat&color=0080ff" alt="repo-language-count">

<em>Built with the tools and technologies:</em>

<img src="https://img.shields.io/badge/Markdown-000000.svg?style=flat&logo=Markdown&logoColor=white" alt="Markdown">
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">

</div>
<br>

---

## Table of Contents

- [Overview](#overview)
- [Description of databases](#Description-of-databases)
- [Methodology](#Methodology)
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Usage](#usage)
    - [Testing](#testing)

---

## Overview

Uber_NYC is a comprehensive data analysis and visualization tool designed to explore ride patterns in New York City’s Uber trip data. It leverages clustering techniques like KMeans to segment trips based on spatial and temporal features, providing valuable insights into urban mobility dynamics.

**Why Uber_NYC?**

This project helps developers analyze, visualize, and interpret NYC Uber trip data to inform operational strategies and optimize ride-sharing services. The core features include:

- 🎯 **🔍 Clustering Analysis:** Segments trips into regions based on location and time, revealing daily and hourly patterns.
- 🌆 **🗺️ Demand Hotspot Visualization:** Displays interactive heatmaps of ride demand across NYC, aiding quick insights.
- 📊 **Pattern Recognition:** Identifies spatial and temporal trends to support data-driven decision-making.
- 🧩 **Exploratory Data Analysis:** Facilitates in-depth analysis of trip distributions and customer behavior.
- ⚙️ **Interactivity & Visualization:** Enhances stakeholder engagement with dynamic, accessible visual tools.

**Streamlit Dashboard:** https://mmatthieu1290-uber-nyc-dashboard-uber-nyc-l0xrkk.streamlit.app/

---
## Description of databases

- This database provides records of 4,534,327 Uber trips that took place in 2014.
- The variables considered are Date/Time, latitude, and longitude. Trips are referenced by day of the week and by 3-hour time slots.

---
## Methodology

- For each day of the week and each time slot, we construct 4 clusters thanks to KMeans and indicate them in a map of New-York city.

---

## Getting Started

### Prerequisites

This project requires the following dependencies:

- **Programming Language:** JupyterNotebook

### Installation

Build Uber_NYC from the source and install dependencies:

1. **Clone the repository:**

    ```sh
    ❯ git clone https://github.com/mmatthieu1290/Uber_NYC
    ```

2. **Navigate to the project directory:**

    ```sh
    ❯ cd Uber_NYC
    ```

3. **Install the dependencies:**

echo 'INSERT-INSTALL-COMMAND-HERE'

### Usage

Run the project with:

echo 'INSERT-RUN-COMMAND-HERE'

### Testing

Uber_nyc uses the {__test_framework__} test framework. Run the test suite with:

echo 'INSERT-TEST-COMMAND-HERE'

---

<div align="left"><a href="#top">⬆ Return</a></div>

---
