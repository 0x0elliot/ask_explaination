# ask_explaination
Explaination

for example, i have a project which looks like this:

/Project
- run.py
- __init__.py
- /static
- apis.ask

In apis.ask i have the API endpoints i want to use in my project like you can see <a href = "https://github.com/0x0elliot/ask_explaination/blob/main/apis.ask">here</a> 

And then we will import the API endpoint on our flask app like I did in this theoretical code sample <a href = "https://github.com/0x0elliot/ask_explaination/blob/main/run.py">here</a>

Then when the code is run, everything functions normally but you can also access /api/v1/products API endpoint that you wrote in ask through flask using the simple integration on the same server without needing to host the Ask server on some other port/server. I hope I got my point across. 
