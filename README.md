# ArchRouter

## Overview
ArchRouter is a Node.js-based web application built using Express.js and Pug as the templating engine. It is designed to provide a structured approach to handling routes efficiently.

## Features
- Modular routing structure
- Error handling using `http-errors`
- Logging with `morgan`
- View rendering with `pug`
- Cookie parsing with `cookie-parser`

## Tech Stack
### Backend:
- **Node.js**: JavaScript runtime environment
- **Express.js**: Web framework for Node.js
- **Pug**: Templating engine

### Middleware:
- **Morgan**: HTTP request logger
- **Cookie-Parser**: Parses cookies in requests
- **Http-Errors**: Error handling module

### Other Dependencies:
- **Child Process**: For executing shell commands
- **Debug**: Debugging utility

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/archrouter.git
   ```
2. Navigate to the project directory:
   ```sh
   cd archrouter
   ```
3. Install dependencies:
   ```sh
   npm install
   ```
4. Start the application:
   ```sh
   npm start
   ```

## Usage
- The application serves dynamic pages using `pug` templates.
- Routes are handled modularly through `app_server/routes`.
- Static files are served from the `public` directory.

## File Structure
```
archrouter/
├── app_server/
│   ├── routes/
│   │   ├── index.js
│   │   ├── users.js
│   ├── views/
│       ├── error.pug
│       ├── index.pug
├── public/
├── bin/
│   ├── www
├── package.json
├── app.js
├── README.md
```

## License
This project is licensed under the MIT License. Feel free to use and modify it as needed.

---
### Contributors
- **Your Name** (your-email@example.com)

---
Happy coding! 🚀

