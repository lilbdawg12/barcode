def python_barcode (
    data, barcode_class="code128", fmt="png", add_checksum=True, **writer_options
):
    """Return a barcode's image data.

    Powered by the Python library ``python-barcode``. See this library's
    documentation for more details.

    Parameters
    ----------
    data
      Data to be encoded in the datamatrix.

    barcode_class
      Class/standard to use to encode the data. Different standards have
      different constraints.
    
    writer_options
      Various options for the writer to tune the appearance of the barcode
      (see python-barcode documentation).

    Returns
    -------
    image_base64_data
      A string ``data:image/png;base64,xxxxxxxxx`` which you can provide as a
      "src" parameter to a ``<img/>`` tag.

    Examples:
    ---------

    >>> data = barcode('EGF12134', barcode_class='code128')
    >>> html_data = '<img src="%s"/>' % data

    Examples of writer options:

    >>> { 'background': 'white',
    >>>   'font_size': 10,
    >>>   'foreground': 'black',
    >>>   'module_height': 15.0,
    >>>   'module_width': 0.2,
    >>>   'quiet_zone': 6.5,
    >>>   'text': '',
    >>>   'text_distance': 5.0,
    >>>   'write_text': True
    >>> }
    """
    constructor = python_barcode.get_barcode_class(barcode_class)
    data = str(data).zfill(constructor.digits)
    writer = {
        "svg": python_barcode.writer.SVGWriter,
        "png": python_barcode.writer.ImageWriter,
    }[fmt]
    if "add_checksum" in getattr(constructor, "__init__").__code__.co_varnames:
        barcode_img = constructor(data, writer=writer(), add_checksum=add_checksum)
    else:
        barcode_img = constructor(data, writer=writer())
    img = barcode_img.render(writer_options=writer_options)
    if fmt == "png":
        return pil_to_html_imgdata(img, fmt="PNG")
    else:
        prefix = "data:image/svg+xml;charset=utf-8;base64,"
        return prefix + base64.b64encode(img).decode()