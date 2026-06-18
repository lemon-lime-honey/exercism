def get_list_of_wagons(*args):
    return list(args)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    return [1] + list(missing_wagons) + list(each_wagons_id)[3:] + list(each_wagons_id)[:2]


def add_missing_stops(route_dict, **kwargs):
    route_dict['stops'] = list()
    for key, value in dict(**kwargs).items():
        route_dict['stops'].append(value)
    return route_dict


def extend_route_information(route, more_route_information):
    route.update(more_route_information)
    return route


def fix_wagon_depot(wagons_rows):
    result = [[] for i in range(3)]
    for wagon in wagons_rows:
        for i in range(3):
            result[i].append(wagon[i])
    return result