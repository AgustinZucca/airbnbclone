from app.models import db, Image

def seed_images():
    img1 = Image(
        spot_id=1,
        url='https://content.fortune.com/wp-content/uploads/2015/08/9133oriole004_ps-1.jpg'
    )
    img2 = Image(
        spot_id=2,
        url='https://listingmedia7.harstatic.com/416217462/hr/1.jpeg?ts=2022-05-24T11:13:12.663'
    )
    img3 = Image(
        spot_id=3,
        url='https://photos.zillowstatic.com/fp/784f984ba106ec1f8146c0d026a47c24-uncropped_scaled_within_1536_1152.webp'
    )
    img4 = Image(
        spot_id=4,
        url='https://luxbnb.s3.us-east-2.amazonaws.com/hamptons2.png'
    )
    img5 = Image(
        spot_id=5,
        url='https://luxbnb.s3.us-east-2.amazonaws.com/pic2.png'
    )
    img6 = Image(
        spot_id=6,
        url='https://luxbnb.s3.us-east-2.amazonaws.com/pic3.png'
    )
    img7 = Image(
        spot_id=7,
        url='https://luxbnb.s3.us-east-2.amazonaws.com/manhattan1.png'
    )
    img8 = Image(
        spot_id=8,
        url='https://luxbnb.s3.us-east-2.amazonaws.com/manhattan2.png'
    )
    img9 = Image(
        spot_id=9,
        url='https://luxbnb.s3.us-east-2.amazonaws.com/chicago1.png'
    )
    img10 = Image(
        spot_id=10,
        url='https://luxbnb.s3.us-east-2.amazonaws.com/dallas1.png'
    )
    img11 = Image(
        spot_id=11,
        url='https://luxbnb.s3.us-east-2.amazonaws.com/boston1.png'
    )
    img12 = Image(
        spot_id=12,
        url='https://luxbnb.s3.us-east-2.amazonaws.com/sf1.png'
    )
    img13 = Image(
        spot_id=13,
        url='https://luxbnb.s3.us-east-2.amazonaws.com/losaltos1.png'
    )
    img14 = Image(
        spot_id=14,
        url='https://luxbnb.s3.us-east-2.amazonaws.com/losaltos2.png'
    )
    img15 = Image(
        spot_id=15,
        url='https://luxbnb.s3.us-east-2.amazonaws.com/bh1.png'
    )
    img16 = Image(
        spot_id=16,
        url='https://luxbnb.s3.us-east-2.amazonaws.com/miami1.png'
    )
    img17 = Image(
        spot_id=17,
        url='https://luxbnb.s3.us-east-2.amazonaws.com/bh2.png'
    )
    img18 = Image(
        spot_id=18,
        url='https://luxbnb.s3.us-east-2.amazonaws.com/ny1.png'
    )


    db.session.add(img1)
    db.session.add(img2)
    db.session.add(img3)
    db.session.add(img4)
    db.session.add(img5)
    db.session.add(img6)
    db.session.add(img7)
    db.session.add(img8)
    db.session.add(img9)
    db.session.add(img10)
    db.session.add(img11)
    db.session.add(img12)
    db.session.add(img13)
    db.session.add(img14)
    db.session.add(img15)
    db.session.add(img16)
    db.session.add(img17)
    db.session.add(img18)

    db.session.commit()

def undo_images():
    db.session.execute('TRUNCATE images RESTART IDENTITY CASCADE;')
    db.session.commit()