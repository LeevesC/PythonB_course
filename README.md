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
    - write(str) depends on the way of opening the file, 'w' overwrite any existing content, 'a' append to the end of the file.
    - writelines([str, str, str]) Note the type of arguments between write() and writelines().

### **csv**
- open csv file (same above)
- read csv file
    - csv.reader return a nested list with each row's value as a list
    - csv.DictReader() return a list of each row as dict.
- writing to csv file
    - csv.writer() initializing for writing data into csv.
    - .writerows() write multiple rows, the argument like this [[],[],[]...].
    - .writerow() write single row, the argument like this [...].
    - .DictWriter(filename, header) create an object which knows how to convert dictionary entries into csv rows. (Using this, you should have headers firstly, then main data)

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
---
## B3_Topic7 (Big O Notation)
### Major types of complexities
* O(1) - Constant Time  
* O(n) - Linear Time  
> The runtime depends on the input size.
* O(log n) - Logarithmic Time  
> Log time is similar to linear thim complexity, except that the runtime does not depend on the input size but rather on half the input size. The larger the data set, the more time or space it will require, but the rate of increase slows down as the data set size increases.  
> **Binary search**
* O(n log n) - Linearithmic Time  
>  
* O($n^2$) - Quadratic Time  
> When you perform nested iteration, meaning having a loop in loop, the time complexity is quadratic.  
* O($n^p$) - Polynomial Time  
> we can generalise quadratic time to any O($n^p$) to cover quadratic($n^2$), cubic($n^3$), quartic($n^4$) etc. functions.  
* O($k^n) - Exponential Time  
> O($2^n$) algorithms double with every additional input. If n=2, the algorithms will run four times; if n=3, they run eight times.  
* O(n!) - Factorial Time  
> Recursion  

### Recursion 

