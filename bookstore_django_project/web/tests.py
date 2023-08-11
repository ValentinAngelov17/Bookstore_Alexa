from django.test import TestCase
from .models import Book, Paper, OfficeSupplies


class BookModelTestCase(TestCase):
    def setUp(self):
        Book.objects.create(title="Test Book", author="Test Author", pages=200, price=25)

    def test_book_title(self):
        book = Book.objects.get(title="Test Book")
        self.assertEqual(book.title, "Test Book")

    def test_book_author(self):
        book = Book.objects.get(title="Test Book")
        self.assertEqual(book.author, "Test Author")

    def test_book_pages(self):
        book = Book.objects.get(title="Test Book")
        self.assertEqual(book.pages, 200)

    def test_book_price(self):
        book = Book.objects.get(title="Test Book")
        self.assertEqual(book.price, 25)

    def test_book_str_method(self):
        book = Book.objects.get(title="Test Book")
        self.assertEqual(str(book), "Test Book")


class PaperModelTestCase(TestCase):
    def setUp(self):
        self.paper = Paper.objects.create(
            title='Test Paper',
            format='A4',
            weight=100,
            number_of_sheets=20,
            price=10.99,

        )

    def test_paper_creation(self):
        self.assertTrue(isinstance(self.paper, Paper))
        self.assertEqual(self.paper.__str__(), 'Test Paper')

    def test_paper_title(self):
        self.assertEqual(self.paper.title, 'Test Paper')

    def test_paper_price(self):
        self.assertEqual(self.paper.price, 10.99)

    def test_paper_weight(self):
        self.assertEqual(self.paper.weight, 100)

    def test_paper_number_of_sheets(self):
        self.assertEqual(self.paper.number_of_sheets, 20)


class OfficeSuppliesModelTestCase(TestCase):
    def setUp(self):
        self.office_supplies = OfficeSupplies.objects.create(
            supplies=OfficeSupplies.SCISSORS,
            title='Test Scissors',
            price=5.99,

        )

    def test_office_supplies_creation(self):
        self.assertTrue(isinstance(self.office_supplies, OfficeSupplies))
        self.assertEqual(self.office_supplies.__str__(), 'ножици')

    def test_office_supplies_supplies(self):
        self.assertEqual(self.office_supplies.supplies, OfficeSupplies.SCISSORS)

    def test_office_supplies_title(self):
        self.assertEqual(self.office_supplies.title, 'Test Scissors')

    def test_office_supplies_price(self):
        self.assertEqual(self.office_supplies.price, 5.99)



    def test_office_supplies_defaults(self):
        new_supplies = OfficeSupplies.objects.create(supplies=OfficeSupplies.PENS, title='Test Pen')
        self.assertEqual(new_supplies.price, 0.0)
        self.assertEqual(new_supplies.quantity, 1)
