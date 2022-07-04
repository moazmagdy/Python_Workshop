def format_name(first_name, last_name, location= None):
    full_name = '%s %s' % (first_name, last_name)

    if location:
        return print('%s (%s)'% (full_name, location))
    else:
        return print(full_name)

format_name('John', 'Smith', location='California')