## E-Commerce Product Management API

A RESTful API built with Django and Django REST Framework for managing products in an online store. This API provides complete CRUD operations, user authentication, search functionality, and filtering capabilities.

Live API URL

**Base URL:** `https://lifeofchurchill.pythonanywhere.com/api/`


## Features

Complete CRUD operations for Products and Categories
User registration and authentication (Token-based)
Search products by name or description
Filter products by category, price, and stock quantity
Pagination for large datasets
Permission-based access control
Automatic timestamps for created products
Input validation for all fields

---

## Technologies Used

- **Backend Framework:** Django
- **API Framework:** Django REST Framework
- **Database:** SQLite (Development)
- **Authentication:** Token Authentication
- **Deployment:** PythonAnywhere

---

## API Endpoints

**Authentication Endpoints**

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/api/users/` | Register new user | No |
| POST | `/api/auth/login/` | Login and get token | No |


**Product Endpoints**

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/api/products/` | Get all products (paginated) | No |
| POST | `/api/products/` | Create new product | Yes |
| GET | `/api/products/{id}/` | Get specific product | No |
| PUT | `/api/products/{id}/` | Update product (full) | Yes |
| PATCH | `/api/products/{id}/` | Update product (partial) | Yes |
| DELETE | `/api/products/{id}/` | Delete product | Yes |


**Category Endpoints**

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/api/categories/` | Get all categories | No |
| POST | `/api/categories/` | Create new category | No |
| GET | `/api/categories/{id}/` | Get specific category | No |
| PUT | `/api/categories/{id}/` | Update category | No |
| DELETE | `/api/categories/{id}/` | Delete category | No |

**Search & Filter Parameters**

| Parameter | Example | Description |
|-----------|---------|-------------|
| `search` | `/api/products/?search=phone` | Search in name and description |
| `category` | `/api/products/?category=1` | Filter by category ID |
| `price` | `/api/products/?price=99.99` | Filter by exact price |
| `stock_quantity` | `/api/products/?stock_quantity=0` | Filter by stock quantity |
| `page` | `/api/products/?page=2` | Pagination (10 items per page) |

---

Authentication

This API uses **Token Authentication**.

### **How to Get a Token:**

1. **Register a new user:**
```http
POST /api/users/
Content-Type: application/json

{
  "username": "your_username",
  "email": "your_email@example.com",
  "password": "your_password"
}
```

2. **Login to get your token:**
```http
POST /api/auth/login/
Content-Type: application/json

{
  "username": "your_username",
  "password": "your_password"
}
```

**Response:**
```json
{
  "token": "a1b2c3d4e5f6g7h8i9j0..."
}
```

3. **Use the token in subsequent requests:**
```http
Authorization: Token a1b2c3d4e5f6g7h8i9j0...
```

---

## 🚀 How to Use

### **1. Register a New User**

**Request:**
```http
POST https://lifeofchurchill.pythonanywhere.com/api/users/
Content-Type: application/json

{
  "username": "shopper1",
  "email": "shopper1@example.com",
  "password": "secure123"
}
```

**Response (201 Created):**
```json
{
  "id": 1,
  "username": "shopper1",
  "email": "shopper1@example.com"
}
```

---

### **2. Login and Get Token**

**Request:**
```http
POST https://lifeofchurchill.pythonanywhere.com/api/auth/login/
Content-Type: application/json

{
  "username": "shopper1",
  "password": "secure123"
}
```

**Response (200 OK):**
```json
{
  "token": "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0"
}
```

---

### **3. Get All Products**

**Request:**
```http
GET https://lifeofchurchill.pythonanywhere.com/api/products/
```

**Response (200 OK):**
```json
{
  "count": 25,
  "next": "https://lifeofchurchill.pythonanywhere.com/api/products/?page=2",
  "previous": null,
  "results": [
    {
      "id": 1,
      "name": "iPhone 15",
      "description": "Latest Apple smartphone",
      "price": "999.99",
      "category": 1,
      "stock_quantity": 50,
      "image": "https://example.com/image.jpg",
      "created_at": "2024-10-19T10:30:00Z",
      "created_by": 1
    }
  ]
}
```

---

### **4. Create a Product (Authentication Required)**

**Request:**
```http
POST https://lifeofchurchill.pythonanywhere.com/api/products/
Authorization: Token a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0
Content-Type: application/json

