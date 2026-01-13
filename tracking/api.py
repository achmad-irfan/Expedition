import requests

# API_KEY= "NNr2EmhSa6eeed439ded092aDX5XUo47"
API_KEY= "J0qGyF0Ea6eeed439ded092aJHBua39T"


def tracking_dummy(resi, courier):
    data={
        "meta": {
            "status": "success",
            "code": 200,
            "message": "Success tracking waybill"
        },
        "data": {
            "summary": {
            "courier": "jne",
            "service": "REG",
            "waybill_number": "JNE1234567890",
            "status": "DELIVERED"
            },
            "detail": {
            "origin": "Malang",
            "destination": "Palembang",
            "shipper": "PT ABC",
            "receiver": "Budi"
            },
            "history": [
            {
                "date": "2024-07-01 08:00",
                "status": "Paket diterima oleh penerima"
            },
            {
                "date": "2024-06-30 22:10",
                "status": "Paket dibawa kurir"
            },
            {
                "date": "2024-06-29 15:00",
                "status": "Paket tiba di gudang Bandung"
            },
            {
                "date": "2024-06-28 09:30",
                "status": "Paket dikirim dari Jakarta"
            }
            ]
        }
        }

    return data
    
def tracking(resi, courier, last_phone_number=None):
    url = "https://rajaongkir.komerce.id/api/v1/track/waybill"
    headers = {
    "key": API_KEY
    }

    params = {
        "awb": resi,
        "courier": courier
    }

    if last_phone_number:
        params["last_phone_number"] = last_phone_number

    data = requests.post(
        url,
        headers=headers,
        params=params,
        timeout=30
    )

    return data.json()

    
    



