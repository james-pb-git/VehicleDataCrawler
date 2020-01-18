# VehicleDataCrawler

## One line description
**Crawlers to fetch structured vehicle data on a regular basis.**

## Background
In this project, I will set up a bunch of crawlers to fetch well-structured data points from vehicle websites on a regular (e.g. daily) basis. The data points should include common specifications for most Year + Make + Model combinations.

This is one of my side projects in 2020, and it is designed to collect data and fill it into relational database, which will enable [another Java Application](https://github.com/sarachen19/JavaSwing_project) to perform more complicated data analysis and visualization tasks.

I started this project as requested by [Sara](https://github.com/sarachen19), but may extend the features in the future for a wider range of use cases (or may not :-p).

## Expected features and roadmap
- Data Source
  - Single automobile websites
  - Multiple automobile websites
  - Automatic & intelligent matching between different data formats
- Data Fetching
  - Fetch data from website
  - Parse data to required format (including year, make, model, engine type etc.)
  - Inlucde detailed specifications in response.
  - Enable crawling images.
  - Data cleaning (optional, as the Java App shouldn't expect data to be clean)
- Fetch jobs
  - One time fetching job
  - Routine jobs on a regular basis
  - Introduce concurrent programming to improve efficiency
- Data storage
  - Save to single local file (e.g. csv file)
  - Store increment data (de-duplication, etc.)
  - Save to database

## Solution
After some research, I've decided to use [Scarpy](https://scrapy.org/), which is an open source Python framework to crawl websites and parse structured data. Its [architecture](https://doc.scrapy.org/en/latest/_images/scrapy_architecture_02.png) enables requests to be scheduled and processed asynchronously. Once onboarding, developers only need to implement data parsing logics, configuration and things like that.

## Milestones

|SN|Date|Description|Comment|
|--|--|--|--|
|1|Jan 18, 2020|Initialize repository, start designing, onboarding Scrapy|

## References
- Scrapy document. https://doc.scrapy.org/en/latest/
- Crawler example (Lang: Chinese) https://github.com/LittleLory/codePool/tree/master/python/autohome_spider

