# Devops All EXPS

## Exp 3 - Demonstrate Continuous Integration process in Jenkins. Build a java program every 2 minutes (addition of two numbers) residing in Github repository. 
> 1. Download Jenkins and Java of ( java of 11 , 17 or 21 ) .
> 2. Create a Job called sum
> 3. First build the job (run it) ( without running the job , the workspace folder will not be visible )
> 4. go to C:\ProgramData\Jenkins\.jenkins\workspace\(your_job_name) place your java file here .
> 5. copy AdditionProgram.java from here and place that in your workspace .
> 6. `javac AdditionProgram.java`
> 7. `java AdditionProgram`
> 8.  copy this two command to run java and paste it in the (Execute Windows batch command) from  configure/build environments
> 9.  Apply and save it and build the JOB , check output in console output section.
> 10. Done

## EXP 4 - Demonstrate CI/CD in Jenkins. Consider 3 html files in Github repository and write a declarative pipeline to deploy on Xampp server.
> 1. Download Xampp download the first one ( https://www.apachefriends.org/download.html ) , create a repo and add index.html (dummy data ) 0r use this repo.
> 2. Refer https://chat.openai.com/share/8b4c823e-211c-486f-8b4d-0a95a6603e68
> 3. copy the code from above Xampp file ( make sure to change the path of github from the code if you are using ur own account ) 
> 4. go to `configure` of the job and paste it in pipeline section's script.
> 5. save and run it.
> 6. go to C:\xampp\htdocs , you will find index.html open it , Done 


## EXP 5 - Create an image of php project and push on Dockerhub repository.
> 1. install docker https://www.docker.com/products/docker-desktop
> 2. create a folder
> 3. create a DockerFile and a php file
> 4. Refer https://chat.openai.com/share/1339d6c3-116e-41d7-895a-8b9d894de9f4
> 5. 
