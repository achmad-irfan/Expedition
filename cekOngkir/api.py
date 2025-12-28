import requests

API_KEY= "J0qGyF0Ea6eeed439ded092aJHBua39T"
BASE_URL = "https://rajaongkir.komerce.id/api/v1/destination"


def get_prov():
    url = f"{BASE_URL}/province"
    headers = {
        "key": API_KEY
        }
    r = requests.get(url, headers=headers, timeout=30)
    return r.json()




def get_cities(province_id):
    url = "https://rajaongkir.komerce.id/api/v1/destination/province"
    headers = {"Key": API_KEY}
    r = requests.get(url, headers=headers, timeout=30)

    if r.status_code != 200:
        return {"data": []}

    return r.json()



    