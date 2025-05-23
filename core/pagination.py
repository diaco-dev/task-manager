def paginated_response(data, offset, limit, count):
    return {
        'pages_count': 0 if count == 0 else int(count / limit) + (
            1 if count % limit > 0 else 0),
        'items_per_page': 0 if count == 0 else limit,
        'current_page_items_count': 0 if count == 0 else len(data),
        'current_page': 0 if count == 0 else int(offset / limit) + 1,
        'total_items': count,
        'items': data
    }
