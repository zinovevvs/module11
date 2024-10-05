def introspection_info(obj):
    obj_type = type(obj).__name__
    all_attributes = dir(obj)

    methods = [attr for attr in all_attributes if callable(getattr(obj, attr))]
    attributes = [attr for attr in all_attributes if not callable(getattr(obj, attr))]
    obj_module = getattr(obj, '__module__', '__main__') # Проверяю, есть ли у объекта атрибут __module__

    result = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': obj_module
    }

    return result

number_info = introspection_info(42)
print(number_info)



