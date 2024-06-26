import uuid
import requests
import json
import random
import string

# First API request
url1 = "https://europe-west1-mobilfox-prod.cloudfunctions.net/api/v1/auth"

headers1 = {
    "Host": "europe-west1-mobilfox-prod.cloudfunctions.net",
    "X-Device-Id": "eea42864a9a84735",
    "Authorization": "Bearer",
    "X-Shopify-Customer-Access-Token": "5732becff54c1b89d905ec338bb421ff",
    "Content-Type": "application/json; charset=utf-8",
    "Accept-Encoding": "gzip, deflate, br",
    "User-Agent": "okhttp/4.12.0"
}

data1 = {
    "countryCode": "RO",
    "phone": "+40771404568",
    "email": "denisdenis77717@gmail.com"
}

response1 = requests.post(url1, headers=headers1, json=data1)
response_data1 = response1.json()
print(response1.text)
data_token = response_data1.get('data', 'No data key found')
print("Data Token: ", data_token)
# Second API request

def send_delete_request(idToken):
    url6 = "https://europe-west1-mobilfox-prod.cloudfunctions.net/api/v1/user"
    headers6 = {
        "Host": "europe-west1-mobilfox-prod.cloudfunctions.net",
        "Authorization": f"Bearer {idToken}",
        "X-Shopify-Customer-Access-Token": "af11e8ddb388bda619495149db1ab6ba",
        "Accept-Encoding": "gzip, deflate, br",
        "User-Agent": "okhttp/4.12.0"
    }
    response6 = requests.delete(url6, headers=headers6)
    print(response6.status_code)
    print(response6.text)

def random_string(length):
    return ''.join(random.choices(string.ascii_letters, k=length))

def random_digits(length):
    return ''.join(random.choices(string.digits, k=length))

def generate_random_email(domain=None):
    if domain is None:
        domain = "example.com"
    name = random_string(random.randint(5, 15))
    address = f"{name}@{domain}"
    return address

def generate_random_ro_phone():
    # For a Romanian phone number, the country code is (+40) followed by a 9-digit number.
    # The following formats are common: 07xx, 03xx, 02xx, 08xx, and 037
    prefixes = ['07', '03', '02', '08', '037']
    prefix = random.choice(prefixes)
    local_number = random_digits(7) if prefix != '037' else random_digits(6)
    phone_number = f"+40{prefix}{local_number}"
    return phone_number

random_email = generate_random_email()
random_phone = generate_random_ro_phone()

url2 = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyCustomToken?key=AIzaSyCSZKPKMkdVnFkIM8ntwwpDYbx4rrEkH3g"
headers2 = {
    "Content-Type": "application/json",
    "X-Android-Package": "com.bitraptors.mobilfox",
    "X-Android-Cert": "5D015420F96CDB1D592C6AB2B68CD97222769CC1",
    "Accept-Language": "en-US",
    "X-Client-Version": "Android/Fallback/X22003001/FirebaseCore-Android",
    "X-Firebase-Gmpid": "1:1065362310606:android:bde93f488b69a773d7979f",
    "X-Firebase-Client": "H4sIAAAAAAAAAKtWykhNLCpJSk0sKVayio7VUSpLLSrOzM9TslIyUqoFAFyivEQfAAAA",
    "X-Firebase-Appcheck": "eyJlcnJvciI6IlVOS05PV05fRVJST1IifQ==",
    "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 11; SM-S908E Build/TP1A.220624.014)",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip, deflate, br"
}
data2 = {
    "token": data_token,
    "returnSecureToken": True
}
response2 = requests.post(url2, headers=headers2, data=json.dumps(data2))
idToken = response2.json().get("idToken", "idToken field not found")
print("idToken: ", idToken)


url4 = "https://europe-west1-mobilfox-prod.cloudfunctions.net/api/v1/user"

headers4 = {
    "Host": "europe-west1-mobilfox-prod.cloudfunctions.net",
    "Authorization": f"Bearer {idToken}",
    "X-Shopify-Customer-Access-Token": "5732becff54c1b89d905ec338bb421ff",
    "Content-Type": "application/json; charset=utf-8",
    "Accept-Encoding": "gzip, deflate, br",
    "User-Agent": "okhttp/4.12.0"

}
data4 = {
    "email": generate_random_email(),
    "phone": generate_random_ro_phone(),
    "countryCode": "RO",
    "dateOfBirth": "2001-06-12",
    "gender": "gender_man",
    "phoneType": "Apple Iphone 13"
}

