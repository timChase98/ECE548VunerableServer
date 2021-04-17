<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

![Forum Image](https://i.imgur.com/YybfP3zh.jpg)

This is a vulnerable "forum" website that can be used to demonstrate the effects of a Cross-site Scripting (XSS) Attack. The website allows for user input to run without protection on the server, so that it's effects can be observed. Alternatively, the user may view a "Secure" version of the forum where these attacks are no longer viable. The end goal of this project is to showcase modern protection techniques to XSS, and how effective they may be. 


### Built With

* []() Python3
* []() Javascript
* []() HTML
* []() CSS


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

In order to run the project, pip3 is required in addition to the Django Python library.
* pip3
  ```sh
  sudo apt install pip3
  ```
* django
  ```sh
  pip3 install django
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/timChase98/ECE548VulnerableServer.git
   ```
2. Open terminal in cloned repository.
3. Run the following commands:
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```
4. Launch the server with the following command:
   ```sh
   python manage.py runserver
   ```
5. The server is being run locally on port 8000.

<!-- USAGE EXAMPLES -->
## Usage

To start, open a browser and connect to the following URL:
   ```HTML
   localhost:8000
   ```
This will bring you to the main page of the forum. Create a new thread by clicking the "Create Thread" button. From here, the user can choose a title and username. Please note, the site is not vulnerable to XSS here. After this, click the submit button.

Now XSS is usable. In either the Reply or Username input box, scripts may be run. Give it a shot by using the following script:
```HTML
   <script>alert("Hello World!")</script>
```
By pressing submit, the script will be run, and an alert will appear on the user's screen. This will occur any time the forum is loaded/refreshed.

To prevent this from happening, the user can select the "View Secure Version" hyperlink located under the Submit button. This will cause the program to "escape" when any HTML tags are encountered in a user-input box. If you ran the script mentioned earlier, you should now see it in the replies. Also note that an alert no longer appears on the user's screen.
