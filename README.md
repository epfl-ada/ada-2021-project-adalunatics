
# Title : Movement's Catalysts.


## Abstract

<div style="text-align: justify">Social and human rights movements usually gain popularity following traumatic events e.g: #BlackLivesMatter was founded in 2013 but gained popularity in 2020 after Floyd’s death. However, non-traumatic events can also act as catalysts for such movements e.g.: Bombshell movie in 2019 opened a conversation about sexual harassment and revived the #metoo movement (originally founded in 2006).</div>

<div style="text-align: justify">Our goal is to build a timeline of the #metoo movement to analyze the influence of (non-)traumatic events on this movement throughout the years, using the Quotebank dataset and twitter dataset as a proxy for measuring impact. This will be implemented by extracting quotes/tweets relevant to #metoo movement over time. Then, construct two timelines, one for traumatic events and another one for non-traumatic events. Finally, we use these timelines to apply statistical/inference analyses to study the occurrence of (non-)traumatic events with changes in quotes/tweets related to #metoo.</div>

## Research questions

 1. Would non-traumatic events cause similar impact as the traumatic ones, in terms of raising a discussion?
 2. Is there a gender bias when comparing speakers of quotes during traumatic and non-traumatic events? (e.g: Men would respond more to traumatic but less for non-traumatic ones)
 3. How the timing of such events matters, e.g. what if we changed the timing of the event to be a few months later?
 4. What would be the estimated impact of a non-traumatic event giving features about the event? (*OBSTACLE: Causality*)

## Proposed additional datasets
In addition to Quotebank dataset from which we'll extract "metoo quotes" (quotes related to metoo movement), we'll be using others datasets in our project.

### Dataset 1 : Metoo tweets
The tweets dataset is acquired from [Harvard Dataverse](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/2SRSKJ) which contains 32,071,469 *#metoo* tweets ranging from October 15 2017 to March 31 2020. The dataset only contains tweet IDs, thus, we applied for access to Twitter API in order to fetch tweets and their metadata from IDs. The dataset is distributed in 33 txt files *(each containing 1M tweet IDs)*.

### Dataset 2 : Traumatic Events 
The history of #metoo has been defined by waves of popularity in the public discourse. These were mostly caused by events that ignited strong feelings and heated discussions into the mainstream, posing a challenge to the status quo of powerful men used to having their ways. In this context, we define traumatic events as the ones directly related to the core issue of sexual harassment, the allegations by victims and direct consequences.
After several unsuccessful tries using the wikidata platform, we decided to abandon this as a primary source of traumatic events as the criteria of inclusion " the wikidata item has a specific property" did not appear to be strong enough to base our analysis on. We then looked at the literature to check how these analyses were carried out in published research. In both [Ghosh 2020](https://journals.sagepub.com/doi/abs/10.1177/1940161220968081) and [Kaufman 2021](https://journals.sagepub.com/doi/abs/10.1177/0886260519868197), the considered events were seemingly picked from the news coverage of the studied period. We set off to do the same. In our final list of traumatic events, we will therefore present a selection of allegations of sexual misconduct extracted from the previously mentioned papers, integrated with more updated lists such as [List](https://www.vox.com/a/sexual-harassment-assault-allegations-list?).

### Dataset 3 : Non-Traumatic Events
This dataset aims to cense all events which are events not related to the core issue of sexual harassment and its direct consequences. After unsuccessful trials to find datasets providing such events, we decided to manually build our own dataset based on articles/blogs such as the [MeToo info page](metoomvmt.org) relating the importance of certain events (movie release/publications/demonstrations, and others..) related to MeToo from 2015-2020.

## Methods
### 1. Data extraction – Quotes of interest
The phase includes extracting the needed quotes from the original datasets through the use of three methods:
 1. Manual Extraction/WordCloud
 2. URL Parsing
 3. NLP-based Methods
All the details and some results concerning each method are illustrated in *notebook.ipynb*.

### 2. Timeline realisation
We aim at creating a certain timeline displaying the amount of #metoo quotes released by day. This will be implemented from Quotebank extracted quotes, tweets, while displaying the dramatic events on the same timeline. A scheme of the expected timeline shown below.

![Nice_plot_2](https://user-images.githubusercontent.com/65892642/141377664-07064faf-c5ee-4d66-82f6-ffee229ad693.png)

### 3. Statistical Analysis between events and number of "#metoo quotes" (quotes related to metoo movement)
<div style="text-align: justify">The measurement of the impact of all considered events will be carried out with the methods described in the *notebook.ipynb*. We plan to measure the before-after difference in coverage related to each event, exploit the peaks in the derivative associated with surges in media interest, and check that our events provoke a lasting change in the time series through *structural-breaks-analysis*.
Afterwards, we will analyze the distributions and compare the impacts of traumatic vs non traumatic events.</div>

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

## Questions for TAs
1.	Alternatives to quantifying impact of events on the timeline besides the ones mentioned in the notebook. 
2.	Ideas for extracting non-traumatic events. 

