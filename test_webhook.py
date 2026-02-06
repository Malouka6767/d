import requests

webhook_url = "https://discord.com/api/webhooks/1469261200163475479/l30GyZfP5NCsD2Mf3NeF55UQeSGBx-omKcajj29pA0ZwVciqumViFntcPbsb8qBmASej"

payload = {
    "content": "✅ Webhook test from Python"
}

r = requests.post(webhook_url, json=payload)
print(r.status_code)
print(r.text)
