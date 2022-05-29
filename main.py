from image_match.goldberg import ImageSignature

# def testSmoke():
#     gis = ImageSignature()
#     a = gis.generate_signature('https://up.kawinski.net/mona1.jpg')
#     b = gis.generate_signature('https://up.kawinski.net/mona2.jpg')
#     dst = gis.normalized_distance(a, b)
#     # print(f"a: {a}")
#     # print(f"b: {b}")
#     print(f"dst: {dst}")
#
#     ses.add_image('https://up.kawinski.net/mona1.jpg')
#     ses.add_image('https://up.kawinski.net/mona2.jpg')
#     result = ses.search_image('https://up.kawinski.net/mona1.jpg')
#     print(result)


if __name__ == '__main__':
    import ca_server
    ca_server.start_server()
