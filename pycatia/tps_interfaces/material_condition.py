#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class MaterialCondition(AnyObject):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MaterialCondition
                | 
                | Interface for accessing Material Condition modifier on a TPS.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.material_condition = com_object

    @property
    def modifier(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Modifier() As CATBSTR (Read Only)
                | 
                |     Retrieves Material Condition modifier.

        :return: str
        :rtype: str
        """

        return self.material_condition.Modifier

    def __repr__(self):
        return f'MaterialCondition(name="{ self.name }")'
