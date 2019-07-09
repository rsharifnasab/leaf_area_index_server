class DB():
    """this is DB class
        it get a file location in contructor and open that file
        and use it for list of tokens
    """

    def __init__(self, file_location):
        """
            only constructor of this class
            if will get input file location and set it
            then it open that file and read it word by  word ( token by token )
        """
        self.FILE_LOCATION = file_location
        with open(file_location) as inp:
            self.user_list = inp.read().split()

    def verify_auth_token(self,token):
        """
            check if the token (in lowercase) is in list or not
        """
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
