# NJ Teachers Salaries Scrapy Script

## Summary
This script was built to scrape teacher salaries, experience, and job information from the [Asbury Park Press' Data Universe](http://php.app.com/agent/educationstaff/search) page. The data is currently hosted on a (data.world repository)[https://data.world/sheilnaik/nj-teacher-salaries-2016].

## Description
The Scrapy script visits each page of search results and gathers a list of teacher URLs on that page. It then visits each individual teacher's page and scrapes all relevant data. Data points were identified using CSS selectors and were not altered aside from regex parsing for salary data.

