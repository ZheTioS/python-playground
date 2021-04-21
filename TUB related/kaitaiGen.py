# Author(s): Udit Kumar Sahoo <udit.k.sahoo@campus.tu-berlin.de>, Vinayak Nair <v.nair@campus.tu-berlin.de>
# Keywords: KaiTai Generator, CSV Input
# Version: 2.0
# Created: 08-Mar-2021

# Usage:
# Run this file in the folder where all the Parameters, Telemetry and Command CSV files are present.
# It will generate KSY file and Error.txt file.
# If no output files are generated, then there are no CSV files in the current directory.

# library imports
import os
from os import listdir
from os.path import isfile, join
import csv

# Open all files in the current working directory
allFiles = [f for f in listdir(os.getcwd()) if isfile(join(os.getcwd(), f))]

# Define empty parameter and telemetry file lists
parameterFiles = []
telemetryFiles = []
commandFiles = []

# Filter all files for Parameters and Telemetry CSVs
for item in allFiles:
   if "_Parameter_.csv" in item:
      parameterFiles.append(item)
   if "_TELEMETRY.csv" in item:
      telemetryFiles.append(item)

#--------------------------------------------------------------------
# KaiTai Header Generator
#--------------------------------------------------------------------
# Ref: https://www.raumfahrttechnik.tu-berlin.de/fileadmin/fg169/amateur-radio/TUBIX10_3800_TN03_TM_Frame_01.pdf
# This reference provides frame information.
metaData = """
meta:
  id: salsat
  title: SALSAT Decoder Struct
  endian: le
"""

docSection = ""

header = """
seq:
  - id: salsat_frame
    type: salsat_frame
    doc-ref: 'https://www.raumfahrttechnik.tu-berlin.de/fileadmin/fg169/amateur-radio/TUBIX10_3800_TN03_TM_Frame_01.pdf'

types:
  salsat_frame:
    seq:
      - id: fsync
        type: b18
        doc: 'MSB first'
      - id: crc
        type: b14
      - id: fcid_major
        type: b6
        doc: 'MSB first'
      - id: fcid_sub
        type: b10
        doc: 'MSB first'
      - id: urgent_flag
        type: b1
      - id: future_use
        type: b1
      - id: crc_check
        type: b1
        doc: '1: Check CRC'
      - id: multiframe
        type: b1
        doc: '0: Single Frame'
      - id: time_tagged_setting
        type: b1
        doc: '1: Abs Time'
      - id: time_tagged
        type: b1
        doc: '1: Time Tagged'
      - id: data_length
        type: b10
        doc: 'MSB first'
      - id: time_tag
        type: u4le
        doc: 'LSB first'
        if: time_tagged == true
"""

#--------------------------------------------------------------------
# KaiTai Datatype Converter
#--------------------------------------------------------------------
# Ref: https://docs.oracle.com/cd/E19253-01/817-6223/chp-typeopexpr-2/index.html
# This reference provides an overview of Data Types and Sizes
# Ref: https://www.raumfahrttechnik.tu-berlin.de/fileadmin/fg169/amateur-radio/TUBIX10_3800_TN03_TM_Frame_01.pdf
# This reference provides Table 7: Size of Parameter
# Ref: https://doc.kaitai.io/user_guide.html#_basic_data_types
# This reference provides KaiTai specific expression language operates on the following primitive data types
# Function Definition
def kaitaiDataType(argument):
   if "float" in argument:
      datatype = "f4"
   elif "double" in argument:
      datatype = "f8"
   elif "int8_t" in argument:
      datatype = "s1"
   elif "uint8_t" in argument:
      datatype = "u1"
   elif "int16_t" in argument:
      datatype = "s2"
   elif "uint16_t" in argument:
      datatype = "u2"
   elif "int32_t" in argument:
      datatype = "s4"
   elif "uint32_t" in argument:
      datatype = "u4"
   elif "int64_t" in argument:
      datatype = "s8"
   elif "uint64_t" in argument:
      datatype = "u8"
   elif "bool" in argument:
      datatype = "b1"
   else:
      datatype = "invalid"
   return datatype

#--------------------------------------------------------------------
# Parameter List Generation
#--------------------------------------------------------------------
# Create empty lists
parameterID = []
parameterType = []
# Loop through all the files in the list
for item in parameterFiles:
   with open(item, mode='r') as csv_file:
      tempDict = csv.DictReader(csv_file)
      for row in tempDict:
         parameterID.append(row.get("UniqueName"))
         parameterType.append(kaitaiDataType({row["ParameterType"]}))

#--------------------------------------------------------------------
# # Define the output file parameters
#--------------------------------------------------------------------
decoderName = "salsat.ksy"
# Open the output file in write mode
outputFile = open(decoderName, "w")
# Open the error output file in write mode
outputErrorFile = open("Errors.txt", "w")

