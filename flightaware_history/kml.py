import typing
from lxml import etree


def xpath(el: etree.ElementTree, path: str) -> typing.List[etree.ElementTree]:
    return el.xpath(
        path,
        namespaces={
            "kml": "http://www.opengis.net/kml/2.2",
            "gx": "http://www.google.com/kml/ext/2.2",
        },
    )


def parse_kml(
    file, label: str = None
) -> typing.Tuple[typing.List[etree.ElementTree], typing.List[etree.ElementTree]]:
    """
    Parse a stream of KML data to lists of tracks and airports as Placemark nodes.
    """
    airports = {}
    tracks = []
    parsed = etree.parse(file, etree.XMLParser(remove_blank_text=True))
    root = parsed.xpath(".")[0]
    for track in xpath(root, "//gx:Track/parent::*"):
        for name in xpath(track, "kml:name"):
            for desc in xpath(track, "kml:description"):
                name.text = f"{desc.text} - {name.text}"
                if label:
                    name.text = f"{label} - {name.text}"
        tracks.append(track)
    for airport in xpath(root, "//kml:Point/parent::*"):
        for name in xpath(airport, "kml:name"):
            if name.text not in airports:
                airports[name.text] = airport
    return tracks, airports.values()


def write_kml(
    filename: str,
    placemarks: typing.List[etree.ElementTree],
    title: str = None,
    template: str = None,
):
    if not template:
        template = default_template
    root = template.xpath(".")[0]
    out_doc = xpath(root, "//kml:Document")[0]
    if title:
        for name in xpath(template, "kml:name"):
            name.text = title
    for el in placemarks:
        out_doc.append(el)
    with open(filename, "wb") as outfile:
        outfile.write(etree.tostring(root))


default_template = """\
<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2">
<Document>
    <name></name>
</Document>
</kml>
"""
