# MiDulceHogar
API

Setup
-----
The application works in Python 3.7.2 <br/>
You can install the dependencies using pip under clone repository:

	$ pip install -r requirements.txt
  
  
Run
-----
Type on project root:

	$ python manage.py runserver
  
* By default the app runs in:
    * http://localhost:8000
    * The API works under /api/products path.


## Requests & Responses Examples

### API Resources

  - [GET /]](#get-getallproducts)
  - [POST /create](#post-createproduct)
  - [GET /getbyid/[id]](#get-getbyid)
  - [GET /getbyname?search=[name]](#get-getbyname)
  - [PUT /updateProductPrice](#post-updateproductprice)
  - [POST /[id]/delete](#post-deleteproduct)
  - [POST /buy](#post-buyproduct)
  - [POST /salesLog](#post-saleslog)
  
  
### POST /create/
Example: http://localhost:8000/api/products/create/

Request body:

{
    "id": 2,
    "name": "Base enfriadora",
    "sku": "CLD23",
    "price": 260,
    "description": "Base enfriadora para laptop 17\"",
    "stock": 300
}
  
 Good response: <br />
 
{
    "id": 2,
    "name": "Base enfriadora",
    "sku": "CLD23",
    "price": 260,
    "description": "Base enfriadora para laptop 17\"",
    "stock": 300
}
  

### GET /getbyid/[id]/
  
Example: http://localhost:8000/api/products/getbyid/[id]

  
 Good response: <br />
 
{
    "id": 2,
    "name": "Base enfriadora",
    "sku": "CLD23",
    "price": 260,
    "description": "Base enfriadora para laptop 17\"",
    "stock": 290
}
  

### GET /getbyname?search=[name]
  
Example: http://localhost:8000/api/products/getbyname?search=Base

  
 Good response: <br />
 
    {
        "id": 2,
        "name": "Base enfriadora",
        "sku": "CLD23",
        "price": 260,
        "description": "Base enfriadora para laptop 17\"",
        "stock": 300
    }
  

### GET /

Example: http://localhost:8000/api/products/

 Good response: <br />
 
    {
        "id": 1,
        "name": "Nuevo",
        "sku": "nev3",
        "price": 150,
        "description": "USB 32GB",
        "stock": 20
    },
    {
        "id": 2,
        "name": "Base enfriadora",
        "sku": "CLD23",
        "price": 260,
        "description": "Base enfriadora para laptop 17\"",
        "stock": 300
    }

### PUT /[id]/updateprice/

Example: http://example.com/api/products/1/updateprice/

Request body:

	{
	   "price" : "30"
	}
  
 Good response: <br />
 
{
    "id": 1,
    "name": "Nuevo",
    "sku": "nev3",
    "price": 30,
    "description": "USB 32GB",
    "stock": 20
}
  

### POST /[id]/delete/

Example: http://localhost:8000/api/products/1/delete/


 Bad response: <br />
 
{
    "detail": "Not found."
}



### POST /buy/
Example: http://localhost:8000/api/products/buy/

Request body:

	{
	   "product" : "2",
	   "quantity" : "10"
	}

 Good response: <br />
 
{
    "quantity": 10,
    "total_price": 1500,
    "product": 2
}


### GET /buy/log
Example: http://localhost:8000/api/products/buy/log


 Good response: <br />
 {
        "id": 1,
        "quantity": 10,
        "total_price": 1500,
        "date": "2020-01-28T21:17:34.046888Z",
        "product": {
            "id": 1,
            "name": "Nuevo",
            "sku": "nev3",
            "price": 30,
            "description": "USB 32GB",
            "stock": 20
        }
 },
 {
        "id": 2,
        "quantity": 10,
        "total_price": 2600,
        "date": "2020-01-28T22:13:10.407615Z",
        "product": {
            "id": 2,
            "name": "Base enfriadora",
            "sku": "CLD23",
            "price": 260,
            "description": "Base enfriadora para laptop 17\"",
            "stock": 290
        }
 }
 

## Live Demo 🚀
You can check live demo deployed on Heroku here:
```
https://powerful-hamlet-07671.herokuapp.com/api/products/
```
