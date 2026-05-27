




# 🛍️ BabyRocks — e-Commerce Platform  
![BabyRocks Banner](./docs/images/banner.png)

A responsive, full-stack e-commerce application built with **Django**, featuring product browsing, categories, variations, reviews, user accounts, cart management, ordering, and an admin dashboard.  
Designed to demonstrate clean architecture, scalability, and professional documentation.

Live site: https://babyrocks.vicstack.uk/
GitHub repository: https://github.com/bukaro8/babyrocks

---

## 💻 Deployment (Run Locally)

```bash
# Clone repository
git clone https://github.com/bukaro8/babyrocks.git
cd babyrocks

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate   # macOS/Linux
# or
.venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt

# Create .env file (example)
cp .env.example .env

# Run migrations
python manage.py migrate

# Create superuser (admin)
python manage.py createsuperuser

# Start development server
python manage.py runserver
````

---

## 🛠 Tech Stack

| Technology  | Purpose                    | Version  |
| ----------- | -------------------------- | -------- |
| Django      | Backend framework          | 6.x      |
| Python      | Core application           | 3.12+    |
| PostgreSQL  | Production database        | 14+      |
| SQLite      | Local development database | Built-in |
| Bootstrap 5 | Front-end styling          | —        |
| FontAwesome | Icons                      | —        |
| Coolify     | Deployment platform        | —        |

---

## 👥 User Stories

This project follows Agile user-centred design.

Only a short summary appears in the main README.

For the full detailed set of user stories (first-time user, returning user, guest checkout, admin tasks, acceptance criteria):

👉 **See full User Stories:**
[`./docs/user-stories.md`](./docs/user-stories.md)

---

## ✨ Features

| Feature               | Description                                     |
| --------------------- | ----------------------------------------------- |
| **User Accounts**     | Register, login, logout, dashboard              |
| **Product Catalogue** | Browse all products, view details, categories   |
| **Variations**        | Colours & sizes using Django Variation Model    |
| **Search System**     | Search products by name/description             |
| **Cart Management**   | Add/remove/edit items, supports anonymous carts |
| **Checkout Flow**     | Capture address, order summary & total          |
| **Order Processing**  | Orders saved with status tracking               |
| **Reviews & Ratings** | Users can review only purchased products        |
| **Admin Dashboard**   | Manage products, orders, categories             |
| **Responsive Design** | Works across desktop, tablet, and mobile        |

---

## 🗂 Database Structure

A complete Entity Relationship Diagram (ERD) of the BabyRocks system:

![Database Diagram](./docs/images/db-diagram.png)

### **Description**

* Products belong to categories
* Products have variations (size, colour)
* A product may have multiple gallery images
* Users may add products to a cart (with variations)
* Orders store cart items at checkout
* Users can review products they have purchased

---

## 🔄 Data Flow

The high-level data flow through the application:

![Data Flow Diagram](./docs/images/data-flow.png)

### **Description**

1. **User** interacts with the interface (product, cart, checkout).
2. **Request** is sent to Django’s URL router.
3. **View** processes business logic and interacts with models.
4. **Models** query or update the **database**.
5. **Templates** render the final output.
6. **Response** is returned to the user browser.

This architecture follows Django’s MTV pattern.

---

## 🎨 Design System

### **Colour Palette**

![Colour Palette](./docs/images/color-palette.png)

| Role            | Hex       | Usage                    |
| --------------- | --------- | ------------------------ |
| Primary Green   | `#00A844` | Buttons, navbar actions  |
| Hover Green     | `#00C851` | Button hover state       |
| Accent Red      | `#FF3B30` | Cart notification badge  |
| Text Dark       | `#212121` | Headings, product titles |
| Text Medium     | `#757575` | Secondary text           |
| Border Grey     | `#E5E5E5` | Cards, separators        |
| Background Grey | `#F5F5F5` | Page background          |

---

## ✒ Typography

![Typography](./docs/typography/typography.png)

| Element   | Font Stack                                                                   | Size    | Weight |
| --------- | ---------------------------------------------------------------------------- | ------- | ------ |
| Headings  | `system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif` | ~2rem   | 600    |
| Body Text | Same as above                                                                | 1rem    | 400    |
| Buttons   | Same as above                                                                | 0.95rem | 600    |

---

## 📐 Wireframes

### **Desktop**

![Desktop Wireframe](./docs/wireframes/desktop.png)

### **Tablet**

![Tablet Wireframe](./docs/wireframes/tablet.png)

### **Mobile**

![Mobile Wireframe](./docs/wireframes/mobile.png)

---

## 📦 Folder Structure

```text
babyrocks/
│
├── accounts/
├── category/
├── carts/
├── orders/
├── store/
│
├── static/
├── templates/
│
├── docs/
│   ├── images/
│   │   ├── banner.png
│   │   ├── db-diagram.png
│   │   ├── data-flow.png
│   │   └── color-palette.png
│   ├── typography/
│   │   └── typography.png
│   └── wireframes/
│       ├── desktop.png
│       ├── tablet.png
│       └── mobile.png
│
└── README.md
```

---



## 🙏 Credits

* **Django Documentation** — [https://docs.djangoproject.com](https://docs.djangoproject.com)
* **Bootstrap 5** — CSS framework for layout & components
* **FontAwesome** — Icons
* **Coolify** — Deployment platform for self-hosting
* Product images sourced from stock photography for demo purposes
* Wireframes & diagrams generated using AI-assisted tools

---

**© 2025 BabyRocks — Created by Victor Ramirez**

```

