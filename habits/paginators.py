from rest_framework import pagination


class HabitPaginator(pagination.PageNumberPagination):
    """
    Пагинация привычек
    """

    page_size = 5
    page_size_query_param = "page_size"
    max_page_size = 5
