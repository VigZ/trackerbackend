from model_utils import Choices
from django.utils.translation import ugettext_lazy as _

TICKET_SEVERITY_CHOICES = Choices(
    (1,"urgent", _('Complete loss of service or a significant feature that is completely unavailable and no workaround exists. It does not include development issues or problems in staging environments.')),
    (2,"high", _('Partial loss of service with severe impact on the business and no workaround exists.')),
    (3,"normal", _('Minor loss of service. The result is an inconvenience, which may require a temporary workaround.')),
    (4,"low", _('No loss of service. The result does not prevent software operation.')),
)

TICKET_PRIORITY_CHOICES = Choices(
    (1,"top", _('Ticket should be completed as soon as possible.')),
    (2,"high", _('Ticket should be completed quickly.')),
    (3,"mid", _('Ticket should be completed after higher priority tickets.')),
    (4,"low", _('Ticket should be completed in spare time.')),
)
