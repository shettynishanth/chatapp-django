![image](https://github.com/user-attachments/assets/d70ace6e-47e8-4572-bdb1-cf5b8acbe4f1)# chatapp-django
Django Chat application
GitHub Repository : https://github.com/shettynishanth/chatapp-django
URL : https://shettynishnath.pythonanywhere.com/

1.	Set up guide 
a.	Extract the Chatproject.zip file 
b.	Open the folder in any editor for example vscode
c.	Open the terminal and ensure that you are in project path 
d.	Install the required dependency by entering command 
e.	pip install -r requirements.txt
f.	next command for to make the changes of database hit the command python manage.py makemigrations
g.	to save the changes use python manage.py migrate
h.	your almost there to run the project but before that you have to set up your email to send the otp to the user while doing signup so for that 
i.	navigate setting.py file and change EMAIL_FROM and EMAIL_HOST_USER as below 


j.	 

k.	After specifying your email make sure in your google account 2F should turn on and generate the app password and specify in EMAIL_HOST_PASSWORD 

l.	One more file you have to change in views.py where change the send_mail () in generate_otp function 


 


		
2.	How to run the project 
a.	Now here we go run the command of py manage.py runserver 
b.	 
c.	Now navigate that URL in your browser which is specified here for example http://127.0.0.1:8000/ 
