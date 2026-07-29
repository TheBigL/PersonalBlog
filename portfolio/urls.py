from django.urls import re_path
from .views import PortfolioDetailView, PortfolioListView, AddPortfolioView, EditPortfolioView, DeletePortfolioView
app_name = 'portfolio'


urlpatterns = [
    re_path(r'^$', PortfolioListView.as_view(), name="portfolio_list"),
    re_path(r'^add_portfolio/', AddPortfolioView.as_view(), name="add_portfolio"),
    re_path(r'^portfolio_detail/(?P<pk>\d+)/$', PortfolioDetailView.as_view(), name="portfolio_detail"),
    re_path(r'^edit_portfolio/(?P<pk>\d+)/$', EditPortfolioView.as_view(), name="edit_portfolio"),  
    re_path(r'^delete_portfolio/(?P<pk>\d+)/$', DeletePortfolioView.as_view(), name="delete_portfolio"),
]
