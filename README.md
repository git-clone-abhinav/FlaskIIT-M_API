# FlaskIIT-M_API 😏
In this project i will be making a webserver, hostied on my Raspberyy Pi, and will be making a Restfull API and then making some get requests to the api to fetch some data from a csv file

## Background: 😲
So the Pichavaram Coding Club is having an event on 28th of August 2021, and the results of the contest have to be updated on our website.
But the main problem is that our Web-Admin could be out of station for some reason, so we needed a BACKUP plan.

## Possible Solutions: 💻
We can get the access for the Source Code of the Website and hardcode it accordingly on the day of results.
Or we could make an API that can return various `STATUS_CODES`, and accordingly a web page can be displayed.


## How we did it: 🔥
This idea got me so mesmerised that i wanted to do it so badly, I told it to the club coordinator and I got a green light

### `STATUS_CODES`
🟢 **`200` meaning `OK`**

🟡 **`300` meaning `Result is yet to be declared`**

🔴 **`404` meaning `Page not found`**

Our API checks for a file called `rankers.csv` in the root directory, if it finds the file it will return the json value from the CSV with a status code of `200`.If it did not find anything there, it will return a status code of `300` meaning `Result is yet to be Declared`.

You can check our API [here](http://iot.ccnet.in:105/rankers).
As for now, we are not getting a barring criteria for the no of request we get, so please be Mindfull and use it accordingly. 🥺

Also I'd love to thank [Sachin](https://github.com/thesachinsingh) 😀 for giving me a helping hand, its hard to find someone who knows the `init.d` and `netstat` in linux now a days, xD. 😜

Thanks

Abhinav
Secretary
Pichavaram Coding Club
