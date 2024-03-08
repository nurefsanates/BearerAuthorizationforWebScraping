import requests

for yil in range(2009,2024):
    endpoint=f"url/api/vehicles/{yil}/makes.json"
    headers = {"Authorization": "Bearer Token"}
    response=requests.get(endpoint,headers=headers)

    if response.status_code==200:
        alanlar= response.json()
        print(f"Yıl {yil} için:")

        for alan1 in alanlar:
            alan1_id= alan1["id"]
            alan1_name=alan1["name"]
            print(f"\tID:{alan1_id} Alan:{alan1_name}")
            seri_endpoint = f"url/api/vehicles/{yil}/makes/{alan1_id}/series.json"
            seri_response = requests.get(seri_endpoint, headers=headers)

            if seri_response.status_code == 200:
                series = seri_response.json()
                series_names = [seri['name'] for seri in series]
                series_string = ",".join(series_names)
                print(f"\tSeriler: {series_string}")

                for seri in series:
                    seri_id = seri["id"]
                    seri_name = seri["name"]
                    detay_endpoint = f"url/api/vehicles/{yil}/makes/{alan1_id}/series/{seri_id}/trims.json"
                    detay_response = requests.get(detay_endpoint, headers=headers)

                    if detay_response.status_code == 200:
                        detaylar = detay_response.json()
                        detaylar_names = [detay["name"] for detay in detaylar]
                        detaylar_string = ",".join(detaylar_names)
                        print(f"\t{seri_name} :{detaylar_string}")
                    else:
                        print(f"\t\tHata kodu: {detay_response.status_code}")
            else:
                print(f"\t\tHata kodu: {seri_response.status_code}")
    else:
        print(f"Hata kodu:{response.status_code}")
