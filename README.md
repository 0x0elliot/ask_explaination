# Explaination for my proposal of the idea
Explaination

for example, i have a project which looks like this:

<code>/Project</code>
- <code>run.py</code>
- <code>__init__.py</code>
- <code>/static</code>
- <code>models.py</code>
- <code>apis.ask</code>

In apis.ask i have the API endpoints i want to use in my project like you can see <a href = "https://github.com/0x0elliot/ask_explaination/blob/main/apis.ask">here</a> 

And then we will import the API endpoint on our flask app like I did in this theoretical code sample <a href = "https://github.com/0x0elliot/ask_explaination/blob/main/run.py">here</a>

Then when the code is run, everything functions normally but you can also access /api/v1/products API endpoint that you wrote in ask through flask using the simple integration on the same server without needing to host the Ask server on some other port/server. I hope I got my point across. 

<h2>Why do I suggest this?</h2>

<a href = "https://github.com/Buscedv/Ask">Ask</a> is a powerful and even more simpler language for REST APIs. To make it mainstream, the best thing that you can do is help Python Backend Developers use Ask to develop Flask REST APIs even more easily without the junk. Developers always want the simplest way to get their shit done. By making Ask more Flask friendly and hopefully even more simpler in the process, we might actually be able to get other developers to pick this up. I sure would start using it if it had this feature. Heck, who wants to import jsonify and all that crap when you can just use Ask for REST APIs in your flask project.
