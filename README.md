# Netflix-Personalisation

Goal: Build a complete end to end personalisation tool that an individual can link their Netflix account to learn more about their content consumption.

Learning Outcomes: 
* Data mining
* Backend - Front End Development
* Machine Learning / Analytics


Summary:

All steps will be documented to allow for any new users to learn with me as I build a product end to end. The goal of the project is to combine my fascianation in the story telling ability of data and the world of software development.

## Goals
1.  Scrap data from multiple sources creating a data lake 
2.  Build an initial analytics profile 
3.  Build an interface for users to upload/connect their Netflix profile


## 1. Data Scrapping
Sources of data
* User's Generated Netflix Data
* Netflix Australia 
* IMDB 
* Wikipedia
* Rotten Tomato 

The overall objective is so users can attach their Netflix Data consumption 

#### User's Generated Netflix Data
Unfortunately Netflix has taken down their public api - hence we're unable to easily obtain users data without using scraping tools such as Selenium. As it stands - for now though as a proof of concept we will have users input their own csv/data file. Netflix allows an option for users to download their viewing history in the following format:

Title | Date
--- | --- 
The Good Place: Season 3: Janet(s) | 28/07/2020 
The Good Place: Season 3: The Worst Possible Use of Free Will | 28/07/2020
The Good Place: Season 3: A Fractured Inheritance | 27/07/2020
The Good Place: Season 3: The Ballad of Donkey Doug | 26/07/2020
The Good Place: Season 3: Jeremy Bearimy | 26/07/2020
The Good Place: Season 3: The Snowplow | 26/07/2020

(Yes its a real example was rewatching the good place). As you can see there isn't as much granuality/data points.

There is an additional option to download all the data collected on my account however this is a requested data retrieval and will take up to 30 days for processing.


## Netflix Australia 
#### Goal:
Extract all the netflix titles for their movies/tv shows - otherwise we can't suggest movies that isn't within their listing.

#### Process:
Once agin with the removal of their API  - we have to use an unofficial api or build data scraping tool using Selenium.

The general concept of the approach was to:
1. Navigate past the authentication page
2. Go to https://www.netflix.com/browse/genre/34399?so=az
3. Scrape the current page view
4. Utilise the scroll function to discover new titles
5. Iterate Steps 3,4 until there's no more new titles

However as I discovered the - their a-z listing page isn't an infinite scroll page. From A-Z the titles for movies caps at "It's Complicated". The 2009 title featuring Meryl Streep and Alec Baldwin. A definitely classic within the romcom genre - however unfotunately it has complicated things..

Performing the same process on the link https://www.netflix.com/browse/genre/34399?so=za, I was hoping the titles would actually meet at a common point however this was not the case.



















