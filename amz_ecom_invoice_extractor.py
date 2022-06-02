import fitz
import sys
import os
import re
import json
import collections

# Order Number: 408-3892061-5286750
order_number_pattern = re.compile(r'Order Number: (\d+-\d+-\d+)')
# Order Date: 13.03.2022
order_date_pattern = re.compile(r'Order Date: (\d+\.\d+\.\d+)')

invoice_table_pattern= re.compile(r'Total\nAmount([\n\w\s,\(\)|:₹\.\-%&\.\/\-]*)TOTAL:', re.MULTILINE)

invoice_item = r'\s*[1-9]\s(?P<ITEM>([\w\s,\(\):|&\.\/\-])*)'
generic_pattern = r'(?P<GENERIC>.)'
invoice_item_pattern = re.compile('|'.join([invoice_item, generic_pattern]))

def extract_items_from_invoice_table(table_data):
    purchased_items = []
    for data in table_data:
        item_scanner = invoice_item_pattern.scanner(data)
        for item in iter(item_scanner.match, None):
            if item.lastgroup == 'ITEM':
                item_detail = item.group('ITEM')
                # remove \n if any
                item_detail = re.sub(r'\n', ' ', item_detail)
                item_detail = item_detail.strip()
                # sometimes we see partial matcher of the invoice pattern
                # sentinel condition is length of the string should be more than atleast 10chars
                if len(item_detail) > 10:
                    purchased_items.append(item_detail)
    return purchased_items


def extract_items_from_invoice(invoice_paths):
    result = {}
    for invoice_path in invoice_paths:
        if not os.path.exists(invoice_path):
            print(f"Invoice path does not exist: {invoice_path}")
            continue
        
        result[invoice_path] = {}

        invoice_pdf = fitz.open(invoice_path)

        result[invoice_path]['items'] = []
        for index, page in enumerate(invoice_pdf, start=1):
            page_content = page.get_text()
            # print(page_content)

            # gather order id and order date from page 1 only
            if index == 1:
                order_number = order_number_pattern.search(page_content)
                if order_number:
                    result[invoice_path]['order_number'] = order_number.group(1)
                order_date = order_date_pattern.search(page_content)
                if order_date:
                    result[invoice_path]['order_date'] = order_date.group(1)

            # Gather data from the invoice
            invoice_table_data = invoice_table_pattern.findall(page_content)
            if len(invoice_table_data) > 0:
                # print(invoice_table_data)
                purchased_items = extract_items_from_invoice_table(invoice_table_data)
                result[invoice_path]['items'].extend(purchased_items)
    
    print(json.dumps(result, indent=2))

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Usage: amz_ecom_invoice_extractor.py <invoice_pdf_path> ...\n")
        print("Example: amz_ecom_invoice_extractor.py invoice.pdf")
        print("Example: amz_ecom_invoice_extractor.py invoice.pdf invoice2.pdf")
        sys.exit(1)

    extract_items_from_invoice(sys.argv[1:])
