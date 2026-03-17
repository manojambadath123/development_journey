

from csv import DictReader

class TrackClass:

    def __init__(self):

        fr = open("task_30_mar12\\spotify-tracks-dataset.csv")

        self.data = list(DictReader(fr))


        print(self.data)
        print(len(self.data),"records found")

    def display_info(self):

        self.track_name_details = [t.get("track_name") for t in self.data  ]
        self.artists_details = [t.get("artists") for t in self.data  ]
        self.popularity_details = [t.get("popularity") for t in self.data  ]


        print(self.track_name_details)
        print(self.artists_details)
        print(self.popularity_details)

    
tc_instance = TrackClass()

# tc_instance.display_info()
