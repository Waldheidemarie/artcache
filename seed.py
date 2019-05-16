from sqlalchemy import func 
from model import Artwork 
from model import Neighborhood
import requests



def load_oneper(): 
    """Load Public 1% Artwork into database"""
    print("Public 1% Artwork")

    r = requests.get("https://data.sfgov.org/resource/cf6e-9e4j.json")
    one_per = r.json()

    for item in one_per: 
        title= item["title"]
        artist= item["title"]
        artist_desc= item["artistlink"]
        location=(item["the_geom"]["latitude"], item["the_geom"]["longitude"])
        medium=item["medium"]
        art_desc=item["name"] + item["location"]
        hint=item["accessibil"]

        art = Artwork(title=title,
                      artist=artist,
                      artist_desc=artist_link,
                      location=location,
                      source='public_oneper',
                      neighborhood_id=fill,
                      medium=medium,
                      art_desc=art_desc,
                      hint=hint)

        # add the data objects to the session
        db.session.add(art)

    # commit the changes to the db 
    db.session.commit()




def load_civic(): 
    """Load Civic Artwork into database."""
    print("Civic Artwork")

    r = requests.get("https://data.sfgov.org/resource/7rjr-9n9w.json")
    civic = r.json()

    for item in civic: 
        title= item["display_title"]
        artist= item["artist"]
        creation_date = item["creation_date"]
        location=(item["point"]["latitude"], item["point"]["longitude"])
        #neighborhood_id= 
        medium=item["medium"]
        art_desc=item["name"] + item["location"]
        hint=item["location_description"]

        art = Artwork(title=title,
                      artist=artist,
                      creation_date=creation_date,
                      location=location,
                      source='civic',
                      neighborhood_id=fill,
                      medium=medium,
                      art_desc=art_dex,
                      hint=hint)

        # add the data objects to the session
        db.session.add(art)

    # commit the changes to the db 
    db.session.commit()


def load_graffiti():
    """Load Graffiti into database."""
    print("Graffiti")

    r = requests.get("https://data.sfgov.org/resource/vg6y-3pcr.json")
    graffiti = r.json()

    for item in graffiti:
        title=item['category'] 
        creation_date=item['opened']
        location=item['point']
        source='graffiti'
        #neighborhood_id= 
        art_desc=item["request_details"]
        hint=item["request_type"]
        img=item["media_url"]



        art = Artwork(title=title,
                  location=location,
                  source='graffiti',
                  neighborhood_id=fill,
                  medium='graffiti',
                  art_desc=art_desc,
                  hint=hint,
                  img=img)

        # add the data objects to the session
        db.session.add(art)

    # commit the changes to the db 
    db.session.commit()



def load_neighborhood():
    """Load neighborhood data into database."""
    print("SF Neighborhoods")

    r = requests.get("https://data.sfgov.org/resource/6ia5-2f8k.json")
    neighborhoods = r.json()
    

    for item in neighborhoods:
        name = item["name"]
        geojson = str(item["the_geom"])
        geom = 

        #shapley: POLYGON(item['the_geom'][coordinates][0][0])
        #geom: use geo to_shape 

        #instanciate a neighboorhood and add coverted geom to column neighborhood_geom

        neighborhood = Neighborhood(name=name,
                                    neighborhood_geojson=geojson,
                                    neighborhood_geom=geom
                                    )

        # add the data objects to the session
        db.session.add(neighborhood)

    # commit the changes to the db 
    db.session.commit()




if __name__ == "__main__":
    
    connect_to_db(app)



