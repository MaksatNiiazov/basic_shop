def get_urls_preprocessor(endpoints):
    filtered = []
    for (path, path_regex, method, callback) in endpoints:
        # Remove all but DRF API endpoints
        if "/api/" in path:
            filtered.append((path, path_regex, method, callback))
    return filtered
