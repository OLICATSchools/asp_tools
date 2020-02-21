""" 
File: prep_dataset.py
Contact: data@olicatschools.org

Description:
Download the pupil list from the ASP website as .xslx files.
"""

import requests

urns = []
ac_years = ['2018', '2019']
key_stages = ['Ks4PupilList', 'Ks2PupilList', 'Ks1PupilList', 'PhonicsPupilList']

# Paste contents of cookie header after logging into ASP website - allows script to interact with ASP
# Can be found by using dev tools built into your browser
cookie = ''

for urn in urns:
  for year in ac_years:
    for ks in key_stages:
      
      # Substitute values from lists into parts of the download url
      url = 'https://www.analyse-school-performance.service.gov.uk/' + year + '/Report/' + ks + '/' + urn + '?exportxlsx'
      
      # Make the request for the Excel file. Cookie header data tells the server the request is comming from an authorised source
      req = requests.get(url, headers = {'Cookie' : cookie})

      # Construct a filename for the current download. 
      # This format means files are separated out into folders for each key stage
      # The script relies on the folders having been created beforehand and will crash if they are not
      filename = ks[:3] + '\\' + urn + '_' + ks[:3] + '_' + year + '.xlsx'

      # Open (create) a blank file named with the value of the filename variable
      # Write the contents of what the ASP server sent back to us into the file
      with open(filename, 'wb') as code:
        code.write(req.content)

      print('Download complete')
