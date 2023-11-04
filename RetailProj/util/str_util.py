def check_null(data):
    if not data:
        return True
    data =data.lower()
    if data == 'null' or data=='none' or data=='undefined' or data==' ':
        return True
    return False

def check_str_null_and_transform_to_sql_null(data):
    if check_null(str(data)):
        return 'Null'
    else:
        return f"'{data}'"



