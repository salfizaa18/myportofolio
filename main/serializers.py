from datetime import date

from django.utils.html import strip_tags
from rest_framework import serializers

from main.models import Project, Education

MIN_YEAR = 1950
MAX_YEAR_AHEAD = 10  

class StarFieldsMixin(serializers.Serializer):
    star_count = serializers.SerializerMethodField()
    is_starred = serializers.SerializerMethodField()
    starred_by_names = serializers.SerializerMethodField()

    def get_star_count(self, obj):
        return obj.starred_by.count()

    def get_is_starred(self, obj):
        request = self.context.get("request")
        if request is None or not request.user.is_authenticated:
            return False
        return request.user in obj.starred_by.all()

    def get_starred_by_names(self, obj):
        return ", ".join(user.username for user in obj.starred_by.all())


class ProjectSerializer(StarFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            "id", "title", "description", "tech_stack",
            "project_url", "project_image_url",
            "star_count", "is_starred", "starred_by_names",
        ]
        read_only_fields = ["id"]

    def validate_title(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Title cannot be empty.")
        return value

    def validate_description(self, value):
        return strip_tags(value)

    def validate_tech_stack(self, value):
        return strip_tags(value)


class EducationSerializer(StarFieldsMixin, serializers.ModelSerializer):
    category_display = serializers.CharField(
        source="get_category_display", read_only=True,
    )

    class Meta:
        model = Education
        fields = [
            "id", "title", "description", "category", "category_display",
            "started_at", "ended_at",
            "star_count", "is_starred", "starred_by_names",
        ]
        read_only_fields = ["id"]

    @staticmethod
    def _check_year(value):
        max_year = date.today().year + MAX_YEAR_AHEAD
        if value is not None and not (MIN_YEAR <= value <= max_year):
            raise serializers.ValidationError(
                f"Year must be between {MIN_YEAR} and {max_year}."
            )
        return value

    def validate_title(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Title cannot be empty.")
        return value

    def validate_description(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Description cannot be empty.")
        return value

    def validate_started_at(self, value):
        return self._check_year(value)

    def validate_ended_at(self, value):
        return self._check_year(value)

    def validate(self, attrs):
        started = attrs.get("started_at", getattr(self.instance, "started_at", None))
        ended = attrs.get("ended_at", getattr(self.instance, "ended_at", None))
        if started is not None and ended is not None and ended < started:
            raise serializers.ValidationError(
                {"ended_at": "End year cannot be earlier than start year."}
            )
        return attrs