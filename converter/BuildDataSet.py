import opengraph
import praw
import time

import requests

from CV import split, get_net_input

import pickle

'''
r = praw.Reddit(user_agent="Cross View training set harvester, /u/space_fountain")
CV = r.get_subreddit("crossview")
new = CV.get_new(limit=300)

possible = []
for c in list(new):
    if c.score > 10:
        possible.append(c)
    time.sleep(0.1)
print("done")
urls = []
for s in possible:
    urls.append(s.url)


def get_image(url):
    r = requests.get(url)
    if r.headers["Content-Type"].split('/')[0] == "image":
        return url
    graph = opengraph.OpenGraph()
    graph.parser(r.text)
    return graph.get("image")
images = []
for u in urls:
    image = get_image(u)
    if image is not None:
        images.append(image)

pickle.dump(images, open("urls", "wb"))
'''

images = pickle.load(open("urls"))
xs = []
ys = []
i = 0.
for u in images:
    try:
        right, left = split(u)
        xs.append(get_net_input(right, left))
        ys.append([-1,])

        xs.append(get_net_input(left, right))
        ys.append([1.,])
        print(i/len(images))
        i+=1
    except:
        print("error")
        pass
print("done")
pickle.dump(xs, open("xs", "wb"))
pickle.dump(ys, open("ys", "wb"))

'''
original = ClassificationDataSet.loadFromFile("data")

ds = ClassificationDataSet(27, 2, class_labels=['CV', 'PV'])

for i, t in original:
    ds.appendLinked(i, ([1, 0] if t[0] == 0 else [0, 1]))

ds.saveToFile("data2")
'''
