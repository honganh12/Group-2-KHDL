import pandas as pd

# Đọc file Excel
df = pd.read_excel('Online Retail.xlsx')

# Kiểm tra kích thước của DataFrame
df.shape

# Chuyển đổi cột 'InvoiceDate' thành kiểu datetime nếu chưa phải
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Lọc dữ liệu từ tháng 2 đến tháng 6
data = df[(df['InvoiceDate'].dt.month >= 2) & (df['InvoiceDate'].dt.month <= 6) & (df['Quantity'] > 0)]

# Kiểm tra kích thước của dữ liệu sau khi lọc
data.shape

# Nhóm theo StockCode và tính tổng Quantity cho mỗi sản phẩm
top_products = data.groupby('StockCode')['Quantity'].sum().reset_index()

# Sắp xếp theo số lượng bán ra từ cao đến thấp
top_products = top_products.sort_values(by='Quantity', ascending=False)

# Lấy 10 sản phẩm bán chạy nhất
top_10_products = top_products.head(10)

# Hiển thị kết quả
print(top_10_products)


# Nhóm theo StockCode và tính tổng Quantity cho mỗi sản phẩm
top_products = data.groupby('StockCode').agg({'Quantity': 'sum', 'Description': 'first'}).reset_index()

# Sắp xếp theo số lượng bán ra từ cao đến thấp
top_products = top_products.sort_values(by='Quantity', ascending=False)

# Lấy 10 sản phẩm bán chạy nhất
top_10_products = top_products.head(10)

# Hiển thị kết quả
print(top_10_products)


