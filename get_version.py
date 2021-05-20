print ("Getting Version")
CHANGELOGFILE = "Changelog.md"
with open (CHANGELOGFILE, "r" ) as changelogfile :
    for line in changelogfile:
        if line.startswith("##"):
            image_version=''.join(characters for characters in line if characters not in '# \r\n')
            break
print (image_version)