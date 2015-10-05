from datetime import datetime
import random
import string
import os


def generate_random_string(digit_length=3, char_length=3):
    digits = "".join([random.choice(string.digits) for i in range(digit_length)])
    chars = "".join([random.choice(string.ascii_letters) for i in range(char_length)])
    return digits + chars


def item_upload_to(instance, filename):
    # Callback for dynamic image name and upload dir
    file_root, file_ext = os.path.splitext(filename)
    date = datetime.now().strftime("%Y%m%d")
    random_name = generate_random_string() + file_ext
    classname = instance.__class__.__name__.lower()
    filename = "%s_%s" % (date, random_name)

    if classname == 'relatedimage':
        return '/'.join([classname, instance.content_type.name, filename])
    return '/'.join([classname, filename])
