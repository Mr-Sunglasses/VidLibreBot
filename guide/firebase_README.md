# Sollutions
><b> if you are facing issues with database read and write than goto your firebase ptoject than realtime database than Rules than change the values of '.read' and '.write' to true and click on publish (ignore the warnMings)</b><br>

# Requirements
><B> pyrebase module for python - <I><B>pip install pyrebase <br>
> create a project in firebase <br>
> enable authentication with email and passowrd <br>
> create firebase realtime data base<br>
> goto Project settings - General - click on Add app<br>
> choose web app <br>
> On Register app git it a name than click on register app<br>
> then copy the fireabseConfig and past it inside firebase.py in the way of python dictaitionary as shown there in the firebase.py module <br>
> check if it contains key value pair of database url if it doesnt than add "databaseURL": " your database link here "<br>
>    - to get fatabase link go to realtime database than click on 🔗 icon <br>
> then again go to project settings - Service accounts - click on  Generate new private key <br>
> then copy the file content into 'serviceAccountKey.json'<br>
> now you are good to go 👍🏿<br>