#--------------------------------------------------------------------
# Telemetry MetaData Generation
#--------------------------------------------------------------------
# Create empty lists
frameName = []
frameFCID = []
# Writing the metaData template for .ksy file
outputFile.write(metaData)

#--------------------------------------------------------------------
# Telemetry Doc Generation
#--------------------------------------------------------------------
# Create empty lists
frameName = []
frameParameters = []
# Writing the doc section template for .ksy file
#outputFile.write(docSection)
# Loop through all the files in the list
#for subsystem in telemetryFiles:
#   with open(subsystem, mode='r') as csv_file:
#      tempDict = csv.DictReader(csv_file)
#      # Extract frame name and FCID Major
#      for row in tempDict:
#         # Check description for error message and parameter0 to be not null
#         if str(row.get("Description")) != "#NoErrorMsg#" and str(row.get("Parameter0")) != "":
#            frameHeaders = list(row.keys())
#            # Obtain the starting point for the first parameter
#            index = frameHeaders.index("Parameter0")
#            while index < len(frameHeaders):
#               parameter = row.get(frameHeaders[index])
#               # Check if parameter name is at least more than 4 characters
#               if len(parameter) > 4:
#                  frameParameters.append(parameter)
#                  # Exception handling for missing data parameters
#                 try:
                     # Extract the data types
       #              dataType = str(parameterType[parameterID.index(parameter)])
                     # Exception handling for missing data types
      #               if dataType != "invalid":
     #                  outputFile.write("  :field " + parameter.lower() + ": salsat_frame.pdu_salsat." + str(row.get("FrameName")).lower() + "." + parameter.lower() + "\n")
    #                 else:
   #                     outputErrorFile.write("In " + subsystem + ", " + parameter + " does not have a valid data type.\n")
  #                except ValueError:
 #                    outputErrorFile.write("In " + subsystem + ", " + parameter + " parameter not found.\n")
#               index = index + 1

#--------------------------------------------------------------------
# Telemetry Sequence Generation
#--------------------------------------------------------------------
# Writing the header template for .ksy file
outputFile.write(header)
# Loop through all the files in the list
for subsystem in telemetryFiles:
   with open(subsystem, mode='r') as csv_file:
      tempDict = csv.DictReader(csv_file)
      # Extract frame name and FCID Major
      for row in tempDict:
         # Check description for error message and parameter0 to be not null
         if str(row.get("Description")) != "#NoErrorMsg#" and str(row.get("Parameter0")) != "":
            outputFile.write("      - id: user_data_" + str(row.get("FrameName")).lower() + "\n")
            outputFile.write("        type: " + str(row.get("FrameName")).lower() + "\n")
            outputFile.write("        if: fcid_major == " + str(int(float(row.get("FCIDMajor")))) + " and" + " fcid_sub == " + str(int(float(row.get("FCIDSub")))) + "\n")

#--------------------------------------------------------------------
# Telemetry List Generation
#--------------------------------------------------------------------
# Loop through all the files in the list
for subsystem in telemetryFiles:
   with open(subsystem, mode='r') as csv_file:
      tempDict = csv.DictReader(csv_file)
      # Extract frame row
      for row in tempDict:
         # Check description for error message and parameter0 to be not null
         if str(row.get("Description")) != "#NoErrorMsg#" and str(row.get("Parameter0")) != "":
            frameHeaders = list(row.keys())
            frameName.append(row.get("FrameName"))
            outputFile.write("  \n")
            outputFile.write("  " + str(row.get("FrameName")).lower() + ":\n")
            outputFile.write("    seq:\n")
            # Obtain the starting point for the first parameter
            index = frameHeaders.index("Parameter0")
            while index < len(frameHeaders):
               parameter = row.get(frameHeaders[index])
               # Check if parameter name is at least more than 4 characters
               if len(parameter) > 4:
                  frameParameters.append(parameter)
                  # Exception handling for missing data parameters
                  try:
                     # Extract the data types
                     dataType = str(parameterType[parameterID.index(parameter)])
                     # Exception handling for missing data types
                     if dataType != "invalid":
                        outputFile.write("      - id: " + parameter.lower() + "\n")
                        outputFile.write("        type: " + dataType + "\n")
                     else:
                        outputErrorFile.write("In " + subsystem + ", " + parameter + " does not have a valid data type.\n")
                  except ValueError:
                     outputErrorFile.write("In " + subsystem + ", " + parameter + " parameter not found.\n")
               index = index + 1

#--------------------------------------------------------------------
# Close the output files
#--------------------------------------------------------------------
outputFile.close()
outputErrorFile.close()
