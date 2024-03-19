import requests

def get_latest_stories(url):
  
  response = requests.get(url)
  content = response.text

  
  stories = []


  title_tag = "<h3>"
  
  link_tag = "<a"

  current_link = ""
  in_title_tag = False
  in_link_tag = False
  in_link_href = False
  for char in content:
    if char == title_tag[0] and not in_title_tag:
      in_title_tag = True
    elif char == title_tag[-1] and in_title_tag:
      in_title_tag = False
      if current_title:
        stories.append({"title": current_title, "link": current_link})
        current_title = ""
        current_link = ""
    
    if char == link_tag[0] and not in_link_tag:
      in_link_tag = True
    elif char == link_tag[-1] and in_link_tag:
      in_link_tag = False

    if in_link_tag and char == 'h':  
      in_link_href = True
    elif in_link_href and char == '=':
      in_link_href = False  
    elif in_link_href and char != '"':  
      current_link += char

    if in_title_tag:
      current_title += char

  return stories[:6]

url = "https://time.com/magazine/"
latest_stories = get_latest_stories(url)

print(json.dumps(latest_stories))