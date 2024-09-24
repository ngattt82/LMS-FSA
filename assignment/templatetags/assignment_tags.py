from django import template
from django.utils import timezone
from ..models import Assignment, Submission

register = template.Library()

@register.filter
def is_overdue(assignment):
    return assignment.end_date < timezone.now()

@register.filter
def time_remaining(assignment):
    if assignment.end_date > timezone.now():
        time_left = assignment.end_date - timezone.now()
        days = time_left.days
        hours, remainder = divmod(time_left.seconds, 3600)
        minutes, _ = divmod(remainder, 60)
        return f"{days}d {hours}h {minutes}m"
    return "Overdue"

@register.simple_tag
def get_submission_status(assignment, user):
    submission = Submission.objects.filter(assignment=assignment, student=user).first()
    if submission:
        return "Submitted"
    elif assignment.end_date < timezone.now():
        return "Overdue"
    else:
        return "Not submitted"

@register.simple_tag
def get_grade(assignment, user):
    submission = Submission.objects.filter(assignment=assignment, student=user).first()
    if submission and submission.grade is not None:
        return f"{submission.grade:.2f}"
    return "Not graded"

@register.inclusion_tag('assignment/assignment_card.html')
def assignment_card(assignment, user):
    return {
        'assignment': assignment,
        'submission_status': get_submission_status(assignment, user),
        'grade': get_grade(assignment, user),
        'is_overdue': is_overdue(assignment),
        'time_remaining': time_remaining(assignment),
    }