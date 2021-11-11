
# Title : Movement of catalysts.


## Abstract

Social and human rights movements, usually gain popularity following traumatic events e.g: Black Lives Matter was founded in 2013 but gained popularity in 2020 after Floyd Mayweather’s death. However, non-traumatic events can also act as catalysts for such movements e.g.: Bombshell movie in 2019 opened a conversation about workplace sexual harassment and revived the #metoo movement (originally founded in 2006).

Our goal is to build a timeline of the #metoo movement to analyze the influence of (non-)traumatic events on this movement throughout the years. Our first step consists of monitoring the number of quotes that include the word #metoo or other related words over time. Next, we create two more timelines, one for traumatic events and another one for non-traumatic events. Finally, we use these timelines to correlate the occurrence of (non-)traumatic events with sudden increases in quotes related to #metoo.

## Research questions

Our first goal is the identification of events that have a significant event on the number of quotes related to a subject. 
Once this is done, given we find enough data we could train a model to predict the impact of certain non-traumatic events. 
Another question is how the timing of such events matters, e.g. what if we changed the timing of the event to be a few weeks later?

## Proposed additional datasets
In addition to Quotebank dataset from which we'll extract "metoo quotes" (quotes related to metoo movement), we'll be using others datasets in our project.

### Dataset 1 : Metoo tweets
The tweets dataset is acquired from [Harvard Dataverse](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/2SRSKJ) which contains 32,071,469 *#metoo* tweets ranging from October 15 2017 to March 31 2020. The dataset only contains tweet IDs, thus, we applied for access to Twitter API in order to fetch tweets and their metadata from IDs. The dataset is distributed in 33 txt files *(each containing 1M tweet IDs)*.

### Dataset 2 : Dramatic Events 
The history of #metoo has been defined by waves of popularity in the public discourse. These were mostly caused by events that ignited strong feelings and heated discussions into the mainstream, posing a challenge to the status quo of powerful men used to having their ways. In this context, we define traumatic events as the ones directly related to the core issue of sexual harassment, the allegations by victims and direct consequences.
After several unsuccessful tries using the wikidata platform, we decided to abandon this as a primary source of traumatic events as the criteria of inclusion " the wikidata item has a specific property" did not appear to be strong enough to base our analysis on. We then looked at the literature to check how these analyses were carried out in published research. In both Ghosh 2020 (https://journals.sagepub.com/doi/abs/10.1177/1940161220968081) and Kaufman 2021 (https://journals.sagepub.com/doi/abs/10.1177/0886260519868197), the considered events were seemingly picked from the news coverage of the studied period. We set off to do the same. In our final list of traumatic events, we will therefore present a selection of allegations of sexual misconduct extracted from the previously mentioned papers, integrated with more updated lists such as https://www.vox.com/a/sexual-harassment-assault-allegations-list?.

### Dataset 3 : Non-Dramatic Events 


## Methods
### 1. Data extraction – Quotes of interest
In the first part, we'll have to preprocess the data, going through the extraction of quotes involved with the #metoo movement from Quotebank[2015-2020]. 
This has been done firstly by manual quote extraction based on the presence of special keywords identified based on the data. The keyword list extraction has been generated thanks to a  wordcloud based on the quotes containing #metoo.
We finally end up with a dataset containing around 6 million quotes involved with the #metoo movement.
We are have also parsed URLs for this purpose, this method would help filter quotes based on the article title which would be extracted from the urls. First, we will extract the hostnames of the URLs. Then, pick the top 20 hostnames in terms of occurrences and extract their titles to hand-pick the relevant titles.
Finally, we are investigating NLP-based method because the quotes extracted so far could still not be related to *Sexual Harassment*. Hence, in this step, we will explore different NLP-based methods to properly perform *Topic Modeling* and only save the quotes related to our project.

### 2. Timeline realisation
We aim at creating a certain timeline displaying the number of #metoo quotes released by day. This will be implemented from Quotebank extracted quotes, tweets, while displaying the dramatic events on the same timeline. 

![Nice_plot_2](https://user-images.githubusercontent.com/65892642/141377664-07064faf-c5ee-4d66-82f6-ffee229ad693.png)





### 3. Statistical Study between events and number of "#metoo quotes" (quotes related to metoo movement)
DO THE SAME FOR DROMATIC AND NON-DRAMATIC
Control : mean of #quotes/#tweets before a certain event 
Event : mean #quotes/#tweets on period after the event
Statistical analysis over this (t-test)

## Proposed Timeline
Our planning for the coming weeks consists of the following steps: 
 - 15-21 November: Finish polishing the Datasets as well as selecting the appropriate statistical test to determine on which dates there is a significant increase in the number of quotes and tweets. 
 -  21-28 November: Start working on the website and perform the actual statistical analysis.
 -  29 November-5 December: Interpret results from statistical analysis and finish the website. 
 -  6-12 December: Fix final problems and (given enough time) perform alternative analysis (see end of **research questions**).
 -  13-17 December:  Polish website and finish all other deliverables.

![haha](https://user-images.githubusercontent.com/65892642/141377506-8b781df9-45d8-4e42-b769-3aba5782d33e.png)




## Organization
We will first all help to complete the dataset of non-traumatic events as this has been the most difficult part of milestone 2. 
- Gasser: polishing datasets and interpreting results from the statistical tests.
- William: Focus on making the website and results visualisation.
- Mathias: Help with website and the main person in charge of completing the dataset for non-traumatic events.
- Milo: Determining optimal statistical test and actually performing statistical analysis.

## Questions for Tas


