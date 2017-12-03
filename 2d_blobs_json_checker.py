import json

filename = '2d_blobs.json'
with open(filename, 'r') as file:
    data = json.load(file)

print('times: ', len(data))

for t in data.keys():
    assert len(data[t]) == 100
    for s in data[t].keys():
        print(t + ' ' + s)
        xs = data[t][s]['xs']
        ys = data[t][s]['ys']
        areas = data[t][s]['areas']
        colors = data[t][s]['colors']
        assert len(xs) == len(ys) == len(areas) == len(colors)
        for a in areas:
            assert float(a) > 100
        for c in colors:
            assert int(c) >= 0

print('valid!')
