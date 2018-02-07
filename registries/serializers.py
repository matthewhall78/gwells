from rest_framework import serializers
from registries.models import Organization

class DrillerListSerializer(serializers.ModelSerializer):
    """
    Serializes Driller model fields for "list" view.
    """

    province_state = serializers.ReadOnlyField(source="province_state.code")

    class Meta:
        model = Organization

        # Using all fields for now
        fields = (
            #'who_created',
            #'when_created',
            #'who_updated',
            #'when_updated',
            'org_guid',
            'name',
            'street_address',
            'city',
            'province_state',
            'postal_code',
            'main_tel',
            #'fax_tel',
            #'website_url',
            #'certificate_authority',
        )


class DrillerSerializer(serializers.ModelSerializer):
    """
    Serializes Driller model fields
    """

    province_state = serializers.ReadOnlyField(source="province_state.code")

    class Meta:
        model = Organization
        fields = (
            'who_created',
            'when_created',
            'who_updated',
            'when_updated',
            'org_guid',
            'name',
            'street_address',
            'city',
            'province_state',
            'postal_code',
            'main_tel',
            'fax_tel',
            'website_url',
            'certificate_authority',
        )
