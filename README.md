# VehicleDataCrawler

## One line description
**Crawlers to fetch structured vehicle data on a regular basis.**

## Background
In this project, we will set up a bunch of crawlers to fetch well-structured data points from vehicle websites on a regular (e.g. daily) basis. The data points should include common specifications for most Year + Make + Model combinations.

This is one of my side projects in 2020, and it is designed to collect data and fill it into relational database, which will enable another Java Application to perform more complicated data analysis and visualization tasks.

## Expected features and roadmap
- Data Source
  - Single automobile websites
  - Multiple automobile websites
  - Automatic & intelligent matching between different data formats
- Data Fetching
  - Fetch data from website
  - Parse data to required format
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
TBD

## Milestones

|SN|Date|Description|Comment|
|--|--|--|--|
|1|Jan 18, 2020|Initialize repository, start designing|
