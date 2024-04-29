# Devops All EXPS

> Make sure to change the github URL in `Expthree` `jenkinsFile` if you are shifting to your own repo . even if you dont change it , the program will run as usual 

## Exp 2 - Demonstrate Building java program (addition of 2 numbers) through Jenkins.
> 1. Download Jenkins and Java of ( java of 11 , 17 or 21 ) .
> 2. Create a Job called jenexp3
> 3. go to `configure` in the Pipeline section , select definition as Pipeline with SCM
> 3. Enter the github URL.
> 4. Change the branch to main in ( Branches to build section )
> 5. script path input should be given as  `ExpThree` ( IMPORTANTTTTTTT )
> 6. save and run it. 
> 7. Done
> 8. Files which are used here are `AdditionProgram.java` and `ExpThree` file you can copy those and add them in ur repo.

## EXP 3 - Demonstrate Continuous Integration process in Jenkins. Build a java program every 2 minutes (addition of two numbers) residing in Github repository. 
> 1. Download Jenkins and Java of ( java of 11 , 17 or 21 ) .
> 2. Create a Job called sum
> 3. go to C:\ProgramData\Jenkins\.jenkins\workspace\(your_job_name) and check if its available (if workspace not available then build the JOB first then check for it it will be visible )
> 4. copy AdditionProgram.java from here and place that in your workspace/(your_job_name) .
> 5. `javac AdditionProgram.java`
> 6. `java AdditionProgram`
> 7.  copy this two command to run java and paste it in the (Execute Windows batch command) from  (your_job_name)/configure/build environments
 ![image](https://github.com/jamAL108/DEVOPS/assets/115083239/e10b54b9-0b68-477e-b5af-7e6b080c9986)
> 8.  Apply and save it and build the JOB , check output in console output section.
> 9. Done
> 10. Files which are used here are `AdditionProgram.java` file you can copy those and add them in ur repo.


## EXP 4 - Demonstrate CI/CD in Jenkins. Consider 3 html files in Github repository and write a declarative pipeline to deploy on Xampp server.
> 1. Download Xampp download the first one ( https://www.apachefriends.org/download.html ) , create a repo and add index.html (dummy data ) 0r use this repo.
> 2. copy the code from above Xampp file ( make sure to change the path of github from the code if you are using ur own account ) 
> 3. go to `configure` of the job and paste it in pipeline section's script.
> 4. save and run it.
> 5. go to C:\xampp\htdocs , you will find index.html open it , Done .
> 8. Files which are used here are  `declarative.html` and `index.html` file you can copy those and add them in ur repo.

## EXP 5 - Demonstrate CI/CD in Jenkins. Consider 3 html files in Github repository and write a declarative pipeline to deploy on Xampp server.
> 1. create a new JOB .
> 2. go to `configure` in the Pipeline section , select definition as Pipeline with SCM and selecct git 
> 3. Enter the github URL.
> 4. Change the branch to main in ( Branches to build section )
> 5. script path input should be given as  `JenkinsFile` ( IMPORTANTTTTTTT )
> 6. save and run it.
> 7. go to C:\xampp\htdocs , you will find index.html , declarative.html open it , Done .
> 8. Files which are used here are `JenkinsFile` and `declarative.html` and `index.html` file you can copy those and add them in ur repo.

## EXP 6 - Write a Selenium script to perform automated testing. 
> 1. copy the selenium.py from above
> 2. create a folder place the file there
> 3. run the command `pip install selenium`
> 4. run the code in vscode or online collab
> 5. chrome will open and microsoft BIng will open automatically.
> 6. Experiment Done.
> 7. Files which are used here are Selenium.py file you can copy those and add them in ur repo

## EXP 7 - Create an image of php project and push on Dockerhub repository.
> 1. install docker https://www.docker.com/products/docker-desktop  check system req for any problem ( https://docs.docker.com/desktop/install/windows-install/ )
> 2. create a folder
> 3. create a DockerFile and a php file
> 4. Refer https://chat.openai.com/share/1339d6c3-116e-41d7-895a-8b9d894de9f4
