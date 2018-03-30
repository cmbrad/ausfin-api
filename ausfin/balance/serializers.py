from collections import OrderedDict

from rest_framework import serializers

from .models import BalanceEvent, Source


class SourceField(serializers.RelatedField):
    def to_representation(self, value):
        return {'name': value.name, 'type': value.source_type.name}

    def get_queryset(self):
        return Source.objects.all()

    # Below code is copied from rest_framework.serializers.RelatedField
    # because we need to override the keys in the return value
    # Source: https://github.com/encode/django-rest-framework/issues/5141
    def get_choices(self, cutoff=None):
        queryset = self.get_queryset()
        if queryset is None:
            # Ensure that field.choices returns something sensible
            # even when accessed with a read-only field.
            return {}

        if cutoff is not None:
            queryset = queryset[:cutoff]

        return OrderedDict([
            (
                # This is the only line that differs
                # from the RelatedField's implementation
                item.pk,
                self.display_value(item)
            )
            for item in queryset
        ])

    def to_internal_value(self, data):
        return Source.objects.get(id=data)


class BalanceEventSerializer(serializers.ModelSerializer):
    source = SourceField()

    class Meta:
        model = BalanceEvent
        fields = ('id', 'source', 'balance', 'created_at', 'updated_at', )

    def create(self, validated_data):
        return BalanceEvent.objects.create(**{k: v for k, v in validated_data.items() if k not in ['owner']})
