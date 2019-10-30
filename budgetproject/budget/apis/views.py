from budget.models import Project, Category, Expense
from .serializers import ProjectSerializer, CategorySerializer, ExpenseSerializer

from django.http import Http404, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import json


class ProjectCreateView(APIView):

    def get(self, request, format = None):
        project = Project.objects.all()
        if project.exists():
            serializer = ProjectSerializer(project, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
            # return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        else:
            return Response({
                'status': False,
                'detail': "Sorry No Data"
            })

    def post(self, request, format=None):

        serializer = ProjectSerializer(data = request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.erros, status = status.HTTP_400_BAD_REQUEST)


class ProjectDetailView(APIView):

    def get_object(self, pk):

        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):

        if request.GET['for'] == 'api':
            obj = self.get_object(pk)

            expense_list = obj.expenses.all()
            serializer = ExpenseSerializer(expense_list, many=True)
            expense_list = []

            for item in serializer.data:
                value = list(item.values())
                str = "{} spent on {}".format(value[3], value[2])
                expense_list.append(str)

            total_transactions = len(expense_list)
            budget_left = obj.budget_left()

            return Response({
                'project' : obj.name,
                'expense_list' : expense_list,
                'total_budget' : obj.budget,
                'budget_left' : budget_left,
                'total_transactions' : total_transactions
            })

        project = Project.objects.all()
        if project.exists():
            serializer = ProjectSerializer(project, many = True)
            return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            return Response({
                'status' : False,
                'detail' : "No Projects in the DataBase"
            })

    def put(self, request, pk, format=None):

        project = self.get_object(pk)
        serializer = ProjectSerializer(project, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.erros, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format = None):

        project = self.get_object(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryCreateView(APIView):

    def get(self, request, format = None):

        category = Category.objects.all()
        if category.exists():
            serializer = CategorySerializer(category, many=True)
            if serializer.is_valid():
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        else:
            return Response({
                'status': False,
                'detail': "Sorry No Data"
            })

    def post(self, request, format=None):

        serializer = CategorySerializer(data = request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class CategoryDetailView(APIView):

    def get(self, request, format=None):

        category = Category.objects.all()
        if category.exists():
            serializer = CategorySerializer(category, many = True)
            return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            return Response({
                'status' : False,
                'detail' : "No Category in the DataBase"
            })


class ExpenseCreateView(APIView):

    def get(self, request, format = None):
        expense = Expense.objects.all()
        if expense.exists():
            serializer = ExpenseSerializer(expense, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({
                'status': False,
                'detail': "Sorry No Data"
            })


    def post(self, request, format=None):

        serializer = ExpenseSerializer(data = request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class ExpenseDetailView(APIView):

    def get_object(self, pk):

        try:
            return Expense.objects.get(pk=pk)
        except Expense.DoesNotExist:
            raise Http404


    def get(self, request, format=None):

        expense = Expense.objects.all()
        if expense.exists():
            serializer = ExpenseSerializer(expense, many = True)
            return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            return Response({
                'status' : False,
                'detail' : "No Category in the DataBase"
            })

    def put(self, request, pk, format=None):

        expense = self.get_object(pk)
        serializer = ExpenseSerializer(expense, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format = None):

        expense = self.get_object(pk)
        expense.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
