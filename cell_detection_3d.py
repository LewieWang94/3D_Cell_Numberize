import json
import math

filename = '2d_blobs.json'
dist_threshold = 3.5
with open(filename, 'r') as file:
    data = json.load(file)


def dist_acceptable(x1, y1, x2, y2):
    # print(math.sqrt(pow((x1-x2), 2) + pow((y1-y2), 2)))
    return math.sqrt(pow((x1-x2), 2) + pow((y1-y2), 2)) < dist_threshold


def find_z_one_time(time):
    # [x,y,z,c,counted]
    result = []
    cell_xs = []
    cell_ys = []
    cell_zs = []
    slices = data[str(time)]
    for i in range(1, 101):
        # print(i)
        new_result = []
        current = slices[str(i)]
        xs = current['xs']
        ys = current['ys']
        colors = current['colors']
        areas = current['areas']
        for j in range(len(xs)):
            k = 0
            is_new = True
            while k < len(result):
                if dist_acceptable(xs[j], ys[j], result[k][0], result[k][1]):
                    is_new = False
                    if colors[j] >= result[k][3]:
                        # result[k] = [xs[j], ys[j], i, colors[j], False]
                        new_result.append([xs[j], ys[j], i, colors[j], False])
                        del result[k]
                        break
                    else:
                        if not result[k][4]:
                            cell_xs.append(result[k][0])
                            cell_ys.append(result[k][1])
                            cell_zs.append(result[k][2])
                        # result[k] = [xs[j], ys[j], i, colors[j], True]
                        new_result.append([xs[j], ys[j], i, colors[j], True])
                        del result[k]
                        break
                        # del result[k]
                        # don't modify k
                else:
                    k += 1
            if is_new:
                # result.append([xs[j], ys[j], i, colors[j], False])
                new_result.append([xs[j], ys[j], i, colors[j], False])
        result = new_result
        # for i in result:

    # for i in result:
    #     if not i[4]:
    #         cell_xs.append(i[0])
    #         cell_ys.append(i[1])
    #         cell_zs.append(i[2])

    return cell_xs, cell_ys, cell_zs


# x, y, z = find_z_one_time(1)
# print(len(x))


def generate_3d_json():
    path = '3d_cells.json'
    out_file = open(path, 'w')
    result = {}
    for n in range(1, 21):
        path_1 = '3d_cells_' + str(n) + '.txt'
        tmp_file = open(path_1, 'w')
        result[n] = {}
        result[n]['xs'] = []
        result[n]['ys'] = []
        result[n]['zs'] = []
        xs, ys, zs = find_z_one_time(n)

        tmp = [0]
        for i in range(0, len(xs)):
            # print(i)
            # print(str(x[i]) + ' ' + str(y[i]) + ' ' + str(z[i]))
            # if (x[i], y[i], z[i]) not in result:
            has_similar = False
            for j in tmp:
                # print(xx, yy, zz)
                if (abs(xs[i]-xs[j]) <= 10) and (abs(ys[i]-ys[j]) <= 10) and (abs(zs[i]-zs[j]) <= 10):
                    has_similar = True
                    break
            if not has_similar:
                tmp.append(i)
        print(len(tmp))

        for t in tmp:
            result[n]['xs'].append(xs[t])
            result[n]['ys'].append(ys[t])
            result[n]['zs'].append(zs[t])
            tmp_file.write(str(xs[t]) + ' ' + str(ys[t]) + ' ' + str(zs[t]))
            tmp_file.write('\n')

    json.dump(result, out_file)


generate_3d_json()

# result = [(x[0], y[0], z[0])]
# for i in range(len(x)):
#     # print(i)
#     # print(str(x[i]) + ' ' + str(y[i]) + ' ' + str(z[i]))
#     # if (x[i], y[i], z[i]) not in result:
#     for (xx, yy, zz) in result:
#         # print(xx, yy, zz)
#         if abs(xx-x[i]) < 6 and abs(yy-y[i]) < 6 and abs(zz-z[i]) < 6:
#             break
#         result.append((x[i], y[i], z[i]))


# result = [0]
# for i in range(0, len(x)):
#     # print(i)
#     # print(str(x[i]) + ' ' + str(y[i]) + ' ' + str(z[i]))
#     # if (x[i], y[i], z[i]) not in result:
#     has_similar = False
#     for j in result:
#         # print(xx, yy, zz)
#         if (abs(x[i]-x[j]) <= 8) and (abs(y[i]-y[j]) <= 8) and (abs(z[i]-z[j]) <= 6):
#             has_similar = True
#             break
#     if not has_similar:
#         result.append(i)
#
# print(len(result))
#
# for i in result:
#     print(str(x[i]) + ' ' + str(y[i]) + ' ' + str(z[i]))
