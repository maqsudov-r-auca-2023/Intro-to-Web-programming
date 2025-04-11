# Task Manager Project

A simple Task Manager application built using Flask and SQLite.

## Features

- Add, edit, and delete tasks.
- Track task progress and deadlines.
- User authentication and security.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/Task-manager.git
    ```

2. Navigate to the project directory:
    ```bash
    cd Task-manager
    ```

3. Set up a virtual environment:
    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

5. Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

6. Run the app:
    ```bash
    python run.py
    ```

## Project Structure

Task-manager/ ├── app/ │ ├── init.py │ ├── forms.py │ ├── models.py │ ├── views.py │ ├── static/ │ │ ├── css/ │ │ └── js/ │ └── templates/ │ ├── base.html │ ├── index.html │ └── add_task.html ├── config.py ├── requirements.txt ├── run.py └── README.md


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

