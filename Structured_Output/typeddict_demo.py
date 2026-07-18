from typing import TypedDict

class ProductReview(TypedDict): 
    product_name : str
    rating : int 
    review : str


new_review : ProductReview = {
    "product_name" : "Wireless Headphones",
    "rating" : "5" , 
    "review" : "Excellent product"
}

print(new_review)