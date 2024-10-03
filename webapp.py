from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

#TODO: Add an @app.route annotation and a function that creates a response based on the user input. 
#The function should set the response variable in response.html and should render the response.html template.
@app.route("/response")
def render_response():
    
    guns = request.args['guns'] 
    world = request.args['world'] 
    car = request.args['car'] 
    #The request object stores information about the request sent to the server.
    #args is an ImmutableMultiDict (like a dictionary but can have mutliple values for the same key and can't be changed)
    #The information in args is visible in the url for the page being requested. ex. .../response?color=blue
    if guns == 'Yes' and world == 'yes' and car == 'yes':
        reply1 = "You should play Far Cry 5!"
        
    elif guns == 'Yes' and world == 'Yes' and car == 'No':
        reply1 = "You should play Red Dead Redemption 2!"
        
    elif guns == 'Yes' and world == 'No' and car == 'Yes':
        reply1 = "You should play Twisted Metal!"
        
    elif guns == 'Yes' and world == 'No' and car == 'No':
        reply1 = "You should play Doom Eterna!"
        
    elif guns == 'No' and world == 'Yes' and car == 'Yes':
        reply1 = "You should play Burn Out Paradise!"
        
    elif guns == 'No' and world == 'Yes' and car == 'No':
        reply1 = "You should play Minecraft!"
        
    elif guns == 'No' and world == 'No' and car == 'Yes':
        rep1y1 = "You should play Red Dead Redemption 2!"
        
    elif guns == 'Yes' and world == 'Yes' and car == 'no':
        reply1 = "You should play F1 2023!"
        
    else:  
        reply1 = "You should play Portal 2!"
        
        

    return render_template('response.html',response = reply1)
    
    
    
if __name__=="__main__":
    app.run(debug=True)
