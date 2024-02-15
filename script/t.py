import json

session = "{'cookies': [{'name': 'csrftoken', 'value': 'gkwAmgXMaw3eRt5R2cEuq7', 'domain': '.instagram.com', 'path': '/', 'expires': 1739374573.776701, 'httpOnly': False, 'secure': True, 'sameSite': 'Lax'}, {'name': 'mid', 'value': 'Zczd5wALAAEo7JApZnkHtfe7CZ4P', 'domain': '.instagram.com', 'path': '/', 'expires': 1742484968.453194, 'httpOnly': False, 'secure': True, 'sameSite': 'Lax'}, {'name': 'ig_did', 'value': 'DAF5C7D9-400A-4C46-A34C-57A53B2C4D62', 'domain': '.instagram.com', 'path': '/', 'expires': 1739460973.7768, 'httpOnly': True, 'secure': True, 'sameSite': 'Lax'}], 'origins': []}"
session = session.replace("'", '"').replace('True', 'true').replace('False', 'false')

# da = {
#     "cookies": [
#         {
#             "name": "csrftoken",
#             "value": "gkwAmgXMaw3eRt5R2cEuq7",
#             "domain": ".instagram.com",
#             "path": "/",
#             "expires": 1739374573.776701,
#             "httpOnly": False,
#             "secure": True,
#             "sameSite": "Lax"
#         },
#         {"name": "mid",
#          "value": "Zczd5wALAAEo7JApZnkHtfe7CZ4P",
#          "domain": ".instagram.com",
#          "path": "/",
#          "expires": 1742484968.453194,
#          "httpOnly": False,
#          "secure": True,
#          "sameSite": "Lax"
#          },
#         {"name": "ig_did",
#          "value": "DAF5C7D9-400A-4C46-A34C-57A53B2C4D62",
#          "domain": ".instagram.com",
#          "path": "/",
#          "expires": 1739460973.7768,
#          "httpOnly": True,
#          "secure": True,
#          "sameSite": "Lax"
#          }
#     ],
#     "origins": []}
print(json.loads(session))
