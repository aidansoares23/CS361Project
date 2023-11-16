# CS361 Project - Microservice Instructions

To request data, the microservice must be ran locally. Save NP_rng.py in your directory with your National Park app, and then navigate to your terminal. Once in your terminal, change directories until you have arrived at the working directory that the apps are saved here. Here, we will run the app.

The command `python NP_rng.py` will start a local development server. Now that that microservice is up, we can begin to make requests. 

Assuming the National Parks app is ready and the user is seeking a random park, they will enter `1` or `generate random park` into the command line. This will prompt the program to begin searching for a park. One way to do this is creating a method to request a random park and save the response into a new variable. Here is an example method that requests a park and a save the response.

`def get_random_park_from_microservice(self):
    microservice_url = "http://127.0.0.1:5000/generate_random_park"  # Adjust the URL if needed
    response = requests.get(microservice_url)
    if response.status_code == 200:
        data = response.json()
        return data.get("random_park", "Failed to get a random park")
    else:
        print("Failed to connect to the microservice")`


One way to call this method may be
`#if user has selected random park...
random park = self.get_random_park_from_microservice()
print(f"Randomly Generated Park: {random_park}")
`

And you will have successfully used the National Park Randomly Generation Microservice to print a random park for your user!
