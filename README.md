# Portfolio Website

This is a simple portfolio website built using Django. The website showcases information about me, my skills, services, and provides a contact form. It is designed to be a personal portfolio that can be shared with potential clients, employers, or collaborators.

## Features

- **Home Page**: Displaying an introduction and overview of my portfolio.
- **About Page**: Information about my background, experience, and achievements.
- **Services Page**: A list of services I offer with descriptions.
- **Contact Page**: A contact form that visitors can use to get in touch with me.
- **Portfolio Page**: A showcase of projects and work I have done.
- **Custom Error Pages**: A custom 404 error page and 500 server error page.

## Technologies Used

- **Django**: Web framework for building the backend of the website.
- **HTML/CSS**: Used for designing and structuring the front-end pages.
- **JavaScript**: Used for interactive elements (like maps).
- **Bootstrap**: CSS framework for responsive design and layout.
- **Google Maps API**: Integrated into the Contact page to display my location.

## Installation
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/your-repository-name.git
   ```

2. Navigate to the project directory:
   ```bash
   cd your-repository-name
   ```

3. Set up a virtual environment:
   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:
   * For **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   * For **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

5. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

6. Run database migrations:
   ```bash
   python manage.py migrate
   ```

7. Start the development server:
   ```bash
   python manage.py runserver
   ```

8. Open your browser and go to `http://127.0.0.1:8000/` to view the website.

## Deployment

To deploy the portfolio website to a production server, make sure to set `DEBUG=False` and configure `ALLOWED_HOSTS` in the `settings.py` file.

You can deploy the website using popular platforms like:
* **Heroku**
* **DigitalOcean**
* **AWS EC2**

## License

This project is open source and available under the MIT License.

## Contact

If you have any questions or would like to collaborate, feel free to reach out to me at:
* **Email**: ajaysolanki.pvt@gmail.com
* **GitHub**: https://github.com/ajays0lanki