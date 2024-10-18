# Activity 21: Introduction of Nested List of Dictionaries Data Structure

products = [
{
"id": 1,
"name": "IPHONE 13",
"category": "Electronics",
"price" : 2500,
"colors" : ["gray", "black"],
"size": ["small", "medium", "large"],
"stock": [{
"gray-small" : 25,
"gray-medium" : 30,
"gray-large" : 34
},
{
"black-small": 23,
"black-medium": 23,
"black-large": 25
}],
},

{
"id": 2,
"name": "IPHONE 15",
"category":"Electronics",
"price" : 2500,
"colors" : ["gray", "black"],
"size": ["small", "medium", "large"],
"stock": [{
"gray-small" : 25,
"gray-medium" : 30,
"gray-large" : 34
},
{
"black-small": 23,
"black-medium": 23,
"black-large": 25
}],
},

{
"id": 3,
"name": "IPHONE 16",
"category":"Electronics",
"price" : 2500,
"colors" : ["gray", "black"],
"size": ["small", "medium", "large"],
"stock": [{
"gray-small" : 25,
"gray-medium" : 30,
"gray-large" : 34
},
{
"black-small": 23,
"black-medium": 23,
"black-large": 25
}],
}
]
print(products)

print()
products[2]["name"] = "IPHONE 16 PROMAX"
print(products)

# TODO ACCESS STOCK OF products[2]
print()
print("product 3 stock: ")
print(products[2]["stock"])

# TODO ACCESS INDEX 2 STOCK OF products[2]
print()
print("product 3 index 2 stock: ")
print(products[2]["stock"][1])

# TODO CHANGE black small quantity - products[2]
print()
products[2]["stock"][1]["black-small"] = 20
print("product 3 black-small stock new quantity: ")
print(products[2]["stock"][1]["black-small"])