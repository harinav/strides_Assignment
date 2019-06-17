# strides_Assignment
Code files
1.Research And RoughWork.ipynb 
  Its is research analysis using different Datacleaning techniques and different Modeling technique.Its just RoughWork Analysis.
 
2.Final_Solution.ipynb
This is Final Submission of code And Analysis.


1.This is Binary Classification Problem.
Steps used for solving the problem.
  1.Preprocessing.
  2.Text to Sequence/Text  to Vector Convertion.
  3.Model Building.
  4.Metrics.

1.DataLoading and Preprocessing:-

 1.I Used filtering techniques like removing stop words removing by using regular expressions
  But if I do like this I drastically loosing my prediction accuracy its shown me that not only I am removing
  unimportant words but also loosing information.

 2.I Used Information Extraction Techniques like a Count Vectorizer,Tfidf,wordEmbeddings.Charecter lever information 
     Extraction Techniques.

 3.I used POS Tagging techique for grouping similar information.

 4.WordEmbeddings(By using word2vec and glove vectors I extracted Feature Matrix .npy file)
     For this I did another anysis in google collab for sentence embedding extraction.
     I used that Embedding in RNNs.
         5.By analyzer I extracted character level and word level information this are available with 
         Vectorizer(tfidf,count)
         
Binary Classification:--

1.First I Converted text data to vectors I applied Basics to Different types of Generative and Disciminative Models
like Naive Bays,Logistic Regression,SVM,LDA ect..
2.After That I Applied Different types of Ensembling Techniques Like Bagging(Random Forest),Boosting(XGBoost) with different levels like character level and word level.
3.At This stage I got some explosure on Modeling I tried with Deep learning Techniques like RNN(LSTM),CNN,Bi-LSTM,Ects.
I changed weights with Word Embeddings Also I expected LSTMS Might Outperform the other Models Because LSTMS are most suitable for Sequence prediction problems.
Sake of resource problem I didnot applied complete Deeplearning modeling got moderate results.

Final Results

From Above Analysis I came to the conclusion that XGboost with Charecter level Model Give good results.
From The Above results we can say Model Can Able to Differenced messages containt intent with 70% Confidence.

F1 Score is Also Showing that How much Our model Confident to predict Based on Precision and Recall.
F1 -Score 81%

Future Work:--

1.I tried to Apply Charecter level Word Embedding like FastText And ELMO Word Embedding Modeling Techniques But Sake of resource Problem I didnot Applied.
2.ELMO or FastText Model will definetlly Improve Classification Accuracy.
