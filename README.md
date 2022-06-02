# how to ?
install requirements.txt (for python3.6 or greater)

command: python3 -m pip install -r requirements.txt
    
    $python3 amz_ecom_invoice_extractor.py ~/Downloads/invoice.pdf
        {
        "/Users/uvadavalasa/Downloads/invoice.pdf": {
            "items": [
            "Dettol Liquid Handwash Refill - Skincare Moisturizing Hand Wash, 1500 ml (Price offer) | Antibacterial Formula | 10x Better Germ Protection | B07M9XYH9K ( B07M9XYH9K )  HSN:34013090",
            "Surf Excel Matic Top Load Liquid Detergent 2 L Refill, Designed For Tough Stain Removal on Laundry in Washing Machines - Super Saver Offer Pack | B07F8D6QLL ( B07F8D6QLL )  HSN:34022010"
            ],
            "order_number": "408-6919249-1365125",
            "order_date": "31.03.2022"
        }
    }
    
    $python3 amz_ecom_invoice_extractor.py ~/Downloads/invoice.pdf ~/Downloads/invoice1.pdf
    {
        "/Users/uday/Downloads/invoice.pdf": {
            "items": [
            "Dettol Liquid Handwash Refill - Skincare Moisturizing Hand Wash, 1500 ml (Price offer) | Antibacterial Formula | 10x Better Germ Protection | B07M9XYH9K ( B07M9XYH9K )  HSN:34013090",
            "Surf Excel Matic Top Load Liquid Detergent 2 L Refill, Designed For Tough Stain Removal on Laundry in Washing Machines - Super Saver Offer Pack | B07F8D6QLL ( B07F8D6QLL )  HSN:34022010"
            ],
            "order_number": "408-6919249-1365125",
            "order_date": "31.03.2022"
        },
        "/Users/uday/Downloads/invoice1.pdf": {
            "items": [
            "Ross Hair Scalp Massager Shampoo Brush with Soft Silicone Bristles, Anti Dandruff, Exfoliating with Scalp Care (Pink) | B07R6QKWZ5 ( B07R6QKWZ5 )  HSN:96031000",
            "Dove Gentle Exfoliating Nourishing Body Wash 190 ml | B07Y57V37S ( B07Y57V37S )  HSN:34013019",
            "Dove Body Wash Deeply Nourishing 190 Ml Bottle | B07Y8TYNCS ( B07Y8TYNCS )  HSN:34013019",
            "NIVEA Body Lotion for Very Dry Skin, Cocoa Nourish, with Coconut Oil & Cocoa Butter, For Men & Women, 400 ml | B00NW7NTTW ( B00NW7NTTW )  HSN:33049930"
            ],
            "order_number": "408-3892061-5286750",
            "order_date": "13.03.2022"
        }
    }
    
