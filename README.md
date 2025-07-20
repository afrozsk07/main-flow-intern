# main-flow-intern

This repository showcases the work completed during my 2-month internship on **Python Programming/Development** at **Main Flow Services & Technologies Pvt. Ltd.** The internship focused on practical skill development through assigned tasks, all of which are documented and included here.

---

### Internship Overview

**Company:** Main Flow Services & Technologies Pvt. Ltd.
**Duration:** June 5, 2024 - August 5, 2024
**Domain:** Python Programming
**Role:** Python Intern

This internship provided valuable exposure to real-world development practices, allowing me to apply and expand my Python knowledge to practical challenges. Each task enhanced my problem-solving abilities and deepened my understanding of key Python concepts, covering areas from core fundamentals to GUI application development.

---

### Internship Tasks & Accomplishments

Here's a detailed breakdown of the tasks accomplished during the internship:

#### Task 1: Fundamental Python Data Structures and Operations

**Objective:** To gain a comprehensive understanding and practical experience with **core Python data structures** (Lists, Dictionaries, Tuples) and fundamental programming concepts, including conditional statements, arithmetic operations, and string manipulation.

**Description:**
This task involved hands-on exploration and demonstration of Python's built-in data types and essential operations. Key areas covered included:

* **Lists:** Creation, element access (positive and negative indexing), modification (appending, extending, deleting), concatenation, and slicing.
* **Dictionaries:** Accessing values by key, retrieving all keys/values/items, updating entries, and removing elements.
* **Tuples:** Creation, element access (indexing), demonstrating immutability, and various slicing techniques.
* **Conditional Statements:** Practical application of `if`, `if-else`, `if-elif-else` constructs, and concise conditional expressions.
* **Basic Operations:** Performing standard arithmetic operations and essential string manipulations like stripping characters, splitting strings, and concatenation.

**Learning Outcomes:**
I solidified my understanding of Python's foundational building blocks, gaining proficiency in efficient data manipulation and controlling program flow. This provided a strong base for tackling more complex programming challenges.

**Code:**
The Python code for this task is located in: `Task1.ipynb`

---

#### Task 2: Data Manipulation with Pandas

**Objective:** To develop practical skills in **data loading, inspection, cleaning, filtering, and sorting** using the **Pandas library**, a fundamental tool for data analysis in Python.

**Description:**
This task focused on utilizing the Pandas library to perform essential data manipulation operations on a CSV dataset (`colors.csv`). The key steps involved:

* **Data Loading:** Reading the `colors.csv` file into a Pandas DataFrame.
* **Missing Value Inspection:** Identifying and quantifying null values across rows and columns.
* **Data Filtering:** Extracting specific rows based on defined conditions.
* **Data Sorting:** Arranging DataFrame rows based on the values within a chosen column.
* **Data Saving:** Exporting the manipulated DataFrame back into a CSV file.
* **Duplicate Removal:** Identifying and eliminating duplicate rows based on specified columns.

**Learning Outcomes:**
This task significantly enhanced my ability to work with tabular data using Pandas. I gained hands-on experience in data preparation, including handling missing entries and duplicates, and effectively organizing data through filtering and sorting.

**Code:**
The Python code for this task is located in: `Task2.ipynb`

---

#### Task 3: Web Scraping with BeautifulSoup and Requests

**Objective:** To learn the fundamentals of **web scraping** in Python using the `requests` and `BeautifulSoup` libraries to extract information programmatically from web pages.

**Description:**
This task involved building a Python script to perform basic web scraping on a target website (GeeksforGeeks). The process included:

* **Fetching Web Content:** Sending HTTP GET requests to retrieve the raw HTML content of a specified URL.
* **Parsing HTML:** Utilizing `BeautifulSoup` to parse the fetched HTML content into a navigable tree structure.
* **Extracting Text:** Retrieving all visible text content from the parsed webpage, with cleaning for readability.
* **Extracting Links:** Identifying and extracting all hyperlinks (`<a>` tags) and their `href` attributes present on the webpage.
* **Extracting Page Title:** Locating and retrieving the official title of the webpage from the `<title>` tag.

**Learning Outcomes:**
This task provided practical experience in web scraping, a valuable skill for automated data collection. I learned how to programmatically access web content, parse HTML, and extract specific information, establishing a foundation for more advanced data extraction projects.

**Code:**
The Python code for this task is located in: `Task3.ipynb`

