# 连接MongoDB数据库
import pymongo

# 创建MongoDB客户端对象
client = pymongo.MongoClient("mongodb://localhost:27017/")

# 创建数据库对象
db = client["mydatabase"]

# 创建集合对象
col = db["customers"]

# 插入数据
data = {"name": "John", "address": "Highway 37"}
col.insert_one(data)

# 查询数据
result = col.find_one()
print(result)

# 更新数据
query = {"address": "Highway 37"}
new_values = {"$set": {"address": "Canyon 123"}}
col.update_one(query, new_values)

# 删除数据
query = {"address": "Canyon 123"}
col.delete_one(query)