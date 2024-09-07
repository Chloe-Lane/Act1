Act1

Overview
---------
Act1 is a web application designed to showcase portfolios with an interactive carousel feature. The application is built with Django and allows users to view different portfolio items in a carousel format.

Features
---------
- Portfolio Carousel: Displays portfolio items in a sliding carousel.
- Dynamic Content: Fetches portfolio items from the database.
- Responsive Design: The carousel adapts to various screen sizes.

Installation
------------
Prerequisites
- Python 3.x
- Django 4.x (or compatible version)

Setup
1. Clone the Repository
   git clone https://github.com/Chloe-Lane/Act1.git
   cd Act1

2. Create a Virtual Environment
   python -m venv venv

3. Activate the Virtual Environment
   - On Windows:
     venv\Scripts\activate
   - On macOS/Linux:
     source venv/bin/activate

4. Install Dependencies
   pip install -r requirements.txt

5. Apply Migrations
   python manage.py migrate

6. Run the Development Server
   python manage.py runserver
   Open your browser and go to http://127.0.0.1:8000 to view the application.

Usage
------
1. Add Portfolio Items
   Use the Django admin interface or create a management command to add portfolio items. Each portfolio item should include:
   - Title: The name of the portfolio item.
   - Description: A brief description of the item.
   - Image: An image representing the item.
   - Link: A URL that users can visit for more details.
   - Date Posted: The date when the item was added.

2. View the Carousel
   Navigate to the URL path /portfolio/ to view the portfolio carousel in action.

Contributing
------------
We welcome contributions to Act1! To contribute:
1. Fork the repository.
2. Create a new branch (git checkout -b feature/your-feature).
3. Commit your changes (git commit -am 'Add new feature').
4. Push to the branch (git push origin feature/your-feature).
5. Open a pull request.

License
-------
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