---

#### Task 4: GUI Calculator using Tkinter

**Objective:** To develop a functional **graphical user interface (GUI) application** using Python's **Tkinter library** to create a basic calculator, building skills in front-end development and event handling.

**Description:**
This task focused on designing and implementing a standard calculator application with a GUI. The key components and functionalities developed included:

* **GUI Initialization:** Setting up the main window, including customizing the title and dimensions.
* **Customization:** Integrating external image files for the window icon and background to enhance visual appeal.
* **Entry Widget:** Implementing a display area for user input and calculation results.
* **Button Creation and Layout:** Designing and arranging interactive buttons for digits (0-9) and arithmetic operations (+, -, \*, /), along with "Equals" and "Clear" functionalities using Tkinter's grid layout manager.
* **Event Handling:** Developing functions to manage button clicks, dynamically updating the display, and handling the state for arithmetic operations.
* **Arithmetic Logic:** Implementing the core logic to perform addition, subtraction, multiplication, and division based on user interactions.

**Learning Outcomes:**
I gained practical experience in GUI programming with Tkinter, understanding how to design user interfaces, handle user events, and integrate basic visual assets. This project strengthened my knowledge of object-oriented programming concepts and state management within a GUI context.

**Code:**
The Python code for this task is located in: `Task4.ipynb`

---

#### Task 5: Real-time Currency Converter GUI

**Objective:** To build a user-friendly graphical **currency converter application** using **Tkinter** for the interface, integrated with the `requests` library to fetch real-time exchange rates from an external API.

**Description:**
This task centered on creating a practical application that enables users to convert amounts between various currencies. Key aspects of this development included:

* **GUI Design with Tkinter:**
    * Setting up the main application window with custom styling, including title, dimensions, and an application icon.
    * Incorporating an image asset for visual branding.
    * Designing intuitive input fields for the amount to convert and corresponding output fields for the converted amount.
    * Utilizing `ttk.Combobox` for user-friendly selection of "From" and "To" currencies from a comprehensive list of global currency codes.
    * Implementing "Convert" and "Clear" buttons to trigger conversions and reset the interface.
    * Including a `Text` widget to log conversion history and display real-time update timestamps.
* **API Integration for Exchange Rates:**
    * Leveraging the `requests` library to make HTTP GET requests to `https://api.exchangerate-api.com/v4/latest/{from_currency}` to retrieve up-to-date exchange rates.
    * Parsing the JSON response from the API to accurately extract the necessary exchange rate.
* **Currency Conversion Logic:**
    * Implementing robust validation for user input, ensuring correct numerical formats and handling empty fields.
    * Performing precise currency conversion calculations based on the retrieved rates.
* **Error Handling:**
    * Providing informative error messages via `messagebox` for invalid inputs or issues encountered during API communication.

**Learning Outcomes:**
This task significantly advanced my skills in developing interactive Python applications. I gained valuable experience in integrating external web APIs into a GUI, handling asynchronous data fetching, managing application state, and creating a responsive user experience with proper input validation and error handling. This project demonstrated the ability to build functional tools that interact with real-world data sources.

**Code:**
The Python code for this task is located in: `Task5.ipynb`

---

#### Task 6: Restaurant Management System GUI Framework

**Objective:** To design and implement a comprehensive **graphical user interface (GUI) framework** for a Restaurant Management System using **Tkinter**, establishing a structured foundation for managing orders, costs, and customer information.

**Description:**
This final task involved building the foundational GUI for a Restaurant Management System, with a focus on architectural design and intuitive user interface layout. Key structural elements and components include:

* **Modular GUI Structure:** The application's interface is organized into distinct `Frame` components for clarity and maintainability:
    * **Title Bar:** Clearly displays the system's name.
    * **Customer Information Section:** Provides input fields for customer name, contact number, and email.
    * **Menu Sections (Drinks and Foods):** Lists various menu items with `Checkbutton` widgets, allowing staff to select ordered items. Each item's selection state is tracked using `tkinter.IntVar()`.
    * **Cost Summary Panel:** Designed to display calculated costs, including "Cost of Drinks," "Cost of Foods," "Service Charge," "Paid Tax," "Sub Total," and "Total Cost." (Note: The detailed calculation logic for these elements would be developed in subsequent stages for a fully operational system.)
    * **Action Buttons:** Includes "Calculate Total" (to initiate cost aggregation), "Generate Bill" (to produce a receipt), "Reset" (to clear all input fields), and "Exit" (to close the application).
    * **Integrated Calculator:** A basic numerical calculator is embedded within the system for quick, on-the-spot computations during order processing.
    * **Receipt Display Area:** A `Text` widget specifically designated for presenting the generated bill or order summary to the user.
