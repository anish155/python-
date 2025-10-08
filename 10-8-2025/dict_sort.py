class Dict:
    def __init__(self):
        self.person=[{"Name": "Anish", "Address": "Kathmandu", "Phone": "9811111111"},
            {"Name": "Rahul", "Address": "Lalitpur", "Phone": "9822222222"},
            {"Name": "Evan", "Address": "Bhaktapur", "Phone": "9833333333"},
            {"Name": "Ria", "Address": "Pokhara", "Phone": "9844444444"},
            {"Name": "Alisha", "Address": "Biratnagar", "Phone": "9855555555"}
            ]
        
    def Sort(self):
        sorted_register=sorted(self.person, key=lambda x:x["Name"])
        for p in sorted_register:
            print(p)
    
dic=Dict()
dic.Sort()