class AttributeSubstituteManager:
    def __init__(self, obj, *, attr_name, attr_value):
        if not hasattr(obj, attr_name):
            raise ValueError('{!r} has no attribute {!r}'.format(obj, attr_name))

        self.obj = obj
        self.attr_name = attr_name
        self.default_attr_value = getattr(obj, attr_name)
        self.attr_value = attr_value

    def __enter__(self):
        setattr(self.obj, self.attr_name, self.attr_value)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        setattr(self.obj, self.attr_name, self.default_attr_value)


class DRFViewSerializerSubstituteManager(AttributeSubstituteManager):
    def __init__(self, view, *, attr_value, attr_name='serializer_class'):
        super().__init__(view, attr_name=attr_name, attr_value=attr_value)


class DRFViewPermissionsSubstituteManager(AttributeSubstituteManager):
    def __init__(self, view, *, attr_value, attr_name='permission_classes', extend=True):
        super().__init__(view, attr_value=attr_value, attr_name=attr_name)
        if extend:
            self.attr_value = tuple(self.attr_value)
            self.attr_value += tuple(self.default_attr_value)