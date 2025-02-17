# Meta --------------------------------------------------------------------

## Title:         Econ/HLTH 470 Homework 2
## Author:        Sarina Tan
## Date Created:  2/15/2025
## Date Edited:   2/15/2025
## Description:   This file renders/runs Python code for the assignment


# Preliminaries -----------------------------------------------------------

# Importing the libraries
import pandas as pd
# Count the number of reports per hospital per year
report_counts = final_hcris_data.groupby(['year', 'provider_number']).size().reset_index(name='report_count')

# Filter hospitals that filed more than one report in the same year
multiple_reports = report_counts[report_counts['report_count'] > 1]

# Count the number of hospitals per year with multiple reports
hospitals_per_year = multiple_reports.groupby('year').size().reset_index(name='num_hospitals')

# Plot the result as a line graph
plt.figure(figsize=(10, 6))
plt.plot(hospitals_per_year['year'], hospitals_per_year['num_hospitals'], marker='o', linestyle='-', color='blue')
plt.title('Number of Hospitals Filing More Than One Report per Year')
plt.xlabel('Year')
plt.ylabel('Number of Hospitals')
plt.grid(True)
plt.show()