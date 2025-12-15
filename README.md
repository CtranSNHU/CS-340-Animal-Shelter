# README - Grazioso Salvare Dashboard Projec

## Project Overview
This project involved the development of a fully functional MongoDB dashboard for Grazioso Salvare, a company specializing in search-and-rescue dog training. The dashboard allows users to interact with and visualize data from Austin animal shelters, enabling them to identify and categorize suitable dogs for rescue training. The project was developed using Python, MongoDB, and the Dash framework.

## Functionality
The dashboard includes the following features:
- An interactive data table displaying unfiltered shelter animal data.
- Filtering options for different rescue types: Water Rescue, Mountain/Wilderness Rescue, Disaster/Individual Tracking.
- A geolocation chart displaying filtered results.
- A secondary chart (chosen visualization) responding to user input.
- The ability to reset filters and return to an unfiltered state.

Screenshots or a screencast are provided as proof of functionality.

## Tools Used and Rationale
- **MongoDB**: Used as the model component due to its flexibility with unstructured data and seamless integration with Python.
- **Python**: Chosen for its extensive data manipulation capabilities and ease of integration with databases.
- **Dash Framework**: Used to create the interactive web dashboard due to its robust visualization components and seamless integration with Python.
- **Pandas**: Utilized for data manipulation and formatting before rendering in the dashboard.
- **Plotly**: Used for creating interactive charts within the dashboard.

## Steps Taken
1. Developed a MongoDB database and implemented CRUD operations in Python (Project One).
2. Built an interactive data table for unfiltered shelter data.
3. Implemented query functions for filtering data based on search-and-rescue training criteria.
4. Created interactive UI components to allow users to filter data.
5. Developed dynamic charts responding to filter selections.
6. Tested and deployed the dashboard, capturing screenshots of different states.
7. Created documentation (README) to explain project implementation and reproduction.

## Challenges and Solutions
- **Data Filtering Issues**: Initially, queries were not returning expected results. Debugging through MongoDB queries and refining filtering logic resolved the issue.
- **UI Responsiveness**: Ensured proper data binding between UI components and database queries for a seamless user experience.
- **Deployment Concerns**: Used Dash’s built-in capabilities to test and deploy the dashboard locally before considering cloud deployment.

---

## Questions & Answers

### 1. How do you write programs that are maintainable, readable, and adaptable?
Maintainable and readable code follows best practices such as modular design, proper documentation, and clear variable/function naming. By creating a separate CRUD Python module in Project One, the database interactions were abstracted, making the code reusable and adaptable. This approach allowed easy integration with the dashboard in Project Two and could be extended for future enhancements.

### 2. How do you approach a problem as a computer scientist?
The approach starts with understanding client requirements, designing a suitable architecture, and incrementally implementing components. For this project, the first step was database design, followed by interactive UI elements, and then testing for user experience improvements. Compared to previous assignments, this project required a more structured and iterative approach, considering both backend and frontend requirements. In the future, structured problem-solving techniques like UML diagrams, flowcharts, and Agile methodologies will be leveraged to meet client needs efficiently.

### 3. What do computer scientists do, and why does it matter?
Computer scientists develop and optimize software solutions that solve real-world problems. In this project, the dashboard enables Grazioso Salvare to efficiently identify suitable dogs for search-and-rescue training, improving operational efficiency and potentially saving lives. The ability to process large datasets and present actionable insights helps organizations make informed decisions and enhances productivity in various industries.

