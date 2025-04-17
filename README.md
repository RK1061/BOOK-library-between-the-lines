# Between the Lines - Book Library

## About the Project

**Between the Lines** is a simple, web-based **book library management system** built using the **Django** framework. The application allows users to perform basic **CRUD (Create, Read, Update, Delete)** operations on books stored in the library, making it easy to manage a collection of books.

The system enables users to:

- **Add new books**: Enter book details like title, author, and price.
- **View books**: List all books stored in the library.
- **Edit books**: Update book details when needed.
- **Delete books**: Remove books from the collection.

This project is aimed at demonstrating basic web application functionality using Django, with a focus on building a simple and easy-to-use interface for managing a book library.

---

## Features

- **Add new books**: Input book title, author, and price.
- **View books**: Display a list of all books in the library.
- **Edit books**: Update book details.
- **Delete books**: Remove books from the library.

---

## Requirements

- Python 3.x
- Django

---

## Installation

1. **Clone the repository**:
    
    ```bash
    git clone <https://github.com/RK1061/BOOK-library-between-the-lines.git>
    
    ```
    
2. **Navigate to the project directory**:
    
    ```bash
    cd BOOK-library-between-the-lines
    
    ```
    
3. **Create a virtual environment** (optional, but recommended):
    
    ```bash
    python -m venv venv
    
    ```
    
4. **Activate the virtual environment**:
    - On **Windows**:
        
        ```bash
        .\\venv\\Scripts\\activate
        
        ```
        
    - On **Mac/Linux**:
        
        ```bash
        source venv/bin/activate
        
        ```
        
5. **Install the required dependencies**:
    
    ```bash
    pip install -r requirements.txt
    
    ```
    
6. **Apply database migrations**:
    
    ```bash
    python manage.py migrate
    
    ```
    
7. **Run the development server**:
    
    ```bash
    python manage.py runserver
    
    ```
    
    You can now access the application by visiting `http://127.0.0.1:8000/` in your browser.
    

---

## Usage

- **Add a new book** by clicking on "Add New Book".
- **View, Edit, or Delete books** from the list of books displayed on the home page.

---

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes and commit them (`git commit -m 'Add feature'`).
4. Push to your branch (`git push origin feature-name`).
5. Open a pull request.

---

## License

This project is open-source and available under the [MIT License](https://www.notion.so/LICENSE).
