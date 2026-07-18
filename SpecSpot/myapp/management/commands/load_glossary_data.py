# Save this as: myapp/management/commands/load_glossary_data.py

from django.core.management.base import BaseCommand
from myapp.models import GlossaryTerm # Make sure 'myapp' is your app name

class Command(BaseCommand):
    help = 'Loads initial tech glossary data into the database'

    def handle(self, *args, **options):
        if GlossaryTerm.objects.exists():
            self.stdout.write(self.style.WARNING('Glossary data already loaded. Aborting.'))
            return

        glossary_data = [
            {
                "term": "Processor (CPU / SoC)",
                "icon_name": "cpu",
                "definition": """The "brain" of the phone. A faster processor means apps open quicker, games run smoother, and the entire phone feels more responsive. Most modern phones use a "System on a Chip" (SoC), which combines the CPU, graphics (GPU), and other components into one package.""",
                "example": "The Snapdragon 8 Gen 3 or Apple A17 Pro are high-end processors. A phone with one of these will be extremely fast at multitasking and handling demanding 3D games."
            },
            {
                "term": "RAM",
                "icon_name": "database",
                "definition": "Stands for Random Access Memory. RAM is your phone's short-term memory. It holds the apps you currently have open. More RAM lets you switch between apps (multitask) without them needing to reload from scratch.",
                "example": "If you have 12GB of RAM, you can have a game, your web browser with 20 tabs, and a music app open at the same time. When you switch from the game to the browser, it will be instantly available, not having to reload the webpage."
            },
            {
                "term": "Storage (ROM)",
                "icon_name": "hard-drive",
                "definition": "This is your phone's long-term memory, like a computer's hard drive. It's where you permanently store your photos, videos, apps, and the phone's operating system (OS).",
                "example": "A phone with 256GB of storage has plenty of space for thousands of photos and many large apps. If you shoot a lot of 4K video, you might want 512GB or 1TB."
            },
            {
                "term": "Display",
                "icon_name": "maximize",
                "definition": """This is your phone's screen. Key terms to look for:
• <strong class="text-slate-700">OLED/AMOLED:</strong> These screens have perfect, deep blacks (because each pixel can turn off completely) and vibrant colors. They are better than older LCD screens.
• <strong class="text-slate-700">Refresh Rate (Hz):</strong> How many times the screen updates per second. Standard is 60Hz. A 120Hz screen updates twice as fast, making scrolling and animations look incredibly smooth.""",
                "example": "A 6.7-inch AMOLED display with a 120Hz refresh rate is a high-end screen. It will be large, colorful, and feel very fluid to use."
            },
            {
                "term": "Battery (mAh)",
                "icon_name": "battery-charging",
                "definition": "Battery capacity is measured in milliampere-hours (mAh). A bigger number generally means a longer battery life, but this is also affected by the processor's efficiency and your screen settings.",
                "example": "A 5,000mAh battery is considered large and should easily last a full day for most users. A phone with a 4,000mAh battery might need to be charged by the evening if you use it heavily."
            },
            {
                "term": "Camera (Megapixels & Aperture)",
                "icon_name": "camera",
                "definition": """Two key numbers describe a camera:
• <strong class="text-slate-700">Megapixels (MP):</strong> This is the resolution of the photo. A higher MP number (like 108MP) means the image is very large and you can zoom in or crop it without losing much detail.
• <strong class="text-slate-700">Aperture (f-stop):</strong> This is the opening in the lens that lets light in, written as f/1.8, f/2.0, etc. A <strong class="text-slate-700">smaller number</strong> (like f/1.7) is better, as it means the opening is wider. This is crucial for good low-light photos.""",
                "example": "A 50MP camera with an f/1.8 aperture is a great main camera. It captures detailed photos and will perform well in dark restaurants or at night, letting in plenty of light."
            },
            {
                "term": "Charging Speed (W)",
                "icon_name": "zap",
                "definition": "Measured in Watts (W), this tells you how quickly the phone's battery can be recharged. This applies to both wired (plug-in) and wireless charging. A higher number is faster.",
                "example": "Standard charging is 15-25W. \"Fast charging\" can be anything from 45W to 120W or more. A phone with 100W charging might go from 0% to 100% in under 30 minutes, while a 25W charger might take over an hour."
            },
            {
                "term": "IP Rating",
                "icon_name": "shield",
                "definition": """This measures a phone's resistance to dust and water. It's written as "IP" followed by two numbers.
• The first number is for dust resistance (max 6).
• The second number is for water resistance (max 9).""",
                "example": "IP68 is the most common rating for high-end phones. This means it is \"dust-tight\" (6) and can be submerged in water up to 1.5 meters for 30 minutes (8). An IP53 rating means it's protected from dust (5) and can withstand splashes of water (3), but not submersion."
            },
            {
                "term": "5G",
                "icon_name": "bar-chart-2",
                "definition": "The 5th generation of mobile network technology. It offers significantly faster download and upload speeds, as well as lower latency (less lag) compared to 4G LTE. Most new smartphones today come with 5G support.",
                "example": "With a 5G connection, you could download a full movie in a few minutes instead of an hour, and online games will feel more responsive."
            },
            {
                "term": "NFC",
                "icon_name": "radio",
                "definition": "Stands for Near Field Communication. This is a short-range wireless technology. Its most common use is for \"contactless payments\" — tapping your phone on a payment terminal to pay.",
                "example": "Using NFC, you can add your credit card to Google Pay or Apple Pay and simply tap your phone to pay for groceries, just like you would with a physical tap-to-pay card."
            },
            {
                "term": "Biometrics",
                "icon_name": "user-check",
                "definition": """Security features that use your unique biological traits to unlock your phone. The two main types are:
• <strong class="text-slate-700">Fingerprint Sensor:</strong> Can be on the back, on the side power button, or "in-display" (under the glass of the screen).
• <strong class="text-slate-700">Face Unlock:</strong> Uses the selfie camera or advanced 3D scanners (like Apple's Face ID) to recognize your face.""",
                "example": "An in-display fingerprint sensor is a common biometric feature that lets you unlock your phone by placing your thumb on a specific area of the screen."
            }
        ]
        
        for item in glossary_data:
            GlossaryTerm.objects.create(
                term=item['term'],
                icon_name=item['icon_name'],
                definition=item['definition'],
                example=item['example']
            )

        self.stdout.write(self.style.SUCCESS(f'Successfully loaded {len(glossary_data)} glossary terms.'))