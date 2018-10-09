import re

def detect_text_uri(uri):
    print('\n')
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()
    image = vision.types.Image()
    image.source.image_uri = uri
    output = ''

    response = client.annotate_image({
    'image': {'source': {'image_uri': uri}},
    'features': [{'type': vision.enums.Feature.Type.TEXT_DETECTION}],
    })
    texts = response.text_annotations

    for text in texts:
        output = output + str(text.description) + ' '

    dateBirthdayRegex = re.compile('DOB: \d\d/\d\d/\d\d\d\d')
    dateBirthday = dateBirthdayRegex.findall(output)

    dateIssuedRegex = re.compile('Issued: \d\d/\d\d/\d\d\d\d')
    dateIssued = dateIssuedRegex.findall(output)

    dateExpireRegex = re.compile('Expires: \d\d/\d\d/\d\d\d\d')
    dateExpire = dateExpireRegex.findall(output)

    print(dateBirthday[0])
    print(dateIssued[0])
    print(dateExpire[0])

    print('\n"{}"'.format(output))

detect_text_uri('https://media.phillyvoice.com/media/images/PA_DL_Adult_Organ_Donor_1.2e16d0ba.fill-735x490.jpg')

#detect_text_uri('http://pa-license.com/wp-content/uploads/2011/05/JR-drivers-license-188x300.png')
