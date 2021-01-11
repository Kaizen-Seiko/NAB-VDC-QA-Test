class BaseFactory(object):
    """
    Object inherited class defines a POM structure
    @author: lex.khuat
    """

    # ------ Public methods -------
    def getObjs(self, classType, exclude=()):
        """
        Return list of instance by classType
        @param classType: type of returned class
        @param exclude: exclude items in return list
        @return: <List>Object
        """
        return list(item for item in self.__dict__.values()
                    if isinstance(item, classType)
                    and item not in exclude)

    def storeObj(self, name, obj, classType):
        """
        Add a class instance by classType
        @param name: instance name
        @param obj: object to add
        @param classType: type of returned class
        @return: self
        """
        if not isinstance(obj, classType):
            raise ValueError('%s must be %s classtype' % (obj, classType))
        for k, v in self.__dict__.items():
            if v is obj:
                if k is not name:
                    raise Exception('%s object already stored under another name: %s' % (obj, k))
                else:
                    return self
        self.__setattr__(name, obj)
        return self

    def destroy(self, obj):
        """
        Destroy stored pages/engines/environment
        @param obj: instance to destroy
        @return: self
        """
        name, val = None, None
        for k, v in self.__dict__.items():
            if v is obj:
                name = k, val = v
                break
        if name not in (None, 'siteName'):
            delattr(self, val)
        return self

    def get(self, name):
        """
        Return an existing attribute object stored in factory instance
        @param name: stored name
        @return: object
        """
        return self.__getattribute__(name)
