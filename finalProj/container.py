#print(self.containerTypes["Small Box"][0])
class Container:
    containerTypes = {"Small Box" : [4, 4, 4], "Medium Box" : [8,4,4], "Large Box" : [8,8,4]}
    DEFAULT_CONTAINER_TYPE : str = "Medium Box"

    def __init__(self, containerType : str = DEFAULT_CONTAINER_TYPE):
        self._containerType = containerType

    @property
    def containerType(self) -> str:
        return self._containerType 
        
    #Allows user to set the type of container
    @containerType.setter
    def containerType(self, conType : str) -> None:
        boxes = ["Small Box", "Medium Box", "Large Box"]
        if conType not in boxes:
            raise ValueError(f"Invalid Container Type: {conType}")
        else:
            self.containerType = conType

    #Prints the dimensions of the container
    def dimensions(self, containerType) -> str:
        return f"Dimensions: {self.containerTypes[containerType][0]} x {self.containerTypes[containerType][1]} x {self.containerTypes[containerType][2]}."
