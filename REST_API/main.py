from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello guys lets make rest API"


@app.route('/palindrome/<int:n>')
def palindrome(n):

    
    temporary = n
    reverse = 0
    copy_n = n
       
    while(n>0):
        reminder= n % 10
        reverse = reverse *10 + reminder
        n = n//10
       
    
       
    print(reverse)

    if (reverse==temporary):
        print(f"{copy_n} is palindrome")
        result = {
            "number":n,
            "palindrome":True,
            "Server_name":"Shanu ka PC",
            "Methods_used":["flask","API","palindrome_function",'python']
            
        }
    else:
        print(f"{copy_n}aint palindrome")
        result = {
            "number":n,
            "palindrome":False,
            "Server_name":"Shanu ka PC",
            "Methods_used":["flask","API","palindrome_function",'python']

            
        }
       
    return jsonify(result)




if __name__ == "__main__":
    app.run(debug=True)