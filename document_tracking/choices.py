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
    ('timesheet', 'Timesheet'),
    ('letter', 'Letter'),
    ('purchase_order', 'Purchase-Order'),
    ('invoice', 'Invoice'),
    ('report', 'Report'),
    (OTHER, 'Other, specify: '),
)
