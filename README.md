# iti0102-2022

## Description
This project contains solutions for exercises given in the course iti0102-2022 - Programming for beginners. <br>

Lecturer: Ago Luberg
This project is written in Python3.

## Sections
This project is divided into sections starting from basics to advanced.

### [ex00_intro](./EX/ex00_intro)
### [ex01_hello](./EX/ex01_hello)
### [ex02_math](./EX/ex02_math)
### [ex03_idcode](./EX/ex03_idcode)
### [ex04_lists](./EX/ex04_lists)
### [ex05_hobbies](./EX/ex05_hobbies)
### [ex06_regex](./EX/ex06_regex)
### [ex07_files](./EX/ex07_files)
Notes:
```Python3
# Opens file with the name "some_file.txt" in reading mode.
file = open("some_file.txt", "r")
# Reads n characters from file. If !n, reads the whole file.
# Attempt to read from closed file raises ValueError: I/O operation on closed file.
file.read(n)
# Reads a text row from file, but not more than n characters from it.
# Returns \n also.
file.readline(n)
# Reads n rows from file.
# Returns a list of lines.
# Returns \n at the end of the element.
file.readlines(n)
# Closes the file.
file.close()
# Opens file with name of "some_file.txt" and closes it afterwards automatically.
with open("some_file") as file:
    for line in file:  # Loops over the lines in file.
        # Do something
# For reading csv files, csv module needs to be imported.
import csv
# Opens the file for operation.
with open("some_file.csv") as csv_file:
    # Saves the file as a csv.reader object and separates the lines in file to list of strings
    # which were separated by the delimiter.
    csv_reader = csv.reader(csv_file, delimiter=",")
    # Loops over the lines in file.
    for row in csv_reader:
        # Do something

```

```Python3
# Opens file with the name "some_file.txt" in writing mode and creates it if it does not exist.
file = open("some_file.txt", "w")
# Writes text to the file. If there is some content already, overwrites it.
file.write("Some text to write.")
# Adds text right after the last text (no new line).
file.write("Write some more.")
# Closes file
file.close()
# Opens the file to add text to the end.
file = open("some_file.txt", "a")
# For writing into csv file, csv module needs to be imported.
import csv

data_to_write = [
    ['First', 'Second', 'Third']
    [1, 2, 3]
]
# Newline needs to be "", because csv-writer adds \n by itself.
with open("some_file.csv"), "w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=";")
    # Write header.
    csv_writer.writerow(['First column', 'Second column', 'Third column'])
    for row in data:
        # Write list of values
        csv_writer.writerow(row)
```
### [ex08_ex05_hobbies](./EX/ex08_ex05_hobbies)
### [ex08_oop_tests](./EX/ex08_oop_tests)
### [ex08_solution_and_tests](./EX/ex08_solution_and_tests)
### [ex09_recursion](./EX/ex09_recursion)
### [ex10_oop](./EX/ex10_oop)
Notes:
```Python3


```
### [ex11_alchemy](./EX/ex11_alchemy)
### [ex12_adventure](./EX/ex12_adventure)
### [ex13_api](./EX/ex13_api)
### [ex14_robot](./EX/ex14_robot)
### [ex15_santas_workshop](./EX/ex15_santas_workshop)


## Badges
On some READMEs, you may see small images that convey metadata, such as whether or not all the tests are passing for the project. You can use Shields to add some to your README. Many services also have instructions for adding a badge.

## Visuals
Depending on what you are making, it can be a good idea to include screenshots or even a video (you'll frequently see GIFs rather than actual videos). Tools like ttygif can help, but check out Asciinema for a more sophisticated method.

## Installation
Within a particular ecosystem, there may be a common way of installing things, such as using Yarn, NuGet, or Homebrew. However, consider the possibility that whoever is reading your README is a novice and would like more guidance. Listing specific steps helps remove ambiguity and gets people to using your project as quickly as possible. If it only runs in a specific context like a particular programming language version or operating system or has dependencies that have to be installed manually, also add a Requirements subsection.

## Usage
Use examples liberally, and show the expected output if you can. It's helpful to have inline the smallest example of usage that you can demonstrate, while providing links to more sophisticated examples if they are too long to reasonably include in the README.

## Support
Tell people where they can go to for help. It can be any combination of an issue tracker, a chat room, an email address, etc.

## Roadmap
If you have ideas for releases in the future, it is a good idea to list them in the README.

## Contributing
State if you are open to contributions and what your requirements are for accepting them.

For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.

You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.

## Authors and acknowledgment
Show your appreciation to those who have contributed to the project.

## License
For open source projects, say how it is licensed.

## Project status
If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.

***********************************************************************

## Getting started

To make it easy for you to get started with GitLab, here's a list of recommended next steps.

Already a pro? Just edit this README.md and make it your own. Want to make it easy? [Use the template at the bottom](#editing-this-readme)!

## Add your files

- [ ] [Create](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#create-a-file) or [upload](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#upload-a-file) files
- [ ] [Add files using the command line](https://docs.gitlab.com/ee/gitlab-basics/add-file.html#add-a-file-using-the-command-line) or push an existing Git repository with the following command:

```
cd existing_repo
git remote add origin https://gitlab.cs.ttu.ee/kkikas/iti0102-2022.git
git branch -M main
git push -uf origin main
```

## Integrate with your tools

- [ ] [Set up project integrations](https://gitlab.cs.ttu.ee/kkikas/iti0102-2022/-/settings/integrations)

## Collaborate with your team

- [ ] [Invite team members and collaborators](https://docs.gitlab.com/ee/user/project/members/)
- [ ] [Create a new merge request](https://docs.gitlab.com/ee/user/project/merge_requests/creating_merge_requests.html)
- [ ] [Automatically close issues from merge requests](https://docs.gitlab.com/ee/user/project/issues/managing_issues.html#closing-issues-automatically)
- [ ] [Enable merge request approvals](https://docs.gitlab.com/ee/user/project/merge_requests/approvals/)
- [ ] [Automatically merge when pipeline succeeds](https://docs.gitlab.com/ee/user/project/merge_requests/merge_when_pipeline_succeeds.html)

## Test and Deploy

Use the built-in continuous integration in GitLab.

- [ ] [Get started with GitLab CI/CD](https://docs.gitlab.com/ee/ci/quick_start/index.html)
- [ ] [Analyze your code for known vulnerabilities with Static Application Security Testing(SAST)](https://docs.gitlab.com/ee/user/application_security/sast/)
- [ ] [Deploy to Kubernetes, Amazon EC2, or Amazon ECS using Auto Deploy](https://docs.gitlab.com/ee/topics/autodevops/requirements.html)
- [ ] [Use pull-based deployments for improved Kubernetes management](https://docs.gitlab.com/ee/user/clusters/agent/)
- [ ] [Set up protected environments](https://docs.gitlab.com/ee/ci/environments/protected_environments.html)

