# Python B course
## B1_Topic2 (directory)
> Assignments regarding git
## B1_Topic3 (directory)
> debugging
---

## B2_Topic4 (Files)
### **Built-in function**
- Open file
    - open() + file.close()
        - 'r': default value, open for reading.
        - 'a': open for appending, creates the file if it does not exist.
        - 'w': open for writing, creates the file if it does not exist. Cover the exist content.
        - 'x': creates the specified file, returns an error if the file exist.
    - with open() as xx: no need to close the file.
- Read file
    - read() **default** or **-1** read the whole file; Positive integer read string with the length.
    - readline() **default** or **-1** read the first line; Positive integer read string with the length.
    - readlines() **default** or **-1** read the whole file line by line; If the number of bytes returned exceed the hint number, no more lines will be returned.
- Change the current file position
    - seek() a number representing the position to set the current file stream position.
- Writing to a file
    - write() depends on the way of opening the file, 'w' overwrite any existing content, 'a' append to the end of the file.

### **csv**
- open csv file (same above)
- read csv file
    - csv.reader return a nested list with each row's value as a list
    - csv.DictReader() return a list of each row as dict.
- writing to csv file
    - csv.writer() initializing for writing data into csv.
    - .writerows() write multiple rows
    - .writerow() write single row

### **JSON**
- reading JSON data (deserialisation)
    - json.loads(jstr) loads a string in JSON format into dict. After that you can operate them as a dict.
- reading JSON file
    - open(encoding='utf-8-sig') 
    - read() (same above, built-in python func, read the JSON format into string)
    - json.loads() the function is same above, change string into dict.
    - json.load() if the file is .json file, don't need read firstly instead of json.load() directly.
- writing JSON data (serialisation)
    - open() with 'w' or 'a'
    - json.dump(data, file) put data into file(JSON file)

### **XML**
- reading and parsing XML file
    - open() open the XML file as file object.
    - parse() this func from XML.dom.minidom module, to parse the file object as DOM(document object model) tree.
- modifying the DOM
    - setAttribute() modifying DOM tree
    - open('newfile', 'w') write the modified DOM in the new file.

### **Binary files**
- open the binary files
    - open('path', 'rb') 'rb' mode stands for 'read binary'
