
# 👥 BabyRocks e-Commerce — User Stories

This document contains the detailed Agile user stories for **BabyRocks e-Commerce**.  
The main `README.md` links here to keep the root documentation clean and focused.

---

## 👶 First-Time Visitor

### 1.1 Browse Products Without an Account  
**As a** first-time visitor  
**I want to** browse products and categories without logging in  
**So that** I can see what the shop offers before creating an account  

**Acceptance Criteria**  
- [ ] I can access the homepage without logging in  
- [ ] I can see a list of categories  
- [ ] I can see a list of “Popular products”  
- [ ] I can click on a product to view its details page  

---

### 1.2 Understand Product Details  
**As a** first-time visitor  
**I want to** see clear product information (image, description, price, sizes, colours)  
**So that** I can decide whether the product is right for me  

**Acceptance Criteria**  
- [ ] Product detail page shows image, name, price and description  
- [ ] Available sizes and colours are clearly shown  
- [ ] Stock availability is visible  
- [ ] I can see existing ratings and reviews (if any)  

---

### 1.3 Search for a Product  
**As a** first-time visitor  
**I want to** search for products by name or keyword  
**So that** I can quickly find items I am interested in  

**Acceptance Criteria**  
- [ ] There is a search bar in the header  
- [ ] Typing a keyword shows matching products  
- [ ] If no products match, a helpful message is shown  
- [ ] Clicking a search result takes me to the product page  

---

### 1.4 Create an Account During Checkout  
**As a** first-time visitor  
**I want to** create an account while placing my first order  
**So that** I do not have to create an account separately beforehand  

**Acceptance Criteria**  
- [ ] I can register from the checkout or login page  
- [ ] On successful registration I am logged in automatically  
- [ ] My cart is preserved after registration  
- [ ] I receive a confirmation that my account has been created  

---

## 🔁 Returning User

### 2.1 Log In to My Account  
**As a** returning user  
**I want to** log in with my email and password  
**So that** I can access my orders and saved details  

**Acceptance Criteria**  
- [ ] There is a clear “Login” link in the header  
- [ ] Invalid credentials show a friendly error message  
- [ ] Successful login redirects me to a useful page (e.g. dashboard or store)  
- [ ] I can log out via the header navigation  

---

### 2.2 View My Dashboard  
**As a** returning user  
**I want to** see an overview of my account  
**So that** I can quickly access my profile and order history  

**Acceptance Criteria**  
- [ ] The dashboard displays a welcome message with my name  
- [ ] I can navigate to my profile details  
- [ ] I can navigate to my order history  
- [ ] I can see key information (e.g. total orders, recent orders)  

---

### 2.3 See Order History  
**As a** returning user  
**I want to** view a list of my past orders  
**So that** I can review what I have bought and when  

**Acceptance Criteria**  
- [ ] I can see a list of previous orders with dates and totals  
- [ ] I can click an order to view its details  
- [ ] The order details page shows the products, quantities and prices  
- [ ] Order status (e.g. New, Completed, Cancelled) is visible  

---

### 2.4 Re-Order a Previous Purchase (Future Enhancement)  
**As a** returning user  
**I want to** quickly re-order a previous order  
**So that** I can buy the same items again with minimal effort  

**Acceptance Criteria**  
- [ ] From an order detail view, I can click a “Re-order” button (future feature)  
- [ ] The products from that order are added to my cart  
- [ ] If a product or variation is no longer available, I am informed  

---

## 🧺 Shopping Cart & Checkout

### 3.1 Add Products to Cart  
**As a** visitor or logged-in user  
**I want to** add products (with selected size and colour) to my cart  
**So that** I can purchase them later  

**Acceptance Criteria**  
- [ ] I can select size and colour (where applicable)  
- [ ] I can add a product to the cart from the product detail page  
- [ ] The cart icon updates with the total quantity  
- [ ] I receive a confirmation (message or toast) that the item was added  

---

### 3.2 View and Edit Cart  
**As a** user  
**I want to** view my cart and adjust quantities  
**So that** I can manage what I am buying before checkout  

**Acceptance Criteria**  
- [ ] Cart page lists each product, variation, quantity and price  
- [ ] I can increase or decrease the quantity of each item  
- [ ] I can remove an item from the cart  
- [ ] Subtotal and total values update correctly  

---

