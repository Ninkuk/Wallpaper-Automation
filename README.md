# Wallpaper Automation
This is written for Linux computers but if you have experience with Task Schedulers you can make it work on Windows and Mac too.

## Table of Contents
- [Wallpaper Automation](#wallpaper-automation)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Linux](#linux)
      - [Cron (Scheduler) Instructions](#cron-scheduler-instructions)
      - [Bash Aliases Instructions](#bash-aliases-instructions)
    - [Windows](#windows)
      - [Task Scheduler Instructions](#task-scheduler-instructions)
      - [Add/Modify Search Terms](#addmodify-search-terms)
  - [Contributing](#contributing)
  - [License](#license)
  - [Contact Me](#contact-me)

## Installation
1. Clone this repository
```bash
$ git clone https://github.com/Ninkuk/Wallpaper-Automation.git
```
2. Use your Linux's inbuilt wallpaper tool to set the wallpaper path to `/Pictures/Wallpapers/wallpaper.jpeg`
3. Get API keys for [Pexels](https://www.pexels.com/api/) and [Unsplash](https://unsplash.com/developers)
4. Place the keys in [credentials.json](credentials.json)

## Usage
### Linux
#### Cron (Scheduler) Instructions
```bash
$ crontab -e
```
then at the bottom of the file add this line and replace `PATH_TO_FOLDER` with the path to the cloned repo location
```bash
0 * * * * cd PATH_TO_FOLDER && python3 wallpaper.py >> PATH_TO_FOLDER/wallpaper.log 2>&1
```

The cron pattern above sets a new wallpaper every hour. If you want some other scheduling pattern please refer here: https://crontab.guru/examples.html

#### Bash Aliases Instructions

To get new wallpaper on demand, add this line to your bash aliases file and replace `PATH_TO_FOLDER` with the path to the cloned repo location
```bash
alias wall='cd PATH_TO_FOLDER && python3 wallpaper.py'
```
now you can get a new wallpaper by typing the following in the terminal (make sure to reload the terminal after making change to bash aliases file)

The new wallpaper replaces the previous one which prevents waste of your storage space. If you want to "save" or "archive" a wallpaper for later use, add this line to the bash aliases file
```bash
alias archive_wall='bash PATH_TO_FOLDER/archive_wall.sh'
```
now you can archive wallpapers by typing the following in the terminal (make sure to reload the terminal after making change to bash aliases file)

### Windows
#### Task Scheduler Instructions
 - Open the Windows Task Scheduler
 - Once opened, on the right side in the Actions tab, click on Create Basic task. Once you click, the create basic task wizard opens up.
 - Define the name and description, then click on Next.
 - Specify the task frequency and also the subsequent questions about that.
 - In the Action tab, choose "Start a program"
 - Click on 'Browse' and select the `wallpaper.py` file in this folder.
 - Confirm the selections and click on Finish.

#### Add/Modify Search Terms
To add, edit or remove search keywords you can edit the [search-term.txt](search-terms.txt) file

## Contributing
Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
Distributed under the MIT License.

## Contact Me
Ninad Kulkarni - ninadk03@gmail.com

Project Link: [https://github.com/Ninkuk/Wallpaper-Automation](https://github.com/Ninkuk/Wallpaper-Automation)