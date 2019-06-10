# BigData_FinalProject
Building a near real-time Twitter streaming analytical pipeline with AWS. Amazon managed services (Amazon Kinesis Firehose, AWS Lambda (Python function), Amazon S3, Amazon Elasticsearch Service) integrated to complete the process.  Amazon Kinesis Firehose is used to capture, transform, and load Twitter streaming data into Amazon S3 automatically. Inserting AWS Lambda function with Python into Kinesis Firehose and Amazon S3 to specify the data. For the analysis part, Amazon Elasticsearch Service is being used and Spark to proceed the network analysis. 

Implementation:
Infrastructure:
The Amazon Web Service suite was used to complete the majority of the work on this project. Data was stored in the S3 cloud and mapreduce code was implemented using EMR. Python was the primary programming language and interfacing with the twitter API occurred using Python. AWS offers data streaming capabilities which will be critical to implementing the monitoring component of this project in the future, 

Network Definition:
The super users twitter users include: @womenintech, @WITwomen, @windows, @microsoftwomen, @sherylsandberg, @ericajoy, @codefirstgirls. The users following at least 3 super users above can be considered as one node in the network in this study. Two steps should be taken in this phase: 1. Pulling down the user lists of super users with Twitter API; 2. Finding out the users following more than 3 super users with applying Map-Reduce on AWS.

Doing a general analysis of twitter users’ trends, we created a list of twitter users, mainly, account holders who have are an ideal example of “Women in Technology”, are active twitter user and have a decent amount of followers. The twitter API was queried and userids for each super users followers were collected as using Python code below. This was implemented using python libraries tweepy and an API pipeline. A csv file stored the list of followers for each “superuser”. 


Given the large magnitude of followers for each super user, the aggregation of users was implemented using a map-reduce algorithm in amazon EMR. The mapper and the reducing as written in python are provided below.

One of the assumptions built into this analysis is that users who follow the super users will be interested in WIT. As can be seen in the mapper code, only users following at least 3 super users were considered in this analysis. This threshold was established boost the likelihood that the previously mentioned assumption would hold true. 

Language Analysis:

TF-IDF is a commonly used natural language processing method and information retrieval method designed to analyze the language contained within all documents in a corpus in vector space. For our purposes, a document is a tweet and the corpus is all the tweets collected as part of phase I. The tf-idf weighting scheme assign to term t a weight in document d given by the following formula:

tf-idft,d    =log(1+tft,d)*log(N/dft ) 

where:
	tft,d= the frequency of term t in document d
	N= the number of documents
Dft =  the number of documents containing the term
	 
The benefit to using this vectorization approach is that terms with a high collection frequency  are given a lower importance score while terms with a high document frequency but a low collection frequency are weighted highly.  This approach allows for the balance measuring importance as a function of the frequency with which a word is used versus the rarity of a word. The assumption being that high frequency rare words and treated with similar importance to high frequency highly used terms. 

Let D be the collection of documents in the corpus. Let T be the collection of terms (unique words) in our collection D.

The term frequency (tf) for a given time ti within a particular document dj is defined as the number of occurrences of that term in the dj th document, which is equal to ni,j: the number of occurrences of the term ti in the document dj .
						
Tf i,j =ni,j
						
The term frequency is often normalized to prevent a bias towards larger documents, as shown below:
						
tfi,j= ni,j ∑k nk,j
						
where ni,j is the number of occurrences of the term ti in the document dj. Note that we are using the total number of terms for normalization. Instead we can use the maximum as well. 

The inverse document frequency (idf) is obtained by dividing the total number of documents by the number of documents containing the term ti , and then taking the logarithm of that quotient:
						
idfi =log |D| |{d:ti ∈d}|
						
with
						
|D|: total number of documents in the collection
|{d : ti ∈ d}|: number of documents where the term ti appears. To avoid divide-by-zero, we can use 1 + |{d : ti ∈ d }|.

For a given corpus D, then the tf-idf is then defined as:
(tf-idf )i,j = tf i,j ×idfi

A high weight in tf-idf is obtained by a high term frequency and a low document frequency of the term in the collection. For common terms, the ratio in idf approaches 1, bringing the logarithm closer to 0. 

We need to compute:
Given a corpus of text, calculate tf-idf for every document and every term

Need to calculate, over the corpus, the following:
Number of terms
Number of unique terms
Number of documents
Number of occurrences of every time in every document and
Number of documents containing each term

IMPLEMENTATION:

To implement tf-idf using MapReduce we will divide it into 2 steps. In the first step we are going to count the documents and in the next we will count the terms in each document and then calculate the tf-idf as with both we have enough information to do so. So the general JobConfig consists of two jobs countTotalDocuments and calculateTfIdf.

From the input the tf-idf for terms in title and text will be calculated and written into a text file. 

STEP 1: To count the documents for our calculation we used Hadoop Counters and read the result from our job runner. We only need a map phase and deactivate reducers.



STEP 2: TF-IDF with Hadoop secondary sorting
 The next step is to calculate the tf-idf score for each term in a document. The overall idea of using secondary sorting for this is to have the values in the reduce phase grouped and sorted by the document id and the term itself. Like this:

doc1:a
doc1:a
doc1:b
doc1:c
doc2:a
doc2:a
doc2:b

We have to make sure that each word gets partitioned to the same reducer and at the reducer we have to assure that the terms are sorted and grouped by the document id. We had to define our own key class NgramFreqKey.class also created our own NgramFreq model. The key and model are later being used by the partitioner and group comparator at the reducer.

In cases where we need to control the way Hadoop partitions and sorts at ‘reduce’ level it offers the possibility of using a custom partitioning and group comparator. We are going to use this in our last step to calculate tf-idf.

Our partitioner will make sure that we partition by the term itself only and not by the document ID contained in the key. By this we achieve a fairly good distribution and the possibility to count the occurrence of a term at the reducer.


P.S. Refer the python scripts

