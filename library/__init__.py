# ********************************************************************************
# *                                                                              *
# *   Copyright (C) 2022 Martijn Cramer <martijn.cramer@outlook.com>             *
# *                                                                              *
# *   This library is free software; you can redistribute it and/or              *
# *   modify it under the terms of the GNU Lesser General Public                 *
# *   License as published by the Free Software Foundation; either               *
# *   version 2.1 of the License, or (at your option) any later version.         *
# *                                                                              *
# *   This library is distributed in the hope that it will be useful,            *
# *   but WITHOUT ANY WARRANTY; without even the implied warranty of             *
# *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU          *
# *   Lesser General Public License for more details.                            *
# *                                                                              *
# *   You should have received a copy of the GNU Lesser General Public           *
# *   License along with this library; if not, write to the Free Software        *
# *   Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  *
# *   USA                                                                        *
# *                                                                              *
# ********************************************************************************

import enum
import os
import typing

__title__ = "Init script of the CAD model library package"
__author__ = "Martijn Cramer"
__url__ = "https://github.com/martcram/FreeCAD-APLAN-benchmark"


def removeLeadingNumbers(string: str) -> str:
    """Removes the leading numbers from a string, if present.
    Otherwise, the original string is returned.

    :param string: string in snake_case
    :type string: str
    :return: string in snake_case without leading numbers
    :rtype: str
    """
    elements: typing.List[str] = string.split('_')
    if elements[0].isalnum():
        return '_'.join(elements[1:])
    else:
        return string


def getSubDirectories(dir: str) -> typing.List[str]:
    """Returns a list of subdirectories of the specified parent directory.

    :param dir: absolute path pointing to the parent directory
    :type dir: str
    :return: list of the subdirectories' names
    :rtype: typing.List[str]
    """
    return [itemName for itemName in os.listdir(dir)
            if os.path.isdir(os.path.join(dir, itemName))]


def getAssemblyFilePath(dir: str) -> typing.Optional[str]:
    """Returns the file path of the first FreeCAD assembly file in the specified directory.
    To be recognized as an assembly file, the file's name must contain the substring 'asm' 
    and should have the '.FCStd' extension.

    :param dir: absolute path pointing to a directory
    :type dir: str
    :return: absolute path pointing to the assembly file or `None` if no file was found
    :rtype: typing.Optional[str]
    """
    for itemName in os.listdir(dir):
        filePath: str = os.path.join(dir, itemName)
        if os.path.isfile(filePath) and \
           os.path.splitext(itemName)[1] == ".FCStd" and ("asm" in itemName):
            return filePath
    return None


# * File path pointing to the CAD model library's directory.
LIBRARY_DIR_PATH: str = os.path.dirname(os.path.realpath(__file__))

# * Enum class representing all available models in the CAD model library and their file location:
# * <Model.DIR_NAME_WITHOUT_LEADING_NUMBERS>: 'file_path_to_FreeCAD_assembly_file'
# * e.g. Model.MULTIPLATE_CLUTCH, Model.SHEAR_MOLD etc.
Model: enum.Enum = enum.Enum("Model", {removeLeadingNumbers(subdirName).upper():  # type: ignore
                                       getAssemblyFilePath(os.path.join(LIBRARY_DIR_PATH, subdirName))
                                       for subdirName in getSubDirectories(LIBRARY_DIR_PATH)})
