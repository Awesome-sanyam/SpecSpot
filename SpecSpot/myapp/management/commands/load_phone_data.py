# import json
# from django.core.management.base import BaseCommand
# from myapp.models import Phone

# class Command(BaseCommand):
#     help = 'Loads phone data from the initial hardcoded list into the database'

#     def handle(self, *args, **options):
#         if Phone.objects.exists():
#             self.stdout.write(self.style.WARNING('Phone data already loaded. Aborting.'))
#             return

#         # The original phone data array
#         phones_data = [
#             # ... (all the phone data from your original file)
#             # Samsung
#             {
#               "name": "Galaxy S24 Ultra", "brand": "Samsung", "price": 129999, "ram": 12, "camera": 200, "battery": 5000, "processor": "Snapdragon", "displayType": "AMOLED",
#               "specs": ["Snapdragon 8 Gen 3 for Galaxy", "200MP Main Camera", "Built-in S Pen", "Galaxy AI Features"]
#             },
#             {
#               "name": "Galaxy S24+", "brand": "Samsung", "price": 99999, "ram": 12, "camera": 50, "battery": 4900, "processor": "Exynos", "displayType": "AMOLED",
#               "specs": ["Exynos 2400", "50MP Triple Camera", "6.7\" Dynamic AMOLED 2X", "QHD+ Resolution"]
#             },
#             # ... all other phone objects go here, just like in the original file
#             {
#                 "name": "iPhone 15 Pro Max", "brand": "Apple", "price": 159900, "ram": 8, "camera": 48, "battery": 4422, "processor": "Apple Bionic", "displayType": "OLED",
#                 "specs": ["A17 Pro Bionic Chip", "5x Telephoto Camera", "Titanium Design", "Action Button"]
#             },
#             {
#                 "name": "Pixel 8 Pro", "brand": "Google", "price": 106999, "ram": 12, "camera": 50, "battery": 5050, "processor": "Google Tensor", "displayType": "OLED",
#                 "specs": ["Google Tensor G3", "Best-in-class AI Camera", "7 Years of OS Updates", "Super Actua Display"]
#             },
#             {
#                 "name": "Xiaomi 14 Ultra", "brand": "Xiaomi", "price": 99999, "ram": 16, "camera": 50, "battery": 5000, "processor": "Snapdragon", "displayType": "AMOLED",
#                 "specs": ["Snapdragon 8 Gen 3", "1-inch Leica Sensor", "120Hz LTPO Display", "90W HyperCharge"]
#             },
#             {
#                 "name": "OnePlus 12", "brand": "OnePlus", "price": 64999, "ram": 12, "camera": 50, "battery": 5400, "processor": "Snapdragon", "displayType": "AMOLED",
#                 "specs": ["Snapdragon 8 Gen 3", "Hasselblad Camera", "100W SUPERVOOC", "2K 120Hz ProXDR Display"]
#             },
#             {
#                 "name": "Realme GT 6", "brand": "Realme", "price": 40999, "ram": 8, "camera": 50, "battery": 5500, "processor": "Snapdragon", "displayType": "AMOLED",
#                 "specs": ["Snapdragon 8s Gen 3", "AI Flagship Killer", "6000 nits Ultra Bright Display", "120W SUPERVOOC"]
#             },
#             {
#                 "name": "Vivo X100 Pro", "brand": "Vivo", "price": 89999, "ram": 16, "camera": 50, "battery": 5400, "processor": "MediaTek Dimensity", "displayType": "AMOLED",
#                 "specs": ["Dimensity 9300", "Zeiss APO Telephoto Camera", "V3 Imaging Chip", "Pro Photography Phone"]
#             },
#             {
#                 "name": "Oppo Find X7 Ultra", "brand": "Oppo", "price": 105000, "ram": 16, "camera": 50, "battery": 5000, "processor": "Snapdragon", "displayType": "AMOLED",
#                 "specs": ["Snapdragon 8 Gen 3", "Dual Periscope Cameras", "Hasselblad Partnership", "1-inch Sony LYT-900 Sensor"]
#             },
#             {
#                 "name": "Motorola Edge 50 Ultra", "brand": "Motorola", "price": 64999, "ram": 12, "camera": 50, "battery": 4500, "processor": "Snapdragon", "displayType": "OLED",
#                 "specs": ["Snapdragon 8s Gen 3", "Real Wood Finish", "Pantone Validated Camera", "125W TurboPower Charging"]
#             },
#             {
#                 "name": "Nothing Phone (2)", "brand": "Nothing", "price": 44999, "ram": 12, "camera": 50, "battery": 4700, "processor": "Snapdragon", "displayType": "OLED",
#                 "specs": ["Snapdragon 8+ Gen 1", "Advanced Glyph Interface", "Nothing OS 2.0", "Premium Build"]
#             },
#             {
#                 "name": "Asus ROG Phone 8 Pro", "brand": "Asus", "price": 94999, "ram": 16, "camera": 50, "battery": 5500, "processor": "Snapdragon", "displayType": "AMOLED",
#                 "specs": ["Snapdragon 8 Gen 3", "AirTriggers & IP68 Rating", "165Hz Gaming Display", "For Serious Gamers"]
#             },
#             {
#                 "name": "Sony Xperia 1 VI", "brand": "Sony", "price": 129990, "ram": 12, "camera": 48, "battery": 5000, "processor": "Snapdragon", "displayType": "OLED",
#                 "specs": ["Snapdragon 8 Gen 3", "New 19.5:9 Display Ratio", "Advanced Telephoto Lens", "Pro Camera Controls"]
#             },
#             {
#                 "name": "Honor 200 Pro", "brand": "Honor", "price": 54999, "ram": 12, "camera": 50, "battery": 5200, "processor": "Snapdragon", "displayType": "OLED",
#                 "specs": ["Snapdragon 8s Gen 3", "AI Portrait Engine", "Silicon-carbon Battery", "50MP Telephoto Lens"]
#             },
#             {
#                 "name": "Infinix GT 20 Pro", "brand": "Infinix", "price": 24999, "ram": 8, "camera": 108, "battery": 5000, "processor": "MediaTek Dimensity", "displayType": "AMOLED",
#                 "specs": ["Dimensity 8200 Ultimate", "Dedicated Gaming Display Chip", "Cyber Mecha Design", "144Hz Display"]
#             },
#             {
#                 "name": "Tecno Phantom V Fold", "brand": "Tecno", "price": 88888, "ram": 12, "camera": 50, "battery": 5000, "processor": "MediaTek Dimensity", "displayType": "AMOLED",
#                 "specs": ["Dimensity 9000+", "Minimal Crease Foldable", "Aerospace-grade Hinge", "Affordable Foldable"]
#             },
#             {
#                 "name": "Lava Agni 2 5G", "brand": "Lava", "price": 21999, "ram": 8, "camera": 50, "battery": 4700, "processor": "MediaTek Dimensity", "displayType": "AMOLED",
#                 "specs": ["Dimensity 7050", "Curved AMOLED Display", "Premium Glass Back", "Clean Android"]
#             }
#         ]
        