### 3.3 Checkout and Place an Order  
**As a** user  
**I want to** complete a checkout form and place an order  
**So that** I can buy the items in my cart  

**Acceptance Criteria**  
- [ ] I must provide required details (name, address, email, phone)  
- [ ] Validation errors are clearly displayed  
- [ ] Order total (including tax if applicable) is visible before confirming  
- [ ] Successful checkout creates an order and shows a confirmation page  

*(Payment integration can be simulated in this version, with a placeholder “Payment successful” step.)*

---

## ⭐ Reviews & Ratings

### 4.1 Leave a Review for a Purchased Product  
**As a** logged-in user who has bought a product  
**I want to** leave a rating and written review  
**So that** I can share my experience with other customers  

**Acceptance Criteria**  
- [ ] I can only review products I have actually ordered  
- [ ] Review form includes rating (e.g. 1–5), subject and review text  
- [ ] On submission, the review is stored and linked to my account  
- [ ] A success message confirms the review has been submitted  

---

### 4.2 Edit an Existing Review  
**As a** user who has already left a review  
**I want to** edit my review  
**So that** I can update my feedback if my opinion changes  

**Acceptance Criteria**  
- [ ] If I revisit a product I have reviewed, I can update the existing review  
- [ ] Editing a review uses the same form, pre-filled with previous data  
- [ ] The updated review replaces the old one  

---

### 4.3 See Average Rating on the Product Page  
**As a** visitor  
**I want to** see the overall rating for each product  
**So that** I can quickly judge quality based on other users’ feedback  

**Acceptance Criteria**  
- [ ] Product detail page shows the average rating  
- [ ] The number of reviews is visible  
- [ ] If no reviews exist, a suitable message is shown  

---

## 👨‍💻 Admin & Store Management

### 5.1 Manage Products  
**As an** admin  
**I want to** create, update and delete products  
**So that** I can keep the catalogue accurate and up to date  

**Acceptance Criteria**  
- [ ] I can add a new product with name, description, price, stock and image  
- [ ] I can update existing product details  
- [ ] I can deactivate or delete products (so they no longer appear in the store)  

---

### 5.2 Manage Categories  
**As an** admin  
**I want to** manage product categories  
**So that** customers can browse products by logical groups  

**Acceptance Criteria**  
- [ ] I can create, edit and delete categories via Django admin  
- [ ] Categories can be assigned to products  
- [ ] Deleting a category does not cause the site to crash (products handled safely)  

---

### 5.3 Manage Orders  
**As an** admin  
**I want to** view and update orders  
**So that** I can track and manage fulfilment  

**Acceptance Criteria**  
- [ ] I can view a list of all orders in the admin  
- [ ] I can filter orders by status (New, Completed, Cancelled, etc.)  
- [ ] I can view order details, including items and customer information  
- [ ] I can update the order status  

---

### 5.4 Moderate Reviews  
**As an** admin  
**I want to** approve or reject reviews  
**So that** I can maintain quality and remove inappropriate content  

**Acceptance Criteria**  
- [ ] New reviews can be marked as approved or rejected (via status field)  
- [ ] Only approved reviews are visible on the product page  
- [ ] Admin can delete reviews if necessary  

---

## ⚙️ Non-Functional Requirements

### 6.1 Performance  
**As a** user  
**I want to** navigate the site without long delays  
**So that** the shopping experience feels smooth  

**Acceptance Criteria**  
- [ ] Pages load within a reasonable time on a typical broadband connection  
- [ ] Basic caching or query optimisation is in place for key views (e.g. store page)  

---

### 6.2 Security  
**As a** site owner  
**I want to** protect user data and admin access  
**So that** the site is secure and trustworthy  

**Acceptance Criteria**  
- [ ] Passwords are stored using Django’s standard hashing  
- [ ] Admin panel is not exposed at `/admin/` in production (custom path / honeypot used)  
- [ ] `DEBUG` is disabled in production  
- [ ] Sensitive settings are stored in environment variables  

---

### 6.3 Responsiveness  
**As a** user  
**I want to** use the site on mobile, tablet and desktop  
**So that** I can shop from any device  

**Acceptance Criteria**  
- [ ] Layout adapts correctly on small, medium and large screens  
- [ ] Navigation remains usable on mobile (burger menu, stacked content)  
- [ ] Key flows (browse, cart, checkout) are fully usable on mobile devices  

---


