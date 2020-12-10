from dateutil.relativedelta import relativedelta

from faker import Faker
from model_mommy.recipe import Recipe, seq

from edc_base.utils import get_utcnow

from .models import Courier, Document, SendDocument

fake = Faker()


document = Recipe(
    Document,
    doc_identifier='D99XXY4A',
    document_name='document 1',
    document_type='contract',
    document_form='soft_copy',
)

senddocument = Recipe(
    SendDocument,
    doc_identifier='D99XXY4A',
    status='sent',
    action_priority='high',
    comment='blah',
    action_date=get_utcnow(),
)

courier = Recipe(
    Courier,
    full_name='Thuto Ditsebe',
    cell='76452177',
    email='blah@gmail.com',)