{
  "name": "MacBook Pro",
  "description": "Apple laptop with M3 chip",
  "price": "2499.99",
  "category": 1,
  "stock_quantity": 25,
  "image": "https://example.com/macbook.jpg"
}
```

**Response (201 Created):**
```json
{
  "id": 2,
  "name": "MacBook Pro",
  "description": "Apple laptop with M3 chip",
  "price": "2499.99",
  "category": 1,
  "stock_quantity": 25,
  "image": "https://example.com/macbook.jpg",
  "created_at": "2024-10-19T11:00:00Z",
  "created_by": 1
}
```

---

### **5. Search Products**

**Request:**
```http
GET https://lifeofchurchill.pythonanywhere.com/api/products/?search=iphone
```

**Response (200 OK):**
```json
{
  "count": 3,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "name": "iPhone 15",
      "description": "Latest Apple smartphone",
      "price": "999.99",
      "category": 1,
      "stock_quantity": 50,
      "image": "https://example.com/image.jpg",
      "created_at": "2024-10-19T10:30:00Z",
      "created_by": 1
    }
  ]
}
```

---

### **6. Filter Products by Category**

**Request:**
```http
GET https://lifeofchurchill.pythonanywhere.com/api/products/?category=1
```

**Response (200 OK):**
```json
{
  "count": 10,
  "next": null,
  "previous": null,
  "results": [
    // Products in category 1
  ]
}
```

---

### **7. Update a Product**

**Request:**
```http
PUT https://lifeofchurchill.pythonanywhere.com/api/products/1/
Authorization: Token a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0
Content-Type: application/json

{
  "name": "iPhone 15 Pro",
  "description": "Updated model",
  "price": "1099.99",
  "category": 1,
  "stock_quantity": 30,
  "image": "https://example.com/iphone15pro.jpg"
}
```

**Response (200 OK):**
```json
{
  "id": 1,
  "name": "iPhone 15 Pro",
  "description": "Updated model",
  "price": "1099.99",
  "category": 1,
  "stock_quantity": 30,
  "image": "https://example.com/iphone15pro.jpg",
  "created_at": "2024-10-19T10:30:00Z",
  "created_by": 1
}
```

---

### **8. Delete a Product**

**Request:**
```http
DELETE https://lifeofchurchill.pythonanywhere.com/api/products/1/
Authorization: Token a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0
```

**Response (204 No Content):**
```
(Empty response body)
```

---

## ⚠️ Error Responses

### **401 Unauthorized**
```json
{
  "detail": "Authentication credentials were not provided."
}
```

### **403 Forbidden**
```json
{
  "detail": "You do not have permission to perform this action."
}
```

### **404 Not Found**
```json
{
  "detail": "Not found."
}
```

### **400 Bad Request (Validation Error)**
```json
{
  "price": ["This field is required."],
  "name": ["This field may not be blank."]
}

## 🎯 Validation Rules

### **Product Validation:**
- ✅ Price must be greater than 0
- ✅ Stock quantity cannot be negative
- ✅ Name cannot be empty
- ✅ All required fields must be provided

### **User Validation:**
- ✅ Username must be unique
- ✅ Email must be valid format
- ✅ Password is required for registration

---

## 📱 Testing the API

### **Using Postman:**

1. **Import the base URL:** `https://lifeofchurchill.pythonanywhere.com/api/`
2. **Register a user** at `/users/`
3. **Get your token** at `/auth/login/`
4. **Set Authorization header:** `Token YOUR_TOKEN_HERE`
5. **Start making requests!**

### **Using cURL:**
```bash
# Get all products
curl https://lifeofchurchill.pythonanywhere.com/api/products/

# Create product (with authentication)
curl -X POST https://lifeofchurchill.pythonanywhere.com/api/products/ \
  -H "Authorization: Token YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Test Product",
    "description": "Test description",
    "price": "99.99",
    "category": 1,
    "stock_quantity": 50,
    "image": "https://via.placeholder.com/150"
  }'
```


## Project Requirements Met

Complete CRUD operations for Products and Users  
Token-based authentication implemented  
Search functionality working  
Filtering by multiple criteria (category, price, stock)  
Pagination implemented  
Input validation on all fields  
Successfully deployed and accessible online  
RESTful API design principles followed  
Complete documentation provided  

