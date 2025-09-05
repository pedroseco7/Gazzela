# Gazzela 🏃💨

**Your running performance, optimized by Artificial Intelligence.**

[![Project Status](https://img.shields.io/badge/status-in%20development-yellowgreen.svg)](https://github.com/pedroseco7/Gazzela)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

---

### Table of Contents

1.  [About The Project](#about-the-project)
2.  [Key Features](#key-features)
3.  [Architecture & Tech Stack](#architecture--tech-stack)
4.  [Getting Started](#getting-started)
    * [Prerequisites](#prerequisites)
    * [Installation & Setup](#installation--setup)
5.  [Project Roadmap](#project-roadmap)
6.  [Contributing](#contributing)
7.  [License](#license)

---

### About The Project

**Gazzela** is an intelligent running coaching platform designed for amateur and professional athletes looking to reach their maximum potential. The application uses Artificial Intelligence models to process large volumes of performance data (pace, heart rate, elevation, cadence) and biometrics, with the goal of creating truly personalized and adaptive training plans.

Gazzela's philosophy is based on scientifically proven training principles, translated into practical and actionable recommendations, delivered through an intuitive mobile application and a WhatsApp chatbot.

---

### Key Features

* 📊 **Predictive Performance Analysis:** Models that estimate your race times (5k, 10k, Half Marathon, etc.) based on your training history.
* 🤖 **Adaptive Training Plans:** Training plans that dynamically adjust based on your performance, recovery, and feedback.
* 🧘 **Fatigue & Injury Risk Detection:** Analysis of data patterns to identify signs of overtraining and suggest active recovery periods.
* 🔗 **Automatic Synchronization:** Seamless integration with major training platforms like Strava and Garmin to automatically import your activities.
* 💬 **Chatbot Interaction:** A virtual assistant via WhatsApp to check your workout of the day, ask questions, and log your feedback quickly and conveniently.

---

### Architecture & Tech Stack

The project is designed with a decoupled services architecture to ensure scalability, maintainability, and performance.

![Gazzela Architecture Diagram](https://github.com/pedroseco7/Gazzela/issues/1#issue-3387299766)
*(Note: I suggest you upload the diagram you created to GitHub or a service like Imgur and replace this link)*

* **Frontend (Mobile App):** `React Native`
* **Backend (API Gateway):** `Python 3` with `FastAPI`
* **Database:** `PostgreSQL`
* **Cache:** `Redis`
* **Message Queue:** `RabbitMQ`
* **AI Service (Async Workers):**
    * Numerical Analysis: `Python` with `Celery`, `Pandas`, and `Scikit-learn`
    * Natural Language Processing: Integration with the `OpenAI` API
* **Infrastructure & Deployment:** `Docker` and `Docker Compose`

---

### Getting Started

Follow these steps to set up the development environment locally.

#### Prerequisites

Make sure you have the following tools installed on your machine:
* [Git](https://git-scm.com/)
* [Docker](https://www.docker.com/products/docker-desktop/)
* [Docker Compose](https://docs.docker.com/compose/install/)
* (Optional, for frontend) [Node.js](https://nodejs.org/) and [Yarn](https://yarnpkg.com/)

#### Installation & Setup

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/YOUR_USERNAME/gazzela.git](https://github.com/YOUR_USERNAME/gazzela.git)
    cd gazzela
    ```

2.  **Set up Environment Variables:**
    The backend requires a `.env` file for its configuration. You can start by copying the example file.
    ```sh
    cp backend/.env.example backend/.env
    ```
    Now, edit the `backend/.env` file and fill in the variables, such as database credentials, API keys for Strava, OpenAI, etc.

3.  **Build and Run the Docker Containers:**
    This command will build the Docker images for each service (API, DB, Cache) and start them in the background.
    ```sh
    docker-compose up --build -d
    ```

4.  **Run the Database Migrations:**
    To create the tables in the database, run the migration command inside the API container (example using Alembic).
    ```sh
    docker-compose exec api alembic upgrade head
    ```

5.  **You're all set!**
    * The API will be accessible at `http://localhost:8000`.
    * The interactive API documentation (Swagger UI) will be at `http://localhost:8000/docs`.

---

### Project Roadmap

* [✅] **Phase 1 (Foundation):** Project setup, Docker environment, user authentication, and Strava OAuth2 integration.
* [⬜] **Phase 2 (MVP):** Data synchronization and visualization in the mobile app. Implementation of static training plans.
* [⬜] **Phase 3 (Intelligence):** Development of the first ML models for performance and training load analysis.
* [⬜] **Phase 4 (Personalization):** Integration of the models to create adaptive training plans.
* [⬜] **Phase 5 (Interaction):** Implementation of the WhatsApp chatbot using the Twilio API.

---

### Contributing

This is currently a personal project, but contributions may be opened in the future. If you have suggestions or find bugs, please open an *Issue* on GitHub.

---

### License

This project is licensed under the MIT License. See the [LICENSE](/LICENSE) file for more details.
