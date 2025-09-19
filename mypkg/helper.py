import pandas as pd

class Helper:
    """
    Helper class for reading/writing data resource

        - 

    """


    old_col_nmz = ['Employee ID', 'Date of Joining', 'Gender', 'Company Type',
                    'WFH Setup Available', 'Designation', 'Resource Allocation',
                    'Mental Fatigue Score', 'Burn Rate']
    
    de_nmz = ['Geschlecht', 'Gewerbetyp', 'Homeoffice', 'Position',
              'Betriebsmittelbindung', 'Ermattungswert', 'BurnOut_Risiko']



    def __init__(self, fnm: str, dbg=False) -> None:
        self.raw = pd.read_csv(fnm) # content save
        self.dbg = dbg

    
    def translate(self):
        pass


        
    def sanitize(self):
        pass