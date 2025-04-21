---
title: Dracula
version: 1.0.0
theme: dracula
footer: Nhóm 2
header: Python
paginate: true
marp: true
size: 4K
---

# Khoa Học Dữ Liệu

Xây dựng hệ thống gợi ý sản phẩm.

Phân tích hành vi mua hàng và xây dựng hệ thống gợi ý sản phẩm cá nhân hóa

*Nhóm 2*

<style scoped>
h1 {
    padding-top: 1.5em;
}
</style>

![bg right](https://acquisitioninternational.digital/wp-content/uploads/2022/12/Data-Science.jpg)

---

# Load các thư viện cần thiết:

```python
import pandas as pd
from IPython.display import display
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics.pairwise import cosine_similarity
import networkx as nx
```

<style scoped>
table {
    margin-left: auto;
    margin-right: auto;
}
</style>

---

# Import Dataset để phân tích

```python
# Import data Online_Retail
df = pd.read_excel("C:\\Users\\Rog\\Downloads\\Online_Retail.xlsx")
# Chuyển đổi InvoiceDate sang dạng Datetime    
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
# Trích cột tháng từ InvoiceDate và lưu vào cột mới có tên Month   
df['Month'] = df['InvoiceDate'].dt.month
# Lọc dữ liệu để chỉ lấy các giao dịch từ tháng 2 tới tháng 6          
data = df[(df['Month'] >= 2) & (df['Month'] <= 6)]
# Tính số tiền thu được từ mỗi giao dịch    
data["OrderValue"] = data["UnitPrice"] * data["Quantity"]     
display(data)    
```

<style scoped>
h1 {
    padding-bottom: 1.5em;
}
</style>

---

# Bats - About

- Small

- Fast

- Mammals

- Scientific name: Chiroptera

![bg right](./img/igam-ogam-unsplash.jpg)


---

# Bats - Implementation

```python
class Bat:
    def __init__(name:str, age:int):
        self.__name = name
        self.__age = age
    @property
    def name(self):
        return self.__name
    @property
    def age(self):
        return self.__age
    @property
    def speed(self):
        return 10 - self.age
```



