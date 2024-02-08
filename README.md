# PyDetecting
> It's a program written in Python that focuses on detecting payment fraud. To achieve this goal, it uses several key libraries:
>
> 1. [Pandas](https://pandas.pydata.org/docs/): This library is used to read and manipulate the data set. PyDetecting loads the data and performs cleaning and transformation operations using Pandas.
>
> 2. [NumPy](https://numpy.org/doc/stable/): PyDetecting uses NumPy to perform matrix operations. This is useful for efficient numerical calculations, such as feature normalization or matrix manipulation.
> 
> 3. [scikit-learn](https://scikit-learn.org/): The scikit-learn library is essential for building and evaluating the machine learning model. PyDetecting uses classification algorithms and evaluation techniques provided by scikit-learn.
>
> PyDetecting combines these tools to process data, build a fraud detection model, and evaluate its performance. Its goal is to improve financial security by identifying suspicious transactions and preventing payment fraud.
>
> [!PyDetecting](https://th.bing.com/th/id/OIG1.C9txntmWwUSbMadWtIY4?w=1024&h=1024&rs=1&pid=ImgDetMain)

## First Steps:
1. clone the repository:
```
git clone https://github.com/GabrielPy28/PyDetecting.git
```

2. Download the dataset from the following link: [dataset](https://www.kaggle.com/datasets/jainilcoder/online-payment-fraud-detection), copy and paste the CSV file inside the programe folder, and rename 'dataset.csv'

3. install requirements:
```
pip install -r requirements.txt
```

4. Run the program
```
python detecting.py
```

> [!NOTE]
> If everything is working correctly, the console printed: 
> ```
> -------------------- Printed Results --------------------
> ['Fraud']
> ```
