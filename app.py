#import the website package and grab the app fucntion defined to use that to actually create an application and run it
from website import create_app 



if __name__ == '__main__': #this means only if we run this main.py file not when we import then run the debug otherwise everytime we import main.py the server will start
    app = create_app()
    app.run(debug=True)
    