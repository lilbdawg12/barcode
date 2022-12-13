import barcode
from barcode.writer import ImageWriter
import barcode

barcode_formats = barcode.PROVIDED_BARCODES

print(barcode_formats)
 
def barcode(data, barcode_class='code128', **kwargs):
    """Render a barcode."""
    python_barcode = barcode_class
    
    constructor = python_barcode.get_barcode_class(barcode_class)

    data = str(data).zfill(constructor.digits)

    writer = python_barcode.writer.ImageWriter

    barcode_image = constructor(data, writer=writer())

    image = barcode_image.render(writer_options=kwargs)

    # Render to byte-encoded PNG
    print(barcode_image)