from django.shortcuts import render
from django.db.models import Count
from .models import VisitorLog

def dashboard(request):
    total_visits   = VisitorLog.objects.count()
    unique_visitors = VisitorLog.objects.values('ip_address').distinct().count()

    # Top 5 most visited pages
    top_pages = (
        VisitorLog.objects
        .values('page_visited')
        .annotate(visits=Count('id'))
        .order_by('-visits')[:5]
    )

    # Last 10 visits
    recent_visits = VisitorLog.objects.order_by('-timestamp')[:10]

    return render(request, 'tracker/dashboard.html', {
        'total_visits':    total_visits,
        'unique_visitors': unique_visitors,
        'top_pages':       top_pages,
        'recent_visits':   recent_visits,
    })
