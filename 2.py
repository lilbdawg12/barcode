def barcode(data,python_barcode,image_data, barcode_class='code128', **kwargs):
    """Render a barcode."""
    constructor = python_barcode.get_barcode_class(barcode_class)

    data = str(data).zfill(constructor.digits)

    writer = python_barcode.writer.ImageWriter

    barcode_image = constructor(data, writer=writer())

    image = barcode_image.render(writer_options=kwargs)

    # Render to byte-encoded PNG
    return image_data(image)