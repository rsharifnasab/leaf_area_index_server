import os
from werkzeug import secure_filename
from shutil import rmtree

class DB():
    """this is DB class
        it get a file location in contructor and open that file
        and use it for list of tokens
    """

    def __init__(self, pre_location, user_list_file,attach_path):
        """
            only constructor of this class
            if will get input file location and set it
            then it open that file and read it word by  word ( token by token )
        """
        self.PRE_LOCATION = pre_location
        self.USER_LIST_LOCATION = pre_location + "/" + user_list_file
        self.ATTACH_PATH = pre_location + attach_path

        self.update_list()


    def update_list(self):
        with open(self.USER_LIST_LOCATION) as inp:
            self.user_list = inp.read().split()

    def verify_auth_token(self,token):
        """
            check if the token (in lowercase) is in list or not
        """
        # self.update_list() # TODO : can be un commented based on pilicy
        token = token.lower()
        return token in self.user_list

    def verify_client(self,client):
        """
            check if the client string is valid or not
            it will check if it is in the valid clients or not
            for now the only valid client is android
        """
        valid_clients = ["android"]
        return (client in valid_clients)

    def save_attach(self, attached_file, username, project_name):

        save_path = "%s/%s/%s/%s"%(self.ATTACH_PATH,username,project_name,secure_filename(attached_file.filename))
        directory = os.path.dirname(save_path)

        if not os.path.exists(directory):
            os.makedirs(directory)

        attached_file.save(save_path)
        return save_path
        

    def clean_attach(self, username):
        if username == "null": return
        try:
            rmtree(self.ATTACH_PATH + "/" +  username)
        except:
            pass
