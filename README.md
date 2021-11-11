# Title


## Abstract

Social movements, as well as human rights movements, usually start or are resurrected after heavily mediatised traumatic events e.g: Black Lives Matter was founded in 2013 and was revived in 2020 after Floyd’s death. 
However, non-traumatic events can also act as catalysts for such movements e.g: Bombshell movie in 2019 opened a conversation about workplace sexual harassment and revived the #metoo movement which was originally founded in 2006. 

The goal of our project is to build a timeline of the #metoo movement to analyze the influence of different events (traumatic as well as non-traumatic events) on this movement throughout the years. 
This could be done by monitoring the number of quotes that include the word #metoo or other related words over time.
Next, we create two other timelines, one which contains traumatic events and another one for non-traumatic events. 
Finally, we can use these timelines to correlate the occurrence of (non-)traumatic events with sudden increases in quotes related to #metoo, a sudden increase in quotes could be related to a specific event. 


## Research questions

Our first goal is the identification of events that have a significant event on the amount of quotes related to a subject. 
Once this is done, given we find enough data we could train a model to predict the impact of certain non-traumatic events. 
Another question is how the timing of such events matters, e.g. what if we changed the timing of the event to be a few weeks later ?

## Proposed additional datasets
In addition of Quotebank dataset from which we'll extract "metoo quotes" (quotes related to metoo movement), we'll be using others datasets in our project.

### Dataset 1 : Metoo tweets
The tweets dataset is acquired from [Harvard Dataverse](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/2SRSKJ) which contains 32,071,469 *#metoo* tweets ranging from October 15, 2017 to March 31, 2020. The dataset only contains tweet IDs, thus, we applied for access to Twitter API in order to fetch tweets and their metadata from IDs. The dataset is distributed in 33 txt files *(each containing 1M tweet IDs)*.

### Dataset 2 : Dramatic Events 
The history of #metoo has been defined by waves of popularity in the public discourse. These were mostly caused by events that ignited strong feelings and heated discussions into the mainstream, posing a challenge to the status quo of powerful men used to havign their ways. In this context, we define traumatic events the ones directly related to the core issue of sexual harassment, the allegations by victims and direct consequences.
After several unsuccessfully tries using the wikidata platform, we decided to abandon this as a primary source of traumatic events as the criteria of inclusion " the wikidata item has a specific property" did not appear to be strong enough to base our analysis on. We then looked at the literature to check how these analyses were carried out in publiched research. In both Ghosh 2020 (https://journals.sagepub.com/doi/abs/10.1177/1940161220968081) and Kaufman 2021 (https://journals.sagepub.com/doi/abs/10.1177/0886260519868197), the considered events were seemingly picked from the news coverage of the studied period. We set off to do the same. In our final list of traumatic events we will therefore present a selection of allegations of sexual misconduct extracted from the previous mentionned papers, integrated with more updated lists such as https://www.vox.com/a/sexual-harassment-assault-allegations-list?.

### Dataset 3 : Non-Dramatic Events 


## Methods

### 1. Data extraction - cleaning / Timeline preparation
### 2. Study correlations between events and number of "metoo quotes" (quotes related to metoo movement)
### 3. Explore the differences between events with high/low impact on the movement. 

## Proposed Timeline

## Organization

## Questions for TAs
