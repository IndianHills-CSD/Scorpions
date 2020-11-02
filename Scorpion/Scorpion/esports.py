import json
import requests

url = 'https://api.pandascore.co/tournaments?token=tvb8UQMtqygWbQ-PdM39gX-l_LkxNKHDlRn9PCx5C8TRqeTYHvs'

response = requests.get(url)

print(response.status_code)
tournaments = response.json()

print(tournaments[1]['begin_at'])