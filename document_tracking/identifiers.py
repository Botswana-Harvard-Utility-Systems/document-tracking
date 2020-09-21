from edc_identifier.simple_identifier import SimpleUniqueIdentifier


class DocumentIdentifier(SimpleUniqueIdentifier):

    random_string_length = 5
    identifier_type = 'document_id'
    template = 'D{device_id}{random_string}'
