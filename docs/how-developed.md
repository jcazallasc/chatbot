# Chatbot: How it was developed

- I created two models: CustomUser and Notification. CustomUser extends the AbstractUser adding the phone field and editing the email field. On the other hand, the Notification model will store all notifications to be sent. In this way, the process of sending notifications will be in the background.

- I create an endpoint to list and create users `http://localhost:8000/api/v1/users/`. Using the method GET it will list all users. Using the method POST it will create a new user with the body data (username, email, and phone).

- I created a Django command to digest all pending notifications (in blocks of 10). I set up a cron job in the Dockerfile to execute this command every minute.

- All features are in PR's and they have tests.