* **Tkinter Widget Mastery:** Demonstrated proficient use of a wide array of Tkinter widgets such as `Frame`, `Label`, `LabelFrame`, `Entry`, `Checkbutton`, `Button`, and `Text` to create an organized and intuitive user interface.
* **Event Handling & State Management:** Implemented fundamental event handling for button clicks (e.g., `reset`, `exit`, calculator interactions) and utilized `IntVar` for efficient management of checkbox states, establishing the groundwork for more complex interactions and data flow within the system.

**Learning Outcomes:**
This task provided valuable experience in building a multi-sectional, feature-rich GUI application, showcasing the ability to structure a larger Python project using Tkinter. It highlighted skills in UI/UX design principles, effective widget management, and setting up a robust foundational framework for a data-driven business application. This project demonstrated an understanding of how to approach and build scalable desktop applications.

**Code:**
The Python code for this task is located in: `Task6.ipynb`

---

### Setup and Usage

To run these projects locally, please follow these steps:

1.  **Prerequisites:**
    * **Python 3.8+** (or the specific version noted in your Jupyter notebooks' metadata).
    * **Git** (to clone the repository).

2.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/YourGitHubUsername/main-flow-intern.git](https://github.com/YourGitHubUsername/main-flow-intern.git)
    cd main-flow-intern
    ```
    *(Replace `YourGitHubUsername` with your actual GitHub username)*

3.  **Create a Virtual Environment (Recommended):**
    It's good practice to use a virtual environment to manage project dependencies.
    ```bash
    python -m venv venv
    # On Windows
    .\venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

4.  **Install Dependencies:**
    The projects utilize several external libraries. Install them using pip:
    ```bash
    pip install pandas beautifulsoup4 requests Pillow jupyter
    ```
    * *Note on `Pillow` (PIL fork):* This library is crucial for image handling in the Tkinter projects (Tasks 4 and 5) and needs to be explicitly installed. Tkinter itself is usually built-in with Python.

5.  **External Files:**
    * **`Task2.ipynb`** requires a `colors.csv` file. Ensure this file is present in the same directory as `Task2.ipynb`.
    * **`Task4.ipynb`** and **`Task5.ipynb`** utilize external image files (`.ico`, `.png`). **It is highly recommended to place these image files in dedicated subdirectories (e.g., `task4_assets/`, `task5_assets/`) within your repository and update the file paths in the corresponding Python code to be relative to the notebook's location.** This ensures portability across different systems.
    * **API Key for Task 5:** The Currency Converter (Task 5) relies on exchange rate data from `exchangerate-api.com`. While the provided code uses a free tier URL that might not strictly require an explicit API key for basic usage, if you may need to register on their site for an API key if you encounter rate limits or need extended functionality, and adjust the `url` in the `convert_currency` method accordingly.

6.  **Run the Notebooks:**
    After installing `jupyter` (as included in step 4's `pip install` command), start the Jupyter Notebook server:
    ```bash
    jupyter notebook
    ```
    Your web browser will open, displaying the contents of your `main-flow-intern` directory. You can then click on each `TaskX.ipynb` file to open and run the code cells.

---

### Conclusion

This internship at Main Flow Services & Technologies Pvt. Ltd. has been an invaluable experience in my journey as a Python programmer. Over the past two months, I've had the opportunity to translate theoretical knowledge into practical applications, ranging from fundamental data manipulation and web scraping to developing interactive graphical user interfaces.

I've gained hands-on experience with critical libraries like Pandas, Requests, BeautifulSoup, and Tkinter, and deepened my understanding of object-oriented programming, API integration, and user interface design principles. The task-based approach fostered a disciplined and problem-solving mindset, allowing me to build a solid foundation in diverse areas of Python development.

I am grateful for the guidance and the practical exposure provided by Main Flow Services & Technologies Pvt. Ltd., which has significantly contributed to my growth and confidence in Python programming. I am enthusiastic about applying these newly acquired skills to future challenges and contributing to impactful projects.

---
