>Апишки для бриджа 
> Twitter
> POST
> http://70.34.218.151:83/api/drop/twitter
```
{
    "address":"0x479268D467648bb567Db1b8FD3b7549498db71Fc",
    "twitter_username":"@IKozhamniyazov"
}
```
##### D случаи успеха
```
{
    "code": 200,
    "status": [
        {
            "code": 200,
            "message": "Success"
        }
    ]
}
```
##### Не валидный адрес
```
{
   "code": 404,
   "errors": [
       {
           "message": "User address is not valid",
           "code": 404
       }
   ]
}, 404
```
##### Если пользователь уже получал токены
```
{
   "code": 403,
   "errors": [
       {
           "message": f"User with this username: {twitter_username}  and address {address} already get free tokens ",
           "code": 403
       }
   ]
}, 403
```



> Tiktok 
> http://70.34.218.151:83/api/drop/tiktok
> POST
```
{
    "address":"0x479268D467648bb567Db1b8FD3b7549498db71Fc",
    "tiktok":"https://www.tiktok.com/@tmqtoday/video/7110541981532654849?is_copy_url=1&is_from_webapp=v1&lang=ru-RU"
}
```
##### В слечаи успеха
```
{
    "code": 200,
    "status": [
        {
            "code": 200,
            "message": "Success"
        }
    ]
}
```
##### Ecли не валидный хэш тэг 
```
{
   "code": 403,
   "status": [
       {
           "message": "No valide hashtag",
           "code": 403
       }
   ]
}, 200
```


##### Если пользователь уже зарестрирован 
```
{
   "code": 403,
   "status": [
       {
           "message": "User with address and this tiktok already exists",
           "code": 403
       }
   ]
}, 200
```