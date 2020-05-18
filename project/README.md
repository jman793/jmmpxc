https://sfteng-48b1d.firebaseapp.com/ THIS IS WHERE THE WEBSITE IS HOSTED THIS IS A PUBLIC LINK

Here you will find the code for the app I am buidling for the last two sprints. For right now my end goal is to have an app that allows users to input JSON data which saves to a Database which then can be displayed on a display page. All of this data is going to be tied to user's account obviously there will likely be technical limitations on this (one problem I can forsee is if somebody puts too many json elements to load then it will cause the page to look funny) All of this will be done using angular firebase and SSO will be used to handle the login.  

From here down is after the initial commit

First commit

This commit adds in basic google sign in functionality. In all senses the SSO part of the project is completed. At this point I want to add the logout before the due date on 5/10, but nevertheless Other than logout and the JSON display the project is done. After the logout is done the rest will be by the 18th

This commit added in the ability to insert data into the cloud database system. This database is also hosted on firebase. A rundown of how this works is that I pull your display name on your google account you used to sign in (so yes this works across all of your google accounts) and have a text box that can have json data inserted into it. This creates issues because if two people had the same google display name then there would be a collision. In my opinion that is a rare enough problem that for demonstration sake I will not deal with it (Im really not sure how to deal with it, but im sure there is some way) Otherwise this commit also sets up the abstract database model that this app uses. For instance the frontend does no form of communication with the database. It is all done through a service that I created specifically for that task. This allows for a Model View Controller setup for the app, and also allows for some pretty slick and abstract code. If you look in services/db.service you can see that the code is actually very minimalistic and this is in part to the fact that the UI does nothing but pull data and send it to the service. 

One thing I wanted to achieve in this app was created a very decoupled application; meaning that the application has a lot of standalone parts that form together to create the app. I would not want an app that has a lot of parts that depend on each other because that (in my opinion) is less professional code.

Second commit

This commit adds in the ability to view your submitted data based on your google account. Keep in mind a guest account was made in order to show some dummy data if you did not want to log in. 

The idea behind this project is to show the backend capabilities of the firebase platform and the extensive API's that Google has set up. If you look at the varius .ts files in this project you can see how simple the code can be while still accomplishing a lot of legwork. I hope that it is understood that I am not much of a front end developer, and I hope that the polished code the backend offers makes up for the lack of good frontend. The name of the game here was clean and readable code. 

Looking under the services directory you can see how the backend database connections are seperate from the frontend display code. I really hope you enjoy this JSON show case of the firebase API's and what this platform can do with SSO and database features. 