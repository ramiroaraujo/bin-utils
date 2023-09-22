import http.client
import json


def make_request(payload):
    conn = http.client.HTTPConnection("localhost:8009")

    headers = {
        'Content-Type': "application/json",
        'User-Agent': "insomnia/2023.5.8",
        'X-LINKEDIN-API-Key': "4f4a38e7-20c4-4b7e-8d1f-3bbcc318450a"
    }

    conn.request("POST", "/external/linkedin", json.dumps(payload), headers)
    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))


if __name__ == '__main__':
    payloads_str = '[{"status": 422, "payload": {"bodyPlain": "body", "resumeUrl": "url here"}}, {...}]'
    payloads = json.loads(payloads_str)

    for payload in payloads:
        make_request(payload)
