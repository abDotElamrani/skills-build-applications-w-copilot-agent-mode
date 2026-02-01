# Octofit Tracker Frontend

## Overview

The Octofit Tracker frontend is a React application designed to provide a user-friendly interface for the Octofit Tracker fitness app. This application allows users to log activities, manage teams, and view leaderboards.

## Project Structure

The project is organized as follows:

```
octofit-tracker
├── frontend
│   ├── node_modules       # Contains all the installed npm packages
│   ├── public             # Public assets
│   │   ├── favicon.ico    # Favicon for the application
│   │   ├── index.html     # Main HTML file
│   │   └── manifest.json   # Metadata for the application
│   ├── src                # Source files for the React application
│   │   ├── App.js         # Main application component
│   │   ├── index.js       # Entry point of the React application
│   │   ├── App.css        # Styles specific to the App component
│   │   └── index.css      # Global CSS styles
│   ├── package.json       # npm configuration file
│   ├── package-lock.json  # Locks the versions of installed packages
│   └── README.md          # Documentation for the project
```

## Setup Instructions

1. **Install Dependencies**: Navigate to the `frontend` directory and run the following command to install the required packages:

   ```
   npm install
   ```

2. **Start the Development Server**: After installing the dependencies, you can start the development server with:

   ```
   npm start
   ```

   This will launch the application in your default web browser.

3. **Build for Production**: To create a production build of the application, run:

   ```
   npm run build
   ```

## Usage

- The application allows users to create and manage their profiles, log activities, and view their standings on the leaderboard.
- Users can also create teams and compete with others.

## Technologies Used

- **React**: A JavaScript library for building user interfaces.
- **Bootstrap**: A CSS framework for responsive design.
- **React Router DOM**: For handling routing within the application.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.