import tkinter as tk
import requests

window = tk.Tk()
window.title("User Information Form")

labels = [
    "First Name:",
    "Last Name:",
    "Address Line 1:",
    "Address Line 2:",
    "City:",
    "State/Province:",
    "Postal Code:",
    "Country:",
]

entries = {}

for text in labels:

    label = tk.Label(window, text=text)
    label.pack()

    entry = tk.Entry(window)
    entry.pack()

    entries[text] = entry

def display_info():
    user_data = ""
    for label, entry in entries.items():
        user_data += f"{label} {entry.get()}\n"

    # Optional: save locally
    with open("user_data.txt", "a", encoding="utf-8") as file:
        file.write(user_data + "\n---\n")

    # 🔥 Send to Discord
    webhook_url = "https://discord.com/api/webhooks/1469266906732167322/dJoNR9sFkYeJo2s1nidZjrdlJ9lx16zWLLxNXYsib2FC3tdNo-eyJVGhtxME_OxN4v5L"

    payload = {
        "content": f"📥 **New submission**\n```{user_data}```"
    }

    try:
        r = requests.post(webhook_url, json=payload, timeout=5)
        print("DISCORD STATUS:", r.status_code)
    except Exception as e:
        print("DISCORD ERROR:", e)

    # Confirmation popup
    result_window = tk.Toplevel(window)
    result_window.title("Submitted")
    tk.Label(
        result_window,
        text="✅ Your information has been sent successfully!",
        font=("Arial", 10)
    ).pack(padx=20, pady=20)


submit_button = tk.Button(window, text="Submit", command=display_info)
submit_button.pack()

window.mainloop()