response4 = requests.post(url4, headers=headers4, data=json.dumps(data4))
response_data4 = response4.json()
referral_code = response_data4.get('data', {}).get('referralCode', 'No referralCode found')
print(response4.text)
print("Referral Code: ", referral_code)

if "error" in response_data4 and response_data4["error"] == "User already exists":
    print("Error: User already exists.")
    send_delete_request(idToken)
    exit()

def add_spins(referral_code):
    custom_user_agent = "Mozilla/5.0 (Linux; Android 12; Pixel; CustomAgent) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Mobile Safari/537.36"

    def generate_device_id():
        unique_id = uuid.uuid4()
        device_id = unique_id.hex[:16]
        return device_id

    def random_string(length):
        return ''.join(random.choice(string.ascii_letters) for _ in range(length))

    def random_phone():
        return '+4077' + ''.join(random.choice(string.digits) for _ in range(7))

    def random_email():
        first_names = [
            'Andrei', 'Ana', 'Ion', 'Maria', 'Vasile', 'Elena', 'Gheorghe', 'Camelia', 'Nicolae', 'Gabriela',
            'Cristian', 'Ioana', 'Adrian', 'Mihai', 'Camelia', 'Mihaela', 'Oana', 'Alexandru', 'Alina', 'Marius',
            'Dorina', 'Sergiu', 'Monica', 'Daniel', 'Larisa', 'Florentin', 'Madalina', 'Florin', 'Constantin', 'Petre'
        ]
        last_names = [
            'Popescu', 'Ionescu', 'Mihai', 'Dumitrescu', 'Popa', 'Marin', 'Stan', 'Stefan',
            'Radu', 'Dumitru', 'Nica', 'Pascal', 'Neagu', 'Lupu', 'Iliescu', 'Barbu',
            'Coman', 'Diaconu', 'Nistor', 'Preda', 'Voicu', 'Manolache', 'Moldovan', 'Georgescu'
        ]
        first_name = random.choice(first_names).lower()
        last_name = random.choice(last_names).lower()
        return f'{first_name}.{last_name}{random.randint(1, 999)}@gmail.com'

    def random_access_token():
        return ''.join(random.choice(string.hexdigits) for _ in range(32))

    def get_shopify_customer_access_token(email, first_name, last_name, phone):
        url = "https://mobilfox-ro.myshopify.com/api/2024-01/graphql"
        headers = {
            "Host": "mobilfox-ro.myshopify.com",
            "Accept": "application/json",
            "X-Buy3-Sdk-Cache-Key": "",
            "X-Buy3-Sdk-Cache-Fetch-Strategy": "NETWORK_ONLY",
            "X-Buy3-Sdk-Expire-Timeout": "9223372036854775807",
            "User-Agent": "Mobile Buy SDK Android/16.3.0/com.bitraptors.mobilfox",
            "X-Sdk-Version": "16.3.0",
            "X-Sdk-Variant": "android",
            "X-Shopify-Storefront-Access-Token": "f23e91a899d7906fb2c9f547c425c1af",
            "Content-Type": "application/graphql; charset=utf-8",
            "Accept-Encoding": "gzip, deflate, br"
        }

        mutation_create_customer = f"""
        mutation {{
            customerCreate(input:{{
                email:"{email}",
                password:"Sisilaputere_7",
                firstName:"{first_name}",
                lastName:"{last_name}",
                phone:"{phone}",
                acceptsMarketing:false
            }}){{
                customerUserErrors{{
                    field,
                    message,
                    code
                }}
            }}
        }}
        """

        response = requests.post(url, headers=headers, data=mutation_create_customer)
        print(response.status_code)
        print(response.text)

        mutation_access_token = f"""
        mutation {{
            customerAccessTokenCreate(input:{{
                email:"{email}",
                password:"Sisilaputere_7"
            }}){{
                customerAccessToken{{
                    accessToken,
                    expiresAt
                }},
                customerUserErrors{{
                    field,
                    message,
                    code
                }}
            }}
        }}
        """

        response = requests.post(url, headers=headers, data=mutation_access_token)
        print(response.status_code)
        print(response.text)
        response_json = response.json()
        access_token = response_json.get('data', {}).get('customerAccessTokenCreate', {}).get('customerAccessToken', {}).get('accessToken', 'Access token not found')


        
        return access_token

    def get_id_token(data_token):
        url = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyCustomToken?key=AIzaSyCSZKPKMkdVnFkIM8ntwwpDYbx4rrEkH3g"
        headers = {
            'Host': 'www.googleapis.com',
            'Content-Type': 'application/json',
            'X-Android-Package': 'com.bitraptors.mobilfox',
            'X-Android-Cert': '5D015420F96CDB1D592C6AB2B68CD97222769CC1',
            'Accept-Language': 'en-US',
            'X-Client-Version': 'Android/Fallback/X22003001/FirebaseCore-Android',
            'User-Agent': custom_user_agent,
            'Accept-Encoding': 'gzip, deflate, br'
        }
        data = {
            "token": data_token,
            "returnSecureToken": True
        }
        response = requests.post(url, headers=headers, data=json.dumps(data))
        print(response.status_code)
        print(response.text)
        response_json = response.json()
        id_token = response_json.get("idToken", "Refresh token not found")
        return id_token


    def submit_user_data(id_token, phone_number, dob, phone_type):
        url = "https://europe-west1-mobilfox-prod.cloudfunctions.net/api/v1/user"
        headers = {
            "Host": "europe-west1-mobilfox-prod.cloudfunctions.net",
            "Authorization": f"Bearer {id_token}",
            "X-Shopify-Customer-Access-Token": x_shopify_customer_access_token,
            "Content-Type": "application/json; charset=utf-8",
            "Accept-Encoding": "gzip, deflate, br",
            "User-Agent": custom_user_agent
        }
        data = {
            "email": random_email(),
            "phone": phone_number,
            "countryCode": "RO",
            "dateOfBirth": dob,
            "gender": "gender_other",
            "phoneType": phone_type,
            "referralCode": referral_code
        }

        response = requests.post(url, headers=headers, data=json.dumps(data))
        print(response.status_code)
        print(response.text)

    date_of_birth_list = ["1993-05-21", "1985-12-12", "2000-09-30", "1972-03-10"]
    phone_type_list = [
        "Samsung Galaxy S20",
        "Apple iPhone 13 Pro",
        "Google Pixel 5",
        "OnePlus 9 Pro",
    ]

    num_iterations = 5

    for i in range(num_iterations):
        print(f"\nIteration {i+1}:")

        random_dob = random.choice(date_of_birth_list)
        random_phone_type = random.choice(phone_type_list)

        x_device_id = generate_device_id()
        random_phone_number = random_phone()
        random_email_address = random_email()

        first_name = random_email_address.split('.')[0]
        last_name = random_email_address.split('.')[1].split('@')[0]

        print(f"X-Device-Id: {x_device_id}")
        print(f"Random Phone: {random_phone_number}")
        print(f"Random Email: {random_email_address}")
        print(f"First Name: {first_name}")
        print(f"Last Name: {last_name}")

        x_shopify_customer_access_token = get_shopify_customer_access_token(
            random_email_address, first_name, last_name, random_phone_number
        )
        print(f"X-Shopify-Customer-AccessToken: {x_shopify_customer_access_token}")

        url = 'https://europe-west1-mobilfox-prod.cloudfunctions.net/api/v1/auth'
        headers = {
            'Host': 'europe-west1-mobilfox-prod.cloudfunctions.net',
            'X-Device-Id': x_device_id,
            'Authorization': 'Bearer',
            'X-Shopify-Customer-Access-Token': x_shopify_customer_access_token,
            'Content-Type': 'application/json; charset=utf-8',
            'Accept-Encoding': 'gzip, deflate, br',
            'User-Agent': custom_user_agent
        }

        data = {
            "countryCode": "RO",
            "phone": random_phone_number,
            "email": random_email_address
        }

        response = requests.post(url, headers=headers, data=json.dumps(data))
        print(response.status_code)
        print(response.text)

        response_json = response.json()
        data_value = response_json.get('data', 'Data not found')


        id_token = get_id_token(data_value)
        print(f"ID token: {id_token}")

        submit_user_data(id_token, random_phone_number, random_dob, random_phone_type)

