# Netflix Movies & TV Shows Data Analysis

## Project Overview
This project analyzes the **Netflix Movies & TV Shows dataset** from Kaggle.  
The goal is to perform **Exploratory Data Analysis (EDA)** and **SQL-based queries** to uncover insights about Netflix's content catalog.

**Objectives:**
- Explore and clean the dataset.
- Generate visual insights using Python libraries.
- Run SQL queries for data analysis.
- Identify trends in content type, release year, country, genres, directors, actors, and ratings.

---

## Dataset
- **Source:** [Netflix Movies & TV Shows Dataset on Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows)
- **Format:** CSV
- **Columns:**  
  `show_id`, `type`, `title`, `director`, `cast`, `country`, `date_added`, `release_year`, `rating`, `duration`, `listed_in`, `description`
- **Rows:** 8807
- **Columns:** 12

---

## Libraries Used
- **Data Handling:** `pandas`, `numpy`
- **Visualization:** `matplotlib`, `seaborn`
- **SQL Queries:** `sqlite3`, `SQLAlchemy`
- **Others:** `warnings` (to ignore warnings)

---

## Data Cleaning & Preprocessing
- Handled missing values by filling `Unknown` for `director`, `cast`, and `country`.
- Converted `date_added` to datetime and extracted `year_added` and `month_added`.
- Removed duplicate rows.
- Standardized categorical columns for consistency.

---

## Exploratory Data Analysis (EDA)

### Movies vs TV Shows
- Movies: **6131**  
- TV Shows: **2676**  
**Insight:** Movies dominate Netflix catalog, but TV Shows are steadily growing.

### Top Countries by Content
| Country         | Count |
|-----------------|-------|
| United States   | 2818  |
| India           | 972   |
| United Kingdom  | 419   |
| Japan           | 245   |
| South Korea     | 199   |

### Releases Over Time
- Sharp increase in content post-2015.
- Peak around 2018–2020.
- Slight decline after 2020 due to pandemic delays.

### Top Directors
| Director           | Titles |
|-------------------|--------|
| Rajiv Chilaka      | 22     |
| Jan Suter          | 21     |
| Raúl Campos        | 19     |
| Suhas Kadav        | 16     |
| Marcus Raboy       | 16     |
| Jay Karas          | 15     |
| Cathy Garcia-Molina| 13     |
| Jay Chapman        | 12     |
| Youssef Chahine    | 12     |
| Martin Scorsese    | 12     |

### Top Actors
| Actor              | Titles |
|------------------|--------|
| Anupam Kher       | 43     |
| Shah Rukh Khan    | 35     |
| Julie Tejwani     | 33     |
| Naseeruddin Shah  | 32     |
| Takahiro Sakurai  | 32     |
| Rupa Bhimani      | 31     |
| Akshay Kumar      | 30     |
| Om Puri           | 30     |
| Yuki Kaji         | 29     |
| Paresh Rawal      | 28     |

### Top Genres
| Genre                   | Count |
|-------------------------|-------|
| International Movies     | 2752  |
| Dramas                   | 2427  |
| Comedies                 | 1674  |
| International TV Shows   | 1351  |
| Documentaries            | 869   |
| Action & Adventure       | 859   |
| TV Dramas                | 763   |
| Independent Movies       | 756   |
| Children & Family Movies | 641   |
| Romantic Movies          | 616   |

### Content Ratings
- Most frequent rating: `TV-MA`
- Other common ratings: `TV-14`, `PG`, `R`, `PG-13`  
**Insight:** Majority of content targets mature audiences.

---

## SQL Queries Examples

### 1. Top 5 Countries by Content
```sql
SELECT country, COUNT(*) AS count
FROM netflix
WHERE country IS NOT NULL AND country != 'Unknown'
GROUP BY country
ORDER BY count DESC
LIMIT 5;
```
### 2. Movies Released in 2020
```sql
SELECT title FROM netflix
WHERE release_year=2020 AND type="Movie";
```
### 3. Shows by Director "Rajiv Chilaka"
```sql
SELECT title FROM netflix
WHERE director LIKE '%Rajiv Chilaka%';
```
### 4. Most Common Content Ratings
```sql
SELECT rating, COUNT(*) AS count
FROM netflix
WHERE rating IS NOT NULL AND rating != 'Unknown'
GROUP BY rating
ORDER BY count DESC
LIMIT 5;
```
---

## Data Visualizations
- **Movies vs TV Shows Count** → Bar Plot  
- **Missing Values Heatmap**  
- **Releases Per Year** → Line Chart  
- **Content Ratings Distribution** → Histogram  
- **Top Countries & Genres** → Bar Plots  
- **Top Directors & Actors** → Bar Plots  

---

## Key Insights & Conclusion
- Netflix catalog is **movie-heavy**, but TV Shows are growing steadily.  
- The **US and India** dominate content production.  
- Popular genres reflect **diverse international content**.  
- Majority of content targets **mature audiences**, aligning with global demand trends.  
- Post-2015 growth trend shows Netflix's **expansion and global outreach**.  

---

## Usage
1. Clone the repository.  
2. Install required libraries:
```bash
pip install pandas numpy matplotlib seaborn sqlite3
```
3. Load the dataset and run the analysis scripts.
4. Explore visualizations and SQL queries for insights.

---

