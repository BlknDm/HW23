def query_filter(param: str, data):
    return list(filter(lambda row: param in row, data))


def query_map(param: str, data):
    col_number = int(param)
    return list(map(lambda row: row.split(' ')[col_number], data))


def query_unique(data, *args, **kwargs):
    result = []
    seen = set()
    for row in data:
        if row in seen:
            continue
        else:
            result.append(row)
            seen.add(row)
    return result


def query_sort(param, data):
    reverse = False if param == 'asc' else True
    return sorted(data, reverse=reverse)


def query_limit(param: str, data):
    limit = int(param)
    return data[:limit]


CMD_TO_FUNCTION = {
    'filter': query_filter,
    'map': query_map,
    'unique': query_unique,
    'sort': query_sort,
    'limit': query_limit
}


def query_build(cmd, param, filename, data=None):
    if not data:
        with open(f'data/{filename}') as file:
            data = list(map(lambda row: row.strip(), file))
    return CMD_TO_FUNCTION[cmd](param=param, data=data)