def send_to_discord(name, code, imageUrl, webhook_url):
    payload = {
        "content": None,
        "embeds": [
            {
                "title": name,
                "description": f"Code: {code}",
                "image": {
                    "url": imageUrl
                }
            }
        ],
        "username": "Spin Bot"
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
    if response.status_code == 204:
        print(f"Successfully sent {name} with code {code} to Discord webhook.")
    else:
        print(f"Failed to send to Discord webhook. Status code: {response.status_code}, Response: {response.text}")

def get_remaining_spins(idToken):
    url7 = "https://europe-west1-mobilfox-prod.cloudfunctions.net/api/v1/user/remaining-spins"
    headers7 = {
        "Host": "europe-west1-mobilfox-prod.cloudfunctions.net",
        "Authorization": f"Bearer {idToken}",
        "X-Shopify-Customer-Access-Token": "af11e8ddb388bda619495149db1ab6ba",
        "Accept-Encoding": "gzip, deflate, br",
        "User-Agent": "okhttp/4.12.0"
    }

    response7 = requests.get(url7, headers=headers7)
    print(response7.status_code)
    print(response7.text)

    remaining_spins_data = response7.json()
    daily_spins = remaining_spins_data["data"]["dailySpins"]
    extra_spins = remaining_spins_data["data"]["extraSpins"]

    return daily_spins + extra_spins

def send_spin_request(idToken, count=17):
    def get_remaining_spins(idToken):
        url_remaining_spins = "https://europe-west1-mobilfox-prod.cloudfunctions.net/api/v1/user/remaining-spins"
        headers_remaining_spins = {
            "Host": "europe-west1-mobilfox-prod.cloudfunctions.net",
            "Authorization": f"Bearer {idToken}",
            "X-Shopify-Customer-Access-Token": "af11e8ddb388bda619495149db1ab6ba",
            "Accept-Encoding": "gzip, deflate, br",
            "User-Agent": "okhttp/4.12.0"
        }
        response_remaining_spins = requests.get(url_remaining_spins, headers=headers_remaining_spins)
        remaining_spins_data = response_remaining_spins.json()
        daily_spins = remaining_spins_data["data"]["dailySpins"]
        extra_spins = remaining_spins_data["data"]["extraSpins"]
        return daily_spins + extra_spins

    def send_to_discord(webhook_url, item_name, code, image_url):
        payload = {
            "content": None,
            "embeds": [
                {
                    "title": item_name,
                    "description": f"Code: {code}",
                    "image": {
                        "url": image_url
                    }
                }
            ],
            "username": "Spin Bot"
        }
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
        if response.status_code == 204:
            print(f"Successfully sent {item_name} with code {code} to Discord webhook.")
        else:
            print(f"Failed to send to Discord webhook. Status code: {response.status_code}, Response: {response.text}")

    url5 = "https://europe-west1-mobilfox-prod.cloudfunctions.net/api/v1/spin"
    headers5 = {
        "Host": "europe-west1-mobilfox-prod.cloudfunctions.net",
        "Authorization": f"Bearer {idToken}",
        "X-Shopify-Customer-Access-Token": "af11e8ddb388bda619495149db1ab6ba",
        "Content-Length": "0",
        "Accept-Encoding": "gzip, deflate, br",
        "User-Agent": "okhttp/4.12.0"
    }

    spins_done = 0
    while spins_done < count:
        response5 = requests.post(url5, headers=headers5)
        print(response5.status_code)
        print(response5.text)

        if response5.status_code != 200:
            print("DEBUG: Spin request failed")
            remaining_spins = get_remaining_spins(idToken)
            print(f"Remaining Spins: {remaining_spins}")
            if remaining_spins == 0:
                send_delete_request(idToken)
                break
            continue

        response_json = response5.json()
        if "data" in response_json and "reward" in response_json["data"]:
            item_name = response_json["data"]["reward"].get("name", "No reward name found")
            code = response_json["data"].get("code", "No code found")
            image_url = response_json["data"]["reward"].get("imageUrl", "No image URL found")

            common_titles = [
                "gift_nano_glass_title",
                "gift_lazy_strap_title",
                "no_gift_title",
                "gift_grinder_title",
                "gift_badge_title",
                "gift_cross_body_title",
                "gift_5_off_coupon_title",
                "another_chance_to_spin_title"
            ]

            if item_name != "another_chance_to_spin_title":
                if item_name not in common_titles:
                    webhook_url = "https://discord.com/api/webhooks/1251470465822625845/eHsvE2mm9qQed-otK_W8GtOQUgttuN_cdkokvOaY-YLYv71fMOZAMxYsHo7AGQbe_tPV"
                else:
                    webhook_url = "https://discord.com/api/webhooks/1251241479230460015/C6BIaJgZ38E46xc4oASZ6vKqWtIsXzejbv4zcbHYCu7bi4vAWlpcsbImKT_Emco0w4um"

                send_to_discord(webhook_url, item_name, code, image_url)
                spins_done += 1
        else:
            print("DEBUG: No more spins available")
            remaining_spins = get_remaining_spins(idToken)
            print(f"Remaining Spins: {remaining_spins}")
            if remaining_spins == 0:
                send_delete_request(idToken)
                break
            else:
                count += remaining_spins - spins_done  # Adjust count for any spins already done



add_spins(referral_code)
send_spin_request(idToken)
