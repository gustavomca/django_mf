from rest_framework import serializers

class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)
        model = kwargs.pop('model', None)

        if 'context' in kwargs:
            if 'request' in kwargs['context']:
                request = kwargs['context']['request']
                if 'fields' in request.query_params:
                    fields = request.query_params.get('fields').split(',')
                    fields = [field.strip() for field in fields]

        if model is not None:
            self.Meta.model = model
        
        super().__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)
    
    class Meta:
        model = None
        fields = '__all__'
        depth = 0