# Physical-Property-Database-of-Molten-Salts
It is well known that experiments to measure the properties of molten salts have many difficulties in the implementation of the operation due to the limitations of the apparatus and the experimental environment. Motivated by the high accuracy of our trained Deep Potential model in predicting physical property data, we sought to build a database of molten salt physical properties, starting with binary carbonate melts. We have constructed a database of physical properties for the molten Li2CO3-Na2CO3, Li2CO3-K2CO3, and Na2CO3-K2CO3 systems using Python language, obtained from Deep Potential calculations. The data has been checked for accuracy both in this work and in other recent literature. 
Although this database is not yet complete and lacks some important features, it can already be used to query properties at specific compositions and temperatures. This is the beginning of our work to build a molten salt properties database. Given the relatively small dataset, we have used Ridge regression from the scikit-learn library to fit the data, but some issues remain for practical application - such as low training score for Na2CO3-K2CO3 and large generalization error. In the future, we will consider more advanced models such as deep neural networks using TensorFlow to improve data fitting. Extensibility of the database has been a priority in our scripting, allowing application to other molten salt systems with fewer modification.
Our team welcomes other researchers to join this effort.
