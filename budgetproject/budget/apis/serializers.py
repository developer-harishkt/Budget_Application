from rest_framework import serializers

from budget.models import Project, Category, Expense


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:

        model = Project
        fields = ('id', 'name', 'slug', 'budget')


class CategorySerializer(serializers.ModelSerializer):

    class Meta:

        model = Category
        fields = ('id', 'project', 'name')


class ExpenseSerializer(serializers.ModelSerializer):

    class Meta:

        model = Expense
        fields = ('id', 'project', 'title', 'amount', 'category')
