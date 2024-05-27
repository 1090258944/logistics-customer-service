import pandas as pd
from sklearn.model_selection import train_test_split

def load_and_preprocess_data(filepath):
    data = pd.read_csv(filepath)
    # 数据清洗和预处理
    data = data.dropna()
    return train_test_split(data['text'], data['label'], test_size=0.2)
