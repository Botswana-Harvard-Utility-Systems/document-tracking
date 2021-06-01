from django.test import TestCase

from model_mommy import mommy

from ..models import Document, SendDocument, Courier


class TestDocument(TestCase):

    def setUp(self):

        self.document = mommy.make_recipe(
            'document_tracking.document'
        )

        self.send_document = mommy.make_recipe(
            'document_tracking.senddocument'
        )

        self.courier = mommy.make_recipe(
            'document_tracking.courier'
        )

    def test_document_created(self):
        """
        Test document created
        """
        self.assertTrue(isinstance(self.document, Document))

    def test_send_document_created(self):
        """
        Test send document created
        """
        self.assertTrue(isinstance(self.send_document, SendDocument))

    def test_courier_created(self):
        """
        Test if courier object has been created
        """
        self.assertTrue(isinstance(self.courier, Courier))