#         for phone_data in phones_data:
#             Phone.objects.create(
#                 name=phone_data['name'],
#                 brand=phone_data['brand'],
#                 price=phone_data['price'],
#                 ram=phone_data['ram'],
#                 camera=phone_data['camera'],
#                 battery=phone_data['battery'],
#                 processor=phone_data['processor'],
#                 display_type=phone_data['displayType'],
#                 specs=phone_data['specs']
#             )

#         self.stdout.write(self.style.SUCCESS('Successfully loaded phone data into the database.'))


import json
from django.core.management.base import BaseCommand
from myapp.models import Phone # Make sure 'myapp' is the correct name of your app

class Command(BaseCommand):
    help = 'Loads phone data from the initial hardcoded list into the database'

    def handle(self, *args, **options):
        if Phone.objects.exists():
            self.stdout.write(self.style.WARNING('Phone data already loaded. Aborting.'))
            return

        # The original phone data array
        phones_data = [
            # Samsung
            {
              "name": "Galaxy S24 Ultra", "brand": "Samsung", "price": 129999, "ram": 12, "camera": 200, "battery": 5000, "processor": "Snapdragon", "displayType": "AMOLED",
              "specs": ["Snapdragon 8 Gen 3 for Galaxy", "200MP Main Camera", "Built-in S Pen", "Galaxy AI Features"]
            },
            {
              "name": "Galaxy S24+", "brand": "Samsung", "price": 99999, "ram": 12, "camera": 50, "battery": 4900, "processor": "Exynos", "displayType": "AMOLED",
              "specs": ["Exynos 2400", "50MP Triple Camera", '6.7" Dynamic AMOLED 2X', "QHD+ Resolution"]
            },
            {
              "name": "Galaxy S24", "brand": "Samsung", "price": 79999, "ram": 8, "camera": 50, "battery": 4000, "processor": "Exynos", "displayType": "AMOLED",
              "specs": ["Exynos 2400", 'Compact 6.2" Display', "Armor Aluminum 2.0 Frame", "AI Photo Editing"]
            },
            {
              "name": "Galaxy S23 FE", "brand": "Samsung", "price": 59999, "ram": 8, "camera": 50, "battery": 4500, "processor": "Exynos", "displayType": "AMOLED",
              "specs": ["Exynos 2200", "Pro-Grade 50MP Camera", "Vibrant 120Hz Display", "Wireless Charging"]
            },
            {
              "name": "Galaxy Z Fold 5", "brand": "Samsung", "price": 154999, "ram": 12, "camera": 50, "battery": 4400, "processor": "Snapdragon", "displayType": "AMOLED",
              "specs": ["Snapdragon 8 Gen 2 for Galaxy", '7.6" Main Screen', "Zero-gap Flex Hinge", "PC-like Multitasking"]
            },
            {
              "name": "Galaxy Z Flip 5", "brand": "Samsung", "price": 99999, "ram": 8, "camera": 12, "battery": 3700, "processor": "Snapdragon", "displayType": "AMOLED",
              "specs": ["Snapdragon 8 Gen 2 for Galaxy", '3.4" Flex Window', "Compact Folding Design", "Hands-free Selfies"]
            },
            {
              "name": "Galaxy A55 5G", "brand": "Samsung", "price": 39999, "ram": 8, "camera": 50, "battery": 5000, "processor": "Exynos", "displayType": "AMOLED",
              "specs": ["Exynos 1480", "Metal Frame, Glass Back", "IP67 Water Resistant", "5 Years of Updates"]
            },
            {
              "name": "Galaxy A35 5G", "brand": "Samsung", "price": 30999, "ram": 8, "camera": 50, "battery": 5000, "processor": "Exynos", "displayType": "AMOLED",
              "specs": ["Exynos 1380", "50MP OIS Camera", '6.6" Super AMOLED', "Knox Security"]
            },
            {
              "name": "Galaxy M55 5G", "brand": "Samsung", "price": 26999, "ram": 8, "camera": 50, "battery": 5000, "processor": "Snapdragon", "displayType": "AMOLED",
              "specs": ["Snapdragon 7 Gen 1", "Super AMOLED+ 120Hz", "Slim & Light Design", "45W Fast Charging"]
            },
            {
              "name": "Galaxy F55 5G", "brand": "Samsung", "price": 26999, "ram": 8, "camera": 50, "battery": 5000, "processor": "Snapdragon", "displayType": "AMOLED",
              "specs": ["Snapdragon 7 Gen 1", "Vegan Leather Back", "Sleek & Stylish", "45W Charging"]
            },
            {
              "name": "Galaxy M34 5G", "brand": "Samsung", "price": 18999, "ram": 6, "camera": 50, "battery": 6000, "processor": "Exynos", "displayType": "AMOLED",
              "specs": ["Exynos 1280", "6000mAh Monster Battery", "120Hz Super AMOLED", "No-Shake 50MP Camera"]
            },
            {
              "name": "Galaxy F15 5G", "brand": "Samsung", "price": 12999, "ram": 4, "camera": 50, "battery": 6000, "processor": "MediaTek Dimensity", "displayType": "AMOLED",
              "specs": ["Dimensity 6100+", "Segment-first sAMOLED", "6000mAh Battery", "4 Years of OS Upgrades"]
            },

            # Apple
            {
              "name": "iPhone 15 Pro Max", "brand": "Apple", "price": 159900, "ram": 8, "camera": 48, "battery": 4422, "processor": "Apple Bionic", "displayType": "OLED",
              "specs": ["A17 Pro Bionic Chip", "5x Telephoto Camera", "Titanium Design", "Action Button"]
            },
            {
              "name": "iPhone 15 Pro", "brand": "Apple", "price": 134900, "ram": 8, "camera": 48, "battery": 3274, "processor": "Apple Bionic", "displayType": "OLED",
              "specs": ["A17 Pro Bionic Chip", "Pro-level Camera System", "USB-C with USB 3 Speed", '6.1" Super Retina XDR']
            },
            {
              "name": "iPhone 15 Plus", "brand": "Apple", "price": 89900, "ram": 6, "camera": 48, "battery": 4383, "processor": "Apple Bionic", "displayType": "OLED",
              "specs": ["A16 Bionic Chip", '6.7" Display', "48MP Main Camera", "Dynamic Island"]
            },
            {
              "name": "iPhone 15", "brand": "Apple", "price": 79900, "ram": 6, "camera": 48, "battery": 3349, "processor": "Apple Bionic", "displayType": "OLED",
              "specs": ["A16 Bionic Chip", "Dynamic Island", "Color-infused Glass", "USB-C Port"]
            },
            {
              "name": "iPhone 14", "brand": "Apple", "price": 69900, "ram": 6, "camera": 12, "battery": 3279, "processor": "Apple Bionic", "displayType": "OLED",
              "specs": ["A15 Bionic Chip", "Crash Detection", "Dual-camera system", "Great value iPhone"]
            },
            {
              "name": "iPhone 13", "brand": "Apple", "price": 59900, "ram": 4, "camera": 12, "battery": 3240, "processor": "Apple Bionic", "displayType": "OLED",
              "specs": ["A15 Bionic Chip", "Cinematic Mode", "Super Retina XDR Display", "Excellent Value"]
            },
            {
              "name": "iPhone SE (2022)", "brand": "Apple", "price": 43900, "ram": 4, "camera": 12, "battery": 2018, "processor": "Apple Bionic", "displayType": "LCD",
              "specs": ["A15 Bionic Chip", "Classic Home Button Design", "5G Connectivity", "Most affordable iPhone"]
            },

            # Google
            {
              "name": "Pixel 8 Pro", "brand": "Google", "price": 106999, "ram": 12, "camera": 50, "battery": 5050, "processor": "Google Tensor", "displayType": "OLED",
              "specs": ["Google Tensor G3", "Best-in-class AI Camera", "7 Years of OS Updates", "Super Actua Display"]
            },
            {
              "name": "Pixel 8", "brand": "Google", "price": 75999, "ram": 8, "camera": 50, "battery": 4575, "processor": "Google Tensor", "displayType": "OLED",
              "specs": ["Google Tensor G3", "Magic Eraser & Photo Unblur", "Clean Android Experience", "Compact & Powerful"]
            },
            {
              "name": "Pixel 8a", "brand": "Google", "price": 52999, "ram": 8, "camera": 64, "battery": 4492, "processor": "Google Tensor", "displayType": "OLED",
              "specs": ["Google Tensor G3", "Flagship Camera on a Budget", "IP67 Rating", "120Hz Actua Display"]
            },
            {
              "name": "Pixel 7a", "brand": "Google", "price": 39999, "ram": 8, "camera": 64, "battery": 4385, "processor": "Google Tensor", "displayType": "OLED",
              "specs": ["Google Tensor G2", "Wireless Charging", "Excellent Camera Performance", "Great Mid-range Value"]
            },

            # Xiaomi
            {
              "name": "Xiaomi 14 Ultra", "brand": "Xiaomi", "price": 99999, "ram": 16, "camera": 50, "battery": 5000, "processor": "Snapdragon", "displayType": "AMOLED",
              "specs": ["Snapdragon 8 Gen 3", "1-inch Leica Sensor", "120Hz LTPO Display", "90W HyperCharge"]
            },
            {
              "name": "Xiaomi 14", "brand": "Xiaomi", "price": 69999, "ram": 12, "camera": 50, "battery": 4610, "processor": "Snapdragon", "displayType": "AMOLED",
              "specs": ["Snapdragon 8 Gen 3", "Leica Co-engineered Optics", "Compact Flagship", "HyperOS"]
            },
            {
              "name": "Xiaomi 14 Civi", "brand": "Xiaomi", "price": 42999, "ram": 8, "camera": 50, "battery": 4700, "processor": "Snapdragon", "displayType": "AMOLED",
              "specs": ["Snapdragon 8s Gen 3", "Leica Professional Lens", "Quad-Curve Display", "Slim & Light"]
            },
            {
              "name": "Redmi Note 13 Pro+", "brand": "Xiaomi", "price": 31999, "ram": 8, "camera": 200, "battery": 5000, "processor": "MediaTek Dimensity", "displayType": "AMOLED",
              "specs": ["Dimensity 7200 Ultra", "200MP Main Camera", "120W Charging", "Curved Display"]
            },
            {
              "name": "Redmi Note 13 Pro", "brand": "Xiaomi", "price": 25999, "ram": 8, "camera": 200, "battery": 5100, "processor": "Snapdragon", "displayType": "AMOLED",
              "specs": ["Snapdragon 7s Gen 2", "200MP OIS Camera", "67W Turbo Charging", "Great All-rounder"]
            },
            {
              "name": "Redmi Note 13", "brand": "Xiaomi", "price": 17999, "ram": 6, "camera": 108, "battery": 5000, "processor": "Snapdragon", "displayType": "AMOLED",
              "specs": ["Snapdragon 685", "120Hz AMOLED Display", "Ultra-thin Bezels", "33W Fast Charging"]
            },
            {
              "name": "Poco F6", "brand": "Xiaomi", "price": 29999, "ram": 8, "camera": 50, "battery": 5000, "processor": "Snapdragon", "displayType": "AMOLED",
              "specs": ["Snapdragon 8s Gen 3", "Performance Focused", "120Hz Gaming Display", "90W Turbo Charging"]
            },
            {
              "name": "Poco X6 Pro", "brand": "Xiaomi", "price": 26999, "ram": 12, "camera": 64, "battery": 5000, "processor": "MediaTek Dimensity", "displayType": "AMOLED",
              "specs": ["Dimensity 8300 Ultra", "64MP OIS Triple Camera", "Performance King", "67W Charging"]
            },
            {
              "name": "Poco X6", "brand": "Xiaomi", "price": 21999, "ram": 8, "camera": 64, "battery": 5100, "processor": "Snapdragon", "displayType": "AMOLED",
              "specs": ["Snapdragon 7s Gen 2", "CrystalRes 1.5K Display", "In-display Fingerprint", "67W Charging"]
            },
            {
              "name": "Poco M6 Pro", "brand": "Xiaomi", "price": 14999, "ram": 8, "camera": 64, "battery": 5000, "processor": "MediaTek Dimensity", "displayType": "AMOLED",
              "specs": ["Helio G99-Ultra", "120Hz Flow AMOLED", "First-in-segment OIS", "67W Turbo Charging"]
            },

            # OnePlus
            {
              "name": "OnePlus 12", "brand": "OnePlus", "price": 64999, "ram": 12, "camera": 50, "battery": 5400, "processor": "Snapdragon", "displayType": "AMOLED",
              "specs": ["Snapdragon 8 Gen 3", "Hasselblad Camera", "100W SUPERVOOC", "2K 120Hz ProXDR Display"]
            },
            {
              "name": "OnePlus 12R", "brand": "OnePlus", "price": 39999, "ram": 8, "camera": 50, "battery": 5500, "processor": "Snapdragon", "displayType": "AMOLED",
              "specs": ["Snapdragon 8 Gen 2", "Flagship-grade Main Camera", "Largest ever OnePlus Battery", "100W Charging"]
            },
            {
              "name": "OnePlus 11R", "brand": "OnePlus", "price": 35999, "ram": 8, "camera": 50, "battery": 5000, "processor": "Snapdragon", "displayType": "AMOLED",
              "specs": ["Snapdragon 8+ Gen 1", "100W SUPERVOOC", "Sony IMX890 Sensor", "Great Gaming Performance"]
            },
            {
              "name": "OnePlus Nord 3 5G", "brand": "OnePlus", "price": 33999, "ram": 8, "camera": 50, "battery": 5000, "processor": "MediaTek Dimensity", "displayType": "AMOLED",
              "specs": ["Dimensity 9000", "Alert Slider", "80W SUPERVOOC", "Smooth 120Hz Display"]
            },
            {
              "name": "OnePlus Nord CE 4", "brand": "OnePlus", "price": 24999, "ram": 8, "camera": 50, "battery": 5500, "processor": "Snapdragon", "displayType": "AMOLED",
              "specs": ["Snapdragon 7 Gen 3", "50MP Sony LYT-600 Camera", "100W SUPERVOOC", "Aqua Touch Display"]
            },
            {
              "name": "OnePlus Nord CE 3 Lite", "brand": "OnePlus", "price": 19999, "ram": 8, "camera": 108, "battery": 5000, "processor": "Snapdragon", "displayType": "LCD",
              "specs": ["Snapdragon 695", "108MP Main Camera", "67W SUPERVOOC", "Large 120Hz Display"]
            },
            {
              "name": "OnePlus Open", "brand": "OnePlus", "price": 139999, "ram": 16, "camera": 48, "battery": 4805, "processor": "Snapdragon", "displayType": "AMOLED",
              "specs": ["Snapdragon 8 Gen 2", "Crease-less Display", "Hasselblad Fold Camera", "Multitasking Powerhouse"]
            },

            # Realme
            {
              "name": "Realme GT 6", "brand": "Realme", "price": 40999, "ram": 8, "camera": 50, "battery": 5500, "processor": "Snapdragon", "displayType": "AMOLED",
              "specs": ["Snapdragon 8s Gen 3", "AI Flagship Killer", "6000 nits Ultra Bright Display", "120W SUPERVOOC"]
            },
            {
              "name": "Realme GT 6T", "brand": "Realme", "price": 30999, "ram": 8, "camera": 50, "battery": 5500, "processor": "Snapdragon", "displayType": "AMOLED",
              "specs": ["Snapdragon 7+ Gen 3", "Top Performer", "120W SUPERVOOC Charge", "Nano Mirror Design"]
            },
            {
              "name": "Realme 12 Pro+", "brand": "Realme", "price": 29999, "ram": 8, "camera": 50, "battery": 5000, "processor": "Snapdragon", "displayType": "AMOLED",
              "specs": ["Snapdragon 7s Gen 2", "64MP Periscope Portrait Camera", "Vegan Leather Design", "Curved Display"]
            },
            {
              "name": "Realme 12 Pro", "brand": "Realme", "price": 25999, "ram": 8, "camera": 50, "battery": 5000, "processor": "Snapdragon", "displayType": "AMOLED",
              "specs": ["Snapdragon 6 Gen 1", "Sony IMX882 OIS Camera", "32MP Telephoto Lens", "120Hz Curved Display"]
            },
            {
              "name": "Realme P1 Pro", "brand": "Realme", "price": 21999, "ram": 8, "camera": 50, "battery": 5000, "processor": "Snapdragon", "displayType": "AMOLED",
              "specs": ["Snapdragon 6 Gen 1", "Curved 120Hz Display", "Phoenix Design", "Performance Mid-ranger"]
            },
            {
              "name": "Realme P1", "brand": "Realme", "price": 15999, "ram": 6, "camera": 50, "battery": 5000, "processor": "MediaTek Dimensity", "displayType": "AMOLED",
              "specs": ["Dimensity 7050", "Fastest Chip in Segment", "120Hz AMOLED Display", "45W SUPERVOOC"]
            },
            {
              "name": "Realme Narzo 70 Pro", "brand": "Realme", "price": 19999, "ram": 8, "camera": 50, "battery": 5000, "processor": "MediaTek Dimensity", "displayType": "AMOLED",
              "specs": ["Dimensity 7050", "Sony IMX890 OIS Camera", "Air Gestures", "67W SUPERVOOC"]
            },
            {
              "name": "Realme Narzo 70x", "brand": "Realme", "price": 11999, "ram": 4, "camera": 50, "battery": 5000, "processor": "MediaTek Dimensity", "displayType": "LCD",
              "specs": ["Dimensity 6300", "120Hz Display", "IP54 Water Resistance", "45W SUPERVOOC"]
            },

            # Vivo / iQOO
            {
              "name": "Vivo X100 Pro", "brand": "Vivo", "price": 89999, "ram": 16, "camera": 50, "battery": 5400, "processor": "MediaTek Dimensity", "displayType": "AMOLED",
              "specs": ["Dimensity 9300", "Zeiss APO Telephoto Camera", "V3 Imaging Chip", "Pro Photography Phone"]
            },
            {
              "name": "Vivo X100", "brand": "Vivo", "price": 63999, "ram": 12, "camera": 50, "battery": 5000, "processor": "MediaTek Dimensity", "displayType": "AMOLED",
              "specs": ["Dimensity 9300", "Zeiss Multifocal Portrait", "8T LTPO Eye Protection Display", "120W FlashCharge"]
            },
            {
              "name": "Vivo V30 Pro", "brand": "Vivo", "price": 41999, "ram": 8, "camera": 50, "battery": 5000, "processor": "MediaTek Dimensity", "displayType": "AMOLED",
              "specs": ["Dimensity 8200", "Zeiss Triple Main Camera", "Aura Light Portrait", "Slimmest Phone of 2024"]
            },
            {
              "name": "Vivo V30", "brand": "Vivo", "price": 33999, "ram": 8, "camera": 50, "battery": 5000, "processor": "Snapdragon", "displayType": "AMOLED",
              "specs": ["Snapdragon 7 Gen 3", "Studio Quality Aura Light", "Slim 3D Curved Display", "80W FlashCharge"]
            },
            {
              "name": "iQOO 12 5G", "brand": "Vivo", "price": 52999, "ram": 12, "camera": 50, "battery": 5000, "processor": "Snapdragon", "displayType": "AMOLED",
              "specs": ["Snapdragon 8 Gen 3", "Supercomputing Chip Q1", "144Hz LTPO Display", "Pro-level Gaming"]
            },
            {
              "name": "iQOO Neo 9 Pro", "brand": "Vivo", "price": 34999, "ram": 8, "camera": 50, "battery": 5160, "processor": "Snapdragon", "displayType": "AMOLED",
              "specs": ["Snapdragon 8 Gen 2", "144Hz LTPO AMOLED", "120W FlashCharge", "Dual Chip Power"]
            },
            {
              "name": "iQOO Z9x", "brand": "Vivo", "price": 12999, "ram": 4, "camera": 50, "battery": 6000, "processor": "Snapdragon", "displayType": "LCD",
              "specs": ["Snapdragon 6 Gen 1", "6000mAh Battery", "Brightest 120Hz Display", "IP64 Rating"]
            },
            {
              "name": "iQOO Z9", "brand": "Vivo", "price": 19999, "ram": 8, "camera": 50, "battery": 5000, "processor": "MediaTek Dimensity", "displayType": "AMOLED",
              "specs": ["Dimensity 7200", "Sony IMX882 OIS Camera", "1200Hz Touch Sampling", "Segment’s Fastest Phone"]
            },

            # Oppo
            {
              "name": "Oppo Find X7 Ultra", "brand": "Oppo", "price": 105000, "ram": 16, "camera": 50, "battery": 5000, "processor": "Snapdragon", "displayType": "AMOLED",
              "specs": ["Snapdragon 8 Gen 3", "Dual Periscope Cameras", "Hasselblad Partnership", "1-inch Sony LYT-900 Sensor"]
            },
            {
              "name": "Oppo Reno 11 Pro", "brand": "Oppo", "price": 39999, "ram": 12, "camera": 50, "battery": 4600, "processor": "MediaTek Dimensity", "displayType": "AMOLED",
              "specs": ["Dimensity 8200", "32MP Telephoto Portrait Camera", "80W SUPERVOOC", "Premium Design"]
            },
            {
              "name": "Oppo Reno 11", "brand": "Oppo", "price": 29999, "ram": 8, "camera": 50, "battery": 5000, "processor": "MediaTek Dimensity", "displayType": "AMOLED",
              "specs": ["Dimensity 7050", "The Portrait Expert", "3D Curved Design", "67W SUPERVOOC"]
            },
            {
              "name": "Oppo F25 Pro 5G", "brand": "Oppo", "price": 23999, "ram": 8, "camera": 64, "battery": 5000, "processor": "MediaTek Dimensity", "displayType": "AMOLED",
              "specs": ["Dimensity 7050", "IP65 Water Resistance", "4K Video Recording", "67W SUPERVOOC"]
            },
            {
              "name": "Oppo F27 Pro+ 5G", "brand": "Oppo", "price": 27999, "ram": 8, "camera": 64, "battery": 5000, "processor": "MediaTek Dimensity", "displayType": "AMOLED",
              "specs": ["Dimensity 7050", "India's First IP69 Phone", "Damage-proof Armor Body", "Monsoon-ready"]
            },

            # Motorola
            {
              "name": "Motorola Edge 50 Ultra", "brand": "Motorola", "price": 64999, "ram": 12, "camera": 50, "battery": 4500, "processor": "Snapdragon", "displayType": "OLED",
              "specs": ["Snapdragon 8s Gen 3", "Real Wood Finish", "Pantone Validated Camera", "125W TurboPower Charging"]
            },
            {
              "name": "Motorola Edge 50 Pro", "brand": "Motorola", "price": 31999, "ram": 8, "camera": 50, "battery": 4500, "processor": "Snapdragon", "displayType": "OLED",
              "specs": ["Snapdragon 7 Gen 3", "Pantone Validated Colors", "AI Photo Enhancement", "Vegan Leather Finish"]
            },
            {
              "name": "Motorola Edge 50 Fusion", "brand": "Motorola", "price": 22999, "ram": 8, "camera": 50, "battery": 5000, "processor": "Snapdragon", "displayType": "OLED",
              "specs": ["Snapdragon 7s Gen 2", "IP68 Water Protection", "144Hz pOLED Curved Display", "Slim & Light"]
            },
            {
              "name": "Moto G64 5G", "brand": "Motorola", "price": 14999, "ram": 8, "camera": 50, "battery": 6000, "processor": "MediaTek Dimensity", "displayType": "LCD",
              "specs": ["Dimensity 7025", "6000mAh Battery", "50MP OIS Camera", "120Hz Display"]
            },
            {
              "name": "Moto G34 5G", "brand": "Motorola", "price": 10999, "ram": 4, "camera": 50, "battery": 5000, "processor": "Snapdragon", "displayType": "LCD",
              "specs": ["Snapdragon 695", "Fastest 5G in Segment", "Vegan Leather Design", "Stereo Speakers"]
            },
            {
              "name": "Motorola Razr 40 Ultra", "brand": "Motorola", "price": 89999, "ram": 8, "camera": 12, "battery": 3800, "processor": "Snapdragon", "displayType": "OLED",
              "specs": ["Snapdragon 8+ Gen 1", "Largest External Display", "Iconic Flip Design", '3.6" pOLED cover screen']
            },

            # Nothing
            {
              "name": "Nothing Phone (2)", "brand": "Nothing", "price": 44999, "ram": 12, "camera": 50, "battery": 4700, "processor": "Snapdragon", "displayType": "OLED",
              "specs": ["Snapdragon 8+ Gen 1", "Advanced Glyph Interface", "Nothing OS 2.0", "Premium Build"]
            },
            {
              "name": "Nothing Phone (2a)", "brand": "Nothing", "price": 23999, "ram": 8, "camera": 50, "battery": 5000, "processor": "MediaTek Dimensity", "displayType": "AMOLED",
              "specs": ["Dimensity 7200 Pro", "Essential Glyph features", "Clean Software", "Affordable Style"]
            },

            # Asus
            {
              "name": "Asus ROG Phone 8 Pro", "brand": "Asus", "price": 94999, "ram": 16, "camera": 50, "battery": 5500, "processor": "Snapdragon", "displayType": "AMOLED",
              "specs": ["Snapdragon 8 Gen 3", "AirTriggers & IP68 Rating", "165Hz Gaming Display", "For Serious Gamers"]
            },
            {
              "name": "Asus Zenfone 10", "brand": "Asus", "price": 69999, "ram": 8, "camera": 50, "battery": 4300, "processor": "Snapdragon", "displayType": "AMOLED",
              "specs": ["Snapdragon 8 Gen 2", '5.9" Compact Flagship', "6-Axis Gimbal Stabilizer 2.0", "One-handed Use"]
            },

            # Sony
            {
              "name": "Sony Xperia 1 VI", "brand": "Sony", "price": 129990, "ram": 12, "camera": 48, "battery": 5000, "processor": "Snapdragon", "displayType": "OLED",
              "specs": ["Snapdragon 8 Gen 3", "New 19.5:9 Display Ratio", "Advanced Telephoto Lens", "Pro Camera Controls"]
            },
            {
              "name": "Sony Xperia 1 V", "brand": "Sony", "price": 114990, "ram": 12, "camera": 48, "battery": 5000, "processor": "Snapdragon", "displayType": "OLED",
              "specs": ["Snapdragon 8 Gen 2", "4K 120Hz HDR Display", "Exmor T for mobile sensor", "Pro Photography Features"]
            },

            # Honor
            {
              "name": "Honor 90 5G", "brand": "Honor", "price": 37999, "ram": 8, "camera": 200, "battery": 5000, "processor": "Snapdragon", "displayType": "AMOLED",
              "specs": ["Snapdragon 7 Gen 1", "200MP Main Camera", "Risk-Free Dimming Display", "Premium Design"]
            },
            {
              "name": "Honor X9b 5G", "brand": "Honor", "price": 25999, "ram": 8, "camera": 108, "battery": 5800, "processor": "Snapdragon", "displayType": "AMOLED",
              "specs": ["Snapdragon 6 Gen 1", "Ultra-Bounce Anti-Drop Display", "Large 5800mAh Battery", "108MP Main Camera"]
            },
            {
              "name": "Honor 200 Pro", "brand": "Honor", "price": 54999, "ram": 12, "camera": 50, "battery": 5200, "processor": "Snapdragon", "displayType": "OLED",
              "specs": ["Snapdragon 8s Gen 3", "AI Portrait Engine", "Silicon-carbon Battery", "50MP Telephoto Lens"]
            },

            # Infinix
            {
              "name": "Infinix GT 20 Pro", "brand": "Infinix", "price": 24999, "ram": 8, "camera": 108, "battery": 5000, "processor": "MediaTek Dimensity", "displayType": "AMOLED",
              "specs": ["Dimensity 8200 Ultimate", "Dedicated Gaming Display Chip", "Cyber Mecha Design", "144Hz Display"]
            },
            {
              "name": "Infinix Note 40 Pro+", "brand": "Infinix", "price": 21999, "ram": 8, "camera": 108, "battery": 5000, "processor": "MediaTek Dimensity", "displayType": "AMOLED",
              "specs": ["Dimensity 7020", "100W All-Round FastCharge 2.0", "20W Wireless MagCharge", "3D Curved AMOLED"]
            },

            # Tecno
            {
              "name": "Tecno Phantom V Fold", "brand": "Tecno", "price": 88888, "ram": 12, "camera": 50, "battery": 5000, "processor": "MediaTek Dimensity", "displayType": "AMOLED",
              "specs": ["Dimensity 9000+", "Minimal Crease Foldable", "Aerospace-grade Hinge", "Affordable Foldable"]
            },
            {
              "name": "Tecno Pova 6 Pro", "brand": "Tecno", "price": 19999, "ram": 8, "camera": 108, "battery": 6000, "processor": "MediaTek Dimensity", "displayType": "AMOLED",
              "specs": ["Dimensity 6080", "Dynamic-Light MiniLED Effect", "6000mAh Battery, 70W Charging", "Gaming Focused"]
            },
            {
              "name": "Tecno Camon 30 Premier", "brand": "Tecno", "price": 39999, "ram": 12, "camera": 50, "battery": 5000, "processor": "MediaTek Dimensity", "displayType": "AMOLED",
              "specs": ["Dimensity 8200 Ultimate", "Sony IMX890 Main Camera", "PolarAce Imaging System", "144Hz LTPO AMOLED"]
            },

            # Lava
            {
              "name": "Lava Agni 2 5G", "brand": "Lava", "price": 21999, "ram": 8, "camera": 50, "battery": 4700, "processor": "MediaTek Dimensity", "displayType": "AMOLED",
              "specs": ["Dimensity 7050", "Curved AMOLED Display", "Premium Glass Back", "Clean Android"]
            },
            {
              "name": "Lava Blaze Curve 5G", "brand": "Lava", "price": 17999, "ram": 8, "camera": 64, "battery": 5000, "processor": "MediaTek Dimensity", "displayType": "AMOLED",
              "specs": ["Dimensity 7050", "120Hz Curved AMOLED", "Dolby Atmos Stereo Speakers", "Made in India"]
            },
        ]
        
        for phone_data in phones_data:
            Phone.objects.create(
                name=phone_data['name'],
                brand=phone_data['brand'],
                price=phone_data['price'],
                ram=phone_data['ram'],
                camera=phone_data['camera'],
                battery=phone_data['battery'],
                processor=phone_data['processor'],
                display_type=phone_data['displayType'], # This field name must match your model
                specs=phone_data['specs']
            )

        self.stdout.write(self.style.SUCCESS('Successfully loaded phone data into the database.'))