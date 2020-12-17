from edc_constants.constants import OTHER

DOCUMENT_STATUS = (
    ('sent', 'Sent'),
    ('received', 'Received'),
    ('processing', 'Processing'),
    ('processed', 'Processed')
)

DOCUMENT_FORM = (
    ('soft_copy', 'Soft-copy'),
    ('hard_copy', 'Hard-copy'),
    ('both', 'Both'),
)

DOCUMENT_TYPE = (
    ('contract', 'Contract'),
    ('letter', 'Letter'),
    ('report', 'Report'),
    (OTHER, 'Other, specify: '),
)

PRIORITY = (
    ('normal', 'Normal'),
    ('Medium', 'Medium'),
    ('high', 'High'),
)
