# strides_Assignment
1.This is Binary Classification Problem.
2.Steps used for solving the problem.
  1.Preprocessing.
  2.Text to Sequence Convertion.
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


Final Results

From Above Analysis I came to the conclusion that XGboost with Charecter level Model Give good results.

From The Above results we can say Model Can Able to Differenced messages containt intent with 70% Confidence.

F1 Score is Also Showing that How much Our model Confident to predict Based on Precision and Recall.
F1 -Score 81%
